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
# Copyright (c) 2010-2015 University of California, Davis
#
# See COPYING for license information.
#
# ----------------------------------------------------------------------

ACLOCAL_AMFLAGS = -I m4

# ----------------------------------------------------------------------
# Packages URL
# ----------------------------------------------------------------------
DEPS_URL=http://geoweb.cse.ucdavis.edu/~buildbot/deps

# ----------------------------------------------------------------------
# Package Versions
# ----------------------------------------------------------------------
GCC_VER=4.7.3
MPC_VER=1.0.2
GMP_VER=4.3.2
MPFR_VER=2.4.2

PYTHON_VER=2.7.6

MPICH_VER=3.1.3
OPENMPI_VER=1.8.4

CPPUNIT_VER=1.13.2

PCRE_VER=8.12
SWIG_VER=2.0.6

GIT_VER=1.8.2.1

NUMPY_VER=1.7.2

PROJ4_VER=4.8.0

HDF5_VER=1.8.11p2
H5PY_VER=2.2.1

NETCDF_VER=4.1.3-p1
NETCDFPY_VER=1.1.8

SCIENTIFICPYTHON_VER=2.9.1
FIAT_VER=0.9.9

PYTHIA_VER=0.8.1.16
NEMESIS_VER=1.1.0

CMAKE_VER=2.8.12.2

if USE_PYLITH_GIT
SPATIALDATA_VER=master
PYLITH_VER=$(pylith_git)
if PETSC_TARBALL
PETSC_VER=2.1.0
endif
else
SPATIALDATA_VER=1.9.5
PYLITH_VER=2.1.0
PETSC_VER=2.1.0
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
	installed_proj4 \
	installed_netcdf \
	installed_netcdfpy \
	installed_hdf5 \
	installed_h5py \
	installed_fiat \
	installed_pythia \
	installed_nemesis \
	installed_spatialdata \
	installed_cmake \
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
	mpich-$(MPICH_VER) \
	cppunit-$(CPPUNIT_VER) \
	swig-$(SWIG_VER) \
	proj-$(PROJ4_VER) \
	netcdf-$(NETCDF_VER) \
	netCDF4-$(NETCDFPY_VER) \
	hdf5-$(HDF5_VER) \
	h5py-$(H5PY_VER) \
	spatialdata-$(SPATIALDATA_VER) \
	pythia-$(PYTHIA_VER) \
	nemesis-$(NEMESIS_VER) \
	cmake-$(CMAKE_VER) \
	pylith-$(PYLITH_VER)


FETCH_SCRIPT = $(top_srcdir)/bin/fetch.sh

# ----------------------------------------------------------------------
# Environment settings.
# ----------------------------------------------------------------------
abs_builddir=`pwd`
env_flags = CPPFLAGS="$(CPPFLAGS)" LDFLAGS="$(LDFLAGS)" CFLAGS="$(CFLAGS)" CXXFLAGS="$(CXXFLAGS) -DMPICH_IGNORE_CXX_SEEK" FCFLAGS="$(FCFLAGS)"

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

rebuild-all: finished_mkdest compilers python mpi cppunit swig numpy proj4 netcdf hdf5 h5py fiat nemesis spatialdata petsc pylith

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
	$(FETCH_SCRIPT) "$(downloader)" gcc-$(GCC_VER).tar.bz2 $(DEPS_URL)
	$(FETCH_SCRIPT) "$(downloader)" mpc-$(MPC_VER).tar.gz $(DEPS_URL)
	$(FETCH_SCRIPT) "$(downloader)" gmp-$(GMP_VER).tar.gz $(DEPS_URL)
	$(FETCH_SCRIPT) "$(downloader)" mpfr-$(MPFR_VER).tar.bz2 $(DEPS_URL)
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
		../gcc-$(GCC_VER)/configure --prefix=$(prefix) \
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
	touch installed_compilers
endif

