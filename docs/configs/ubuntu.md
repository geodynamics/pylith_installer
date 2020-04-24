# Ubuntu

## Ubuntu 18.04

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
    zlib1g-dev \
    unzip \
    git \
    ca-certificates \
    libcppunit-1.14.0 \
    libcppunit-dev \
    libopenmpi-dev \
    libopenmpi2 \
    openmpi-bin \
    openmpi-common \
    libhdf5-openmpi-100 \
    libhdf5-openmpi-dev \
    python-h5py \
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
PREFIX_DIR=$HOME/pylith
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
    --disable-h5py \
    --enable-cftime \
    --enable-pcre \
    --enable-swig \
    --enable-proj \
    --enable-netcdf \
    --enable-netcdfpy
```


## Ubuntu 19.10

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

In order to set `mpicc` to the MPICH library, we use `update-alternatives`:
```
bash> update-alternatives --set mpi /usr/bin/mpicc.mpich
```

### Environment variables

```
PYTHON_VERSION=2.7
HDF5_INCDIR=/usr/include/hdf5/mpich
HDF5_LIBDIR=/usr/lib/x86_64-linux-gnu/hdf5/mpich
PREFIX_DIR=$HOME/pylith
```

### Configure

```
$HOME/src/pylith/pylith-installer-{{ site.installer-version }}/configure \
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
    --disable-hdf5 \
    --disable-h5py \
    --disable-numpy \
    --enable-pcre \
    --enable-swig \
    --enable-proj \
    --enable-cftime \
    --enable-netcdf \
    --enable-netcdfpy
```


## Ubuntu 20.04

Python 2 support is minimal in Ubuntu 20.04, so we use the installer to build several Python packages. We need cython to
build the `h5py` Python package with the installer.

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
  python2-dev \
  libpython2.7 \
  cython \
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
PYTHON_VERSION=2.7
HDF5_INCDIR=/usr/include/hdf5/openmpi
HDF5_LIBDIR=/usr/lib/x86_64-linux-gnu/hdf5/openmpi
PREFIX_DIR=$HOME/pylith
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
  --disable-hdf5 \
  --enable-numpy \
  --enable-setuptools \
  --enable-six \
  --enable-h5py \
  --enable-pcre \
  --enable-swig \
  --enable-proj \
  --enable-cftime \
  --enable-netcdf \
  --enable-netcdfpy
```
