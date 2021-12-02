# Building for PyLith development

:::{important}
PyLith v2.2.2 requires the versions of Pythia, nemesis, spatialdata, and PETSc at the time of the PyLith v2.2.2 release.
You cannot use the current versions of those packages with PyLith v2.2.2.
:::

:::{danger}
There are many significant changes from PyLith v2.2.2 to v3.x.
In general, any work done extending v2.2.2 will require major rewriting to be compatible with v3.x.
:::

There are a few modifications to the usual process when using the installer to build for PyLith development.
There are several configure arguments relevant to using the installer for development:

`--with-pylith-repo=URL`
: Clone the PyLith source code from this URL. The URL corresponds to your fork of the PyLith repository.
If you are accessing GitHub via SSH, the URL usually has the form `git@github.com:YOUR_GITHUB_USERNAME/pylith.git`.
If you are accessing GitHub via HTTPS, the URL usually has the form `https://github.com/YOUR_GITHUB_USERNAME/pylith.git`.
The default URL is the `geodynamics/pylith` repository, <https://github.com/geodynamics/pylith.git>.

`--with-pylith-git=BRANCH`
:  Build branch `BRANCH` of PyLith.
If you are just starting development and have not created any feature branches, then use the `main` branch.

Other arguments commonly used when configuring for PyLith development include:

`--enable-swig`
: Build the SWIG library for generating the Python/C++ interface.

 `--enable-pcre`
 : Build the PCRE library for use by SWIG.

`--enable-debugging`
: Use debugging (generate debugging symbols and use low-level optimization) when building spatialdata, PETSc, and PyLith.

:::{tip}
We always have debugging turned on when we are developing.
We build the code in directories separate from the source code.
This makes it easy to build an optimized version in a different directory.
We use environment variables to set the paths to the desired build.
:::

## Setting up the environment

Prerequisites:

* git
* make
* fork of PyLith repository

We use the following directory structure:

```bash
pylith-developer/
├── pylith_installer-2.2.2-2 # source code for the installer
├── build
│   └── debug # top-level directory for building with debugging
└── dest
    └── debug # directory where PyLith and other CIG code is installed by installer
```


```{code-block} console
---
caption: Setting up the installer for PyLith development.
---
# Set some variables to hold information about our installer setup.
# The PYLITH_REPO should be https://github.com/YOUR_GITHUB_USERNAME/pylith.git if using a personal
# access token or git@github.com:YOUR_GITHUB_USERNAME/pylith.git if using SSH.
$ PYLITH_DIR=$HOME/pylith-developer
$ PYLITH_REPO=git@github.com:YOUR_GITHUB_USERNAME/pylith.git
$ PYLITH_BRANCH=main

# Create a top-level directory for PyLith.
$ mkdir -p $PYLITH_DIR
$ cd $PYLITH_DIR

# Place the installer source code tarball in $PYLITH_DIR and then unpack the tarball.
$ tar -xf pylith_installer-2.2.2-2.tar.gz
```

## Linux

This configuration is for the Ubuntu 20.04 Linux distribution.
The setup is similar for other Linux distributions.

Install the operating system packages as listed in the [user installation for Ubuntu 20.04](../configs/ubuntu.md).
We also recommend installing the following packages.

```bash
apt-get install -y --no-install-recommends \
      gnupg2 \
      lcov \
      gdb \
      valgrind
```

We use `gdb` and `valgrind` for debugging and `lcov` to measure code coverage of tests.

Set some environment variables to aid the PyLith configuration.

```bash
export PYTHON_VERSION=2.7
export HDF5_INCDIR=/usr/include/hdf5/mpich
export HDF5_LIBDIR=/usr/lib/x86_64-linux-gnu/hdf5/mpich
```

Configure the installer.

```bash
mkdir -p $PYLITH_DIR/build/debug
cd $PYLITH_DIR/build/debug
$PYLITH_DIR/pylith-installer-2.2.2-2/configure \
    --with-pylith-git=$PYLITH_BRANCH \
    --with-pylith-repo=$PYLITH_REPO \
    --enable-debugging \
    --with-fetch=curl \
    --with-make-threads=$(nproc) \
    --prefix=$PYLITH_DIR/dest/debug \
    --with-hdf5-incdir=${HDF5_INCDIR} \
    --with-hdf5-libdir=${HDF5_LIBDIR} \
    --disable-mpi \
    --disable-cppunit \
    --disable-cmake \
    --disable-hdf5 \
	--enable-swig \
    --enable-pcre
```

Check the configure output to make sure it ran without errors and the configuration matches what you want.
Setup your environment by running `source setup.sh` (bash shell).
Just like in a user installation, you need to rerun `source setup.sh` in every terminal shell used for PyLith development, or transfer the environment settings to your `.bashrc`. 

First, we build the remaining dependencies.

```bash
cd $PYLITH_DIR/build/debug
make external_deps
```

Next, we configure and build pythia, nemesis, spatialdata, and PETSc.

```bash
cd $PYLITH_DIR/build/debug
make installed_pythia
make installed_nemesis
make installed_spatialdata
make installed_petsc
```

Finally, configure and build PyLith.

```bash
cd $PYLITH_DIR/build/debug
make installed_pylith
```

## macOS

:::{important}
You will need to install XCode or XCode command line tools before configuring the installer.
:::

This configuration is for Big Sur (11.6.x).
We use the Apple clang/clang++ compiler.
We use the installer to build autotools and Python 2.7.

Set some environment variables to aid the PyLith configuration.

```
export PYTHON_VERSION=2.7
```

Configure the installer.

```bash
${HOME}/src/pylith/pylith_installer-2.2.2-2/configure  \
    --with-pylith-git=$PYLITH_BRANCH \
    --with-pylith-repo=$PYLITH_REPO \
    --enable-debugging \
    --with-fetch=curl \
    --prefix=$PYLITH_DIR/dest/debug \
    --enable-force-install \
    --with-make-threads=4 \
    --with-fortran=no \
    --enable-autotools \
    --enable-mpi=mpich \
    --enable-openssl \
    --with-numpy-blaslapack=no \
    --enable-swig \
    --enable-pcre \
    CC=clang CXX=clang++ \
	CFLAGS="-isysroot /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk -Wno-implicit-function-declaration"```

Check the configure output to make sure it ran without errors and the configuration matches what you want.
Setup your environment by running `source setup.sh` (bash shell).
Just like in a user installation, you need to rerun `source setup.sh` in every terminal shell used for PyLith development, or transfer the environment settings to your `.bashrc`. 

First, we build the dependencies.

```bash
cd $PYLITH_DIR/build/debug
make external_deps
```

Next, we configure and build pythia, nemesis, spatialdata, and PETSc.

```bash
cd $PYLITH_DIR/build/debug
make installed_pythia
make installed_nemesis
make installed_spatialdata
make installed_petsc
```

Finally, configure and build PyLith.

```bash
cd $PYLITH_DIR/build/debug
make installed_pylith
```

## Modifying and Rebuilding PyLith

The PyLith source will be in the directory `$PYLITH_DIR/build/debug/pylith/$PYLITH_BRANCH`.
You can manage the source using Git to create branches, make commits, and push changes to your fork.

You can rebuild PyLith by running `make install` in the `$PYLITH_DIR/build/debug/pylith-build` directory.
Similarly, use `make check` to run the test suite.
