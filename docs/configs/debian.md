# Debian

## Debian stable (buster)

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
      python3-dev \
      libpython3.7 \
      python3-pip \
      python3-setuptools \
      python3-numpy \
      python3-cftime \
      python3-coverage \
      python3-h5py \
      zlib1g-dev \
      unzip \
      git \
      ca-certificates \
      libcppunit-dev \
      libmpich-dev \
      mpich \
      libhdf5-mpich-103 \
      libhdf5-mpich-dev \
      sqlite3 \
      libsqlite3-0 \
      libsqlite3-dev \
      cmake
```

### Environment variables

```
PYTHON_VERSION=3.7
HDF5_INCDIR=/usr/include/hdf5/mpich
HDF5_LIBDIR=/usr/lib/x86_64-linux-gnu/hdf5/mpich
```

### Configure

```bash
$HOME/src/pylith/pylith-installer-3.0.0-0/configure \
    --prefix=$PREFIX_DIR \
    --with-fetch=curl \
    --with-fortran=no \
    --with-make-threads=$(nproc) \
    --with-hdf5-incdir=$HDF5_INCDIR \
    --with-hdf5-libdir=$HDF5_LIBDIR \
    --with-deps-prefix=$PREFIX_DIR/dependencies \
    --disable-mpi \
    --disable-hdf5 \
    --disable-h5py \
    --disable-cppunit \
    --disable-cmake \
    --disable-sqlite \
    --disable-numpy \
    --disable-setuptools \
    --disable-cftime \
    --enable-pcre \
    --enable-swig \
    --enable-proj \
    --enable-netcdf \
    --enable-netcdfpy
```


## Debian testing

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
      libpython3.9 \
      python3-pip \
      python3-setuptools \
      python3-numpy \
      python3-cftime \
      python3-six \
      python3-coverage \
      cython3 \
      zlib1g-dev \
      unzip \
      git \
      ca-certificates \
      libcppunit-dev \
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
      cmake \
      swig
```

### Environment variables

```
PYTHON_VERSION=3.9
HDF5_INCDIR=/usr/include/hdf5/openmpi
HDF5_LIBDIR=/usr/lib/x86_64-linux-gnu/hdf5/openmpi
```

### Configure

```bash
$HOME/src/pylith/pylith-installer-3.0.0-0/configure \
    --prefix=$PREFIX_DIR \
    --with-fetch=curl \
    --with-fortran=no \
    --with-make-threads=$(nproc) \
    --with-hdf5-incdir=$HDF5_INCDIR \
    --with-hdf5-libdir=$HDF5_LIBDIR \
    --with-deps-prefix=$PREFIX_DIR/dependencies \
    --disable-mpi \
    --disable-cppunit \
    --disable-cmake \
    --disable-sqlite \
    --disable-numpy \
    --disable-setuptools \
    --disable-cftime \
    --disable-hdf5 \
    --disable-proj \
    --enable-h5py \
    --enable-netcdf \
    --enable-netcdfpy
```
