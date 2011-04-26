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

PCRE_VER=8.12
SWIG_VER=2.0.2

NUMPY_VER=1.5.1

PROJ4_VER=4.7.0

NETCDF_VER=4.1.1
HDF5_VER=1.8.6

SCIENTIFICPYTHON_VER=2.9.1
FIAT_VER=0.9.9

NEMESIS_VER=1.0.2

if USE_PYLITH_SVN
SPATIALDATA_VER=dev
PYLITH_VER=dev
else
SPATIALDATA_VER=0.6.0
PYLITH_VER=1.5.2
endif


# ----------------------------------------------------------------------
# Files
# ----------------------------------------------------------------------
SUBDIRS = \
	bin

EXTRA_DIST = \
	AUTHORS \
	CHANGES \
	COPYING \
	INSTALL \
	NEWS \
	README


noinst_tmp = \
	installed_compilers \
	installed_python \
	installed_mpi \
	installed_cppunit \
	installed_swig \
	installed_numpy \
	installed_proj \
	installed_netcdf \
	installed_hdf5 \
	installed_fiat \
	installed_nemesis \
	installed_spatialdata \
	installed_petsc \
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
	nemesis-build \
	spatialdata-build \
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
# Environment settings.
# ----------------------------------------------------------------------
env_flags = CPPFLAGS=$(CPPFLAGS) LDFLAGS=$(LDFLAGS)

if WITH_FORTRAN
env_compilers = CC=$(CC) CXX=$(CXX) FC=$(FC)
env_mpicompilers = CC=mpicc CXX=mpicxx FC=mpif90
else
env_compilers = CC=$(CC) CXX=$(CXX)
env_mpicompilers = CC=mpicc CXX=mpicxx
endif

# ----------------------------------------------------------------------
# Targets
# ----------------------------------------------------------------------
all: installed_pylith

rebuild-all: finished_mkdest compilers python mpi cppunit swig numpy proj4 netcdf hdf5 fiat nemesis spatialdata petsc pylith

# ----------------------------------------------------------------------
# Note on configure invocations
#
# Normally, we would like to do configure ARGS && make && make
# install. However a bug in autoconf results in d.SYM directories
# generating an error when configure tries to remove them with "rm"
# rather than "rm -r". As a result, we use configure ARGS ; make &&
# make install.

# ----------------------------------------------------------------------
# setup
# ----------------------------------------------------------------------
mkdest:
	$(MKDIR_P) $(prefix)/include $(prefix)/lib $(prefix)/bin

finished_mkdest:
	$(MAKE) $(AM_MAKEFLAGS) mkdest && touch $@

# ----------------------------------------------------------------------
# compilers
# ----------------------------------------------------------------------
compilers: finished_mkdest
if INSTALL_GCC
	$(FETCH_SCRIPT) "$(downloader)" gcc-$(GCC_VER).tar.bz2 http://geodynamics.org/~buildbot/deps
	$(FETCH_SCRIPT) "$(downloader)" mpc-$(MPC_VER).tar.gz http://geodynamics.org/~buildbot/deps
	$(FETCH_SCRIPT) "$(downloader)" gmp-$(GMP_VER).tar.gz http://geodynamics.org/~buildbot/deps
	$(FETCH_SCRIPT) "$(downloader)" mpfr-$(MPFR_VER).tar.bz2 http://geodynamics.org/~buildbot/deps
	$(TAR) -jxf gcc-$(GCC_VER).tar.bz2
	cd gcc-$(GCC_VER) ; \
		tar -zxf ../gmp-$(GMP_VER).tar.gz; \
		ln -sf gmp-$(GMP_VER)/ gmp; \
		tar -zxf ../mpc-$(MPC_VER).tar.gz; \
		ln -sf mpc-$(MPC_VER)/ mpc; \
		tar -jxf ../mpfr-$(MPFR_VER).tar.bz2; \
		ln -sf mpfr-$(MPFR_VER)/ mpfr
	$(MKDIR_P) gcc-build
	cd gcc-build && \
		../gcc-4.5.2/configure --prefix=$(prefix) \
			--disable-multilib \
			--enable-languages=$(gcc_languages) \
			$(env_flags) && \
		make -j $(make_threads) $(env_flags) && \
		make install && \
		touch ../installed_compilers

