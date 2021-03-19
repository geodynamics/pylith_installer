# PyLith development environment

The `pylith-devenv` Docker image provides all of the dependencies and
defines the environment for PyLith development. It is intended to be
read only with a separate Docker volume, which provides persistent
storage, for the PyLith development workspace.

## Setup

You only need to run these setup steps once.

### Fork repositories on GitHub

1. Log in to your [GitHub](https://github.com) account, creating an
account if you do not already have one.

2. Fork the following repositories:
* https://github.com/geodynamics/pythia
* https://github.com/geodynamics/spatialdata
* https://github.com/geodynamics/pylith

This creates a copy of the repository in your GitHub account.

### Create Docker volume for persistent storage

```
docker volume create pylith-dev
```

### Start PyLith development Docker container

```
docker run --name pylith-dev-workspace -d -v pylith-dev:/opt/pylith \
    registry.gitlab.com/cig-pylith/pylith_installer/pylith-devenv
```

### Setup directory structure

We will use the directory following directory structure for the
persistent storage.

```
/opt/pylith
    ├── src
    │    ├── pythia
    │    ├── spatialdata
    │    ├── petsc
    │    └── pylith
    ├── build
    │   ├── debug
    │   │   ├── pythia
    │   │   ├── spatialdata
    │   │   └── pylith
    │   └── opt
    │       ├── pythia
    │       ├── spatialdata
    │       └── pylith
    └── dest
        ├── debug
        │   ├── bin
        │   ├── include
        │   ├── lib
        │   └── share
        └── opt
            ├── bin
            ├── include
            ├── lib
            └── share
```
All of the source code will be placed under `/opt/pylith/src`. You
only need to create the top-level source directory as the
subdirectories will be created when you clone the repositories.

This directory structure is setup for both a debugging version for
development (debug directory) and an optimized version for performance
testing (opt directory). For now, we will only setup the debugging
version.

```
cd /opt/pylith
mkdir src
mkdir -p ${TOPBUILD_DIR} && pushd ${TOPBUILD_DIR} && mkdir pythia spatialdata pylith && popd
mkdir -p ${INSTALL_DIR}
```

### Clone repositories

This creates a local copy of the repositories in the persistent
storage volume of the PyLith development container. These are your
working copies of the repositories.

```
cd /opt/pylith/src
git clone --recursive https://github.com/GITHUB_USERNAME/pythia.git
git clone --recursive https://github.com/GITHUB_USERNAME/spatialdata.git
git clone --recursive https://github.com/GITHUB_USERNAME/pylith.git
git clone https://gitlab.com/petsc/petsc.git && git checkout knepley/pylith
```

### Configure and build for development

1. Pythia

```
cd ${TOPBUILD_DIR}/pythia
pushd ${TOPSRC_DIR}/pythia && autoreconf -if && popd
${TOPSRC_DIR}/pythia/configure --prefix=${INSTALL_DIR} --enable-testing \
    CC=mpicc CXX=mpicxx CFLAGS="-g -Wall" CXXFLAGS="-std=c++11 -g -Wall"
make install
make check
```

2. Spatialdata

```
cd ${TOPBUILD_DIR}/spatialdata
pushd ${TOPSRC_DIR}/spatialdata && autoreconf -if && popd
${TOPSRC_DIR}/spatialdata/configure --prefix=${INSTALL_DIR} \
    --enable-swig --enable-testing --enable-test-coverage \
    --with-python-coverage=python3-coverage \
	CPPFLAGS="-I${DEPS_DIR}/include -I${INSTALL_DIR}/include" \
	LDFLAGS="-L${DEPS_DIR}/lib -L${INSTALL_DIR}/lib --coverage" \
	CXX=mpicxx CXXFLAGS="-std=c++11 -g -Wall --coverage"
make install -j$(nproc)
make check -j$(nproc)
```

3. PETSc

```
cd ${TOPSRC_DIR}/petsc
python3 ./configure --with-c2html=0 --with-lgrind=0 --with-fc=0 \
    --with-x=0 --with-clanguage=C --with-mpicompilers=1 \
    --with-shared-libraries=1 --with-64-bit-points=1 --with-large-file-io=1 \
    --with-hdf5=1 --download-chaco=1 --download-ml=1 \
	--download-f2cblaslapack=1 --with-debugging=1 CFLAGS="-g -O -Wall" \
	CPPFLAGS="-I${HDF5_INCDIR} -I${DEPS_DIR}" LDFLAGS="-L${HDF5_LIBDIR} -L${DEPS_DIR}"
make 
make check
```

4. PyLith

```
cd ${TOPBUILD_DIR}/pylith
pushd ${TOPSRC_DIR}/pylith && autoreconf -if && popd
${TOPSRC_DIR}/pylith/configure --prefix=${INSTALL_DIR} \
    --enable-cubit --enable-hdf5 --enable-swig --enable-testing \
    --enable-test-coverage --with-python-coverage=python3-coverage \
	CPPFLAGS="-I${HDF5_INCDIR} -I${DEPS_DIR}/include -I${INSTALL_DIR}/include" \
	LDFLAGS="-L${HDF5_LIBDIR} -L${DEPS_DIR}/lib -L${INSTALL_DIR}/lib --coverage" \
	CC=mpicc CFLAGS="-g -Wall" CXX=mpicxx CXXFLAGS="-std=c++11 -g -Wall --coverage"
make install -j$(nproc)
make check -j$(nproc)
```
