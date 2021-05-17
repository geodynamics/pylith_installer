# Ubuntu

## Ubuntu 18.04

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
      ssh \
      libpython3.7 \
      python3-dev \
      python3-pip \
      python3-setuptools \
      python3-coverage \
	  python3-six \
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
      sqlite3 \
      libsqlite3-0 \
      libsqlite3-dev \
      cmake
```

### Environment variables

```bash
export PYTHON_VERSION=3.7
export HDF5_INCDIR=/usr/include/hdf5/openmpi
export HDF5_LIBDIR=/usr/lib/x86_64-linux-gnu/hdf5/openmpi
PREFIX_DIR=$HOME/pylith
```

### Configure

```bash
$HOME/src/pylith/pylith-installer-3.0.0-0/configure \
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
    --disable-numpy \
    --disable-setuptools \
    --disable-hdf5 \
    --enable-numpy \
    --enable-cython \
    --enable-cftime \
    --enable-h5py \
    --enable-pcre \
    --enable-swig \
    --enable-proj \
    --enable-cftime \
    --enable-netcdf \
    --enable-netcdfpy
```


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
      python3-dev \
      libpython3.8 \
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
      cmake \
      swig
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
$HOME/src/pylith/pylith-installer-3.0.0-0/configure \
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
    --disable-numpy \
    --disable-hdf5 \
    --disable-h5py \
    --enable-netcdf \
    --enable-netcdfpy
```


## Ubuntu 20.10

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
      libpython3.8 \
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
      proj-bin \
      proj-data \
      libproj-dev \
      cmake \
      swig
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
$HOME/src/pylith/pylith-installer-3.0.0-0/configure \
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
    --disable-numpy \
    --disable-hdf5 \
    --disable-h5py \
    --enable-cftime \
    --enable-netcdf \
    --enable-netcdfpy
```
