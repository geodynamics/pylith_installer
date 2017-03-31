#!/usr/bin/env python
#
# ----------------------------------------------------------------------
#
# Brad T. Aagaard, U.S. Geological Survey
# Charles A. Williams, GNS Science
# Matthew G. Knepley, University of Chicago
#
# This code was developed as part of the Computational Infrastructure
# for Geodynamics (http://geodynamics.org).
#
# Copyright (c) 2010-2016 University of California, Davis
#
# See COPYING for license information.
#
# ----------------------------------------------------------------------
#
# Create binary tarballs on Unix style systems.
#
# Step 1: Clone pylith_installer repository.
# Step 2: Use this utility to create tarballs.
#   Source setup.sh after running --configure.

import os
import shutil
import subprocess

class BinaryApp(object):

    def __init__(self, base_dir, pylith_branch, nthreads, force_config):
        self.baseDir = base_dir
        self.pylithBranch = pylith_branch
        self.nthreads = nthreads
        self.forceConfig = force_config

        self.srcDir = os.path.join(base_dir, "src", "pylith_installer")
        self.destDir = os.path.join(base_dir, "dist")
        self.buildDir = os.path.join(base_dir, "build")

        sysname, hostname, release, version, machine = os.uname()
        self.os = sysname
        self.arch = machine
        self.pythonVersion = "2.7" # :KLUDGE:
        return


    def setup(self):
        print("Cleaning destination directory '%s'..." % self.destDir)
        if os.path.isdir(self.destDir):
            shutil.rmtree(self.destDir)
        print("Cleaning build directory '%s'..." % self.buildDir)
        if os.path.isdir(self.buildDir):
            shutil.rmtree(self.buildDir)

        os.mkdir(self.destDir)
        os.mkdir(self.buildDir)
        return


    def configure(self):
        if self.os == "Linux":
            configArgs = ("--enable-gcc",
                          "--enable-python", 
                          "--enable-mpi=mpich",
                          "--enable-cppunit",
                          "--enable-numpy",
                          "--with-numpy-blaslapack",
                          "--enable-proj4",
                          "--enable-hdf5",
                          "--enable-netcdfpy",
                          "--enable-cmake",
                          "--enable-nemesis",
                          "--enable-fiat",
                          "--enable-pcre",
                          "--enable-swig",
                          "--enable-setuptools",
                      )
            petscOptions = ("--download-chaco=1",
                            "--download-ml=1",
                            "--download-f2cblaslapack=1",
                            "--with-hwloc=0",
                            "--with-ssl=0",
                            "--with-x=0",
                            "--with-c2html=0",
                            "--with-lgrind=0",
                            )
        elif self.os == "Darwin":
            configArgs = ("--enable-autotools",
                          "--enable-mpi=mpich",
                          "--enable-swig",
                          "--enable-pcre",
                          "--enable-numpy",
                          "--enable-cmake",
                          "--with-fortran=no",
                          "--with-fetch=curl",
                          )
            petscOptions = ("--download-chaco=1",
                            "--download-ml",
                            "--with-fc=0",
                            "--with-hwloc=0",
                            "--with-ssl=0",
                            "--with-x=0",
                            "--with-c2html=0",
                            "--with-lgrind=0",
                            "--with-blas-lib=/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/Versions/Current/libBLAS.dylib",
                            "--with-lapack-lib=/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/Versions/Current/libLAPACK.dylib",
                            )
        else:
            raise ValueError("Unknown os '%s'." % self.os)

        # autoreconf
        os.chdir(self.srcDir)
        cmd = ("autoreconf", "--install", "--force", "--verbose")
        self._runCmd(cmd)

        self._setEnviron()

        # configure
        os.chdir(self.buildDir)
        cmd = ("%s" % os.path.join(self.srcDir, "configure"),
               "--with-make-threads=%d" % self.nthreads,
               "--prefix=%s" % self.destDir,
        )
        if not self.pylithBranch is None:
            cmd += ("--with-pylith-git=%s" % self.pylithBranch,)
        if self.forceConfig:
            cmd += ("--enable-force-install",)

        cmd += configArgs
        cmd += ("--with-petsc-options=%s" % " ".join(petscOptions),)
        self._runCmd(cmd)
        return


    def build(self):
        os.chdir(self.buildDir)
        self._setEnviron()

        cmd = ("make",)
        self._runCmd(cmd)
        return


    def package(self):
        if self.os == "Darwin":
            filename = "setup_darwin.sh"
        elif self.os == "Linux":
            if self.arch == "x86_64":
                filename = "setup_linux64.sh"
            elif self.arch == "i686":
                filename = "setup_linux32.sh"
            else:
                raise ValueError("Unknown architecture '%s'." % self.arch)
        else:
            raise ValueError("Unknown os '%s'." % self.os)

        shutil.copyfile(os.path.join(self.srcDir, "packager", filename), os.path.join(self.destDir, "setup.sh"))
        os.chdir(os.path.join(self.buildDir, "pylith-build"))
        cmd = (os.path.join(self.srcDir, "packager", "make_package.py"),)
        self._runCmd(cmd)

        # Darwin
        if self.os == "Darwin":
            print("May need to add 'tar-pax' to AM_INIT_AUTOMAKE in pylith src/configure.ac to get 'make dist' to work in pylith-build.")
            print("Unpack tarball, unzip Python eggs (netCDF4)")
            print("Run packager/update_darwinlinking.py")
            print("Update Python eggs (zip -ru EGG DIR)")
            print("Regenerate tarball")
        return


    def _setEnviron(self):
        print("Setting environment...")

        path = (os.path.join(self.destDir, "bin"),
                "/bin", 
                "/usr/bin",
        )
        os.environ["PATH"] = ":".join(path)

        pythonpath = (os.path.join(self.destDir, "lib", "python%s" % self.pythonVersion, "site-packages"),)
        if self.arch == "x86_64":
            pythonpath += (os.path.join(self.destDir, "lib64", "python%s" % self.pythonVersion, "site-packages"),)
        os.environ["PYTHONPATH"] = ":".join(pythonpath)
        
        if self.os == "Linux":
            ldpath = (os.path.join(self.destDir, "lib"),)
            if self.arch == "x86_64":
                ldpath += (os.path.join(self.destDir, "lib64"),)
            os.environ["LD_LIBRARY_PATH"] = ":".join(ldpath)
        return


    def _runCmd(self, cmd):
        print("Running '%s'..." % " ".join(cmd))
        subprocess.check_call(cmd)
        return

    
# ======================================================================
if __name__ == "__main__":
    import argparse

    baseDirDefault = os.path.join(os.environ["HOME"], "pylith-binary")

    parser = argparse.ArgumentParser()
    parser.add_argument("--setup", action="store_true", dest="setup")
    parser.add_argument("--configure", action="store_true", dest="configure")
    parser.add_argument("--build", action="store_true", dest="build")
    parser.add_argument("--package", action="store_true", dest="package")
    parser.add_argument("--all", action="store_true", dest="all")
    parser.add_argument("--base-dir", action="store", dest="base_dir", default=baseDirDefault)
    parser.add_argument("--pylith-branch", action="store", dest="pylith_branch")
    parser.add_argument("--make-threads", action="store", dest="make_threads", type=int, default=4)
    parser.add_argument("--force-config", action="store", dest="force_config", default=False)
    args = parser.parse_args()

    app = BinaryApp(args.base_dir, args.pylith_branch, args.make_threads, args.force_config)

    if args.setup or args.all:
        app.setup()

    if args.configure or args.all:
        app.configure()

    if args.build or args.all:
        app.build()
        
    if args.package or args.all:
        app.package()
        
    
# End of file


