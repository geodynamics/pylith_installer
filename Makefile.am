# -*- Makefile -*-
#
# ----------------------------------------------------------------------
#
# Brad T. Aagaard, U.S. Geological Survey
# Charles A. Williams, GNS Science
# Matthew G. Knepley, University of Chicago
#
# This code was developed as part of the Computational Infrastructure
# for Geodynamics (http://geodynamics.org).
#
# Copyright (c) 2010 University of California, Davis
#
# See COPYING for license information.
#
# ----------------------------------------------------------------------

ACLOCAL_AMFLAGS = -I m4

# ----------------------------------------------------------------------
# Package Versions
# ----------------------------------------------------------------------
GCC_VER=4.5.2
MPC_VER=0.8.2
GMP_VER=4.3.2
MPFR_VER=2.4.2

PYTHON_VER=2.6.6

MPICH2_VER=1.3.2p1
OPENMPI_VER=1.4.3

CPPUNIT_VER=1.12.1

SWIG_VER=2.0.2

NUMPY_VER=1.5.1

PROJ4_VER=4.7.0

NETCDF_VER=4.1.1
HDF5_VER=1.8.6

SCIENTIFICPYTHON_VER=2.9.1
FIAT_VER=0.9.9

NEMESIS_VER=1.0.1
SPATIALDATA_VER=0.6.0
PYLITH_VER=1.5.1


# ----------------------------------------------------------------------
# Files
# ----------------------------------------------------------------------
SUBDIRS = \
	bin

noinst_tmp = \
	installed_gcc \
	installed_python \
	installed_mpi \
	installed_cppunit \
	installed_swig \
	installed_numpy \
	installed_proj \
	installed_netcdf \
	installed_hdf5 \
	installed_petsc \
	installed_spatialdata \
	installed_nemesis \
	installed_fiat \
	installed_pylith

noinst_builddirs = \
	gcc-build \
	python-build \
	openmpi-build \
	mpich-build \
	cppunit-build \
	swig-build \
	proj4-build \
	netcdf-build \
	hdf5-build \
	spatialdata-build \
	nemesis-build \
	pylith-build

noinst_srcdirs = \
	gcc-$(GCC_VER) \
	Python-$(PYTHON_VER) \
	openmpi-$(OPENMPI_VER) \
	mpich2-$(MPICH2_VER) \
	cppunit-$(CPPUNIT_VER) \
	swig-$(SWIG_VER) \
	proj-$(PROJ4_VER) \
	netcdf-$(NETCDF_VER) \
	hdf5-$(HDF5_VER) \
	spatialdata-$(SPATIALDATA_VER) \
	nemesis-$(NEMESIS_VER) \
	pylith-$(PYLITH_VER)


FETCH_SCRIPT = $(top_srcdir)/bin/fetch.sh

# ----------------------------------------------------------------------
# Targets
# ----------------------------------------------------------------------
default: installed_pylith

all: gcc python mpi cppunit swig numpy proj4 netcdf hdf5 petsc nemesis spatialdata fiat

# ----------------------------------------------------------------------
# Note on configure invocations
#
# Normally, we would like to do configure ARGS && make && make
# install. However a bug in autoconf results in d.SYM directories
# generating an error when configure tries to remove them with "rm"
# rather than "rm -r". As a result, we use configure ARGS ; make &&
# make install.

# ----------------------------------------------------------------------
# gcc
# ----------------------------------------------------------------------
gcc:
if INSTALL_GCC
	LANGUAGES = "c,c++"
if WITH_FORTRAN
	$(LANGUAGES) += ",fortran"