installed_compilers:
	$(MAKE) $(AM_MAKEFLAGS) compilers


# ----------------------------------------------------------------------
# python
# ----------------------------------------------------------------------
python: installed_compilers
if INSTALL_PYTHON
	$(FETCH_SCRIPT) "$(downloader)" Python-$(PYTHON_VER).tgz $(DEPS_URL)
	$(TAR) -zxf Python-$(PYTHON_VER).tgz
	$(MKDIR_P) python-build
	cd python-build && \
		../Python-$(PYTHON_VER)/configure --prefix=$(prefix) \
		--enable-shared $(env_flags) $(env_compilers) && \
		make -j $(make_threads) && \
		make install && \
		touch ../installed_python
else
	@echo "$@ already installed. Skipping installation."
	touch installed_python
endif

installed_python:
	$(MAKE) $(AM_MAKEFLAGS) python


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
	touch installed_mpi
endif

installed_mpi:
	$(MAKE) $(AM_MAKEFLAGS) mpi


# ----------------------------------------------------------------------
# openmpi
# ----------------------------------------------------------------------
openmpi: installed_compilers
	$(FETCH_SCRIPT) "$(downloader)" openmpi-$(OPENMPI_VER).tar.gz $(DEPS_URL)
	$(TAR) -zxf openmpi-$(OPENMPI_VER).tar.gz
	$(MKDIR_P) openmpi-build
	cd openmpi-build && \
		../openmpi-$(OPENMPI_VER)/configure \
			--prefix=$(prefix) $(env_flags) $(env_compilers); \
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
	$(FETCH_SCRIPT) "$(downloader)" mpich-$(MPICH_VER).tar.gz $(DEPS_URL)
	$(TAR) -zxf mpich-$(MPICH_VER).tar.gz
	$(MKDIR_P) mpich-build
	cd mpich-build && \
		../mpich-$(MPICH_VER)/configure \
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
	$(FETCH_SCRIPT) "$(downloader)" cppunit-$(CPPUNIT_VER).tar.gz $(DEPS_URL)
	$(TAR) -zxf cppunit-$(CPPUNIT_VER).tar.gz
	$(MKDIR_P) cppunit-build
	cd cppunit-build && \
		../cppunit-$(CPPUNIT_VER)/configure \
			--prefix=$(prefix) $(env_flags) $(env_compilers); \
		make -j $(make_threads) && \
		make install && \
		touch ../installed_cppunit

else
	@echo "$@ already installed. Skipping installation."
	touch installed_cppunit
endif

installed_cppunit:
	$(MAKE) $(AM_MAKEFLAGS) cppunit


# ----------------------------------------------------------------------
# pcre
# ----------------------------------------------------------------------
pcre: installed_compilers
if INSTALL_PCRE
	$(FETCH_SCRIPT) "$(downloader)" pcre-$(PCRE_VER).tar.gz $(DEPS_URL)
	$(TAR) -zxf pcre-$(PCRE_VER).tar.gz
	$(MKDIR_P) pcre-build
	cd pcre-build && \
		../pcre-$(PCRE_VER)/configure \
			--prefix=$(prefix) $(env_flags) $(env_compilers) ; \
		make -j $(make_threads) && \
		make install && \
		touch ../installed_pcre
else
	@echo "$@ already installed. Skipping installation."
	touch installed_pcre
endif

installed_pcre:
	$(MAKE) $(AM_MAKEFLAGS) pcre


# ----------------------------------------------------------------------
# swig
# ----------------------------------------------------------------------
swig: installed_pcre installed_compilers installed_python
if INSTALL_SWIG
	$(FETCH_SCRIPT) "$(downloader)" swig-$(SWIG_VER).tar.gz $(DEPS_URL)
	$(TAR) -zxf swig-$(SWIG_VER).tar.gz
	$(MKDIR_P) swig-build
	cd swig-build && \
		../swig-$(SWIG_VER)/configure \
			--prefix=$(prefix) $(env_flags) $(env_compilers) ; \
		make -j $(make_threads) && \
		make install && \
		touch ../installed_swig
