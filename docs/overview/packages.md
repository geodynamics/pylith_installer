# Versions of dependencies

When the installer is used to build dependencies, it will build the
following versions of the packages.

:::{important}
In some cases we have patched the libraries to address portability
issues.

The dependencies will be downloaded from <http://geoweb.cse.ucdavis.edu/~buildbot/deps/>.
:::

* Autotools
  * m4 1.4.19
  * autoconf 2.72
  * automake 1.17
  * libtool 2.5.3

* Gcc compiler
  * gcc/g++/gfortran 14.2.0
  * mpc 1.3.1
  * gmp 6.3.0
  * mpfr 4.2.1

* MPI (select one)
  * MPICH 4.2.3
  * OpenMPI 5.0.5

* Python
  * Python 3.12.7
  * netCDF (Python) via pip
  * h5py via pip
  * numpy 1.26.4
  * cftime via pip

* General tools
  * OpenSSL 3.4.0
  * libxcrypt 4.4.36
  * libffi 3.7.0
  * Curl 8.11.0
  * Catch2 3.7.1
  * PCRE 10.44
  * SWIG 4.3.0
  * SQLITE 3410200
  * Proj 9.5.0
  * HDF5 1.14.5
  * NetCDF 4.9.2
  * Cmake 3.31.0

* CIG tools
  * pythia 1.0.0
  * spatialdata 2.0.0