if GCC_FORTRAN_ONLY
	mv $(prefix)/bin/gcc $(prefix)/bin/gcc-$(GCC_VER)
endif

else
	@echo "$@ already installed. Skipping installation."
endif

installed_compilers:
	$(MAKE) $(AM_MAKEFLAGS) compilers
	touch $@


# ----------------------------------------------------------------------
# python
# ----------------------------------------------------------------------
python: installed_compilers
if INSTALL_PYTHON
	$(FETCH_SCRIPT) "$(downloader)" Python-$(PYTHON_VER).tgz http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf Python-$(PYTHON_VER).tgz
	$(MKDIR_P) python-build
	cd python-build && \
		../Python-$(PYTHON_VER)/configure --prefix=$(prefix) \
		--enable-shared $(env_flags) && \
		make -j $(make_threads) && \
		make install && \
		touch ../installed_python
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
openmpi: installed_compilers
	$(FETCH_SCRIPT) "$(downloader)" openmpi-$(OPENMPI_VER).tar.gz http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf openmpi-$(OPENMPI_VER).tar.gz
	$(MKDIR_P) openmpi-build
	cd openmpi-build && \
		../openmpi-$(OPENMPI_VER)/configure \
			--prefix=$(prefix) $(env_flags) ; \
		make -j $(make_threads) && \
		make install && \
		touch ../installed_mpi
	if [ ! -x $(prefix)/bin/mpirun ]; then cd $(prefix)/bin && $(LN_S) mpiexec mpirun; fi


# ----------------------------------------------------------------------
# mpich
# ----------------------------------------------------------------------
if WITH_FORTRAN
mpich_options = --enable-fc
else
mpich_options = --disable-fc
endif
mpich: installed_compilers
	$(FETCH_SCRIPT) "$(downloader)" mpich2-$(MPICH2_VER).tar.gz http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf mpich2-$(MPICH2_VER).tar.gz
	$(MKDIR_P) mpich-build
	cd mpich-build && \
		../mpich2-$(MPICH2_VER)/configure \
			--with-pm=gforker \
			--enable-shared \
			--enable-sharedlibs=$(mpich_sharedarch) \
			--disable-static --disable-mpe \
			--prefix=$(prefix) \
			$(env_flags) $(env_compilers) $(mpich_options) ; \
		make -j $(make_threads) && \
		make install && \
		touch ../installed_mpi
	if [ ! -x $(prefix)/bin/mpirun ]; then cd $(prefix)/bin && $(LN_S) mpiexec mpirun; fi


# ----------------------------------------------------------------------
# cppunit
# ----------------------------------------------------------------------
cppunit: installed_compilers
if INSTALL_CPPUNIT
	$(FETCH_SCRIPT) "$(downloader)" cppunit-$(CPPUNIT_VER).tar.gz http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf cppunit-$(CPPUNIT_VER).tar.gz
	$(MKDIR_P) cppunit-build
	cd cppunit-build && \
		../cppunit-$(CPPUNIT_VER)/configure \
			--prefix=$(prefix) $(env_flags) ; \
		make -j $(make_threads) && \
		make install && \
		touch ../installed_cppunit

else
	@echo "$@ already installed. Skipping installation."
endif

installed_cppunit:
	$(MAKE) $(AM_MAKEFLAGS) cppunit
	touch $@


# ----------------------------------------------------------------------
# pcre
# ----------------------------------------------------------------------
pcre: installed_compilers
if INSTALL_PCRE
	$(FETCH_SCRIPT) "$(downloader)" pcre-$(PCRE_VER).tar.gz http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf pcre-$(PCRE_VER).tar.gz
	$(MKDIR_P) pcre-build
	cd pcre-build && \
		../pcre-$(PCRE_VER)/configure \
			--prefix=$(prefix) $(env_flags) ; \
		make -j $(make_threads) && \
		make install && \
		touch ../installed_pcre
else
	@echo "$@ already installed. Skipping installation."
endif

installed_pcre:
	$(MAKE) $(AM_MAKEFLAGS) pcre
	touch $@


