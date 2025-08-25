#!/usr/bin/env python3
# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://geodynamics.org).
#
# Copyright (c) 2010-2024, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
#
# Create binary tarballs on Unix style systems.
#
# macOS: PYLITH_INSTALLER_PATH=$PATH_TO_AUTOTOOLS
#
# Step 1: Clone pylith_installer repository.
# Step 2: Use this utility to create tarballs.

import os
import stat
import shutil
import subprocess
import argparse
import pathlib
import tarfile
import platform

PYTHON_VERSION = "3.12"  # :KLUDGE:


class Darwin:

    @staticmethod
    def update_linking(dist_dir):
        for filepath in dist_dir.glob("bin/*"):
            Darwin.update_deplibs(filepath)
        for filepath in dist_dir.glob("*/*.dylib"):
            Darwin.update_deplibs(filepath)
        for filepath in dist_dir.glob("**/vtkmodules/*.so"):
            Darwin.update_deplibs(filepath, newPath="@loader_path/.dylibs")
        for filepath in dist_dir.glob("**/*.so"):
            Darwin.update_deplibs(filepath)

    @staticmethod
    def update_deplibs(filename, newPath="@executable_path/../lib"):
        if filename.is_symlink() or filename.is_dir():
            return

        proc = subprocess.run(
            ["otool", "-L", filename], stdout=subprocess.PIPE, check=True
        )
        output = proc.stdout.decode("utf-8")
        deplibs = []
        libId = None
        for line in output.split("\t")[1:]:
            objName = line.split()[0]
            libName = os.path.split(objName)[1]
            if str(filename).endswith(libName):
                libId = objName
            else:
                deplibs.append(objName)

        # Change id
        if libId:
            libName = os.path.split(libId)[1]
            libNameNew = f"@rpath/{libName}"
            cmd = [
                "install_name_tool",
                "-id",
                libNameNew,
                str(filename),
            ]
            subprocess.run(cmd, check=True)

        # Change path to dependencies
        for libPathAbs in deplibs:
            if libPathAbs.startswith("/usr") or libPathAbs.startswith("/System"):
                continue
            if libPathAbs.startswith("@loader_path"):
                continue
            libName = os.path.split(libPathAbs)[1]
            libPathNew = f"{newPath}/{libName}"
            cmd = [
                "install_name_tool",
                "-change",
                libPathAbs,
                libPathNew,
                str(filename),
            ]
            subprocess.run(cmd, check=True)


