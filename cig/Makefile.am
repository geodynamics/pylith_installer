# ----------------------------------------------------------------------
#
# Brad T. Aagaard, U.S. Geological Survey
# Charles A. Williams, GNS Science
# Matthew G. Knepley, University of Chicago
#
# This code was developed as part of the Computational Infrastructure
# for Geodynamics (http://geodynamics.org).
#
# Copyright (c) 2010-2016 University of California, Davis
#
# See COPYING for license information.
#
# ----------------------------------------------------------------------

include $(top_srcdir)/packages.am
include $(top_srcdir)/environment.am

# ----------------------------------------------------------------------
# Files
# ----------------------------------------------------------------------
noinst_tmp = \
	installed_pythia \
	installed_nemesis \
	installed_spatialdata \
	installed_petsc \
	installed_pylith \
	installed_parametersgui


noinst_builddirs = \
	nemesis-build \
	spatialdata-build \
	pylith-build


noinst_srcdirs = \
	spatialdata-$(SPATIALDATA_VER) \
	pythia-$(PYTHIA_VER) \
	nemesis-$(NEMESIS_VER) \
	pylith-$(PYLITH_VER)

# ----------------------------------------------------------------------
# Targets
# ----------------------------------------------------------------------
all: installed_pythia installed_nemesis installed_spatialdata installed_petsc installed_pylith installed_parametersgui

# ----------------------------------------------------------------------
# Note on configure invocations
#
# Normally, we would like to do configure ARGS && make && make
# install. However a bug in autoconf results in d.SYM directories
# generating an error when configure tries to remove them with "rm"
# rather than "rm -r". As a result, we use configure ARGS ; make &&
# make install.

# ----------------------------------------------------------------------
# pythia
# ----------------------------------------------------------------------
pythia:
if INSTALL_PYTHIA
	$(FETCH_SCRIPT) "$(downloader)" setuptools-0.6c11.tar.gz $(DEPS_URL)
	$(FETCH_SCRIPT) "$(downloader)" pythia-$(PYTHIA_VER).tar.gz https://github.com/geodynamics/pythia/releases/download/v$(PYTHIA_VER)
	$(TAR) -xf pythia-$(PYTHIA_VER).tar.gz
	$(CP) -p setuptools-0.6c11.tar.gz pythia-$(PYTHIA_VER)
	cd pythia-$(PYTHIA_VER) && $(PYTHON) setup.py install --prefix=$(prefix) && touch $(abs_builddir)/installed_pythia

else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_pythia
endif

installed_pythia:
	$(MAKE) $(AM_MAKEFLAGS) pythia


# ----------------------------------------------------------------------
# nemesis
# ----------------------------------------------------------------------
nemesis: installed_pythia
if INSTALL_NEMESIS
	$(FETCH_SCRIPT) "$(downloader)" nemesis-$(NEMESIS_VER).tar.gz https://github.com/geodynamics/nemesis/releases/download/v$(NEMESIS_VER)
	$(TAR) -xf nemesis-$(NEMESIS_VER).tar.gz
	$(MKDIR_P) nemesis-build
	cd nemesis-build && \
		../nemesis-$(NEMESIS_VER)/configure \
			--prefix=$(prefix) $(env_flags_cig) $(env_mpicompilers); \
		make && \
		make install && \
		touch $(abs_builddir)/installed_nemesis

else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_nemesis
endif

installed_nemesis:
	$(MAKE) $(AM_MAKEFLAGS) nemesis


# ----------------------------------------------------------------------
# spatialdata
# ----------------------------------------------------------------------
spatialdata: installed_pythia installed_git
if INSTALL_SPATIALDATA
spatialdata_options = 
if WITH_TESTING
spatialdata_options += --enable-testing
endif
if WITH_DEBUGGING
endif
if USE_PYLITH_GIT
spatialdata_options += --enable-swig
	$(GIT) clone --branch master --single-branch --recursive $(spatialdata_repo) spatialdata-$(SPATIALDATA_VER)
	cd spatialdata-$(SPATIALDATA_VER) && $(AUTORECONF) -if
else
	$(FETCH_SCRIPT) "$(downloader)" spatialdata-$(SPATIALDATA_VER).tgz https://github.com/geodynamics/spatialdata/releases/download/v$(SPATIALDATA_VER)
	$(TAR) -xf spatialdata-$(SPATIALDATA_VER).tgz
endif
	$(MKDIR_P) spatialdata-build
	cd spatialdata-build && \
		../spatialdata-$(SPATIALDATA_VER)/configure \
			--prefix=$(prefix) $(env_flags_cig) $(env_compilers) \
			CPPFLAGS="$(CPPFLAGS) $(CPPUNIT_INCLUDES) $(PROJ_INCLUDES)" \
			LDFLAGS="$(LDFLAGS) $(CPPUNIT_LDFLAGS) $(PROJ_LDFLAGS)" \
			$(spatialdata_options) ; \
		make -j $(make_threads) && \
		make install
if WITH_TESTING
	cd spatialdata-build && \
		make -j $(make_threads) check && \
		touch $(abs_builddir)/installed_spatialdata
