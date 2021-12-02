# Linux clusters

## Operating system packages

The following software should be installed by the system administrator:

* C, C++ compilers
* MPI
* wget (default used by installer) or curl

:::{danger}
The `configure` script will look for `mpicc` and `mpicxx` for building packages requiring MPI.
Do not set `CC=mpicc` or `CXX=mpicxx` as this can lead to packages assuming you are using an Intel compiler.
For example, the Python configure detects use of an Intel compiler by comparing `$CC` against the pattern `*icc*`.
:::

## Configure

We use 8 threads when building.

```bash
$HOME/pylith/src/pylith-installer-2.2.2-2/configure --with-make-threads=8 --prefix=$HOME/pylith
```
