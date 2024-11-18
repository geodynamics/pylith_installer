# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://geodynamics.org).
#
# Copyright (c) 2010-2024, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information. 
# =================================================================================================

include $(top_srcdir)/packages.am
include $(top_srcdir)/environment.am

# ----------------------------------------------------------------------
# Files
# ----------------------------------------------------------------------
noinst_tmp = \
	installed_autotools \
	installed_compilers \
	installed_openssl \
	installed_curl \
	installed_libxcrypt \
	installed_libffi \
	installed_python \
	installed_mpi \
	installed_catch2 \
	installed_pcre \
	installed_swig \
	installed_sqlite \
	installed_tiff \
	installed_proj \
	installed_hdf5 \
	installed_h5py \
	installed_netcdf \
	installed_netcdfpy \
	installed_cmake


noinst_builddirs = \
	gcc-build \
	m4-build \
	autoconf-build \
	automake-build \
	libtool-build \
	openssl-build \
	curl-build \
	libxcrypt-build \
	libffi-build \
	python-build \
	openmpi-build \
	mpich-build \
	catch2-build \
	swig-build \
	sqlite-build \
	tiff-build \
	proj4-build \
	hdf5-build \
	netcdf-build


noinst_srcdirs = \
	m4-$(M4_VER) \
	autoconf-$(AUTOCONF_VER) \
	automake-$(AUTOMAKE_VER) \
	libtool-$(LIBTOOL_VER) \
	gcc-$(GCC_VER) \
	Python-$(PYTHON_VER) \
	openssl-$(OPENSSL_VER) \
	curl-$(CURL_VER) \
	libxcrupt-$(LIBXCRYPT_VER) \
	libffi-$(LIBFFI_VER) \
	openmpi-$(OPENMPI_VER) \
	mpich-$(MPICH_VER) \
	catch2-$(CATCH2_VER) \
	pcre-$(PCRE_VER) \
	swig-$(SWIG_VER) \
	sqlite-$(SQLITE_VER) \
	proj-$(PROJ4_VER) \
	hdf5-$(HDF5_VER) \
	h5py-$(H5PY_VER) \
	netcdf-$(NETCDF_VER) \
	netCDF4-$(NETCDFPY_VER) \
	cmake-$(CMAKE_VER)

# ----------------------------------------------------------------------
# Targets
# ----------------------------------------------------------------------
all: finished_mkdest installed_autotools installed_compilers installed_openssl installed_curl installed_sqlite installed_python installed_mpi installed_catch2 installed_swig installed_sqlite installed_proj installed_hdf5 installed_h5py installed_netcdf installed_netcdfpy installed_cmake

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
	$(MKDIR_P) \
		$(prefix)/include \
		$(prefix)/lib \
		$(prefix)/bin \
		$(prefix)/$(PYTHON_SITEPKGS) \
		$(prefix)/$(PYTHON64_SITEPKGS)

finished_mkdest:
	$(MAKE) $(AM_MAKEFLAGS) mkdest && touch $@