# ----------------------------------------------------------------------
# swig
# ----------------------------------------------------------------------
swig: installed_pcre installed_compilers
if INSTALL_SWIG
	$(FETCH_SCRIPT) "$(downloader)" swig-$(SWIG_VER).tar.gz http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf swig-$(SWIG_VER).tar.gz
	$(MKDIR_P) swig-build
	cd swig-build && \
		../swig-$(SWIG_VER)/configure \
			--prefix=$(prefix) $(env_flags) ; \
		make -j $(make_threads) && \
		make install && \
		touch ../installed_swig
else
if WITH_SWIG
	@echo "$@ already installed. Skipping installation."
else
	@echo "$@ not required. Skipping installation."
endif
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
	cd numpy-1.5.1 && \
		$(PYTHON) setup.py install --prefix=$(prefix) && \
		touch ../installed_numpy

else
	@echo "$@ already installed. Skipping installation."
endif

installed_numpy:
	$(MAKE) $(AM_MAKEFLAGS) numpy
	touch $@


# ----------------------------------------------------------------------
# proj4
# ----------------------------------------------------------------------
proj4: installed_compilers
if INSTALL_PROJ4
	$(FETCH_SCRIPT) "$(downloader)" proj-$(PROJ4_VER).tar.gz http://geodynamics.org/~buildbot/deps
	$(FETCH_SCRIPT) "$(downloader)" proj-datumgrid-1.3.zip http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf proj-$(PROJ4_VER).tar.gz
	$(MKDIR_P) proj4-build/nad
	cd proj4-build/nad && \
		unzip ../../proj-datumgrid-1.3.zip
	cd proj4-build && \
		../proj-$(PROJ4_VER)/configure \
			--prefix=$(prefix) $(env_flags) ; \
		make -j $(make_threads) && \
		make install && \
		touch ../installed_proj4

else
	@echo "$@ already installed. Skipping installation."
endif

installed_proj4:
	$(MAKE) $(AM_MAKEFLAGS) proj4
	touch $@


# ----------------------------------------------------------------------
# netcdf
# ----------------------------------------------------------------------
netcdf: installed_compilers
if INSTALL_NETCDF
	$(FETCH_SCRIPT) "$(downloader)" netcdf-$(NETCDF_VER).tar.gz http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf netcdf-$(NETCDF_VER).tar.gz
	$(MKDIR_P) netcdf-build
	cd netcdf-build && \
		../netcdf-$(NETCDF_VER)/configure \
			--prefix=$(prefix) $(env_flags) \
			--enable-shared --disable-static --disable-netcdf-4 ; \
		make -j $(make_threads) && \
		make install && \
		touch ../installed_netcdf

else
if WITH_NETCDF
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
		../hdf5-$(HDF5_VER)/configure \
			--enable-parallel --enable-shared \
			--disable-static --prefix=$(prefix) \
			$(env_flags) $(env_mpicompilers) ; \
		make -j $(make_threads) && \
		make install && \
		touch ../installed_hdf5

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
# fiat
# ----------------------------------------------------------------------
fiat: installed_numpy
if INSTALL_FIAT
	$(FETCH_SCRIPT) "$(downloader)" ScientificPython-$(SCIENTIFICPYTHON_VER).tar.gz http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf ScientificPython-$(SCIENTIFICPYTHON_VER).tar.gz
	cd ScientificPython-$(SCIENTIFICPYTHON_VER) && $(PYTHON) setup.py install --prefix=$(prefix)
	$(FETCH_SCRIPT) "$(downloader)" fiat-$(FIAT_VER).tar.gz http://geodynamics.org/~buildbot/deps
	$(TAR) -zxf fiat-$(FIAT_VER).tar.gz
	cd fiat-$(FIAT_VER) && $(PYTHON) setup.py install --prefix=$(prefix)

else
	@echo "$@ already installed. Skipping installation."
endif

installed_fiat:
	$(MAKE) $(AM_MAKEFLAGS) fiat
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
		../nemesis-$(NEMESIS_VER)/configure \
			--prefix=$(prefix) $(env_flags) ; \
		make && \
		make install

else
	@echo "$@ already installed. Skipping installation."
endif

installed_nemesis:
	$(MAKE) $(AM_MAKEFLAGS) nemesis
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
if USE_PYLITH_SVN
spatialdata_options += --enable-swig
	$(SVN) co http://geodynamics.org/svn/cig/cs/spatialdata/trunk spatialdata-$(SPATIALDATA_VER)
	cd spatialdata-$(SPATIALDATA_VER) && $(AUTORECONF) -if
