#!/usr/bin/env python3
#
# ----------------------------------------------------------------------
#
# Brad T. Aagaard, U.S. Geological Survey
# Charles A. Williams, GNS Science
# Matthew G. Knepley, University at Buffalo
#
# This code was developed as part of the Computational Infrastructure
# for Geodynamics (http://geodynamics.org).
#
# Copyright (c) 2010-2022 University of California, Davis
#
# See LICENSE.md for license information.
#
# ----------------------------------------------------------------------
#
# Create binary tarballs on Unix style systems.
#
# Step 1: Clone pylith_installer repository.
# Step 2: Use this utility to create tarballs.
#   Source setup.sh after running --configure.

import os
import stat
import shutil
import subprocess
import argparse
import pathlib
import tarfile
import platform
from distutils.sysconfig import parse_makefile

class Darwin:

    @staticmethod
    def update_linking(dist_dir):
        for filepath in dist_dir.glob("bin/*"):
            Darwin.update_deplibs(filepath)
        for filepath in dist_dir.glob("*/*.dylib"):
            Darwin.update_deplibs(filepath)
        for filepath in dist_dir.glob("**/*.so"):
            Darwin.update_deplibs(filepath)

    @staticmethod
    def update_deplibs(filename):
        if filename.is_symlink() or filename.is_dir():
            return

        proc = subprocess.run(["otool", "-L", filename], stdout=subprocess.PIPE, check=True)
        output = proc.stdout.decode("utf-8")
        deplibs = []
        for line in output.split("\t")[1:]:
            deplibs.append(line.split()[0])
        for libPathAbs in deplibs:
            if libPathAbs.startswith("/usr") or libPathAbs.startswith("/System"):
                continue
            if libPathAbs.startswith("@loader_path"):
                continue
            libName = os.path.split(libPathAbs)[1]
            libPathNew = f"@executable_path/../lib/{libName}"
            cmd = ["install_name_tool", "-change", libPathAbs, libPathNew, str(filename)]
            subprocess.run(cmd, check=True)


class Packager:

    def __init__(self, dist_dir, build_dir):
        self.dist_dir = dist_dir
        self.build_dir = build_dir

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

    def _get_makeinfo(self):
        os.chdir(self.build_dir)
        makefile = parse_makefile("Makefile")
        self.make = {
            "package_name": makefile["PACKAGE_NAME"],
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
                if line.startswith(f"#!{old_path}"):
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

    @staticmethod
    def _get_arch():
        op_sys = platform.system().lower()
        if op_sys=="darwin":
            mac_ver = platform.mac_ver()
            if "OSX_DEPLOYMENT_TARGET" in os.environ:
                target = os.environ["OSX_DEPLOYMENT_TARGET"]
            else:
                target = mac_ver[0]
            arch = f"macOS-{target}-{mac_ver[2]}"
        else:
            machine = (platform.processor() or platform.machine())
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
            "python", # use python3
            "lto-dump",
            "swig",
            )
        filepath = tarinfo.name
        if os.path.splitext(filepath)[1] == ".a":
            return None
        rootpath, filename = os.path.split(filepath)
        if filename in EXCLUDE:
            return None
        if filename.startswith("x86_64-pc-linux-gnu"):
            return None
        if filename.startswith("libasan") or \
            filename.startswith("libtsan") or \
            filename.startswith("libubsan") or \
            filename.startswith("liblsan"):
            return None
        if rootpath.endswith("libexec"):
            return None
        if rootpath.endswith("doc") and filename.startswith("cmake"):
            return None
        if rootpath.endswith("share"):
            if filename.startswith("cmake") or \
              filename.startswith("petsc"):
                return None
        return tarinfo


