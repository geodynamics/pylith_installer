# ----------------------------------------------------------------------
#
# Brad T. Aagaard, U.S. Geological Survey
# Charles A. Williams, GNS Science
# Matthew G. Knepley, University of Chicago
#
# This code was developed as part of the Computational Infrastructure
# for Geodynamics (http://geodynamics.org).
#
# Copyright (c) 2010-2023 University of California, Davis
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
	installed_spatialdata \
	installed_petsc \
	installed_pylith \
	installed_parametersgui


noinst_builddirs = \
	pythia-build \
	spatialdata-build \
	pylith-build


noinst_srcdirs = \
	spatialdata-$(SPATIALDATA_VER) \
	pythia-$(PYTHIA_VER) \
	pylith-$(PYLITH_VER)

# ----------------------------------------------------------------------
# Targets
# ----------------------------------------------------------------------
all: installed_pythia installed_spatialdata installed_petsc installed_pylith installed_parametersgui

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
if USE_PYLITH_GIT
	$(GIT) clone --single-branch --recursive $(pythia_repo) pythia-$(PYTHIA_VER)
	cd pythia-$(PYTHIA_VER) && $(AUTORECONF) -if
else
	$(FETCH_SCRIPT) "$(downloader)" pythia-$(PYTHIA_VER).tar.gz $(GITHUB_URL)/pythia/releases/download/v$(PYTHIA_VER)
	$(TAR) -xf pythia-$(PYTHIA_VER).tar.gz
endif
	$(MKDIR_P) pythia-build
	cd pythia-build && \
		../pythia-$(PYTHIA_VER)/configure --enable-testing \
			--prefix=$(prefix) $(env_flags_cig) $(env_mpicompilers); \
		$(MAKE) && \
		$(MAKE) install && \
		touch $(abs_builddir)/installed_pythia

else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_pythia
endif

installed_pythia:
	$(MAKE) $(AM_MAKEFLAGS) pythia


# ----------------------------------------------------------------------
# spatialdata
# ----------------------------------------------------------------------
spatialdata: installed_pythia
if INSTALL_SPATIALDATA
spatialdata_options = 
if WITH_TESTING
spatialdata_options += --enable-testing
endif
if WITH_DEBUGGING
endif
if USE_PYLITH_GIT
spatialdata_options += --enable-swig
	$(GIT) clone --single-branch --recursive $(spatialdata_repo) spatialdata-$(SPATIALDATA_VER)
	cd spatialdata-$(SPATIALDATA_VER) && $(AUTORECONF) -if
else
	$(FETCH_SCRIPT) "$(downloader)" spatialdata-$(SPATIALDATA_VER).tar.gz $(GITHUB_URL)/spatialdata/releases/download/v$(SPATIALDATA_VER)
	$(TAR) -xf spatialdata-$(SPATIALDATA_VER).tar.gz
endif
	$(MKDIR_P) spatialdata-build
	cd spatialdata-build && \
		../spatialdata-$(SPATIALDATA_VER)/configure \
			--prefix=$(prefix) $(env_flags_cig) $(env_compilers) \
			CPPFLAGS="$(CPPFLAGS) $(CATCH2_INCLUDES) $(PROJ_INCLUDES)" \
			LDFLAGS="$(LDFLAGS) $(CATCH2_LDFLAGS) $(PROJ_LDFLAGS)" \
			$(spatialdata_options) ; \
		$(MAKE) -j$(make_threads) && \
		$(MAKE) install
if WITH_TESTING
	cd spatialdata-build && \
		$(MAKE) -j$(make_threads) check && \
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
build_petsc: 
petsc_options += --with-hdf5=1
PETSC_DIR_BUILD = $(abs_top_builddir)/cig/petsc-pylith
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
	$(FETCH_SCRIPT) "$(downloader)" petsc-pylith-$(PETSC_VER).tar.gz $(GITHUB_URL)/pylith/releases/download/v$(PETSC_VER)
	$(TAR) -xf petsc-pylith-$(PETSC_VER).tar.gz