else
if WITH_SWIG
	@echo "$@ already installed. Skipping installation."
else
	@echo "$@ not required. Skipping installation."
endif
	touch installed_swig
endif

installed_swig:
	$(MAKE) $(AM_MAKEFLAGS) swig


# ----------------------------------------------------------------------
# numpy
# ----------------------------------------------------------------------
numpy: installed_python
if INSTALL_NUMPY
	$(FETCH_SCRIPT) "$(downloader)" numpy-$(NUMPY_VER).tar.gz $(DEPS_URL)
	$(TAR) -zxf numpy-$(NUMPY_VER).tar.gz
	cd numpy-$(NUMPY_VER) && \
		$(PYTHON) setup.py install --prefix=$(prefix) && \
		touch ../installed_numpy

else
	@echo "$@ already installed. Skipping installation."
	touch installed_numpy
endif

installed_numpy:
	$(MAKE) $(AM_MAKEFLAGS) numpy


# ----------------------------------------------------------------------
# proj4
# ----------------------------------------------------------------------
proj4: installed_compilers
if INSTALL_PROJ4
	$(FETCH_SCRIPT) "$(downloader)" proj-$(PROJ4_VER).tar.gz $(DEPS_URL)
	$(FETCH_SCRIPT) "$(downloader)" proj-datumgrid-1.3.zip $(DEPS_URL)
	$(TAR) -zxf proj-$(PROJ4_VER).tar.gz
	$(MKDIR_P) proj4-build/nad
	cd proj4-build/nad && \
		unzip ../../proj-datumgrid-1.3.zip
	cd proj4-build && \
		../proj-$(PROJ4_VER)/configure \
			--prefix=$(prefix) $(env_flags) $(env_compilers) ; \
		make -j $(make_threads) && \
		make install && \
		touch ../installed_proj4

else
	@echo "$@ already installed. Skipping installation."
	touch installed_proj4
endif

installed_proj4:
	$(MAKE) $(AM_MAKEFLAGS) proj4


# ----------------------------------------------------------------------
# hdf5
# ----------------------------------------------------------------------
hdf5: installed_mpi
if WITH_FORTRAN
hdf5_options = --enable-fortran
endif
if INSTALL_HDF5
	$(FETCH_SCRIPT) "$(downloader)" hdf5-$(HDF5_VER).tar.gz $(DEPS_URL)
	$(TAR) -zxf hdf5-$(HDF5_VER).tar.gz
	$(MKDIR_P) hdf5-build
	cd hdf5-build && \
		../hdf5-$(HDF5_VER)/configure \
			--enable-parallel --enable-shared --enable-unsupported \
			--disable-static --prefix=$(prefix) $(hdf5_options) \
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
	touch installed_hdf5
endif

installed_hdf5:
	$(MAKE) $(AM_MAKEFLAGS) hdf5


# ----------------------------------------------------------------------
# h5py
# ----------------------------------------------------------------------
h5py: installed_hdf5 installed_numpy
if INSTALL_H5PY
	$(FETCH_SCRIPT) "$(downloader)" h5py-$(H5PY_VER).tar.gz $(DEPS_URL)
	$(TAR) -zxf h5py-$(H5PY_VER).tar.gz
	cd h5py-$(H5PY_VER) && \
		CC=mpicc python setup.py build --hdf5=$(prefix) && \
		python setup.py install --prefix=$(prefix) && \
		touch ../installed_h5py
else
if WITH_H5PY
	@echo "$@ already installed. Skipping installation."
else
	@echo "h5py option not requested. To enable h5py option, "
	@echo "reconfigure with --enable-h5py (to install H5PY)."
endif
	touch installed_h5py
endif

installed_h5py:
	$(MAKE) $(AM_MAKEFLAGS) h5py


