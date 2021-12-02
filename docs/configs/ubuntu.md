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
      zlib1g-dev \
      unzip \
      git \
      ca-certificates \
	  libssl-dev \
      libcppunit-dev \
      libmpich-dev \
      mpich \
      libhdf5-mpich-103 \
      libhdf5-mpich-dev \
      cmake
```

### Environment variables

```bash
export PYTHON_VERSION=2.7
export HDF5_INCDIR=/usr/include/hdf5/mpich
export HDF5_LIBDIR=/usr/lib/x86_64-linux-gnu/hdf5/mpich
PREFIX_DIR=$HOME/pylith
```

### Configure

```bash
$HOME/src/pylith/pylith-installer-2.2.2-2/configure \
    --prefix=$PREFIX_DIR \
    --with-fetch=curl \
    --with-fortran=no \
    --with-make-threads=$(nproc) \
    --with-hdf5-incdir=${HDF5_INCDIR} \
    --with-hdf5-libdir=${HDF5_LIBDIR} \
    --disable-mpi \
    --disable-cppunit \
    --disable-cmake \
    --disable-hdf5
```
