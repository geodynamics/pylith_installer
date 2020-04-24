# MacOS

We use the Apple clang/clang++ compiler, system Python, and MPICH implementation of MPI. MacOS does not come with
autotools (autoconf, automake, and libtool), so we install those as well.

## Environment variables

```
PYTHON_VERSION=2.7
PREFIX=$HOME/pylith
```

### Configure

```[bash]
bash> petsc_options="--download-chaco=1 --download-ml --with-fc=0 --with-hwloc=0 --with-ssl=0 --with-x=0 --with-c2html=0 --with-lgrind=0 --with-blas-lib=/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/Versions/Current/libBLAS.dylib --with-lapack-lib=/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/Versions/Current/libLAPACK.dylib"

bash> ${HOME}/src/pylith/pylith_installer-{{ site.installer-version }}/configure  \
  --prefix=${PREFIX} \
  --enable-force-install \
  --with-fetch=curl \
  --with-make-threads=4 \
  --with-fortran=no \
  --enable-autotools \
  --enable-mpi=mpich \
  --enable-swig \
  --enable-pcre \
  --enable-numpy \
  --enable-cmake \
  --with-petsc-options="${petsc_options}" \
  --with-pylith-git \
  CC=clang CXX=clang++
```
