# Debian

## Debian stable (bullseye)

### Operating system packages

```bash
apt-get install -y --no-install-recommends \
      g++ \
      make \
      file \
      automake \
      autoconf \
      libtool \
      curl \
      libcurl4 \
      libcurl4-openssl-dev \
      openssl \
      libssl3 \
      libssl-dev \
      python3-dev \
      libpython3.11 \
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
      libtiff5 \
      libtiff5-dev \
      libproj-dev \
      proj-bin \
      proj-data \
      cmake
```

### Environment variables

```
PYTHON_VERSION=3.11
HDF5_INCDIR=/usr/include/hdf5/mpich
HDF5_LIBDIR=/usr/lib/x86_64-linux-gnu/hdf5/mpich
```

### Configure

```bash
$HOME/src/pylith/pylith-installer-4.1.1-0/configure \
    --prefix=$PREFIX_DIR \
    --with-fetch=curl \
    --with-fortran=no \
    --with-make-threads=$(nproc) \
    --with-hdf5-incdir=$HDF5_INCDIR \
    --with-hdf5-libdir=$HDF5_LIBDIR \
    --with-deps-prefix=$PREFIX_DIR/dependencies \
    --disable-mpi \
    --disable-hdf5 \
    --disable-sqlite \
    --disable-cmake \
    --disable-proj \
    --enable-catch2 \
    --enable-h5py \
    --enable-netcdf \
    --enable-netcdfpy
```

## Debian testing (bookworm)

### Operating system packages

```bash
apt-get install -y --no-install-recommends \
      g++ \
      make \
      file \
      automake \
      autoconf \
      libtool \
      curl \
      ssh \
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
      libproj-dev \
      proj-bin \
      proj-data \
      cmake
```

### Environment variables

```
PYTHON_VERSION=3.11
HDF5_INCDIR=/usr/include/hdf5/openmpi
HDF5_LIBDIR=/usr/lib/x86_64-linux-gnu/hdf5/openmpi
```

### Configure

```bash
$HOME/src/pylith/pylith-installer-4.1.1-0/configure \
    --prefix=$PREFIX_DIR \
    --with-fetch=curl \
    --with-fortran=no \
    --with-make-threads=$(nproc) \
    --with-hdf5-incdir=$HDF5_INCDIR \
    --with-hdf5-libdir=$HDF5_LIBDIR \
    --with-deps-prefix=$PREFIX_DIR/dependencies \
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
