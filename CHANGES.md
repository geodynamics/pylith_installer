See <https://github.com/geodynamics/pylith_installer/commits/main> for the complete log of changes made to PyLith Installer.

## Version 3.0.3-1

* Bugfixes
  * Switch netCDF4 build from pip to `python setup.py install` to avoid Python module import failure.
  * Use current PyPI version for h5py (avoids incompatibilities between cython and pinned 5py version).

## Version 3.0.3-0

* Install PyLith to Python virtual environment and use pip to install Python modules (setuptools, certifi, numpy, cftime).
* Migrate documentation to Sphinx+MyST
* Separate build directory for external dependencies and CIG-related code (pythia, spatialdata, PETSc, PyLith)
* Update versions of dependencies.
  * gcc 10.3.0
  * mpc 1.2.1
  * gmp 6.2.1
  * mpfr 4.1.0
  * mpich 3.4.2
  * openmpi 4.1.1
  * openssl 1.1.1l
  * libffi 3.4.2
  * curl 7.83.1
  * cmake 3.21.3
  * python 3.10.6
  * pcre 8.40
  * swig 4.0.2
  * cppunit 1.15.1
  * sqlite 3.31
  * tiff 4.3.0
  * proj 8.1.1
  * hdf5 1.12.1
  * h5py 3.6.0
  * netcdf 4.8.1
  * netCDF4 1.5.7
  * pythia 1.0.0
  * spatialdata 3.0.0
* Remove installing dependencies that are now obsolete.
  * ScientificPython
  * FIAT
  * Cython
* Use projsync to install PROJ datum files.
* Allow specification of MPICH options in configure.
* Provide `--enable-developer` configure argument to install pacakges for development. 

## Version 2.2.2-1

* Install `cython` when building `h5py` and `netCDF4`.
* Install `cftime` when building `netCDF4`.

## Version 2.2.2-0

* Update versions of dependencies.

  * pythia 0.8.1.19
  * spatialdata 1.10.0

## Version 2.2.1-1

* Update versions of dependencies.

  * gcc 7.3.0
  * mpc 1.0.3
  * gmp 6.1.0
  * mpfr 3.1.4
  * Python 2.7.15
  * mpich 3.2.1
  * numpy 1.14.3
  * proj4 5.0.1
  * HDF5 1.10.2
  * h5py 2.7.1
  * netCDF 4.6.1
  * netCDF4 (Python module) 1.3.1
  * setuptools 39.1.0
  * cmake 3.11.2

## Version 2.2.1-0

* Increment to PyLith version 2.2.1
* Update Spatialdata to 1.9.10
* Update pylith_parameters to 1.1.0
* Build openssl
* Add configure check for unzip (Proj.4 datums) and generate error if building gcc but not MPI.

## Version 2.2.0-0

* Increment to PyLith version 2.2.0
* Add installation of PyLith Parameter Viewer 1.0.0.
* Updated Pythia to 0.8.1.18.
* Update Spatialdata to 1.9.8.
* Update dependencies so they are similar to Ubuntu 16.04 LTS.
  * m4 1.4.17
  * autoconf 2.69
  * automake 1.15
  * libtool 2.4.6
  * gcc-5.4.0
  * Python 2.7.13
  * pcre 8.40
  * cmake 3.7.0
  * numpy.1.11.2
* Updated to latest SWIG that works with Pyre
  * swig 3.0.2
* Other updates
  * openmpi-1.8.8
  * NetCDF 4.4.1.1
  * netCDF4 (python) 1.2.7
* Updates with patches for using numpy 1.11.2.
  * ScientificPython-2.9.1p1
  * FIAT-0.9.9p1

## Version 2.1.4-0

* Increment to PyLith version 2.1.4.
* Update NetCDF to 4.4.0.
* Updated Pythia to 0.8.1.17.
* Update Spatialdata to 1.9.7.

## Version 2.1.3-0

* Increment to PyLith version 2.1.3.
* Update netCDF4 Python module to 1.1.8p1 (disable use of cython by default).
