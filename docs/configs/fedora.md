# Fedora

## Fedora 32

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
    python3-setuptools \
    python3-numpy \
    python3-cftime \
    python3-coverage \
    python3-six \
    python3-Cython \
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
    proj \
    proj-devel \
    proj-datumgrid \
    cmake \
    swig
```

### Environment variables

```
export PYTHON_VERSION=3.8
export HDF5_INCDIR=/usr/include/openmpi-x86_64
export HDF5_LIBDIR=/usr/lib64/openmpi/lib
PREFIX_DIR=$HOME/pylith
PATH=$PATH:/usr/lib64/openmpi/bin
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
    --disable-proj \
    --disable-cftime \
    --enable-h5py \
    --enable-netcdf \
    --enable-netcdfpy
```


## Fedora 33

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
    python3-setuptools \
    python3-numpy \
    python3-cftime \
    python3-coverage \
    python3-six \
    python3-Cython \
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
    proj \
    proj-devel \
    proj-datumgrid \
    cmake \
    swig
```

### Environment variables

```
export PYTHON_VERSION=3.9
export HDF5_INCDIR=/usr/include/openmpi-x86_64
export HDF5_LIBDIR=/usr/lib64/openmpi/lib
PREFIX_DIR=$HOME/pylith
PATH=$PATH:/usr/lib64/openmpi/bin
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
    --disable-setuptools \
    --disable-numpy \
    --disable-hdf5 \
    --disable-proj \
    --enable-h5py \
    --enable-netcdf \
    --enable-netcdfpy
```
