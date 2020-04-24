# Debian

## Debian stable (buster)

### Operating system packages

```
bash> apt-get install -y --no-install-recommends \
  g++ \
  make \
  file \
  automake \
  autoconf \
  libtool \
  curl \
  python-dev \
  libpython2.7 \
  python-setuptools \
  python-numpy \
  python-cftime \
  zlib1g-dev \
  unzip \
  git \
  ca-certificates \
  libcppunit-dev \
  libmpich-dev \
  mpich \
  libhdf5-mpich-103 \
  libhdf5-mpich-dev \
  python-h5py \
  sqlite3 \
  libsqlite3-0 \
  libsqlite3-dev \
  cmake
```

### Environment variables

```
PYTHON_VERSION=2.7
HDF5_INCDIR=/usr/include/hdf5/mpich
HDF5_LIBDIR=/usr/lib/x86_64-linux-gnu/hdf5/mpich
```

### Configure

```
bash> $HOME/src/pylith/pylith-installer-{{ site.installer-version }}/configure \
    --prefix=$PREFIX_DIR
    --with-fetch=curl \
    --with-fortran=no \
    --with-make-threads=8 \
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
    --disable-cftime \
    --enable-pcre \
    --enable-swig \
    --enable-proj \
    --enable-netcdf \
    --enable-netcdfpy
```


## Debian testing

### Operating system packages

```
bash> apt-get install -y --no-install-recommends \
  g++ \
  make \
  file \
  automake \
  autoconf \
  libtool \
  curl \
  python-dev \
  libpython2.7 \
  python-setuptools \
  python-numpy \
  python-six \
  cython \
  zlib1g-dev \
  unzip \
  git \
  ca-certificates \
  libcppunit-dev \
  libopenmpi-dev \
  libopenmpi3 \
  openmpi-bin \
  openmpi-common \
  libhdf5-openmpi-103 \
  libhdf5-openmpi-dev \
  sqlite3 \
  libsqlite3-0 \
  libsqlite3-dev \
  cmake
```

### Environment variables

```
PYTHON_VERSION=2.7
HDF5_INCDIR=/usr/include/hdf5/openmpi
HDF5_LIBDIR=/usr/lib/x86_64-linux-gnu/hdf5/openmpi
```

### Configure

```
bash> $HOME/src/pylith/pylith-installer-{{ site.installer-version }}/configure \
    --prefix=$PREFIX_DIR
    --with-fetch=curl \
    --with-fortran=no \
    --with-make-threads=8 \
    --with-hdf5-incdir=$HDF5_INCDIR \
    --with-hdf5-libdir=$HDF5_LIBDIR \
    --with-deps-prefix=$PREFIX_DIR/dependencies \
    --disable-mpi \
    --disable-cppunit \
    --disable-cmake \
    --disable-sqlite \
    --disable-numpy \
    --disable-hdf5 \
    --enable-pcre \
    --enable-swig \
    --enable-proj \
    --enable-h5py \
    --enable-cftime \
    --enable-netcdf \
    --enable-netcdfpy
```
