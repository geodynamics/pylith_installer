# Building for PyLith development

There are a few modifications to the usual process when using the installer to build for PyLith development.
There are several configure arguments relevant to using the installer for development:

`--enable-developer`
: Enable installation of development tools (for example, generating documentation).
PETSc is kept in its build directory to prevent conflicts when rebuilding.

`--with-pylith-repo=URL`
: Clone the PyLith source code from this URL. The URL corresponds to your fork of the PyLith repository. If you are accessing GitHub via SSH, the URL usually has the form `git@github.com:YOUR_GITHUB_USERNAME/pylith.git`. If you are accessing GitHub via HTTPS, the URL usually has the form `https://github.com/YOUR_GITHUB_USERNAME/pylith.git`. The default URL is the `geodynamics/pylith` repository, <https://github.com/geodynamics/pylith.git>.

`--with-pylith-git=BRANCH`
:  Build branch `BRANCH` of PyLith. If you are just starting development and have not created any feature branches, then use the `main` branch.

`--with-spatialdata-repo=URL`
: Clone the spatialdata source code from this URL. The default is the `geodynamics/spatialdata` repository, <https://github.com/geodynamics/spatialdata.git>. You do not need to change this unless you want to contribute to development of the spatialdata library.

Other arguments commonly used when configuring for PyLith development include:

`--with-debugging`
: Use debugging (generate debugging symbols and use low-level optimization) when building spatialdata, PETSc, and PyLith.

`--enable-swig`
: Build the SWIG library for generating the Python/C++ interface.

 `--enable-pcre`
 : Build the PCRE library for use by SWIG.

:::{tip}
We always have debugging turned on when we are developing.
We build the code in directories separate from the source code.
This makes it easy to build an optimized version in a different directory.
We use environment variables to set the paths to the desired build.
:::

## Setting up the environment

Prerequisites:

* C/C++-11 compiler
* git
* make
* fork of PyLith repository

We use the following directory structure:

```{code-block} console
pylith-developer/
├── pylith_installer-3.0.0-0 # source code for the installer
├── build-debug # top-level directory for building with debugging
└── pylith-debug # directory where PyLith and other CIG code is installed by installer
```

:::{important}
The installer will create a virtual Python environment for PyLith in `pylith-debug`.

***You will need to activate the virtual Python environment for PyLith in every shell where you rebuild or use PyLith.***

Running configure will generate a bash script `setup.sh` in the `build-debug` directory.
You should activate the virtual environment using this bash script, because we include any additional environment variables that need to be set in the setup.sh script.

```{code-block} bash
---
caption: Activate the environment using setup.sh
---
source $PYLITH_DIR/build-debug/setup.sh
```

:::

:::{note}
We do not install PETSc to `$PYLITH_DIR/pylith-debug`.
Instead we run leave its build in place.
This prevents conflicts between the installed location and the local source files when rebuilding.
:::

```{code-block} bash
---
caption: Setting up the installer for PyLith development.
---
# Set some variables to hold information about our installer setup.
# The PYLITH_REPO should be https://github.com/YOUR_GITHUB_USERNAME/pylith.git if using a personal
# access token or git@github.com:YOUR_GITHUB_USERNAME/pylith.git if using SSH.
PYLITH_DIR=$HOME/pylith-developer
PYLITH_REPO=git@github.com:YOUR_GITHUB_USERNAME/pylith.git
PYLITH_BRANCH=main

# Create a top-level directory for PyLith.
mkdir -p $PYLITH_DIR
cd $PYLITH_DIR

# Place the installer source code tarball in $PYLITH_DIR and then unpack the tarball.
tar -xf pylith_installer-3.0.0-0.tar.gz
```

## Linux

This configuration is for the Ubuntu 20.04 Linux distribution.
The setup is similar for other Linux distributions.
Some older distributions may not provide Python 3 packages for the PyLith dependencies.

Install all of the system packages listed in the [user installation for Ubuntu 20.04](../configs/ubuntu.md).
You will also need to set the `PYTHON_VERSION`, `HDF5_INCDIR`, and `HDF5_LIBDIR` environment variables as in the user installation.
Then, install the additional packages recommended for development:

```{code-block} console
apt-get install -y --no-install-recommends \
      python3-autopep8 \
      uncrustify \
      gnupg2 \
      lcov \
      gdb \
      valgrind
```

We use `autopep8` and `uncrustify` to format the source code, `gdb` and `valgrind` for debugging, and `lcov` to measure code coverage of tests.

Configure the installer.

```{code-block} bash
mkdir $PYLITH_DIR/build-debug
cd $PYLITH_DIR/build-debug
$PYLITH_DIR/pylith_installer-3.0.0-0/configure \
    --enable-developer \
    --with-debugging \
    --with-pylith-git=$PYLITH_BRANCH \
    --with-pylith-repo=$PYLITH_REPO \
    --with-fetch=curl \
    --with-make-threads=$(nproc) \
    --prefix=$PYLITH_DIR/pylith-debug \
    --with-hdf5-incdir=${HDF5_INCDIR} \
    --with-hdf5-libdir=${HDF5_LIBDIR} \
    --disable-cppunit \
    --disable-cmake \
    --disable-sqlite \
    --disable-numpy \
    --disable-hdf5 \
    --enable-h5py \
    --enable-netcdf \
    --enable-netcdfpy
```

Check the configure output to make sure it ran without errors and the configuration matches what you want.
Setup your environment, and then build the remaining dependencies and then Pythia, SpatialData, PETSc, and PyLith.

```{code-block} bash
cd $PYLITH_DIR/build-debug
source setup.sh
make
```

## macOS

:::{important}
You will need to install XCode or XCode command line tools before configuring the installer.
:::

This configuration is for Monterey (12.6.X).
We use the Apple clang/clang++ compiler.
macOS does not provide a standard installation of Python 3, so we use the installer to build Python 3.
XCode does not contain the autotools suite (automake, autoconf, libtool), so we also use the installer to build autotools.

:::{important}
When the installer builds Python, it will create a virtual environment for PyLith.
You will need to activate this virtual environment for PyLith in every shell (terminal) where you want to build or use PyLith.
You may want to add `source $PYLITH_DIR/pylith-debug/bin/activate` to your `.bashrc` or local `setup.sh` file.
:::

Configure the installer.

```{code-block} bash
mkdir $PYLITH_DIR/build-debug
cd $PYLITH_DIR/build-debug
${HOME}/src/pylith/pylith_installer-3.0.0-0/configure  \
    --enable-developer \
    --with-debugging \
    --with-pylith-git=$PYLITH_BRANCH \
    --with-pylith-repo=$PYLITH_REPO \
    --with-fetch=curl \
    --prefix=$PYLITH_DIR/pylith-debug \
    --enable-force-install \
    --with-make-threads=8 \
    --with-fortran=no \
    --enable-autotools \
    --enable-mpi=mpich \
    --enable-openssl \
    --enable-libffi \
    --enable-curl \
    --enable-sqlite \
    --enable-python \
    --enable-swig \
    --enable-pcre \
    --enable-tiff \
    --enable-proj \
    --enable-hdf5 \
    --enable-cmake \
    CC=clang CXX=clang++
```

Check the configure output to make sure it ran without errors and the configuration matches what you want.
Setup your environment, and then build the remaining dependencies and then Pythia, SpatialData, PETSc, and PyLith.

```{code-block} bash
cd $PYLITH_DIR/build-debug
source setup.sh
make
```