# ----------------------------------------------------------------------
# netcdf
# ----------------------------------------------------------------------
netcdf: installed_compilers installed_hdf5
if INSTALL_NETCDF
if WITH_HDF5
netcdf_4_options = --enable-netcdf-4
else
netcdf_4_options = --disable-netcdf-4
endif
	$(FETCH_SCRIPT) "$(downloader)" netcdf-$(NETCDF_VER).tar.gz $(DEPS_URL)
	$(TAR) -zxf netcdf-$(NETCDF_VER).tar.gz
	$(MKDIR_P) netcdf-build
	cd netcdf-build && \
		../netcdf-$(NETCDF_VER)/configure \
			--prefix=$(prefix) $(env_flags) $(env_mpicompilers) \
			--enable-shared --disable-static $(netcdf_4_options) --disable-dap ; \
		sed -e "s/-l //g" libtool > libtool.tmp && mv -f libtool.tmp libtool; \
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
	touch installed_netcdf
endif

installed_netcdf:
	$(MAKE) $(AM_MAKEFLAGS) netcdf


# ----------------------------------------------------------------------
# netcdfpy
# ----------------------------------------------------------------------
netcdfpy: installed_netcdf installed_numpy
if INSTALL_NETCDFPY
	$(FETCH_SCRIPT) "$(downloader)" netCDF4-$(NETCDFPY_VER).tar.gz $(DEPS_URL)
	$(TAR) -zxf netCDF4-$(NETCDFPY_VER).tar.gz
	cd netCDF4-$(NETCDFPY_VER) && \
		CC=mpicc $(env_flags) python setup.py build && \
		python setup.py install --prefix=$(prefix) && \
		touch ../installed_netcdfpy
else
if WITH_NETCDFPY
	@echo "$@ already installed. Skipping installation."
else
	@echo "netCDF4 option not requested. To enable netCDF4 option, "
	@echo "reconfigure with --enable-netcdfpy (to install netCDF4)."
endif
	touch installed_netcdfpy
endif

installed_netcdfpy:
	$(MAKE) $(AM_MAKEFLAGS) netcdfpy


# ----------------------------------------------------------------------
# fiat
# ----------------------------------------------------------------------
fiat: installed_numpy
if INSTALL_FIAT
	$(FETCH_SCRIPT) "$(downloader)" ScientificPython-$(SCIENTIFICPYTHON_VER).tar.gz $(DEPS_URL)
	$(TAR) -zxf ScientificPython-$(SCIENTIFICPYTHON_VER).tar.gz
	cd ScientificPython-$(SCIENTIFICPYTHON_VER) && $(PYTHON) setup.py install --prefix=$(prefix)
	$(FETCH_SCRIPT) "$(downloader)" fiat-$(FIAT_VER).tar.gz $(DEPS_URL)
	$(TAR) -zxf fiat-$(FIAT_VER).tar.gz
	cd fiat-$(FIAT_VER) && $(PYTHON) setup.py install --prefix=$(prefix) && touch ../installed_fiat

else
	@echo "$@ already installed. Skipping installation."
	touch installed_fiat
endif

installed_fiat:
	$(MAKE) $(AM_MAKEFLAGS) fiat


# ----------------------------------------------------------------------
# pythia
# ----------------------------------------------------------------------
pythia: installed_python
if INSTALL_PYTHIA
	$(FETCH_SCRIPT) "$(downloader)" pythia-$(PYTHIA_VER).tar.gz https://github.com/geodynamics/pythia/releases/download/v$(PYTHIA_VER)
	$(TAR) -zxvf pythia-$(PYTHIA_VER).tar.gz
	cd pythia-$(PYTHIA_VER) && $(PYTHON) setup.py install --prefix=$(prefix) && touch ../installed_pythia

else
	@echo "$@ already installed. Skipping installation."
	touch installed_pythia
endif