class MakeBinaryApp:

    MACOS_DEPLOYMENT_TARGET = "10.15"
    
    def __init__(self):
        sysname, hostname, release, version, machine = os.uname()
        self.os = sysname
        self.arch = machine
        self.python_version = "3.9" # :KLUDGE:

    def main(self):
        args = self._parse_command_line()
        self.base_dir = pathlib.Path(args.base_dir)
        self.pylith_branch = args.pylith_branch
        self.make_threads = args.make_threads
        self.force_config = args.force_config

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
            config_args = ("--enable-gcc",
                          "--enable-mpi=mpich",
                          "--enable-openssl",
                          "--enable-libffi", 
                          "--enable-curl",
                          "--enable-sqlite",
                          "--enable-cppunit",
                          "--enable-python", 
                          "--enable-swig",
                          "--enable-pcre",
                          "--enable-proj",
                          "--enable-hdf5",
                          "--enable-cmake",
                          "--enable-addons",
                          "--enable-tiff",
                          "--with-fortran=no",
                          "--with-fetch=curl",
                      )
        elif self.os == "Darwin":
            config_args = ("--enable-mpi=mpich",
                          "--enable-openssl",
                          "--enable-libffi", 
                          "--enable-curl", 
                          "--enable-sqlite",
                          "--enable-cppunit",
                          "--enable-python",
                          "--enable-swig",
                          "--enable-pcre",
                          "--enable-proj",
                          "--enable-hdf5",
                          "--enable-cmake",
                          "--enable-addons",
                          "--enable-tiff",
                          "--with-fortran=no",
                          "--with-fetch=curl",
                          )

        else:
            raise ValueError(f"Unknown os '{self.os}'.")
        if "CERT_PATH" in os.environ:
            config_args += ("--with-cert-path=${CERT_PATH}", "--with-cert-file=${CERT_FILE}")

        petscOptions = ("--download-chaco=1",
                        "--download-f2cblaslapack=1",
                        "--with-fc=0",
                        "--with-hwloc=0",
                        "--with-ssl=0",
                        "--with-x=0",
                        "--with-c2html=0",
                        "--with-lgrind=0",
                        )

        # autoreconf
        os.chdir(self.src_dir)
        cmd = ("autoreconf", "--install", "--force", "--verbose")
        self._run_cmd(cmd)
        self._setEnviron()

        # configure
        os.chdir(self.build_dir)
        cmd = (str(self.src_dir / "configure"),
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
        self._setEnviron()

        cmd = ("make",)
        self._run_cmd(cmd)

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
        shutil.copyfile(self.src_dir / "packager" / filename, self.dist_dir / "setup.sh")

        build_dir = self.build_dir / "cig" / "pylith-build"
        packager = Packager(build_dir=build_dir, dist_dir=self.dist_dir)
        packager.make_src_tarball()
        packager.make_dist_tarball()

    def _parse_command_line(self):
        baseDirDefault = "/opt"

        parser = argparse.ArgumentParser()
        parser.add_argument("--setup", action="store_true", dest="setup")
        parser.add_argument("--configure", action="store_true", dest="configure")
        parser.add_argument("--build", action="store_true", dest="build")
        parser.add_argument("--package", action="store_true", dest="package")
        parser.add_argument("--all", action="store_true", dest="all")
        parser.add_argument("--base-dir", action="store", dest="base_dir", default=baseDirDefault)
        parser.add_argument("--pylith-branch", action="store", dest="pylith_branch")
        parser.add_argument("--make-threads", action="store", dest="make_threads", type=int, default=8)
        parser.add_argument("--force-config", action="store_true", dest="force_config", default=False)
        args = parser.parse_args()
        return args

    
    def _setEnviron(self):
        print("Setting environment...")

        if "PYLITH_INSTALLER_PATH" in os.environ: # Local tools needed for building
            path = os.environ["PYLITH_INSTALLER_PATH"].split(":")
        else:
            path = []
        path += (os.path.join(self.dist_dir, "bin"),
                "/bin",
                "/usr/bin",
                "/sbin",
                "/usr/sbin",
        )
        os.environ["PATH"] = ":".join(path)

        pythonpath = (os.path.join(self.dist_dir, "lib", "python%s" % self.python_version, "site-packages"),)
        if self.arch == "x86_64":
            pythonpath += (os.path.join(self.dist_dir, "lib64", "python%s" % self.python_version, "site-packages"),)
        os.environ["PYTHONPATH"] = ":".join(pythonpath)
        
        if self.os == "Linux":
            ldpath = (os.path.join(self.dist_dir, "lib"),)
            if self.arch == "x86_64":
                ldpath += (os.path.join(self.dist_dir, "lib64"),)
            os.environ["LD_LIBRARY_PATH"] = ":".join(ldpath)
        elif self.os == "Darwin":
            os.environ["OSX_DEPLOYMENT_TARGET"] = self.MACOS_DEPLOYMENT_TARGET
            
        return

    def _run_cmd(self, cmd):
        print("Running '%s'..." % " ".join(cmd))
        subprocess.check_call(cmd)


# ======================================================================
if __name__ == "__main__":
    MakeBinaryApp().main()
