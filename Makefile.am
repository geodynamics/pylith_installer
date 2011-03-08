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
	gcc-4.5.2 \
	Python-2.6.6 \
	openmpi-1.4.3 \
	mpich2-1.3.2p1 \
	cppunit-1.12.1 \
	swig-2.0.2 \
	proj-4.7.0 \
	netcdf-4.1.1 \
	hdf5-1.8.6 \
	spatialdata-X.X.X \
	nemesis-X.X.X \
	pylith-X.X.X

default: installed_pylith

all: gcc python mpi cppunit swig numpy proj4 netcdf hdf5 petsc nemesis spatialdata fiat

FETCH_SCRIPT = $(top_srcdir)/bin/fetch.sh

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
	$(FETCH_SCRIPT) "$(downloader)" gcc-4.5.2.tar.bz2 http://geodynamics.org/~buildbot/deps
	$(FETCH_SCRIPT) "$(downloader)" mpc-0.8.2.tar.gz http://geodynamics.org/~buildbot/deps
	$(FETCH_SCRIPT) "$(downloader)" gmp-4.3.2.tar.gz http://geodynamics.org/~buildbot/deps
	$(FETCH_SCRIPT) "$(downloader)" mpfr-2.4.2.tar.bz2 http://geodynamics.org/~buildbot/deps
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
		../gcc-4.5.2/configure --prefix=$(prefix) \
if ENABLE_FORTRAN
			--enable-languages=c,c++,fortran && \
else
			--enable-languages=c,c++ && \
endif
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
	$(FETCH_SCRIPT) $(downloader) Python-2.6.6.tgz http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf Python-2.6.6.tgz
	$(MKDIR_P) python-build
	cd python-build && \
		../Python-2.6.6/configure --prefix=$(prefix) && \
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
	$(FETCH_SCRIPT) "$(downloader)" mpich2-1.3.2p1.tar.gz http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf mpich2-1.3.2p1.tar.gz
	$(MKDIR_P) mpich-build
	cd mpich-build && \
		../mpich2-1.3.2p1/configure --with-pm=gforker \
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
	$(FETCH_SCRIPT) "$(downloader)" cppunit-1.12.1.tar.gz http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf cppunit-1.12.1.tar.gz
	$(MKDIR_P) cppunit-build
	cd cppunit-build && \
		../cppunit-1.12.1/configure --prefix=$(prefix) ; \
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
	$(FETCH_SCRIPT) "$(downloader)" swig-2.0.2.tar.gz http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf swig-2.0.2.tar.gz
	$(MKDIR_P) swig-build
	cd swig-build && \
		../swig-2.0.2/configure --prefix=$(HOME)/pylith_deps ; \
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
	$(FETCH) "(downloader)" swig-2.0.2.tar.gz http://geodynamics.org/~buildbot/deps
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
	$(FETCH_SCRIPT) "$(downloader)" proj-4.7.0.tar.gz http://geodynamics.org/~buildbot/deps
	$(FETCH_SCRIPT) "$(downloader)" proj-datumgrid-1.3.zip http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf proj-4.7.0.tar.gz
	$(MKDIR_P) proj4-build/nad
	cd proj4-build/nad && \
		unzip ../../proj-datumgrid-1.3.zip
	cd proj4-build && \
		../proj-4.7.0/configure --prefix=$(prefix) ; \
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
	$(FETCH_SCRIPT) "$(downloader)" netcdf-4.1.1.tar.gz http://geodynamics.org/~buildbot/deps
	$(TAR) -zxvf netcdf-4.1.1.tar.gz
	$(MKDIR_P) netcdf-build
	cd netcdf-build && \
		../netcdf-4.1.1/configure --prefix=$(prefix) \
			--enable-shared --disable-static --disable-netcdf-4 ; \
		make -j $(make_threads) && \
		make install

else
	@echo "$@ already installed. Skipping installation."
endif

installed_netcdf:
	$(MAKE) $(AM_MAKEFLAGS) netcdf
	touch $@

# ----------------------------------------------------------------------
# hdf5
# ----------------------------------------------------------------------
hdf5: installed_mpi
if INSTALL_HDF5
	$(FETCH_SCRIPT) "$(downloader)" hdf5-1.8.6.tar.gz http://geodynamics.org/~buildbot/deps
	$(TAR) -zxvf hdf5-1.8.6.tar.gz
	$(MKDIR_P) hdf5-build
	cd hdf5-build && \
		../hdf5-1.8.6/configure --enable-parallel --enable-shared --disable-static --prefix=$(prefix) CC=mpicc CXX=mpicxx FC=mpif90 ; \
		make -j $(make_threads) && \
		make install

else
	@echo "$@ already installed. Skipping installation."
endif

installed_hdf5:
	$(MAKE) $(AM_MAKEFLAGS) hdf5
	touch $@

# ----------------------------------------------------------------------
# petsc
# ----------------------------------------------------------------------
petsc: installed_mpi
if INSTALL_PETSC

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
	$(FETCH_DIR) "$(downloader)" nemesis.tar.gz 
	$(TAR) -zxvf hdf5-1.8.6.tar.gz
	$(MKDIR_P) nemesis-build
	cd nemesis-build && \
		../nemesis-dev/configure --prefix=$(prefix) ; \
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
	$(FETCH_SCRIPT) "$(downloader)" ScientificPython-2.9.1.tar.gz http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf ScientificPython-2.9.1.tar.gz
	cd ScientificPython-2.9.1 && python setup.py install --prefix=$(prefix)
	$(FETCH_SCRIPT) "$(downloader)" ScientificPython-2.9.1.tar.gz http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf fiat-0.9.9.tar.gz
	cd fiat-0.9.9 && python setup.py install --prefix=$(prefix)

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