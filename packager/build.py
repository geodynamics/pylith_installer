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

import os
import shutil
import subprocess

class BinaryApp(object):

    def __init__(self, base_dir, pylith_branch, nthreads):
        self.baseDir = base_dir
        self.pylithBranch = pylith_branch
        self.nthreads = nthreads

        self.srcDir = os.join(base_dir, "src", "pylith_installer")
        self.destDir = os.join(base_dir, "dist")
        self.buildDir = os.join(base_dir, "build")

        sysname, hostname, release, version, machine = os.uname()
        self.os = sysname
        self.arch = machine
        return


    def setup(self):
        shutil.rmtree(self.destDir)
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
        cmd = "autoreconf --install --force --verbose"
        self._runCmd(cmd)

        if os.environ.has_key("PYTHONPATH"):
            del os.environ["PYTHONPATH"]
        if os.environ.has_key("LD_LIBRARY_PATH"):
            del os.environ["LD_LIBRARY_PATH"]
        os.environ["PATH"] = "/bin:/usr/bin"

        # configure
        os.chdir(self.buildDir)
        cmd = "%(configure)s --with-pylith-git=%(pylith_branch)s --with-make-threads=%(nthreads)d --prefix=%(dest_dir)s %(config_args)s --with-petsc-options=%(petsc_options)s" % {
            'configure': os.join(srcDir, "configure"),
            'pylith_branch': self.pylithBranch,
            'nthreads': self.nthreads,
            'dest_dir': self.destDir,
            'config_args': " ".join(configArgs),
            'petsc_options': " ".join(petscOptions),
        }
        self._runCmd(cmd)
        return


    def build(self):
        os.chdir(self.buildDir)
        cmd = ". %s" % os.path.join(self.buildDir, "setup.sh")
        self._runCmd(cmd)
        self._runCmd("make >& make.log")
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
        self._runCmd(os.path.join(self.srcDir, "packager", "make_package.py"))

        # Darwin
        if self.os == "Darwin":
            print("Unpack tarball, unzip Python eggs (netCDF4)")
            print("Run packager/update_darwinlinking.py")
            print("Update Python eggs (zip -ru EGG DIR)")
            print("Regenerate tarball")
        return


    def _runCmd(self, cmd):
        print("Running '%s'..." % cmd)
        subprocess.check_call(cmd.split())
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
    parser.add_argument("--pylith-branch", action="store", dest="pylith_branch", default="master")
    parser.add_argument("--make-threads", action="store", dest="make_threads", type=int, default=4)
    args = parser.parse_args()

    app = BinaryApp(args.base_dir, args.pylith_branch, args.make_threads)

    if args.setup or args.all:
        app.setup()

    if args.configure or args.all:
        app.configure()

    if args.build or args.all:
        app.build()
        
    if args.package or args.all:
        app.package()
        
    
# End of file