else
	$(FETCH_SCRIPT) "$(downloader)" spatialdata-$(SPATIALDATA_VER).tgz http://www.geodynamics.org/cig/software/pylith
	$(TAR) -zxvf spatialdata-$(SPATIALDATA_VER).tgz
endif
	$(MKDIR_P) spatialdata-build
	cd spatialdata-build && \
		../spatialdata-$(SPATIALDATA_VER)/configure \
			--prefix=$(prefix) $(env_flags) \
			$(spatialdata_options) ; \
		make -j $(make_threads) && \
		make install && \
		touch ../installed_spatialdata
if WITH_TESTING
	cd spatialdata-build && make -j $(make_threads) check
endif
else
	@echo "$@ already installed. Skipping installation."
endif

installed_spatialdata:
	$(MAKE) $(AM_MAKEFLAGS) spatialdata
	touch $@


# ----------------------------------------------------------------------
# petsc
# ----------------------------------------------------------------------
petsc: installed_mpi
if INSTALL_PETSC
if WITH_HDF5
petsc_options += --with-hdf5=1
endif
if INSTALL_HDF5
petsc_options += --with-hdf5-include=$(prefix)/include --with-hdf5-lib=$(prefix)/lib/libhdf5.dylib
endif
if USE_PYLITH_SVN
	hg clone http://petsc.cs.iit.edu/petsc/petsc-dev
	cd petsc-dev/config && \
		hg clone http://petsc.cs.iit.edu/petsc/BuildSystem BuildSystem
else
	$(FETCH_SCRIPT) "$(downloader)" petsc-dev-pylith-$(PYLITH_VER).tgz http://www.geodynamics.org/cig/software/pylith
	$(TAR) -zxf petsc-dev-pylith-$(PYLITH_VER).tgz
endif
	cd petsc-dev && \
		./configure --prefix=$(prefix) \
			--with-c2html=0 --with-x=0 \
			--CXXFLAGS=-DMPICH_IGNORE_CXX_SEEK \
			--with-clanguage=C++ \
			--with-mpicompilers=1 \
			--with-debugging=0 \
			--with-shared-libraries=1 \
			--with-sieve=1 \
			--download-boost=1 \
			$(petsc_options) $(env_flags) \
			PETSC_DIR=$(abs_builddir)/petsc-dev ; \
		make PETSC_DIR=$(abs_builddir)/petsc-dev && \
		make PETSC_DIR=$(abs_builddir)/petsc-dev install && \
		make PETSC_DIR=$(abs_builddir)/petsc-dev test && \
		touch ../installed_petsc
else
	@echo "$@ already installed. Skipping installation."
endif

installed_petsc:
	$(MAKE) $(AM_MAKEFLAGS) petsc
	touch $@


# ----------------------------------------------------------------------
# pylith
# ----------------------------------------------------------------------
pylith: installed_cppunit installed_swig installed_netcdf installed_hdf5 installed_fiat installed_nemesis installed_spatialdata installed_petsc
pylith_options = 
if WITH_NETCDF
pylith_options += --enable-cubit
endif
if WITH_TESTING
pylith_options += --enable-testing
endif
if USE_PYLITH_SVN
pylith_options += --enable-swig
	$(SVN) co http://geodynamics.org/svn/cig/short/3D/PyLith/$(pylith_svn) pylith-$(PYLITH_VER)
	cd pylith-$(PYLITH_VER) && $(AUTORECONF) -if
else
	$(FETCH_SCRIPT) "$(downloader)" pylith-$(PYLITH_VER).tgz http://www.geodynamics.org/cig/software/pylith
	$(TAR) -zxvf pylith-$(PYLITH_VER).tgz
endif
	$(MKDIR_P) pylith-build
	cd pylith-build && \
		../pylith-$(PYLITH_VER)/configure \
			--prefix=$(prefix) $(pylith_options) $(env_flags) \
			PETSC_DIR=$(PETSC_DIR) PETSC_ARCH=$(PETSC_ARCH) ; \
		make -j $(make_threads) && \
		make install && \
		touch ../installed_pylith
if WITH_TESTING
	cd pylith-build && make -j $(make_threads) check
endif

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
