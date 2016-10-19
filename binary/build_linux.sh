#!/bin/bash

BINARY_ROOT=${HOME}/pylith-binary

args="--enable-gcc --enable-python --enable-mpi=mpich --enable-cppunit --enable-numpy --with-numpy-blaslapack --enable-proj4 --enable-hdf5 --enable-netcdfpy --enable-cmake --enable-nemesis --enable-fiat --enable-pcre --enable-swig"

DEST_DIR=${BINARY_ROOT}/dist
SRC_DIR=${BINARY_ROOT}/src/pylith_installer
BUILD_DIR=${BINARY_ROOT}/build

cd ${SRC_DIR} && autoreconf --install --verbose --force

mkdir -p ${BUILD_DIR}
cd ${BUILD_DIR}
${SRC_DIR}/configure --with-make-threads=4 --prefix=${DEST_DIR} ${args}