class Packager:

    def __init__(self, dist_dir, build_dir, macos_target):
        self.dist_dir = dist_dir
        self.build_dir = build_dir
        self.macos_target = macos_target

        self._get_makeinfo()
        self._get_git_version()

    def make_src_tarball(self):
        os.chdir(self.build_dir)
        self._run_cmd(("make", "dist"))
        filename_dist = f"{self.make['package']}-{self.make['version']}.tar.gz"
        prefix = self.git_version or "release"
        filename_tagged = f"{prefix}-{filename_dist}"
        self._run_cmd(("mv", filename_dist, filename_tagged))
        self.src_tarball = self.build_dir / filename_tagged

    def make_dist_tarball(self):
        os.chdir(self.build_dir)
        arch = self._get_arch()

        self._fix_python_path()

        dist_name = f"{self.make['package']}-{self.make['version']}-{arch}"
        self._install_src(self.dist_dir)
        prefix = self.git_version or "release"
        tfilename = f"{prefix}-{dist_name}.tar.gz"
        print(f"Making binary package tarball '{tfilename}'...")
        with tarfile.open(tfilename, mode="w:gz") as tfile:
            tfile.add(self.dist_dir, arcname=dist_name, filter=self._exclude)
        shutil.rmtree(self.dist_dir / "src")

        self._update_linking(dist_name, tfilename)

    def _run_cmd(self, cmd):
        print("Running '%s'..." % " ".join(cmd))
        subprocess.check_call(cmd)

    def _parse_makefile_vars(self):
        os.chdir(self.build_dir)
        vars = {}
        with open("Makefile") as fin:
            lines = fin.readlines()
        for line in lines:
            if len(line.split("=")) == 2 and not "$" in line:
                key, value = line.split("=")
                vars[key.strip()] = value.strip()
        return vars

    def _get_makeinfo(self):
        makefile = self._parse_makefile_vars()
        self.make = {
            "package": makefile["PACKAGE"],
            "version": makefile["VERSION"],
            "src_dir": makefile["abs_top_srcdir"],
        }

    def _get_git_version(self):
        os.chdir(self.make["src_dir"])
        cmd = ("git", "describe", "--tags")
        status = subprocess.run(cmd, capture_output=True)
        self.git_version = status.stdout.strip().decode()

    def _install_src(self, target_dir):
        dist_src = target_dir / "src"
        shutil.rmtree(dist_src, ignore_errors=True)
        dist_src.mkdir(exist_ok=True)
        tfile = tarfile.open(self.src_tarball, mode="r:*")
        tfile.extractall(path=dist_src)

    def _fix_python_path(self):
        def _rewrite(filename):
            mode = os.stat(filename).st_mode
            filename_tmp = str(filename) + "-tmp"
            with open(filename, "r") as fin, open(filename_tmp, "w") as fout:
                line0 = fin.readline()
                line0 = line0.replace(old_path, new_path)
                line0 = line0.replace("python\n", "nemesis\n")
                line0 = line0.replace("python3\n", "nemesis\n")
                fout.write(line0)
                fout.writelines(fin.readlines())
            os.replace(filename_tmp, filename)
            os.chmod(filename, mode | stat.S_IEXEC)

        dist_bin = self.dist_dir / "bin"
        old_path = f"{dist_bin}/"
        new_path = "/usr/bin/env "
        for filename in dist_bin.glob("*"):
            if filename.is_dir() or filename.is_symlink():
                continue
            with open(filename, "r") as fin:
                try:
                    line = fin.readline()
                except UnicodeDecodeError:
                    continue
                if (
                    line.startswith(f"#!{old_path}")
                    or line.endswith("python\n")
                    or line.endswith("python3\n")
                ):
                    _rewrite(filename)

    def _update_linking(self, dist_name, tfilename):
        if platform.system().lower() != "darwin":
            return

        print(f"Updating linking...")
        tarball_dir = self.build_dir / dist_name
        shutil.rmtree(tarball_dir, ignore_errors=True)
        with tarfile.open(tfilename, "r:*") as tfile:
            tfile.extractall(path=self.build_dir)
        Darwin.update_linking(tarball_dir)
        with tarfile.open(tfilename, mode="w:gz") as tfile:
            tfile.add(tarball_dir, arcname=dist_name)
        shutil.rmtree(tarball_dir)

    def _get_arch(self):
        op_sys = platform.system().lower()
        if op_sys == "darwin":
            mac_ver = platform.mac_ver()
            target = self.macos_target or mac_ver[0]
            arch = f"macOS-{target}-{mac_ver[2]}"
        else:
            machine = platform.processor() or platform.machine()
            arch = f"{op_sys}-{machine}"
        return arch

    @staticmethod
    def _exclude(tarinfo):
        EXCLUDE = (
            "include",
            "ccmake",
            "cmake",
            "cpack",
            "ctest",
            "gcc",
            "g++",
            "gcov",
            "gcov-dump",
            "gcov-tool",
            "cpp",
            "cc",
            "c++",
            "python",  # use python3
            "lto-dump",
            "swig",
            "TrilinosRepoVersion.txt",
        )
        filepath = tarinfo.name
        if os.path.splitext(filepath)[1] == ".a":
            return None
        rootpath, filename = os.path.split(filepath)
        if filename in EXCLUDE:
            return None
        if filename.startswith("x86_64-pc-linux-gnu"):
            return None
        if (
            filename.startswith("libasan")
            or filename.startswith("libtsan")
            or filename.startswith("libubsan")
            or filename.startswith("liblsan")
        ):
            return None
        if rootpath.endswith("libexec"):
            return None
        if rootpath.endswith("doc") and filename.startswith("cmake"):
            return None
        if rootpath.endswith("share"):
            if filename.startswith("cmake") or filename.startswith("petsc"):
                return None
        return tarinfo