else
	git clone --branch knepley/pylith --single-branch $(petsc_repo) petsc-pylith
endif
	cd petsc-pylith && \
		$(env_cert) $(PYTHON) ./configure \
			--prefix=$(prefix) \
			--with-c2html=0 --with-x=0 \
			--with-clanguage=C \
			--with-mpicompilers=1 \
			--with-shared-libraries=1 --with-64-bit-points=1 --with-large-file-io=1 \
			$(petsc_options) $(env_flags_cig) \
			CPPFLAGS="$(CPPFLAGS) $(HDF5_INCLUDES)" LDFLAGS="$(LDFLAGS) $(HDF5_LDFLAGS)" \
			PETSC_DIR=$(PETSC_DIR_BUILD)  PETSC_ARCH=$(PETSC_ARCH) && \
		$(MAKE) -j$(make_threads) PETSC_DIR=$(PETSC_DIR_BUILD) PETSC_ARCH=$(PETSC_ARCH)

petsc:
if INSTALL_PETSC
if INSTALL_DEVELOPER
	$(MAKE) PETSC_DIR=$(PETSC_DIR_BUILD) check && \
		touch $(abs_builddir)/installed_petsc
else
	$(MAKE) PETSC_DIR=$(PETSC_DIR_BUILD) install && \
		$(MAKE) PETSC_DIR=$(PETSC_DIR_BUILD) check && \
		touch $(abs_builddir)/installed_petsc
endif
else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_petsc
endif

installed_petsc:
	$(MAKE) $(AM_MAKEFLAGS) build_petsc
	$(MAKE) $(AM_MAKEFLAGS) petsc


# ----------------------------------------------------------------------
# pylith
# ----------------------------------------------------------------------
pylith: installed_pythia installed_spatialdata installed_petsc
pylith_options = --enable-cubit --enable-hdf5
if WITH_TESTING
pylith_options += --enable-testing
endif
if USE_PYLITH_GIT
pylith_options += --enable-swig
	$(GIT) clone --branch $(pylith_git) --single-branch --recursive $(pylith_repo) pylith-$(PYLITH_VER)
	cd pylith-$(PYLITH_VER) && $(AUTORECONF) -if
else
	$(FETCH_SCRIPT) "$(downloader)" pylith-$(PYLITH_VER).tar.gz https://github.com/geodynamics/pylith/releases/download/v$(PYLITH_VER)
	$(TAR) -xf pylith-$(PYLITH_VER).tar.gz
endif
	$(MKDIR_P) pylith-build
	cd pylith-build && \
		../pylith-$(PYLITH_VER)/configure \
			--prefix=$(prefix) $(pylith_options) \
                        $(env_flags_cig) $(env_mpicompilers) \
			CPPFLAGS="$(CPPFLAGS) $(CATCH2_INCLUDES) $(PROJ_INCLUDES) $(HDF5_INCLUDES) $(NETCDF_INCLUDES)" \
			LDFLAGS="$(LDFLAGS) $(CATCH2_LDFLAGS) $(PROJ_LDFLAGS) $(HDF5_LDFLAGS) $(NETCDF_LDFLAGS)" \
			PETSC_DIR=$(PETSC_DIR) PETSC_ARCH=$(PETSC_ARCH) ; \
		$(MAKE) -j $(make_threads) && \
		$(MAKE) install
if WITH_TESTING
	cd pylith-build && \
		$(MAKE) -j $(make_threads) check && \
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
	$(FETCH_SCRIPT) "$(downloader)" pylith_parameters-$(PARAMETERSGUI_VER).tar.gz https://github.com/geodynamics/pylith_parameters/releases/download/v$(PARAMETERSGUI_VER)
	cd $(prefix) && $(TAR) -xf $(abs_builddir)/pylith_parameters-$(PARAMETERSGUI_VER).tar.gz && \
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