endif
	$(FETCH_SCRIPT) "$(downloader)" gcc-$(GCC_VER).tar.bz2 http://geodynamics.org/~buildbot/deps
	$(FETCH_SCRIPT) "$(downloader)" mpc-$(MPC_VER).tar.gz http://geodynamics.org/~buildbot/deps
	$(FETCH_SCRIPT) "$(downloader)" gmp-$(GMP_VER).tar.gz http://geodynamics.org/~buildbot/deps
	$(FETCH_SCRIPT) "$(downloader)" mpfr-$(MPFR_VER).tar.bz2 http://geodynamics.org/~buildbot/deps
	$(TAR) -jxf gcc-4.5.2.tar.bz2
	cd gcc-4.5.2; \
		tar -zxf ../gmp-4.3.2.tar.gz; \
		ln -sf gmp-4.3.2/ gmp; \
		tar -zxf ../mpc-0.8.2.tar.gz; \
		ln -sf mpc-0.8.2/ mpc; \
		tar -jxf ../mpfr-2.4.2.tar.bz2; \
		ln -sf mpfr-2.4.2/ mpfr
	$(MKDIR_P) gcc-build
	cd gcc-build && \
		../gcc-4.5.2/configure --prefix=$(prefix) $(LANGUAGES)
		make -j $(make_threads) && \
		make install

else
	@echo "$@ already installed. Skipping installation."
endif

installed_gcc:
	$(MAKE) $(AM_MAKEFLAGS) gcc
	touch $@


# ----------------------------------------------------------------------
# python
# ----------------------------------------------------------------------
python: installed_gcc
if INSTALL_PYTHON
	$(FETCH_SCRIPT) $(downloader) Python-$(PYTHON_VER).tgz http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf Python-$(PYTHON_VER).tgz
	$(MKDIR_P) python-build
	cd python-build && \
		../Python-$(PYTHON_VER)/configure --prefix=$(prefix) && \
		make -j $(make_threads) && \
		make install
else
	@echo "$@ already installed. Skipping installation."
endif

installed_python:
	$(MAKE) $(AM_MAKEFLAGS) python
	touch $@


# ----------------------------------------------------------------------
# mpi
# ----------------------------------------------------------------------
if INSTALL_MPI
if INSTALL_OPENMPI
mpi: openmpi
endif

if INSTALL_MPICH
mpi: mpich
endif

else
mpi:
	@echo "$@ already installed. Skipping installation."
endif

installed_mpi:
	$(MAKE) $(AM_MAKEFLAGS) mpi
	touch $@


# ----------------------------------------------------------------------
# openmpi
# ----------------------------------------------------------------------
openmpi: installed_gcc


# ----------------------------------------------------------------------
# mpich
# ----------------------------------------------------------------------
mpich: installed_gcc
	$(FETCH_SCRIPT) "$(downloader)" mpich2-$(MPICH2_VER).tar.gz http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf mpich2-$(MPICH2_VER).tar.gz
	$(MKDIR_P) mpich-build
	cd mpich-build && \
		../mpich2-$(MPICH2_VER)/configure --with-pm=gforker \
			--enable-shared --enable-sharedlibs=gcc \
			--disable-static --disable-mpe \
			--prefix=$(HOME)/install/$(BUILDBOT) \
			CC=gcc CXX=g++ FC=gfortran ; \
		make && \
		make install
	if [ ! -x $(prefix)/mpirun ]; then cd $(prefix)/bin && $(LN_S) mpiexec mpirun; fi


# ----------------------------------------------------------------------
# cppunit
# ----------------------------------------------------------------------
cppunit: installed_gcc
if INSTALL_CPPUNIT
	$(FETCH_SCRIPT) "$(downloader)" cppunit-$(CPPUNIT_VER).tar.gz http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf cppunit-$(CPPUNIT_VER).tar.gz
	$(MKDIR_P) cppunit-build
	cd cppunit-build && \
		../cppunit-$(CPPUNIT_VER)/configure --prefix=$(prefix) ; \
		make -j $(make_threads) && \
		make install

else
	@echo "$@ already installed. Skipping installation."
endif

installed_cppunit:
	$(MAKE) $(AM_MAKEFLAGS) cppunit
	touch $@


# ----------------------------------------------------------------------
# swig
# ----------------------------------------------------------------------
swig: installed_gcc
if INSTALL_SWIG
	$(FETCH_SCRIPT) "$(downloader)" swig-$(SWIG_VER).tar.gz http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf swig-$(SWIG_VER).tar.gz
	$(MKDIR_P) swig-build
	cd swig-build && \
		../swig-$(SWIG_VER)/configure --prefix=$(HOME)/pylith_deps ; \
		make -j 4 && \
		make install