class MakeBinaryApp:

    def __init__(self):
        sysname, hostname, release, version, machine = os.uname()
        self.os = sysname
        self.arch = machine
        self.python_version = PYTHON_VERSION
        self.env = None

    def main(self):
        args = self._parse_command_line()
        self.base_dir = pathlib.Path(args.base_dir)
        self.pylith_branch = args.pylith_branch
        self.make_threads = args.make_threads
        self.force_config = args.force_config
        self.macos_target = None
        if self.os == "Darwin" and args.macos_target != "None":
            self.macos_target = args.macos_target

        self.src_dir = self.base_dir / "src" / "pylith_installer"
        self.dist_dir = self.base_dir / "dist"
        self.build_dir = self.base_dir / "build"

        if args.setup or args.all:
            self.setup()
        if args.configure or args.all:
            self.configure()
        if args.build or args.all:
            self.build()
        if args.package or args.all:
            self.package()

    def setup(self):
        print(f"Cleaning destination directory '{self.dist_dir}'...")
        if self.dist_dir.is_dir():
            shutil.rmtree(self.dist_dir)
        print(f"Cleaning build directory '{self.build_dir}'...")
        if self.build_dir.is_dir():
            shutil.rmtree(self.build_dir)

        self.dist_dir.mkdir(parents=True, exist_ok=True)
        self.build_dir.mkdir(parents=True, exist_ok=True)

    def configure(self):
        if self.os == "Linux":
            config_args = (
                "--enable-gcc",
                "--enable-mpi=mpich",
                "--with-mpich-options=--with-device=ch4:ofi --with-pm=gforker",
                "--enable-openssl",
                "--enable-libxcrypt",
                "--enable-libffi",
                "--enable-curl",
                "--enable-sqlite",
                "--enable-catch2",
                "--enable-python",
                "--enable-swig",
                "--enable-pcre",
                "--enable-proj",
                "--enable-hdf5",
                "--enable-cmake",
                "--enable-matplotlib",
                "--enable-pyvista",
                "--enable-gmsh",
                "--enable-tiff",
                "--with-fortran=no",
                "--with-fetch=curl",
            )
        elif self.os == "Darwin":
            config_args = (
                "--enable-mpi=mpich",
                "--with-mpich-options=--with-pm=gforker",
                "--enable-openssl",
                "--enable-libffi",
                "--enable-curl",
                "--enable-sqlite",
                "--enable-catch2",
                "--enable-python",
                "--enable-swig",
                "--enable-pcre",
                "--enable-proj",
                "--enable-hdf5",
                "--enable-cmake",
                "--enable-matplotlib",
                "--enable-pyvista",
                "--enable-gmsh",
                "--enable-tiff",
                "--with-fortran=no",
                "--with-fetch=curl",
            )

        else:
            raise ValueError(f"Unknown os '{self.os}'.")
        if "CERT_PATH" in os.environ:
            cert_path = os.environ["CERT_PATH"]
            cert_file = os.environ["CERT_FILE"]
            config_args += (
                f"--with-cert-path={cert_path}",
                f"--with-cert-file={cert_file}",
            )

        petscOptions = (
            "--download-parmetis=1",
            "--download-metis=1",
            "--download-f2cblaslapack=1",
            "--download-ml",
            "--with-fc=0",
            "--with-hwloc=0",
            "--with-ssl=0",
            "--with-x=0",
            "--with-c2html=0",
            "--with-lgrind=0",
        )

        # autoreconf
        os.chdir(self.src_dir)
        self._set_environ()
        cmd = ("autoreconf", "--install", "--force", "--verbose")
        self._run_cmd(cmd)

        # configure
        os.chdir(self.build_dir)
        cmd = (
            str(self.src_dir / "configure"),
            f"--with-make-threads={self.make_threads}",
            f"--prefix={self.dist_dir}",
        )
        if not self.pylith_branch is None:
            cmd += (f"--with-pylith-git={self.pylith_branch}",)
        if self.force_config:
            cmd += ("--enable-force-install",)

        cmd += config_args
        cmd += ("--with-petsc-options=" + " ".join(petscOptions),)
        self._run_cmd(cmd)

    def build(self):
        os.chdir(self.build_dir)
        self._set_environ()
        self._run_cmd(("make",))

    def package(self):
        if self.os == "Darwin":
            filename = "setup_macos.sh"
        elif self.os == "Linux":
            if self.arch == "x86_64":
                filename = "setup_linux.sh"
            else:
                raise ValueError(f"Unknown architecture '{self.arch}'.")
        else:
            raise ValueError(f"Unknown os '{self.os}'.")
        shutil.copyfile(
            self.src_dir / "packager" / filename, self.dist_dir / "setup.sh"
        )

        build_dir = self.build_dir / "cig" / "pylith-build"
        packager = Packager(
            build_dir=build_dir, dist_dir=self.dist_dir, macos_target=self.macos_target
        )
        packager.make_src_tarball()
        packager.make_dist_tarball()

    def _set_environ(self):
        print("Setting environment...")

        if "PYLITH_INSTALLER_PATH" in os.environ:  # Local tools needed for building
            path = os.environ["PYLITH_INSTALLER_PATH"].split(":")
        else:
            path = []
        path += (
            os.path.join(self.dist_dir, "bin"),
            "/bin",
            "/usr/bin",
            "/sbin",
            "/usr/sbin",
        )
        env = {"PATH": ":".join(path)}

        pythonpath = (
            os.path.join(
                self.dist_dir, "lib", "python%s" % self.python_version, "site-packages"
            ),
        )
        if self.arch == "x86_64":
            pythonpath += (
                os.path.join(
                    self.dist_dir,
                    "lib64",
                    "python%s" % self.python_version,
                    "site-packages",
                ),
            )
        env["PYTHONPATH"] = ":".join(pythonpath)

        if self.os == "Linux":
            ldpath = (os.path.join(self.dist_dir, "lib"),)
            if self.arch == "x86_64":
                ldpath += (os.path.join(self.dist_dir, "lib64"),)
            env["LD_LIBRARY_PATH"] = ":".join(ldpath)
        elif self.os == "Darwin" and self.macos_target:
            env["MACOSX_DEPLOYMENT_TARGET"] = self.macos_target
            MINOS_FLAGS = f"-mmacos-version-min={self.macos_target}"
            env["CFLAGS"] = MINOS_FLAGS
            env["CXXFLAGS"] = MINOS_FLAGS
            env["LDFLAGS"] = MINOS_FLAGS
            env["FI_PROVIDER"] = "tcp"
        self.env = env

    def _run_cmd(self, cmd):
        print("Running '%s'..." % " ".join(cmd))
        subprocess.run(cmd, check=True, env=self.env)

    def _parse_command_line(self):
        baseDirDefault = "/opt"

        parser = argparse.ArgumentParser()
        parser.add_argument("--setup", action="store_true", dest="setup")
        parser.add_argument("--configure", action="store_true", dest="configure")
        parser.add_argument("--build", action="store_true", dest="build")
        parser.add_argument("--package", action="store_true", dest="package")
        parser.add_argument("--all", action="store_true", dest="all")
        parser.add_argument(
            "--base-dir", action="store", dest="base_dir", default=baseDirDefault
        )
        parser.add_argument("--pylith-branch", action="store", dest="pylith_branch")
        parser.add_argument(
            "--make-threads", action="store", dest="make_threads", type=int, default=8
        )
        parser.add_argument(
            "--force-config", action="store_true", dest="force_config", default=False
        )
        parser.add_argument(
            "--macos-target", action="store", dest="macos_target", default="10.15"
        )
        args = parser.parse_args()
        return args


# ======================================================================
if __name__ == "__main__":
    MakeBinaryApp().main()
