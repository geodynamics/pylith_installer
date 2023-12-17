# Fedora

## Fedora 38

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
export PYTHON_VERSION=3.11
export HDF5_INCDIR=/usr/include/mpich-x86_64
export HDF5_LIBDIR=/usr/lib64/mpich/lib
PREFIX_DIR=$HOME/pylith
PATH=$PATH:/usr/lib64/mpich/bin
```

### Configure

```bash
$HOME/src/pylith/pylith-installer-4.0.0-0/configure \
    --prefix=$PREFIX_DIR \
    --with-fetch=curl \
    --with-fortran=no \
    --with-make-threads=$(nproc) \
    --with-hdf5-incdir=${HDF5_INCDIR} \
    --with-hdf5-libdir=${HDF5_LIBDIR} \
    --disable-mpi \
    --disable-cmake \
    --disable-sqlite \
    --disable-hdf5 \
    --disable-proj \
    --enable-catch2 \
    --enable-h5py \
    --enable-netcdf \
    --enable-netcdfpy
```

## Fedora 39

### Operating system packages

We use the operating system packages for most of the dependencies. In
this example, we use OpenMPI for MPI and the corresponding HDF5 library.

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
    openmpi-devel \
    hdf5-openmpi \
    hdf5-openmpi-devel \
    sqlite \
    sqlite-libs \
    sqlite-devel \
    proj \
    proj-devel \
    cmake
```

### Environment variables

```
export PYTHON_VERSION=3.12
export HDF5_INCDIR=/usr/include/openmpi-x86_64
export HDF5_LIBDIR=/usr/lib64/openmpi/lib
PREFIX_DIR=$HOME/pylith
PATH=$PATH:/usr/lib64/openmpi/bin
```

### Configure

```bash
$HOME/src/pylith/pylith-installer-4.0.0-0/configure \
    --prefix=$PREFIX_DIR \
    --with-fetch=curl \
    --with-fortran=no \
    --with-make-threads=$(nproc) \
    --with-hdf5-incdir=${HDF5_INCDIR} \
    --with-hdf5-libdir=${HDF5_LIBDIR} \
    --disable-mpi \
    --disable-cmake \
    --disable-sqlite \
    --disable-hdf5 \
    --disable-proj \
    --enable-catch2 \
    --enable-h5py \
    --enable-netcdf \
    --enable-netcdfpy
```