else
	@echo "$@ already installed. Skipping installation."
endif

installed_swig:
	$(MAKE) $(AM_MAKEFLAGS) swig
	touch $@


# ----------------------------------------------------------------------
# numpy
# ----------------------------------------------------------------------
numpy: installed_python
if INSTALL_NUMPY
	$(FETCH_SCRIPT) "$(downloader)" numpy-$(NUMPY_VER).tar.gz http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf numpy-1.5.1.tar.gz
	cd numpy-1.5.1 && $(PYTHON) setup.py install --prefix=$(prefix)

else
	@echo "$@ already installed. Skipping installation."
endif

installed_numpy:
	$(MAKE) $(AM_MAKEFLAGS) numpy
	touch $@


# ----------------------------------------------------------------------
# proj4
# ----------------------------------------------------------------------
proj4: installed_gcc
if INSTALL_PROJ4
	$(FETCH_SCRIPT) "$(downloader)" proj-$(PROJ4_VER).tar.gz http://geodynamics.org/~buildbot/deps
	$(FETCH_SCRIPT) "$(downloader)" proj-datumgrid-1.3.zip http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf proj-$(PROJ4_VER).tar.gz
	$(MKDIR_P) proj4-build/nad
	cd proj4-build/nad && \
		unzip ../../proj-datumgrid-1.3.zip
	cd proj4-build && \
		../proj-$(PROJ4_VER)/configure --prefix=$(prefix) ; \
		make -j $(make_threads) && \
		make install

else
	@echo "$@ already installed. Skipping installation."
endif

installed_proj4:
	$(MAKE) $(AM_MAKEFLAGS) proj4
	touch $@


# ----------------------------------------------------------------------
# netcdf
# ----------------------------------------------------------------------
netcdf: installed_gcc
if INSTALL_NETCDF
	$(FETCH_SCRIPT) "$(downloader)" netcdf-$(NETCDF_VER).tar.gz http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf netcdf-$(NETCDF_VER).tar.gz
	$(MKDIR_P) netcdf-build
	cd netcdf-build && \
		../netcdf-$(NETCDF_VER)/configure --prefix=$(prefix) \
			--enable-shared --disable-static --disable-netcdf-4 ; \
		make -j $(make_threads) && \
		make install

else
if WITH_HDF5
	@echo "$@ already installed. Skipping installation."
else
	@echo "netcdf option not requested. To enable NetCDF option, "
	@echo "reconfigure with --enable-netcdf (to install NetCDF) or "
	@echo "--with-netcdf (to use an existing installation)."
endif
endif

installed_netcdf:
	$(MAKE) $(AM_MAKEFLAGS) netcdf
	touch $@


# ----------------------------------------------------------------------
# hdf5
# ----------------------------------------------------------------------
hdf5: installed_mpi
if INSTALL_HDF5
	$(FETCH_SCRIPT) "$(downloader)" hdf5-$(HDF5_VER).tar.gz http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf hdf5-$(HDF5_VER).tar.gz
	$(MKDIR_P) hdf5-build
	cd hdf5-build && \
		../hdf5-$(HDF5_VER)/configure --enable-parallel --enable-shared --disable-static --prefix=$(prefix) CC=mpicc CXX=mpicxx FC=mpif90 ; \
		make -j $(make_threads) && \
		make install

else
if WITH_HDF5
	@echo "$@ already installed. Skipping installation."
else
	@echo "hdf5 option not requested. To enable HDF5 option, "
	@echo "reconfigure with --enable-hdf5 (to install HDF5) or "
	@echo "--with-hdf5 (to use an existing installation)."
endif
endif

installed_hdf5:
	$(MAKE) $(AM_MAKEFLAGS) hdf5
	touch $@


