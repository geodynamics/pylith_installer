# Linux clusters

## Operating system packages

The following software should be installed by the system administrator:

* C, C++ compilers
* MPI

:::{danger}
The `configure` will look for `mpicc` and `mpicxx` for building packages requiring MPI. Do not set `CC=mpicc` or `CXX=mpicxx` as this can lead to packages assuming you are using an Intel compiler. For example, the Python configure detects use of an Intel compiler by comparing `$CC` against the pattern `*icc*`.
:::

## Configure

We assume that Python was not built with the same compiler suite as MPI. The `--enable-python` option will also trigger building all of the Python modules needed. We use 8 threads when building.

If Python was built with the same compilers used to build MPI, then then you do not need the `--enable-python` option.

```bash
$HOME/src/pylith/pylith-installer-4.2.0-0/configure --enable-python --with-make-threads=8 --prefix=$HOME/pylith
```
