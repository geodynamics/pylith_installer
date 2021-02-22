# Fedora

## Fedora 30

### Operating system packages

```
bash> dnf install -y \
  gcc \
  gcc-c++ \
	make \
  file \
  automake \
  autoconf \
  libtool \
  curl \
	python2 \
	python2-devel \
	python2-libs \
	python2-numpy \
  python2-setuptools \
	python2-six \
	python2-Cython \
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
	openmpi \
	openmpi-devel \
	hdf5-openmpi \
	hdf5-openmpi-devel \
	sqlite \
	sqlite-libs \
	sqlite-devel \
	cmake
```

### Environment variables

```
PATH=$PATH:/usr/lib64/openmpi/bin
PYTHON_VERSION=2.7
HDF5_INCDIR=/usr/include/openmpi-x86_64
HDF5_LIBDIR=/usr/lib64/openmpi/lib
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
    --enable-pcre \
    --enable-swig \
    --enable-proj \
    --enable-h5py \
    --enable-cftime \
    --enable-netcdf \
    --enable-netcdfpy
```


## Fedora 31

### Operating system packages

```
bash> dnf install -y \
  gcc \
  gcc-c++ \
  make \
  file \
  automake \
  autoconf \
  libtool \
  curl \
  python2 \
  python2-devel \
  python2-libs \
  python2-numpy \
  python2-setuptools \
  python2-six \
  python2-Cython \
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
  mpich \
  mpich-devel \
  hdf5-mpich \
  hdf5-mpich-devel \
  sqlite \
  sqlite-libs \
  sqlite-devel \
  cmake
```

### Environment variables

```
PATH=$PATH:/usr/lib64/mpich/bin
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
    --enable-pcre \
    --enable-swig \
    --enable-proj \
    --enable-h5py \
    --enable-cftime \
    --enable-netcdf \
    --enable-netcdfpy
```


## Fedora 32

Python 2 support is minimal in Fedora 32, so we use the installer to build several Python packages.

### Operating system packages

```
bash> dnf install -y \
  gcc \
  gcc-c++ \
  make \
  file \
  automake \
  autoconf \
  libtool \
  curl \
  python2 \
  python2-devel \
  python2-numpy \
  python2-setuptools \
  python2-six \
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
  openmpi \
  openmpi-devel \
  hdf5-openmpi \
  hdf5-openmpi-devel \
  sqlite \
  sqlite-libs \
  sqlite-devel \
  cmake
```

### Environment variables

```
PATH=$PATH:/usr/lib64/openmpi/bin
PYTHON_VERSION=2.7
HDF5_INCDIR=/usr/include/openmpi-x86_64
HDF5_LIBDIR=/usr/lib64/openmpi/lib
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
  --enable-pcre \
  --enable-swig \
  --enable-proj \
  --enable-h5py \
  --enable-cftime \
  --enable-netcdf \
  --enable-netcdfpy
```
