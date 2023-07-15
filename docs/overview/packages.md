# Versions of dependencies

When the installer is used to build dependencies, it will build the
following versions of the packages.

:::{important}
In some cases we have patched the libraries to address portability
issues.

The dependencies will be downloaded from <http://geoweb.cse.ucdavis.edu/~buildbot/deps/>.
:::

* Autotools
  * m4 1.4.17
  * autoconf 2.69
  * automake 1.16.4
  * libtool 2.4.6

* Gcc compiler
  * gcc/g++/gfortran 10.3.0
  * mpc 1.2.1
  * gmp 6.2.1
  * mpfr 4.1.0

* MPI (select one)
  * MPICH 4.1.1
  * OpenMPI 4.1.5

* Python
  * Python 3.10.10
  * netCDF (Python) 1.6.3
  * h5py 3.8.0

* General tools
  * OpenSSL 3.1.0
  * Catch2 3.2.2
  * PCRE 10.42
  * SWIG 4.1.1
  * SQLITE 3410200
  * Proj 9.2.0
  * HDF5 1.14.0
  * NetCDF 4.9.2
  * Cmake 3.26.2

* CIG tools
  * pythia 1.0.0
  * spatialdata 2.0.0
