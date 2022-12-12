# Fedora

## Fedora 35

### Operating system packages

We use the operating system packages for most of the dependencies. In
this example, we use MPICH for MPI and the corresponding HDF5 library.

```bash
dnf install -y \
    gcc \
    gcc-c++ \
    make \
    file \
    diffutils \
    automake \
    autoconf \
    libtool \
    curl \
    openssh \
    python3 \
    python3-devel \
    python3-pip \
    zlib \
    zlib-devel \
    blas \
    blas-devel \
    lapack \
    lapack-devel \
    atlas \
    atlas-devel \
    openssl \
    openssl-libs \
    unzip \
    git \
    ca-certificates \
    cppunit \
    cppunit-devel \
    mpich-devel \
    hdf5-mpich \
    hdf5-mpich-devel \
    sqlite \
    sqlite-libs \
    sqlite-devel \
    proj \
    proj-devel \
    cmake
```

### Environment variables

```
export PYTHON_VERSION=3.10
export HDF5_INCDIR=/usr/include/mpich-x86_64
export HDF5_LIBDIR=/usr/lib64/mpich/lib
PREFIX_DIR=$HOME/pylith
PATH=$PATH:/usr/lib64/mpich/bin
```

### Configure

```bash
$HOME/src/pylith/pylith-installer-3.0.3-0/configure \
    --prefix=$PREFIX_DIR \
    --with-fetch=curl \
    --with-fortran=no \
    --with-make-threads=$(nproc) \
    --with-hdf5-incdir=${HDF5_INCDIR} \
    --with-hdf5-libdir=${HDF5_LIBDIR} \
    --with-deps-prefix=${PREFIX_DIR}/dependencies \
    --disable-mpi \
    --disable-cppunit \
    --disable-cmake \
    --disable-sqlite \
    --disable-hdf5 \
    --disable-proj \
    --enable-h5py \
    --enable-netcdf \
    --enable-netcdfpy
```

## Fedora 36

### Operating system packages

We use the operating system packages for most of the dependencies. In
this example, we use MPICH for MPI and the corresponding HDF5 library.

```bash
dnf install -y \
    gcc \
    gcc-c++ \
    make \
    file \
    diffutils \
    automake \
    autoconf \
    libtool \
    curl \
    openssh \
    python3 \
    python3-devel \
    python3-pip \
    zlib \
    zlib-devel \
    blas \
    blas-devel \
    lapack \
    lapack-devel \
    atlas \
    atlas-devel \
    openssl \
    openssl-libs \
    unzip \
    git \
    ca-certificates \
    cppunit \
    cppunit-devel \
    mpich-devel \
    hdf5-mpich \
    hdf5-mpich-devel \
    sqlite \
    sqlite-libs \
    sqlite-devel \
    proj \
    proj-devel \
    cmake
```

### Environment variables

```
export PYTHON_VERSION=3.10
export HDF5_INCDIR=/usr/include/mpich-x86_64
export HDF5_LIBDIR=/usr/lib64/mpich/lib
PREFIX_DIR=$HOME/pylith
PATH=$PATH:/usr/lib64/mpich/bin
```

### Configure

```bash
$HOME/src/pylith/pylith-installer-3.0.3-0/configure \
    --prefix=$PREFIX_DIR \
    --with-fetch=curl \
    --with-fortran=no \
    --with-make-threads=$(nproc) \
    --with-hdf5-incdir=${HDF5_INCDIR} \
    --with-hdf5-libdir=${HDF5_LIBDIR} \
    --with-deps-prefix=${PREFIX_DIR}/dependencies \
    --disable-mpi \
    --disable-cppunit \
    --disable-cmake \
    --disable-sqlite \
    --disable-hdf5 \
    --disable-proj \
    --enable-h5py \
    --enable-netcdf \
    --enable-netcdfpy
```

## Fedora 37

### Operating system packages

We use the operating system packages for most of the dependencies. In
this example, we use MPICH for MPI and the corresponding HDF5 library.

```bash
dnf install -y \
    gcc \
    gcc-c++ \
    make \
    file \
    diffutils \
    automake \
    autoconf \
    libtool \
    curl \
    openssh \
    python3 \
    python3-devel \
    python3-pip \
    zlib \
    zlib-devel \
    blas \
    blas-devel \
    lapack \
    lapack-devel \
    atlas \
    atlas-devel \
    openssl \
    openssl-libs \
    unzip \
    git \
    ca-certificates \
    cppunit \
    cppunit-devel \
    mpich-devel \
    hdf5-mpich \
    hdf5-mpich-devel \
    sqlite \
    sqlite-libs \
    sqlite-devel \
    proj \
    proj-devel \
    cmake
```

### Environment variables

```
export PYTHON_VERSION=3.10
export HDF5_INCDIR=/usr/include/mpich-x86_64
export HDF5_LIBDIR=/usr/lib64/mpich/lib
PREFIX_DIR=$HOME/pylith
PATH=$PATH:/usr/lib64/mpich/bin
```

### Configure

```bash
$HOME/src/pylith/pylith-installer-3.0.3-0/configure \
    --prefix=$PREFIX_DIR \
    --with-fetch=curl \
    --with-fortran=no \
    --with-make-threads=$(nproc) \
    --with-hdf5-incdir=${HDF5_INCDIR} \
    --with-hdf5-libdir=${HDF5_LIBDIR} \
    --with-deps-prefix=${PREFIX_DIR}/dependencies \
    --disable-mpi \
    --disable-cppunit \
    --disable-cmake \
    --disable-sqlite \
    --disable-hdf5 \
    --disable-proj \
    --enable-h5py \
    --enable-netcdf \
    --enable-netcdfpy
```
