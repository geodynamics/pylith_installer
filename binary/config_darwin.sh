#!/bin/bash

BINARY_ROOT=${HOME}/pylith-binary
if [ $# == 1 ]; then
  BINARY_ROOT=$1
fi

CONFIG_ARGS="--enable-autotools --enable-mpi=mpich --enable-swig --enable-pcre --enable-numpy --enable-force-install --enable-cmake --with-fortran=no"

PETSC_OPTIONS="--download-chaco=1 --download-ml --with-fc=0 --with-hwloc=0 --with-ssl=0 --with-x=0 --with-c2html=0 --with-lgrind=0 --with-blas-lib=/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/Versions/Current/libBLAS.dylib --with-lapack-lib=/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/Versions/Current/libLAPACK.dylib"

DEST_DIR=${BINARY_ROOT}/dist
SRC_DIR=${BINARY_ROOT}/src/pylith_installer
BUILD_DIR=${BINARY_ROOT}/build

cd ${SRC_DIR} && autoreconf --install --verbose --force

mkdir -p ${BUILD_DIR}
cd ${BUILD_DIR}
${SRC_DIR}/configure --with-pylith-git=master --with-make-threads=4 --prefix=${DEST_DIR} ${ARGS} --with-petsc-options="${PETSC_OPTIONS}" CC=clang CXX=clang++


