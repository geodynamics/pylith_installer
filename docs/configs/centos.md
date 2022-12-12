# CentOS

## CentOS 7 (similar to Red Hat 7)

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
    libtiff \
    libtiff-devel \
    sqlite \
    sqlite-devel \
    zlib-devel \
    libffi-devel \
    unzip \
    bzip2 \
    git \
    ca-certificates
```

### Environment variables

```
export PYTHON_VERSION 3.10
PREFIX_DIR=$HOME/pylith
export HDF5_LIBDIR=${PREFIX_DIR}/dependencies/lib
export HDF5_INCDIR=${PREFIX_DIR}/dependencies/include
```

### Configure

```bash
$HOME/src/pylith/pylith-installer-3.0.-0/configure \
    --prefix=$PREFIX_DIR \
    --with-fetch=curl \
    --with-fortran=no \
    --with-make-threads=$(nproc) \
    --with-deps-prefix=${PREFIX_DIR}/dependencies \
    --disable-cmake \
    --disable-sqlite \
    --enable-gcc \
    --enable-openssl \
    --enable-mpi=openmpi \
    --enable-cppunit \
    --enable-python \
    --enable-sqlite \
    --enable-proj \
    --enable-hdf5 \
    --enable-h5py \
    --enable-netcdf \
    --enable-netcdfpy
```

## Rocky Linux 8 (similar to RedHat 8)

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
    libcurl-devel \
    openssl \
    openssl-devel \
    zlib-devel \
    unzip \
    git \
    ca-certificates \
    python38 \
    python38-devel \
    python38-pip \
    mpich \
    mpich-devel \
    cmake \
    sqlite \
    sqlite-devel \
    libtiff \
    libtiff-devel \
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
$HOME/src/pylith/pylith-installer-3.0.-0/configure \
    --prefix=$PREFIX_DIR \
    --with-fetch=curl \
    --with-fortran=no \
    --with-make-threads=$(nproc) \
    --with-deps-prefix=${PREFIX_DIR}/dependencies \
    --disable-cmake \
    --disable-sqlite \
    --disable-cppunit \
    --enable-proj \
    --enable-hdf5 \
    --enable-h5py \
    --enable-netcdf \
    --enable-netcdfpy
```