else
	touch $(abs_builddir)/installed_spatialdata
endif
else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_spatialdata
endif

installed_spatialdata:
	$(MAKE) $(AM_MAKEFLAGS) spatialdata


# ----------------------------------------------------------------------
# petsc
# ----------------------------------------------------------------------
petsc: installed_cmake installed_git installed_hdf5 installed_compilers
if INSTALL_PETSC
petsc_options += --with-hdf5=1
if INSTALL_HDF5
petsc_options += --with-zlib=1 --LIBS=-lz
endif
if WITH_DEBUGGING
petsc_options += --with-debugging=1
else
petsc_options += --with-debugging=0
endif
if WITH_FORTRAN
petsc_options += 
else
petsc_options += --with-fc=0
endif
if PETSC_TARBALL
	$(FETCH_SCRIPT) "$(downloader)" petsc-pylith-$(PETSC_VER).tgz https://github.com/geodynamics/pylith/releases/download/v$(PETSC_VER)
	$(TAR) -xf petsc-pylith-$(PETSC_VER).tgz && mv petsc-pylith $(PETSC_DIR)
else
	git clone --branch knepley/pylith --single-branch $(petsc_repo) $(PETSC_DIR)
endif
	cd $(PETSC_DIR) && \
		./configure \
			--with-c2html=0 --with-x=0 \
			--with-clanguage=C \
			--with-mpicompilers=1 \
			--with-shared-libraries=1 --with-64-bit-points=1 --with-large-file-io=1 \
			$(petsc_options) $(env_flags_cig) \
			CPPFLAGS="$(CPPFLAGS) $(HDF5_INCLUDES)" LDFLAGS="$(LDFLAGS) $(HDF5_LDFLAGS)" \
			PETSC_DIR=$(PETSC_DIR) PETSC_ARCH=$(PETSC_ARCH) && \
		make -j$(make_threads) PETSC_DIR=$(PETSC_DIR) PETSC_ARCH=$(PETSC_ARCH) && \
		make PETSC_DIR=$(PETSC_DIR) test && \
		touch $(abs_builddir)/installed_petsc
else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_petsc
endif


installed_petsc:
	$(MAKE) $(AM_MAKEFLAGS) petsc


# ----------------------------------------------------------------------
# pylith
# ----------------------------------------------------------------------
pylith: installed_pythia installed_nemesis installed_spatialdata installed_petsc installed_git
pylith_options = --enable-netcdf --enable-hdf5
if WITH_TESTING
pylith_options += --enable-testing
endif
if USE_PYLITH_GIT
pylith_options += --enable-swig
	$(GIT) clone --branch $(pylith_git) --single-branch --recursive $(pylith_repo) pylith-$(PYLITH_VER)
	cd pylith-$(PYLITH_VER) && $(AUTORECONF) -if
else
	$(FETCH_SCRIPT) "$(downloader)" pylith-$(PYLITH_VER).tgz https://github.com/geodynamics/pylith/releases/download/v$(PYLITH_VER)
	$(TAR) -xf pylith-$(PYLITH_VER).tgz
endif
	$(MKDIR_P) pylith-build
	cd pylith-build && \
		../pylith-$(PYLITH_VER)/configure \
			--prefix=$(prefix) $(pylith_options) \
                        $(env_flags_cig) $(env_mpicompilers) \
			CPPFLAGS="$(CPPFLAGS) $(CPPUNIT_INCLUDES) $(PROJ_INCLUDES) $(HDF5_INCLDUES) $(NETCDF_INCLUDES)" \
			LDFLAGS="$(LDFLAGS) $(CPPUNIT_LDFLAGS) $(PROJ_LDFLAGS) $(HDF5_LDFLAGS) $(NETCDF_LDFLAGS)" \
			PETSC_DIR=$(PETSC_DIR) PETSC_ARCH=$(PETSC_ARCH) ; \
		make -j $(make_threads) && \
		make install
if WITH_TESTING
	cd pylith-build && \
		make -j $(make_threads) check && \
		touch $(abs_builddir)/installed_pylith
else
	touch $(abs_builddir)/installed_pylith
endif

installed_pylith:
	$(MAKE) $(AM_MAKEFLAGS) pylith


# ----------------------------------------------------------------------
# parametersgui (pylith-parameters)
# ----------------------------------------------------------------------
parametersgui: 
if INSTALL_PARAMETERSGUI
	$(FETCH_SCRIPT) "$(downloader)" pylith_parameters-$(PARAMETERSGUI_VER).tgz https://github.com/geodynamics/pylith_parameters/releases/download/v$(PARAMETERSGUI_VER)
	cd $(prefix) && $(TAR) -xf $(abs_builddir)/pylith_parameters-$(PARAMETERSGUI_VER).tgz && \
		cd $(abs_builddir) && \
		touch $(abs_builddir)/installed_parametersgui

else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_parametersgui
endif

installed_parametersgui:
	$(MAKE) $(AM_MAKEFLAGS) parametersgui

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