installed_pythia:
	$(MAKE) $(AM_MAKEFLAGS) pythia


# ----------------------------------------------------------------------
# nemesis
# ----------------------------------------------------------------------
nemesis: installed_mpi installed_python installed_pythia
if INSTALL_NEMESIS
	$(FETCH_SCRIPT) "$(downloader)" nemesis-$(NEMESIS_VER).tar.gz https://github.com/geodynamics/nemesis/releases/download/v$(NEMESIS_VER)
	$(TAR) -zxvf nemesis-$(NEMESIS_VER).tar.gz
	$(MKDIR_P) nemesis-build
	cd nemesis-build && \
		../nemesis-$(NEMESIS_VER)/configure \
			--prefix=$(prefix) $(env_flags) $(env_mpicompilers); \
		make && \
		make install && \
		touch ../installed_nemesis

else
	@echo "$@ already installed. Skipping installation."
	touch installed_nemesis
endif

installed_nemesis:
	$(MAKE) $(AM_MAKEFLAGS) nemesis


# ----------------------------------------------------------------------
# spatialdata
# ----------------------------------------------------------------------
spatialdata: installed_numpy installed_pythia installed_proj4 installed_swig installed_cppunit
if INSTALL_SPATIALDATA
spatialdata_options = 
if WITH_TESTING
spatialdata_options += --enable-testing
endif
if USE_PYLITH_GIT
spatialdata_options += --enable-swig
	$(GIT) clone --recursive --depth 1 https://github.com/geodynamics/spatialdata.git spatialdata-$(SPATIALDATA_VER)
	cd spatialdata-$(SPATIALDATA_VER) && $(AUTORECONF) -if
else
	$(FETCH_SCRIPT) "$(downloader)" spatialdata-$(SPATIALDATA_VER).tgz https://github.com/geodynamics/spatialdata/releases/download/v$(SPATIALDATA_VER)
	$(TAR) -zxvf spatialdata-$(SPATIALDATA_VER).tgz
endif
	$(MKDIR_P) spatialdata-build
	cd spatialdata-build && \
		../spatialdata-$(SPATIALDATA_VER)/configure \
			--prefix=$(prefix) $(env_flags) $(env_compilers) \
			$(spatialdata_options) ; \
		make -j $(make_threads) && \
		make install && \
		touch ../installed_spatialdata
if WITH_TESTING
	cd spatialdata-build && make -j $(make_threads) check
endif
else
	@echo "$@ already installed. Skipping installation."
	touch installed_spatialdata
endif

installed_spatialdata:
	$(MAKE) $(AM_MAKEFLAGS) spatialdata


# ----------------------------------------------------------------------
# git
# ----------------------------------------------------------------------
git: installed_python
if INSTALL_GIT
	$(FETCH_SCRIPT) "$(downloader)" git-$(GIT_VER).tar.gz $(DEPS_URL)
	$(TAR) -zxf git-$(GIT_VER).tar.gz
	cd git-$(GIT_VER) && \
		make prefix=$(prefix) NO_EXPAT=1 NO_TCLTK=1 NO_GETTEXT=1 all install && \
		touch ../installed_git

else
	@echo "$@ already installed. Skipping installation."
	touch installed_git
endif

installed_git:
	$(MAKE) $(AM_MAKEFLAGS) git


# ----------------------------------------------------------------------
# cmake
# ----------------------------------------------------------------------
cmake:
if INSTALL_CMAKE
	$(FETCH_SCRIPT) "$(downloader)" cmake-$(CMAKE_VER).tar.gz $(DEPS_URL)
	$(TAR) -zxf cmake-$(CMAKE_VER).tar.gz
	cd cmake-$(CMAKE_VER) && \
		./bootstrap  --prefix=$(prefix) && make && make install && \
		touch ../installed_cmake
else
	@echo "Skipping $@ installation."
	touch installed_cmake
endif

installed_cmake:
	$(MAKE) $(AM_MAKEFLAGS) cmake


