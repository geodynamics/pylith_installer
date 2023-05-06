# 2. Running configure

The `configure` script is used to specify which dependencies to build and which ones are already present.

:::{important}
The output at the end of running configure lists the packages to be built. Double-check to make sure this matches what you expect.
:::

## Speeding up the build process

On multi-core and multi-processor systems (not clusters but systems with more than one core and/or processor), the build process can be sped up by using multiple threads when running `make`. Use the configure argument `--with-make-threads=NTHREADS` where `NTHREADS` is the number of threads to use (1, 2, 4, 8, etc). The default is to use only one thread. In the examples below, we set the number of threads to 2.

## Default configuration

The default configure options assume you have:

* C/C++ 14 compilers
* Python 3.6 or later
* automake 1.14 or later
* MPI

In this case, you simply specify the number of threads and the destination directory:
```bash
mkdir -p $HOME/build/pylith
$HOME/src/pylith/pylith-installer-3.0.3-0/configure --with-make-threads=2 --prefix=$HOME/pylith
```

## Configure options

The examples in the [common configurations section](../configs/index.md) illustrate most common cases and how to adjust the configure arguments for cases in which you use dependencies provided by the operating system.

:::{warning}
NetCDF depends on HDF5 (we use the parallel version built with MPI) which, in turn, depends on MPI. Most Linux distributions do not provide NetCDF that is built upon a parallel version of HDF5. As a result, we build NetCDF using the installer rather than using a version supplied by the operating system.
:::

:::{tip}
Run `$HOME/src/pylith/configure --help` to see all of the command line arguments and the default values.
:::

### Resolving incompatibilities

To remedy incompatible compiler suite, MPI, and Python versions, simply use the command line options for the installer `configure` script and request the installer build a new version of the incompatible package (e.g., `--enable-python`, `--enable-mpi=openmpi`).