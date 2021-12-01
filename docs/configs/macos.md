# macOS

:::{important}
You will need to install XCode or XCode command line tools before configuring the installer.
:::

## Big Sur (11.6.x)

We use the Apple clang/clang++ compiler.
XCode does not provide autotools (autoconf, automake, and libtool) so have the installer build them.
Installing autotools will also install a more recent version of GNU `make`; some versions of `make` provided with XCode have limited support for parallel builds.
We also use the installer to build Python 2.7; this ensures proper installation of the standard Python modules.

## Environment variables

```
export PYTHON_VERSION=2.7
PREFIX=$HOME/pylith
```

### Configure

We use the `-isysroot` argument in `CFLAGS` to specify the location of the XCode software development kit (SDK).
The location on your machine may be different.
We also specify `-Wno-implicit-function-declaration` in `CFLAGS` to allow implicit function declarations; this is needed to build some PyLith dependencies and may not be needed with older macOS versions.

```bash
# Define PETSc options
petsc_options="--download-chaco=1 --download-ml --download-f2cblaslapack --with-fc=0 --with-hwloc=0 --with-ssl=0 --with-x=0 --with-c2html=0 --with-lgrind=0"
#
${HOME}/src/pylith/pylith_installer-2.2.2-2/configure  \
    --prefix=${PREFIX} \
    --enable-force-install \
    --with-fetch=curl \
    --with-make-threads=4 \
    --with-fortran=no \
    --enable-autotools \
    --enable-mpi=mpich \
    --enable-openssl \
    --with-numpy-blaslapack=no \
    --with-petsc-options="${petsc_options}" \
    CC=clang CXX=clang++ \
	CFLAGS="-g -O3 -isysroot /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk -Wno-implicit-function-declaration" \
	CXXFLAGS="-g -O3"
```