# ----------------------------------------------------------------------
# petsc
# ----------------------------------------------------------------------
petsc: installed_mpi installed_hdf5 installed_git installed_cmake
if INSTALL_PETSC
if WITH_HDF5
petsc_options += --with-hdf5=1
endif
if INSTALL_HDF5
petsc_options += --with-hdf5-include=$(prefix)/include --with-hdf5-lib=$(prefix)/lib/libhdf5.dylib --LIBS=-lz
endif
if WITH_CUDA
petsc_options += --with-cuda=1 --with-cusp=1 --with-thrust=1 --with-nvcc=$(NVCC)
endif
if INSTALL_CMAKE
petsc_build_options = -j$(make_threads) -C $(PETSC_ARCH) 
else
petsc_build_options = 
endif
if PETSC_TARBALL
	$(FETCH_SCRIPT) "$(downloader)" petsc-pylith-$(PETSC_VER).tgz https://github.com/geodynamics/pylith/releases/download/v$(PETSC_VER)
	$(TAR) -zxf petsc-pylith-$(PETSC_VER).tgz
else
	git clone -b knepley/pylith https://bitbucket.org/petsc/petsc.git petsc-pylith
endif
	cd petsc-pylith && \
		./configure --prefix=$(prefix) \
			--with-c2html=0 --with-x=0 \
			--with-clanguage=C \
			--with-mpicompilers=1 \
			--with-debugging=0 \
			--with-shared-libraries=1 \
			$(petsc_options) $(env_flags) \
			PETSC_DIR=$(abs_builddir) PETSC_ARCH=$(PETSC_ARCH) ; \
		make $(petsc_build_options) PETSC_DIR=$(abs_builddir) PETSC_ARCH=$(PETSC_ARCH) && \
		make PETSC_DIR=$(abs_builddir) install && \
		make PETSC_DIR=$(abs_builddir) test && \
		touch ../installed_petsc
else
	@echo "$@ already installed. Skipping installation."
	touch installed_petsc
endif

installed_petsc:
	$(MAKE) $(AM_MAKEFLAGS) petsc


# ----------------------------------------------------------------------
# pylith
# ----------------------------------------------------------------------
pylith: installed_cppunit installed_swig installed_netcdf installed_hdf5 installed_h5py installed_fiat installed_nemesis installed_pythia installed_spatialdata installed_petsc installed_netcdfpy 
pylith_options = 
if WITH_NETCDF
pylith_options += --enable-cubit
endif
if WITH_HDF5
pylith_options += --enable-hdf5
endif
if WITH_TESTING
pylith_options += --enable-testing
endif
if WITH_CUDA
pylith_options += --enable-cuda
endif
if USE_PYLITH_GIT
pylith_options += --enable-swig
	$(GIT) clone --recursive -b $(pylith_git) https://github.com/geodynamics/pylith.git pylith-$(PYLITH_VER)
	cd pylith-$(PYLITH_VER) && $(AUTORECONF) -if
else
	$(FETCH_SCRIPT) "$(downloader)" pylith-$(PYLITH_VER).tgz https://github.com/geodynamics/pylith/releases/download/v$(PYLITH_VER)
	$(TAR) -zxvf pylith-$(PYLITH_VER).tgz
endif
	$(MKDIR_P) pylith-build
	cd pylith-build && \
		../pylith-$(PYLITH_VER)/configure \
			--prefix=$(prefix) $(pylith_options) \
                        $(env_flags) $(env_mpicompilers) \
			PETSC_DIR=$(PETSC_DIR) PETSC_ARCH=$(PETSC_ARCH) ; \
		make -j $(make_threads) && \
		make install && \
		touch ../installed_pylith
if WITH_TESTING
	cd pylith-build && make -j $(make_threads) check
endif

installed_pylith:
	$(MAKE) $(AM_MAKEFLAGS) pylith


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
