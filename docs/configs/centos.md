# CentOS

## CentOS 7

CentOS 7 does not (by default) provide a C++11 compiler. As a result,
we use the installer to build a more recent gcc version and only use a
few operating system packages to satisfy PyLith dependency requirements.

### Operating system packages

```bash
yum install -y \
    gcc \
    gcc-c++ \
    make \
    file \
    which \
    diffutils \
    gettext \
    automake \
    autoconf \
    libtool \
    curl \
    curl-devel \
    openssh \
    openssl \
    openssl-devel \
    sqlite \
    sqlite-devel \
    zlib-devel \
    libffi-devel \
    unzip \
    bzip2 \
    git \
    ca-certificates \
    cmake
```

### Environment variables

```
export PYTHON_VERSION 3.9
PREFIX_DIR=$HOME/pylith
```

### Configure

```bash
$HOME/src/pylith/pylith-installer-3.0.0-0/configure \
    --prefix=$PREFIX_DIR \
    --with-fetch=curl \
    --with-fortran=no \
    --with-make-threads=$(nproc) \
    --with-deps-prefix=${PREFIX_DIR}/dependencies \
    --disable-cmake \
    --disable-sqlite \
    --enable-gcc \
    --enable-mpi=openmpi \
    --enable-cppunit \
    --enable-python \
    --enable-setuptools \
    --enable-cython \
    --enable-pcre \
    --enable-swig \
    --enable-proj \
    --enable-numpy \
    --enable-six \
    --enable-cftime \
    --enable-hdf5 \
    --enable-h5py \
    --enable-netcdf \
    --enable-netcdfpy
```


## CentOS 8

### Operating system packages


```bash
dnf install -y \
    gcc \
    gcc-c++ \
    redhat-rpm-config \
    make \
    file \
    which \
    diffutils \
    automake \
    autoconf \
    libtool \
    curl \
    openssl \
    openssl-devel \
    zlib-devel \
    unzip \
    git \
    ca-certificates \
    python38 \
    python38-devel \
    python38-pip \
    python38-setuptools \
    python38-six \
    python38-numpy \
    python38-Cython \
    python3-coverage \
    mpich \
    mpich-devel \
    cmake \
    sqlite \
    sqlite-devel \
    dnf-plugins-core
#
# Use python3.8 for python3	
alternatives --set python3 /usr/bin/python3.8
#
# We enable use of the powertools repository so that we can install CppUnit.
dnf config-manager --set-enabled powertools && dnf install -y cppunit cppunit-devel
```

### Environment variables

```
PATH=$PATH:/usr/lib64/mpich/bin
export PYTHON_VERSION 3.8
PREFIX_DIR=$HOME/pylith
export HDF5_LIBDIR=${PREFIX_DIR}/dependencies/lib
export HDF5_INCDIR=${PREFIX_DIR}/dependencies/include
```

### Configure

```bash
$HOME/src/pylith/pylith-installer-3.0.0-0/configure \
    --prefix=$PREFIX_DIR \
    --with-fetch=curl \
    --with-fortran=no \
    --with-make-threads=$(nproc) \
    --with-deps-prefix=${PREFIX_DIR}/dependencies \
    --disable-cmake \
    --disable-sqlite \
    --disable-setuptools \
    --disable-numpy \
    --disable-six \
    --disable-cppunit \
    --enable-pcre \
    --enable-swig \
    --enable-proj \
    --enable-cftime \
    --enable-hdf5 \
    --enable-h5py \
    --enable-netcdf \
    --enable-netcdfpy
```
