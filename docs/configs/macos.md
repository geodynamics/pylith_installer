# macOS

:::{important}
You will need to install the following tools before configuring the installer:

1. XCode or XCode command line tools
2. [Python](https://www.python.org/downloads/macos/)
:::

## Ventura (13.6.x)

We use the Apple clang/clang++ compiler.
We use the installer to build autotools.
We use the Python binary from Python.org.

## Environment variables

```{code-block} bash
PREFIX=$HOME/pylith
```

### Configure

```{code-block} bash
# Define PETSc options
petsc_options="--download-chaco=1 --download-ml --download-f2cblaslapack --with-fc=0 --with-hwloc=0 --with-ssl=0 --with-x=0 --with-c2html=0 --with-lgrind=0"
#
${HOME}/src/pylith/pylith_installer-4.1.1-0/configure  \
    --prefix=${PREFIX} \
    --enable-force-install \
    --with-fetch=curl \
    --with-make-threads=8 \
    --with-fortran=no \
    --enable-autotools \
    --enable-mpi=mpich \
    --with-mpich-options=--with-pm=gforker \
    --enable-catch2 \
    --enable-proj \
    --enable-hdf5 \
    --enable-cmake \
    --enable-matplotlib \
    --enable-gmsh \
    --enable-tiff \
    --enable-force-install \
    --enable-cmake \
    --with-petsc-options="${petsc_options}" \
    CC=clang CXX=clang++
```