# ----------------------------------------------------------------------
# petsc
# ----------------------------------------------------------------------
petsc: installed_mpi
if INSTALL_PETSC
# :TODO: Use nightly tarball if PyLith is coming from SVN repository
	$(FETCH_SCRIPT) "$(downloader)" petsc-dev-pylith-$(PYLITH_VER).tgz http://www.geodynamics.org/cig/software/pylith
	$(TAR) -zxf petsc-dev-$(PYLITH_VER).tar.gz
else
	@echo "$@ already installed. Skipping installation."
endif

installed_petsc:
	$(MAKE) $(AM_MAKEFLAGS) petsc
	touch $@


# ----------------------------------------------------------------------
# spatialdata
# ----------------------------------------------------------------------
spatialdata: installed_numpy installed_proj4 installed_swig installed_cppunit
if INSTALL_SPATIALDATA
	spatialdata_options =
if WITH_TESTING
	spatialdata_options += --enable-testing
endif
# :TODO: Add switch for using SVN repository (add --enable-swig)
	$(FETCH_DIR) "$(downloader)" spatialdata-$(SPATIALDATA_VER).tgz http://www.geodynamics.org/cig/software/pylith
	$(TAR) -zxvf spatialdata-$(SPATIALDATA_VER).tgz
	$(MKDIR_P) spatialdata-build
	cd spatialdata-build && \
		../spatialdata-$(SPATIALDATA_VER)/configure --prefix=$(prefix) $(spatialdata_options)
else
	@echo "$@ already installed. Skipping installation."
endif

installed_spatialdata:
	$(MAKE) $(AM_MAKEFLAGS) spatialdata
	touch $@


# ----------------------------------------------------------------------
# nemesis
# ----------------------------------------------------------------------
nemesis: installed_mpi installed_python
if INSTALL_NEMESIS
	$(FETCH_SCRIPT) "$(downloader)" nemesis-$(NEMESIS_VER).tar.gz http://www.geodynamics.org/cig/software/pythia
	$(TAR) -zxvf nemesis-$(NEMESIS_VER).tar.gz
	$(MKDIR_P) nemesis-build
	cd nemesis-build && \
		../nemesis-$(NEMESIS_VER)/configure --prefix=$(prefix) ; \
		make && \
		make install

else
	@echo "$@ already installed. Skipping installation."
endif

installed_nemesis:
	$(MAKE) $(AM_MAKEFLAGS) nemesis
	touch $@


# ----------------------------------------------------------------------
# fiat
# ----------------------------------------------------------------------
fiat: installed_numpy
if INSTALL_FIAT
	$(FETCH_SCRIPT) "$(downloader)" ScientificPython-$(SCIENTIFICPYTHON_VER).tar.gz http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf ScientificPython-$(SCIENTIFICPYTHON_VER).tar.gz
	cd ScientificPython-$(SCIENTIFICPYTHON_VER) && python setup.py install --prefix=$(prefix)
	$(FETCH_SCRIPT) "$(downloader)" fiat-$(FIAT_VER).tar.gz http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf fiat-$(FIAT_VER).tar.gz
	cd fiat-$(FIAT_VER) && python setup.py install --prefix=$(prefix)

else
	@echo "$@ already installed. Skipping installation."
endif

installed_fiat:
	$(MAKE) $(AM_MAKEFLAGS) fiat
	touch $@


# ----------------------------------------------------------------------
# pylith
# ----------------------------------------------------------------------
pylith: installed_cppunit installed_swig installed_netcdf installed_hdf5 installed_petsc installed_nemesis installed_spatialdata installed_fiat

installed_pylith:
	$(MAKE) $(AM_MAKEFLAGS) pylith
	touch $@


# ----------------------------------------------------------------------
# clean
# ----------------------------------------------------------------------
CLEANFILES = $(noinst_tmp)

clean-builddirs:
	$(RM) $(RMFLAGS) -r $(noinst_builddirs)

clean-srcdirs:
	$(RM) $(RMFLAGS) -r $(noinst_srcdirs)

clean-local: clean-builddirs clean-srcdirs

# End of file
