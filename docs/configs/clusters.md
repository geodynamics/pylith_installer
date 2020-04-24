# Configuration on a cluster


## Dependencies already installed

The following software should be installed by the system administrator:

* C, C++ compilers
* MPI

**TIP**: We recommend using the environment arguments to configure to use the MPI compilers for all compilation. If the
MPI compilers are `mpicc` and `mpicxx`, then we use `CC=mpicc CXX=mpicxx` in the call to `configure`.

## Configure

We assume that Python was not built with the same compiler suite as MPI. If it was then you do not need the
`--enable-python` option. We use 8 threads when building.

```
bash> $HOME/src/pylith/pylith-installer-{{ site.installer-version }}/configure --enable-python --with-make-threads=8 --prefix=$HOME/pylith
```