# ----------------------------------------------------------------------
# autotools
# ----------------------------------------------------------------------
autotools: finished_mkdest
if INSTALL_AUTOTOOLS
	$(FETCH_SCRIPT) $(CURL) m4-$(M4_VER).tar.gz $(DEPS_URL)
	$(FETCH_SCRIPT) $(CURL) autoconf-$(AUTOCONF_VER).tar.gz $(DEPS_URL)
	$(FETCH_SCRIPT) $(CURL) automake-$(AUTOMAKE_VER).tar.gz $(DEPS_URL)
	$(FETCH_SCRIPT) $(CURL) libtool-$(LIBTOOL_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf m4-$(M4_VER).tar.gz
	mkdir -p m4-build
	cd m4-build && \
		../m4-$(M4_VER)/configure --prefix=$(prefix) $(env_flags_deps) && \
		$(MAKE) -j$(make_threads) && \
		$(MAKE) install
	$(TAR) -xf autoconf-$(AUTOCONF_VER).tar.gz
	mkdir -p autoconf-build
	cd autoconf-build && \
		../autoconf-$(AUTOCONF_VER)/configure --prefix=$(prefix) $(env_flags_deps) && \
		$(MAKE) -j$(make_threads) && \
		$(MAKE) install
	$(TAR) -xf automake-$(AUTOMAKE_VER).tar.gz
	mkdir -p automake-build
	cd automake-build && \
		../automake-$(AUTOMAKE_VER)/configure --prefix=$(prefix) $(env_flags_deps) && \
		$(MAKE) -j$(make_threads) && \
		$(MAKE) install
	$(TAR) -xf libtool-$(LIBTOOL_VER).tar.gz
	mkdir -p libtool-build
	cd libtool-build && \
		../libtool-$(LIBTOOL_VER)/configure --prefix=$(prefix)  $(env_flags_deps) && \
		$(MAKE) -j$(make_threads) && \
		$(MAKE) install && \
		touch $(abs_builddir)/installed_autotools
else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_autotools
endif

installed_autotools:
	$(MAKE) $(AM_MAKEFLAGS) autotools

# ----------------------------------------------------------------------
# cmake
# ----------------------------------------------------------------------
cmake:
if INSTALL_CMAKE
	$(FETCH_SCRIPT) $(CURL) cmake-$(CMAKE_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf cmake-$(CMAKE_VER).tar.gz
	cd cmake-$(CMAKE_VER) && \
		$(env_flags_deps) ./bootstrap --verbose --prefix=$(prefix) && make -j$(make_threads) && $(MAKE) install && \
		touch $(abs_builddir)/installed_cmake
else
	@echo "Skipping $@ installation."
	touch $(abs_builddir)/installed_cmake
endif

installed_cmake:
	$(MAKE) $(AM_MAKEFLAGS) cmake


# ----------------------------------------------------------------------
# compilers
# ----------------------------------------------------------------------
compilers: finished_mkdest
if INSTALL_GCC
	$(FETCH_SCRIPT) $(CURL) gcc-$(GCC_VER).tar.gz $(DEPS_URL)
	$(FETCH_SCRIPT) $(CURL) mpc-$(MPC_VER).tar.gz $(DEPS_URL)
	$(FETCH_SCRIPT) $(CURL) gmp-$(GMP_VER).tar.gz $(DEPS_URL)
	$(FETCH_SCRIPT) $(CURL) mpfr-$(MPFR_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf gcc-$(GCC_VER).tar.gz
	cd gcc-$(GCC_VER) ; \
		$(TAR) -xf ../gmp-$(GMP_VER).tar.gz; \
		ln -sf gmp-$(GMP_VER)/ gmp; \
		$(TAR) -xf ../mpc-$(MPC_VER).tar.gz; \
		ln -sf mpc-$(MPC_VER)/ mpc; \
		$(TAR) -xf ../mpfr-$(MPFR_VER).tar.gz; \
		ln -sf mpfr-$(MPFR_VER)/ mpfr
	$(MKDIR_P) gcc-build
	cd gcc-build && \
		../gcc-$(GCC_VER)/configure --prefix=$(prefix) \
			--disable-multilib \
			--enable-languages=$(gcc_languages) \
			$(env_flags_deps) && \
		$(MAKE) -j $(make_threads) $(env_flags_deps) && \
		$(MAKE) install && \
		touch $(abs_builddir)/installed_compilers

else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_compilers
endif

installed_compilers:
	$(MAKE) $(AM_MAKEFLAGS) compilers


# ----------------------------------------------------------------------
# openssl
# ----------------------------------------------------------------------
openssl: installed_compilers

if INSTALL_OPENSSL
	$(FETCH_SCRIPT) $(CURL) openssl-$(OPENSSL_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf openssl-$(OPENSSL_VER).tar.gz
	$(MKDIR_P) openssl-build
	cd openssl-build && \
		../openssl-$(OPENSSL_VER)/Configure \
			--prefix=$(prefix) --openssldir=$(prefix)/share/openssl \
			$(env_flags_deps) \
			CPPFLAGS="$(CPPFLAGS)" LDFLAGS="$(LDFLAGS)" \
			shared ; \
		$(MAKE) -j $(make_threads) && \
		$(MAKE) install_sw && \
		touch $(abs_builddir)/installed_openssl

else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_openssl
endif

installed_openssl:
	$(MAKE) $(AM_MAKEFLAGS) openssl


# ----------------------------------------------------------------------
# curl
# ----------------------------------------------------------------------
curl: installed_compilers installed_openssl
if INSTALL_CURL
	$(FETCH_SCRIPT) $(CURL) curl-$(CURL_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf curl-$(CURL_VER).tar.gz
	$(MKDIR_P) curl-build
	cd curl-build && \
		../curl-$(CURL_VER)/configure --prefix=$(prefix) \
			--enable-shared --with-openssl --disable-ldap --without-libpsl \
			$(env_flags_deps) $(env_compilers) \
			CPPFLAGS="$(CPPFLAGS)" LDFLAGS="$(LDFLAGS)" && \
		$(MAKE) -j $(make_threads) && \
		$(MAKE) install && \
		touch $(abs_builddir)/installed_curl

else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_curl
endif

installed_curl:
	$(MAKE) $(AM_MAKEFLAGS) curl


# ----------------------------------------------------------------------
# libxcrypt
# ----------------------------------------------------------------------
libxcrypt: installed_compilers installed_openssl
if INSTALL_LIBXCRYPT
	$(FETCH_SCRIPT) $(CURL) libxcrypt-$(LIBXCRYPT_VER).tar.xz $(DEPS_URL)
	$(TAR) -xf libxcrypt-$(LIBXCRYPT_VER).tar.xz
	$(MKDIR_P) libxcrypt-build
	cd libxcrypt-build && \
		../libxcrypt-$(LIBXCRYPT_VER)/configure --prefix=$(prefix) \
			--enable-shared --disable-obsolete-api --enable-hashes=all \
			$(env_flags_deps) $(env_compilers) \
			CPPFLAGS="$(CPPFLAGS)" LDFLAGS="$(LDFLAGS)" && \
		$(MAKE) -j $(make_threads) && \
		$(MAKE) install && \
		touch $(abs_builddir)/installed_libxcrypt

else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_libxcrypt
endif

installed_libxcrypt:
	$(MAKE) $(AM_MAKEFLAGS) libxcrypt


# ----------------------------------------------------------------------
# libffi
# ----------------------------------------------------------------------
libffi: installed_compilers installed_openssl
if INSTALL_LIBFFI
	$(FETCH_SCRIPT) $(CURL) libffi-$(LIBFFI_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf libffi-$(LIBFFI_VER).tar.gz
	$(MKDIR_P) libffi-build
	cd libffi-build && \
		../libffi-$(LIBFFI_VER)/configure --prefix=$(prefix) \
			--enable-shared \
			$(env_flags_deps) $(env_compilers) \
			CPPFLAGS="$(CPPFLAGS)" LDFLAGS="$(LDFLAGS)" && \
		$(MAKE) -j $(make_threads) && \
		$(MAKE) install && \
		touch $(abs_builddir)/installed_libffi

else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_libffi
endif

installed_libffi:
	$(MAKE) $(AM_MAKEFLAGS) libffi


# ----------------------------------------------------------------------
# python
# ----------------------------------------------------------------------
python: installed_compilers installed_openssl installed_sqlite installed_curl installed_libxcrypt installed_libffi
if INSTALL_PYTHON
if INSTALL_OPENSSL
OPENSSL=--with-openssl=$(prefix)
endif
	$(FETCH_SCRIPT) $(CURL) Python-$(PYTHON_VER).tgz $(DEPS_URL)
	$(TAR) -xf Python-$(PYTHON_VER).tgz
	$(MKDIR_P) python-build
	cd python-build && \
		../Python-$(PYTHON_VER)/configure --build=x86_64 --prefix=$(prefix) \
			--enable-shared --enable-optimizations $(OPENSSL) \
			$(env_flags_deps) $(env_compilers) \
			CPPFLAGS="$(CPPFLAGS)" LDFLAGS="$(LDFLAGS)"; \
		$(MAKE) -j $(make_threads) && \
		$(MAKE) install && \
		$(LN_S) $(prefix)/bin/python3 $(prefix)/bin/python && \
		touch $(abs_builddir)/installed_python
else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_python
endif

python_postinstall:
	python3 -m venv $(prefix)
	$(env_cert) $(PYTHON) -m pip install --no-cache-dir --upgrade pip setuptools certifi
	$(env_cert) $(PYTHON) -m pip install numpy --no-cache-dir 
	rm -f $(prefix)/share/openssl/cert.pem && $(MKDIR_P) $(prefix)/share/openssl && $(LN_S) $(prefix)/lib/python3.10/site-packages/certifi/cacert.pem $(prefix)/share/openssl/cert.pem 
if INSTALL_DEVELOPER
	$(env_cert) $(PYTHON) -m pip install --no-cache-dir coverage autopep8
	$(env_cert) $(PYTHON) -m pip install --no-cache-dir sphinx myst-parser pydata-sphinx-theme sphinx_design sphinx-copybutton sphinx-proof sphinxcontrib.bibtex
endif
if INSTALL_PYQT
	$(env_cert) $(PYTHON) -m pip install --no-cache-dir PyQt6
endif
if INSTALL_MATPLOTLIB
	$(env_cert) $(PYTHON) -m pip install --no-cache-dir matplotlib
endif
if INSTALL_PYVISTA
	$(env_cert) $(PYTHON) -m pip install --no-cache-dir pyvista
endif
if INSTALL_GMSH
	$(env_cert) $(PYTHON) -m pip install --no-cache-dir gmsh
endif

installed_python:
	$(MAKE) $(AM_MAKEFLAGS) python
	$(MAKE) $(AM_MAKEFLAGS) python_postinstall

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
	touch $(abs_builddir)/installed_mpi
endif

installed_mpi:
	$(MAKE) $(AM_MAKEFLAGS) mpi


# ----------------------------------------------------------------------
# openmpi
# ----------------------------------------------------------------------
openmpi: installed_compilers
	$(FETCH_SCRIPT) $(CURL) openmpi-$(OPENMPI_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf openmpi-$(OPENMPI_VER).tar.gz
	$(MKDIR_P) openmpi-build
	cd openmpi-build && \
		../openmpi-$(OPENMPI_VER)/configure --prefix=$(prefix) \
			$(env_flags_deps) $(env_compilers) \
			CPPFLAGS="$(CPPFLAGS)" LDFLAGS="$(LDFLAGS)"; \
		$(MAKE) -j $(make_threads) && \
		$(MAKE) install && \
		touch $(abs_builddir)/installed_mpi
	if [ ! -x $(prefix)/bin/mpirun ]; then cd $(prefix)/bin && $(LN_S) mpiexec mpirun; fi


# ----------------------------------------------------------------------
# mpich
# ----------------------------------------------------------------------
if WITH_FORTRAN
mpich_options += --enable-fc
else
mpich_options += --disable-fortran
endif
mpich: installed_compilers
	$(FETCH_SCRIPT) $(CURL) mpich-$(MPICH_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf mpich-$(MPICH_VER).tar.gz
	$(MKDIR_P) mpich-build
	cd mpich-build && \
		../mpich-$(MPICH_VER)/configure --prefix=$(prefix) \
			--enable-shared --disable-static \
			 $(mpich_options) \
			$(env_flags_deps) $(env_compilers) \
			CPPFLAGS="$(CPPFLAGS)" LDFLAGS="$(LDFLAGS)"; \
		$(MAKE) -j $(make_threads) && \
		$(MAKE) install && \
		touch $(abs_builddir)/installed_mpi
	if [ ! -x $(prefix)/bin/mpirun ]; then cd $(prefix)/bin && $(LN_S) mpiexec mpirun; fi


# ----------------------------------------------------------------------
# catch2
# ----------------------------------------------------------------------
catch2: installed_compilers installed_cmake
if INSTALL_CATCH2
	$(FETCH_SCRIPT) $(CURL) Catch2-$(CATCH2_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf Catch2-$(CATCH2_VER).tar.gz
	$(MKDIR_P) catch2-build
	cd catch2-build && \
		$(env_compilers) cmake -DCMAKE_INSTALL_PREFIX=$(prefix) -DCMAKE_POSITION_INDEPENDENT_CODE=ON ../Catch2-$(CATCH2_VER); \
		$(MAKE) -j $(make_threads) && \
		$(MAKE) install && \
		touch $(abs_builddir)/installed_catch2

else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_catch2
endif

installed_catch2:
	$(MAKE) $(AM_MAKEFLAGS) catch2


# ----------------------------------------------------------------------
# pcre
# ----------------------------------------------------------------------
pcre: installed_compilers
if INSTALL_PCRE
	$(FETCH_SCRIPT) $(CURL) pcre2-$(PCRE_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf pcre2-$(PCRE_VER).tar.gz
	$(MKDIR_P) pcre-build
	cd pcre-build && \
		../pcre2-$(PCRE_VER)/configure --prefix=$(prefix) \
			$(env_flags_deps) $(env_compilers) \
			CPPFLAGS="$(CPPFLAGS)" LDFLAGS="$(LDFLAGS)"; \
		$(MAKE) -j $(make_threads) && \
		$(MAKE) install && \
		touch $(abs_builddir)/installed_pcre
else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_pcre
endif

installed_pcre:
	$(MAKE) $(AM_MAKEFLAGS) pcre


# ----------------------------------------------------------------------
# swig
# ----------------------------------------------------------------------
swig: installed_pcre installed_compilers installed_python
if INSTALL_SWIG
	$(FETCH_SCRIPT) $(CURL) swig-$(SWIG_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf swig-$(SWIG_VER).tar.gz
	$(MKDIR_P) swig-build
	cd swig-build && \
		../swig-$(SWIG_VER)/configure --prefix=$(prefix) \
			$(env_flags_deps) $(env_compilers) \
			CPPFLAGS="$(CPPFLAGS) $(PCRE_INCLUDES)" LDFLAGS="$(LDFLAGS) $(PCRE_LDFLAGS)"; \
		$(MAKE) -j $(make_threads) && \
		$(MAKE) install && \
		touch $(abs_builddir)/installed_swig
else
if WITH_SWIG
	@echo "$@ already installed. Skipping installation."
else
	@echo "$@ not required. Skipping installation."
endif
	touch $(abs_builddir)/installed_swig
endif

installed_swig:
	$(MAKE) $(AM_MAKEFLAGS) swig


# ----------------------------------------------------------------------
# sqlite
# ----------------------------------------------------------------------
sqlite: installed_compilers
if INSTALL_SQLITE
	$(FETCH_SCRIPT) $(CURL) sqlite-autoconf-$(SQLITE_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf sqlite-autoconf-$(SQLITE_VER).tar.gz
	$(MKDIR_P) sqlite-build
	cd sqlite-build && \
		../sqlite-autoconf-$(SQLITE_VER)/configure --prefix=$(prefix) \
			--enable-shared $(env_flags_deps) $(env_compilers) \
			CPPFLAGS="$(CPPFLAGS)" LDFLAGS="$(LDFLAGS)"; \
		$(MAKE) -j $(make_threads) && \
		$(MAKE) install && \
		touch $(abs_builddir)/installed_sqlite

else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_sqlite
endif

installed_sqlite:
	$(MAKE) $(AM_MAKEFLAGS) sqlite


# ----------------------------------------------------------------------
# tiff
# ----------------------------------------------------------------------
tiff: installed_compilers
if INSTALL_TIFF
	$(FETCH_SCRIPT) $(CURL) tiff-$(TIFF_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf tiff-$(TIFF_VER).tar.gz
	$(MKDIR_P) tiff-build
	cd tiff-build && \
		../tiff-$(TIFF_VER)/configure --prefix=$(prefix) \
			--enable-shared $(env_flags_deps) $(env_compilers) \
			CPPFLAGS="$(CPPFLAGS)" LDFLAGS="$(LDFLAGS)"; \
		$(MAKE) -j $(make_threads) && \
		$(MAKE) install && \
		touch $(abs_builddir)/installed_tiff

else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_tiff
endif

installed_tiff:
	$(MAKE) $(AM_MAKEFLAGS) tiff


# ----------------------------------------------------------------------
# proj
# ----------------------------------------------------------------------
proj: installed_compilers installed_sqlite installed_tiff installed_curl installed_cmake
if INSTALL_PROJ
	$(FETCH_SCRIPT) $(CURL) proj-$(PROJ_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf proj-$(PROJ_VER).tar.gz
	$(MKDIR_P) proj-build
	cd proj-build && \
cmake -DCMAKE_INSTALL_PREFIX=$(prefix) -DCMAKE_C_COMPILER=$(CC) -DCMAKE_CXX_COMPILER=$(CXX) -DCMAKE_INSTALL_NAME_DIR=$(prefix)/lib TIFF_INCLUDE_DIR=${TIFF_INCDIR} TIFF_LIBRARY=${TIFF_LIBDIR} SQLITE3_INCLUDE_DIR=${SQLITE3_INCDIR} SQLITE3_LIBRARY=${SQLITE3_LIBDIR} -DBUILD_TESTING=OFF -DCMAKE_BUILD_TYPE=Release ../proj-${PROJ_VER} && \
		$(MAKE) -j$(make_threads) && $(MAKE) install && \
		$(env_cert) projsync --system-directory --all && \
		touch $(abs_builddir)/installed_proj

else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_proj
endif

installed_proj:
	$(MAKE) $(AM_MAKEFLAGS) proj


# ----------------------------------------------------------------------
# hdf5
# ----------------------------------------------------------------------
hdf5: installed_mpi
if WITH_FORTRAN
hdf5_options = --enable-fortran
endif
if INSTALL_HDF5
	$(FETCH_SCRIPT) $(CURL) hdf5-$(HDF5_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf hdf5-$(HDF5_VER).tar.gz
	$(MKDIR_P) hdf5-build
	cd hdf5-build && \
		../hdf5-$(HDF5_VER)/configure  --prefix=$(prefix) \
			--enable-parallel --enable-shared --enable-unsupported \
			--disable-static$(hdf5_options) \
			$(env_flags_deps) $(env_mpicompilers) \
			CPPFLAGS="$(CPPFLAGS)" LDFLAGS="$(LDFLAGS)"; \
		$(MAKE) -j $(make_threads) && \
		$(MAKE) install && \
		touch $(abs_builddir)/installed_hdf5
else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_hdf5
endif

installed_hdf5:
	$(MAKE) $(AM_MAKEFLAGS) hdf5


# ----------------------------------------------------------------------
# h5py
# ----------------------------------------------------------------------
h5py: installed_hdf5 installed_python
if INSTALL_H5PY
	CFLAGS="$(CFLAGS)" CC=mpicc HDF5_LIBDIR=$(HDF5_LIBDIR) HDF5_INCLUDEDIR=$(HDF5_INCDIR) $(env_cert) $(PYTHON) -m pip install --no-cache-dir --no-binary=h5py h5py && \
		touch $(abs_builddir)/installed_h5py
else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_h5py
endif

installed_h5py:
	$(MAKE) $(AM_MAKEFLAGS) h5py


# ----------------------------------------------------------------------
# netcdf
# ----------------------------------------------------------------------
netcdf: installed_compilers installed_hdf5
if INSTALL_NETCDF
	$(FETCH_SCRIPT) $(CURL) netcdf-c-$(NETCDF_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf netcdf-c-$(NETCDF_VER).tar.gz
	$(MKDIR_P) netcdf-build
	cd netcdf-build && \
		../netcdf-c-$(NETCDF_VER)/configure --prefix=$(prefix) \
			$(env_flags_deps) $(env_mpicompilers) \
			CPPFLAGS="$(CPPFLAGS) $(HDF5_INCLUDES)" LDFLAGS="$(LDFLAGS) $(HDF5_LDFLAGS)" \
			--enable-shared --disable-static --enable-netcdf-4 --disable-dap4 $(NETCDF_OPTIONS) ; \
		sed -e "s/-l //g" libtool > libtool.tmp && mv -f libtool.tmp libtool; \
		$(MAKE) -j $(make_threads) && \
		$(MAKE) install && \
		touch $(abs_builddir)/installed_netcdf

else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_netcdf
endif

installed_netcdf:
	$(MAKE) $(AM_MAKEFLAGS) netcdf


# ----------------------------------------------------------------------
# netcdfpy
# ----------------------------------------------------------------------
netcdfpy: installed_netcdf installed_python
if INSTALL_NETCDFPY
	$(env_cert) $(PYTHON) -m pip install --no-cache-dir --prefer-binary cftime netCDF4
endif
	touch $(abs_builddir)/installed_netcdfpy

installed_netcdfpy:
	$(MAKE) $(AM_MAKEFLAGS) netcdfpy


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
