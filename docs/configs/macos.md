# macOS

:::{important}
You will need to install XCode or XCode command line tools before configuring the installer.
:::

## Monterey (12.6.x)

We use the Apple clang/clang++ compiler.
We use the installer to build autotools and Python 3.10.

## Environment variables

```
PREFIX=$HOME/pylith
```

### Configure

```bash
# Define PETSc options
petsc_options="--download-chaco=1 --download-ml --download-f2cblaslapack --with-fc=0 --with-hwloc=0 --with-ssl=0 --with-x=0 --with-c2html=0 --with-lgrind=0"
#
${HOME}/src/pylith/pylith_installer-3.0.3-0/configure  \
    --prefix=${PREFIX} \
    --enable-force-install \
    --with-fetch=curl \
    --with-make-threads=4 \
    --with-fortran=no \
    --enable-autotools \
    --enable-mpi=mpich \
    --enable-openssl \
    --enable-sqlite \
    --enable-python \
    --enable-force-install \
    --enable-cmake \
    --with-petsc-options="${petsc_options}" \
    CC=clang CXX=clang++
```
