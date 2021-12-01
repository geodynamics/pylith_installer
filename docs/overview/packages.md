# Versions of dependencies

When the installer is used to build dependencies, it will build the following versions of the packages.

:::{important}
In some cases we have patched the libraries to address portability issues.

The dependencies will be downloaded from <http://geoweb.cse.ucdavis.edu/~buildbot/deps/>.
:::

* Autotools
  * make 4.3
  * m4 1.4.17
  * autoconf 2.69
  * automake 1.15
  * libtool 2.4.6

* Gcc compiler
  * gcc/g++/gfortran 7.3.0
  * mpc 1.0.3
  * gmp 6.1.0
  * mpfr 3.1.4

* MPI (select one)
  * MPICH 3.2.1
  * OpenMPI 3.1.0

* Python
  * Python 2.7.18
  * setuptools 39.1.0
  * Cython 0.29.16
  * numpy 1.14.3
  * six 1.12.0
  * cftime 1.1.1
  * netCDF (Python) 1.5.0.1
  * h5py 2.10.0

* General tools
  * OpenSSL 1.1.1l
  * CppUnit 1.13.2
  * PCRE 8.40
  * SWIG 3.0.2
  * Proj 5.0.1
  * HDF5 1.10.8p1
  * NetCDF 4.6.3
  * Cmake 3.14.2

* CIG tools
  * pythia 0.8.1.19
  * spatialdata 1.10.0
