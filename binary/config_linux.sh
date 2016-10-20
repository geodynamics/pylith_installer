#!/bin/bash

PYLITH_BRANCH=master
BINARY_ROOT=${HOME}/pylith-binary
if [ $# == 1 ]; then
  BINARY_ROOT=$1
fi

CONFIG_ARGS="--enable-gcc --enable-python --enable-mpi=mpich --enable-cppunit --enable-numpy --with-numpy-blaslapack --enable-proj4 --enable-hdf5 --enable-netcdfpy --enable-cmake --enable-nemesis --enable-fiat --enable-pcre --enable-swig"

PETSC_OPTIONS="--download-chaco=1 --download-ml=1 --download-f2cblaslapack=1 --with-hwloc=0 --with-ssl=0 --with-x=0 --with-c2html=0 --with-lgrind=0"

DEST_DIR=${BINARY_ROOT}/dist
SRC_DIR=${BINARY_ROOT}/src/pylith_installer
BUILD_DIR=${BINARY_ROOT}/build

cd ${SRC_DIR} && autoreconf --install --verbose --force

unset PYTHONPATH LD_LIBRARY_PATH
PATH=/bin:/usr/bin

mkdir -p ${BUILD_DIR}
cd ${BUILD_DIR}
${SRC_DIR}/configure --with-pylith-git=${PYLITH_BRANCH} --with-make-threads=4 --prefix=${DEST_DIR} ${CONFIG_ARGS} --with-petsc-options="${PETSC_OPTIONS}"
. ${BUILD_DIR}/setup.sh
make >& make.log
cp -f ${BUILD_DIR}/pylith-${PYLITH_BRANCH}/packager/setup_linux64.sh ${DEST_DIR}/setup.sh
cd ${BUILD_DIR}/pylith-build && python ${BUILD_DIR}/pylith-${PYLITH_BRANCH}/packager/make_package.py
