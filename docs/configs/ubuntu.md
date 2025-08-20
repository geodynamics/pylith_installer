# Ubuntu

## Ubuntu 20.04

### Operating system packages

We use the operating system packages for most of the dependencies. In
this example, we use MPICH for MPI and the corresponding HDF5 library.

```bash
apt-get install -y --no-install-recommends \
      g++ \
      make \
      file \
      automake \
      autoconf \
      libtool \
      curl \
      libcurl4-openssl-dev \
      python3-dev \
      libpython3.8 \
      python3-venv \
      python3-pip \
      zlib1g-dev \
      unzip \
      git \
      ca-certificates \
      libmpich-dev \
      mpich \
      libhdf5-mpich-103 \
      libhdf5-mpich-dev \
      sqlite3 \
      libsqlite3-0 \
      libsqlite3-dev \
      proj-bin \
      proj-data \
      libproj-dev \
      openssl \
      libssl1.1 \
      libssl-dev
```

### Environment variables

```bash
export PYTHON_VERSION=3.8
export HDF5_INCDIR=/usr/include/hdf5/mpich
export HDF5_LIBDIR=/usr/lib/x86_64-linux-gnu/hdf5/mpich
PREFIX_DIR=$HOME/pylith
```

### Configure

```bash
$HOME/src/pylith/pylith-installer-4.2.1-0/configure \
    --prefix=$PREFIX_DIR \
    --with-fetch=curl \
    --with-fortran=no \
    --with-make-threads=$(nproc) \
    --with-hdf5-incdir=${HDF5_INCDIR} \
    --with-hdf5-libdir=${HDF5_LIBDIR} \
    --disable-mpi \
    --disable-sqlite \
    --disable-hdf5 \
    --disable-proj \
    --enable-cmake \
    --enable-catch2 \
    --enable-h5py \
    --enable-netcdf \
    --enable-netcdfpy
```

## Ubuntu 22.04

### Operating system packages

We use the operating system packages for most of the dependencies. In
this example, we use MPICH for MPI and the corresponding HDF5 library.

```bash
apt-get install -y --no-install-recommends \
      g++ \
      make \
      file \
      automake \
      autoconf \
      libtool \
      curl \
      python3-dev \
      libpython3.10 \
      python3-venv \
      python3-pip \
      zlib1g-dev \
      unzip \
      git \
      ca-certificates \
      libmpich-dev \
      mpich \
      libhdf5-mpich-103-1 \
      libhdf5-mpich-dev \
      sqlite3 \
      libsqlite3-0 \
      libsqlite3-dev \
      proj-bin \
      proj-data \
      libproj-dev \
      cmake 
```

### Environment variables

```bash
export PYTHON_VERSION=3.10
export HDF5_INCDIR=/usr/include/hdf5/mpich
export HDF5_LIBDIR=/usr/lib/x86_64-linux-gnu/hdf5/mpich
PREFIX_DIR=$HOME/pylith
```

### Configure

```bash
$HOME/src/pylith/pylith-installer-4.2.1-0/configure \
    --prefix=$PREFIX_DIR \
    --with-fetch=curl \
    --with-fortran=no \
    --with-make-threads=$(nproc) \
    --with-hdf5-incdir=${HDF5_INCDIR} \
    --with-hdf5-libdir=${HDF5_LIBDIR} \
    --disable-mpi \
    --disable-sqlite \
    --disable-hdf5 \
    --disable-proj \
    --enable-catch2 \
    --enable-h5py \
    --enable-netcdf \
    --enable-netcdfpy
```

## Ubuntu 23.04

### Operating system packages

We use the operating system packages for most of the dependencies. In
this example, we use OpenMPI for MPI and the corresponding HDF5 library.

```bash
apt-get install -y --no-install-recommends \
      g++ \
      make \
      file \
      automake \
      autoconf \
      libtool \
      curl \
      python3-dev \
      libpython3.11 \
      python3-venv \
      python3-pip \
      zlib1g-dev \
      unzip \
      git \
      ca-certificates \
      libopenmpi-dev \
      libopenmpi3 \
      openmpi-bin \
      openmpi-common \
      libhdf5-openmpi-103-1 \
      libhdf5-openmpi-dev \
      sqlite3 \
      libsqlite3-0 \
      libsqlite3-dev \
      proj-bin \
      proj-data \
      libproj-dev \
      cmake
```

### Environment variables

```bash
export PYTHON_VERSION=3.11
export HDF5_INCDIR=/usr/include/hdf5/openmpi
export HDF5_LIBDIR=/usr/lib/x86_64-linux-gnu/hdf5/openmpi
PREFIX_DIR=$HOME/pylith
```

### Configure

```bash
$HOME/src/pylith/pylith-installer-4.2.1-0/configure \
    --prefix=$PREFIX_DIR \
    --with-fetch=curl \
    --with-fortran=no \
    --with-make-threads=$(nproc) \
    --with-hdf5-incdir=${HDF5_INCDIR} \
    --with-hdf5-libdir=${HDF5_LIBDIR} \
    --with-deps-prefix=${PREFIX_DIR}/dependencies \
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

## Ubuntu 23.10

### Operating system packages

We use the operating system packages for most of the dependencies. In
this example, we use MPICH for MPI and the corresponding HDF5 library.

```bash
apt-get install -y --no-install-recommends \
      g++ \
      make \
      file \
      automake \
      autoconf \
      libtool \
      curl \
      python3-dev \
      libpython3.11 \
      python3-venv \
      python3-pip \
      zlib1g-dev \
      unzip \
      git \
      ca-certificates \
      libmpich-dev \
      libmpich \
      libhdf5-mpich-103-1 \
      libhdf5-mpich-dev \
      sqlite3 \
      libsqlite3-0 \
      libsqlite3-dev \
      proj-bin \
      proj-data \
      libproj-dev \
      cmake
```

### Environment variables

```bash
export PYTHON_VERSION=3.11
export HDF5_INCDIR=/usr/include/hdf5/mpich
export HDF5_LIBDIR=/usr/lib/x86_64-linux-gnu/hdf5/mpich
PREFIX_DIR=$HOME/pylith
```

### Configure

```bash
$HOME/src/pylith/pylith-installer-4.2.1-0/configure \
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
