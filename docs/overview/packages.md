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
  * automake 1.16.1
  * libtool 2.4.6

* Gcc compiler
  * gcc/g++/gfortran 7.3.0
  * mpc 1.0.3
  * gmp 6.1.0
  * mpfr 3.1.4

* MPI (select one)
  * MPICH 3.3.2
  * OpenMPI 4.1.0

* Python
  * Python 3.9.1
  * setuptools 51.1.1
  * Cython 0.29.21
  * numpy 1.19.5
  * six 1.15.0
  * cftime 1.4.1
  * netCDF (Python) 1.5.5.1
  * h5py 3.1.0

* General tools
  * OpenSSL 1.1.1i
  * CppUnit 1.15.1
  * PCRE 8.40
  * SWIG 4.0.2
  * SQLITE 3310100
  * Proj 6.3.0
  * HDF5 1.12.0
  * NetCDF 4.7.4
  * Cmake 3.19.2

* CIG tools
  * pythia 1.0.0
  * spatialdata 2.0.0
