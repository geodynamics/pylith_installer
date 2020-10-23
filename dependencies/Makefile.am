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
	installed_autotools \
	installed_compilers \
	installed_openssl \
	installed_python \
	installed_mpi \
	installed_cppunit \
	installed_pcre \
	installed_swig \
	installed_setuptools \
	installed_cython \
	installed_numpy \
	installed_six \
	installed_cftime \
	installed_sqlite \
	installed_proj \
	installed_hdf5 \
	installed_h5py \
	installed_netcdf \
	installed_netcdfpy \
	installed_fiat \
	installed_git \
	installed_cmake


noinst_builddirs = \
	gcc-build \
	m4-build \
	autoconf-build \
	automake-build \
	libtool-build \
	openssl-build \
	git-build \
	python-build \
	openmpi-build \
	mpich-build \
	cppunit-build \
	swig-build \
	sqlite-build \
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
	openssl-${OPENSSL_VER) \
	openmpi-$(OPENMPI_VER) \
	mpich-$(MPICH_VER) \
	cppunit-$(CPPUNIT_VER) \
	pcre-$(PCRE_VER) \
	swig-$(SWIG_VER) \
	setuptools-$(SETUPTOOLS_VER) \
	Cython-$(CYTHON_VER) \
	numpy-$(NUMPY_VER) \
	size-$(SIX_VER) \
	cftime-$(CFTIME_VER) \
	sqlite-$(SQLITE_VER) \
	proj-$(PROJ4_VER) \
	hdf5-$(HDF5_VER) \
	h5py-$(H5PY_VER) \
	netcdf-$(NETCDF_VER) \
	netCDF4-$(NETCDFPY_VER) \
	ScientificPython-$(SCIENTIFICPYTHON_VER) \
	FIAT-$(FIAT_VER) \
	git-$(GIT_VER) \
	cmake-$(CMAKE_VER)

# ----------------------------------------------------------------------
# Targets
# ----------------------------------------------------------------------
all: finished_mkdest installed_autotools installed_compilers installed_openssl installed_sqlite installed_python installed_mpi installed_cppunit installed_swig installed_setuptools installed_cython installed_numpy installed_six installed_proj installed_hdf5 installed_h5py installed_netcdf installed_netcdfpy installed_git installed_cmake installed_fiat

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
		$(prefix_deps)/include \
		$(prefix_deps)/lib \
		$(prefix_deps)/bin \
		$(prefix_deps)/$(PYTHON_SITEPKGS) \
		$(prefix_deps)/$(PYTHON64_SITEPKGS)

finished_mkdest:
	$(MAKE) $(AM_MAKEFLAGS) mkdest && touch $@

# ----------------------------------------------------------------------
# autotools
# ----------------------------------------------------------------------
autotools: finished_mkdest
if INSTALL_AUTOTOOLS
	$(FETCH_SCRIPT) "$(downloader)" m4-$(M4_VER).tar.gz $(DEPS_URL)
	$(FETCH_SCRIPT) "$(downloader)" autoconf-$(AUTOCONF_VER).tar.gz $(DEPS_URL)
	$(FETCH_SCRIPT) "$(downloader)" automake-$(AUTOMAKE_VER).tar.gz $(DEPS_URL)
	$(FETCH_SCRIPT) "$(downloader)" libtool-$(LIBTOOL_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf m4-$(M4_VER).tar.gz
	mkdir -p m4-build
	cd m4-build && \
		../m4-$(M4_VER)/configure --prefix=$(prefix_deps) $(env_flags_deps) && \
		make -j $(MAKE_THREADS) && \
		make install
	$(TAR) -xf autoconf-$(AUTOCONF_VER).tar.gz
	mkdir -p autoconf-build
	cd autoconf-build && \
		../autoconf-$(AUTOCONF_VER)/configure --prefix=$(prefix_deps) $(env_flags_deps) && \
		make -j $(MAKE_THREADS) && \
		make install
	$(TAR) -xf automake-$(AUTOMAKE_VER).tar.gz
	mkdir -p automake-build
	cd automake-build && \
		../automake-$(AUTOMAKE_VER)/configure --prefix=$(prefix_deps) $(env_flags_deps) && \
		make -j $(MAKE_THREADS) && \
		make install
	$(TAR) -xf libtool-$(LIBTOOL_VER).tar.gz
	mkdir -p libtool-build
	cd libtool-build && \
		../libtool-$(LIBTOOL_VER)/configure --prefix=$(prefix_deps)  $(env_flags_deps) && \
		make -j $(MAKE_THREADS) && \
		make install && \
		touch $(abs_builddir)/installed_autotools
else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_autotools
endif

installed_autotools:
	$(MAKE) $(AM_MAKEFLAGS) autotools

# ----------------------------------------------------------------------
# git
# ----------------------------------------------------------------------
git:
if INSTALL_GIT
	$(FETCH_SCRIPT) "$(downloader)" git-$(GIT_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf git-$(GIT_VER).tar.gz
	cd git-$(GIT_VER) && \
		./configure --prefix=$(prefix_deps) && \
		make -j $(MAKE_THREADS) all && \
		make install && \
		touch $(abs_builddir)/installed_git
else
	@echo "Skipping $@ installation."
	touch $(abs_builddir)/installed_git
endif

installed_git:
	$(MAKE) $(AM_MAKEFLAGS) git


# ----------------------------------------------------------------------
# cmake
# ----------------------------------------------------------------------
cmake:
if INSTALL_CMAKE
	$(FETCH_SCRIPT) "$(downloader)" cmake-$(CMAKE_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf cmake-$(CMAKE_VER).tar.gz
	cd cmake-$(CMAKE_VER) && \
		$(env_flags_deps) ./bootstrap --verbose --prefix=$(prefix_deps) && make && make install && \
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
	$(FETCH_SCRIPT) "$(downloader)" gcc-$(GCC_VER).tar.gz $(DEPS_URL)
	$(FETCH_SCRIPT) "$(downloader)" mpc-$(MPC_VER).tar.gz $(DEPS_URL)
	$(FETCH_SCRIPT) "$(downloader)" gmp-$(GMP_VER).tar.bz2 $(DEPS_URL)
	$(FETCH_SCRIPT) "$(downloader)" mpfr-$(MPFR_VER).tar.bz2 $(DEPS_URL)
	$(TAR) -xf gcc-$(GCC_VER).tar.gz
	cd gcc-$(GCC_VER) ; \
		$(TAR) -xf ../gmp-$(GMP_VER).tar.bz2; \
		ln -sf gmp-$(GMP_VER)/ gmp; \
		$(TAR) -xf ../mpc-$(MPC_VER).tar.gz; \
		ln -sf mpc-$(MPC_VER)/ mpc; \
		$(TAR) -xf ../mpfr-$(MPFR_VER).tar.bz2; \
		ln -sf mpfr-$(MPFR_VER)/ mpfr
	$(MKDIR_P) gcc-build
	cd gcc-build && \
		../gcc-$(GCC_VER)/configure --prefix=$(prefix_deps) \
			--disable-multilib \
			--enable-languages=$(gcc_languages) \
			$(env_flags_deps) && \
		make -j $(make_threads) $(env_flags_deps) && \
		make install && \
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
	$(FETCH_SCRIPT) "$(downloader)" openssl-$(OPENSSL_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf openssl-$(OPENSSL_VER).tar.gz
	cd openssl-$(OPENSSL_VER) && \
		$(env_compilers) ./config \
			--prefix=$(prefix_deps) --openssldir=$(prefix_deps)/share/openssl  shared; \
		make -j $(make_threads) && \
		make install && \
		touch $(abs_builddir)/installed_openssl

else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_openssl
endif

installed_openssl:
	$(MAKE) $(AM_MAKEFLAGS) openssl


# ----------------------------------------------------------------------
# python
# ----------------------------------------------------------------------
python: installed_compilers installed_openssl installed_sqlite
if INSTALL_PYTHON
	$(FETCH_SCRIPT) "$(downloader)" Python-$(PYTHON_VER).tgz $(DEPS_URL)
	$(TAR) -xf Python-$(PYTHON_VER).tgz
	$(MKDIR_P) python-build
	cd python-build && \
		../Python-$(PYTHON_VER)/configure --prefix=$(prefix_deps) \
		--enable-shared --enable-optimizations CPPFLAGS="$(CPPFLAGS)" LDFLAGS="$(LDFLAGS)" \
		$(env_flags_deps) $(env_compilers) && \
		make -j $(make_threads) && \
		make install && \
		touch $(abs_builddir)/installed_python
else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_python
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
	touch $(abs_builddir)/installed_mpi
endif

installed_mpi:
	$(MAKE) $(AM_MAKEFLAGS) mpi


# ----------------------------------------------------------------------
# openmpi
# ----------------------------------------------------------------------
openmpi: installed_compilers
	$(FETCH_SCRIPT) "$(downloader)" openmpi-$(OPENMPI_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf openmpi-$(OPENMPI_VER).tar.gz
	$(MKDIR_P) openmpi-build
	cd openmpi-build && \
		../openmpi-$(OPENMPI_VER)/configure \
			--prefix=$(prefix_deps) $(env_flags_deps) $(env_compilers); \
		make -j $(make_threads) && \
		make install && \
		touch $(abs_builddir)/installed_mpi
	if [ ! -x $(prefix_deps)/bin/mpirun ]; then cd $(prefix_deps)/bin && $(LN_S) mpiexec mpirun; fi


# ----------------------------------------------------------------------
# mpich
# ----------------------------------------------------------------------
if WITH_FORTRAN
mpich_options = --enable-fc
else
mpich_options = --disable-fortran
endif
mpich: installed_compilers
	$(FETCH_SCRIPT) "$(downloader)" mpich-$(MPICH_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf mpich-$(MPICH_VER).tar.gz
	$(MKDIR_P) mpich-build
	cd mpich-build && \
		../mpich-$(MPICH_VER)/configure \
			--with-pm=gforker \
			--enable-shared \
			--enable-sharedlibs=$(mpich_sharedarch) \
			--disable-static --disable-mpe \
			--prefix=$(prefix_deps) \
			$(env_flags_deps) $(env_compilers) $(mpich_options) ; \
		make -j $(make_threads) && \
		make install && \
		touch $(abs_builddir)/installed_mpi
	if [ ! -x $(prefix_deps)/bin/mpirun ]; then cd $(prefix_deps)/bin && $(LN_S) mpiexec mpirun; fi


# ----------------------------------------------------------------------
# cppunit
# ----------------------------------------------------------------------
cppunit: installed_compilers
if INSTALL_CPPUNIT
	$(FETCH_SCRIPT) "$(downloader)" cppunit-$(CPPUNIT_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf cppunit-$(CPPUNIT_VER).tar.gz
	$(MKDIR_P) cppunit-build
	cd cppunit-build && \
		../cppunit-$(CPPUNIT_VER)/configure \
			--prefix=$(prefix_deps) $(env_flags_deps) $(env_compilers); \
		make -j $(make_threads) && \
		make install && \
		touch $(abs_builddir)/installed_cppunit

else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_cppunit
endif

installed_cppunit:
	$(MAKE) $(AM_MAKEFLAGS) cppunit


# ----------------------------------------------------------------------
# pcre
# ----------------------------------------------------------------------
pcre: installed_compilers
if INSTALL_PCRE
	$(FETCH_SCRIPT) "$(downloader)" pcre-$(PCRE_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf pcre-$(PCRE_VER).tar.gz
	$(MKDIR_P) pcre-build
	cd pcre-build && \
		../pcre-$(PCRE_VER)/configure \
			--prefix=$(prefix_deps) $(env_flags_deps) $(env_compilers) ; \
		make -j $(make_threads) && \
		make install && \
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
	$(FETCH_SCRIPT) "$(downloader)" swig-$(SWIG_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf swig-$(SWIG_VER).tar.gz
	$(MKDIR_P) swig-build
	cd swig-build && \
		../swig-$(SWIG_VER)/configure \
			--prefix=$(prefix_deps) $(env_flags_deps) $(env_compilers) \
			CPPFLAGS="$(CPPFLAGS) $(PCRE_INCLUDES)" LDFLAGS="$(LDFLAGS) $(PCRE_LDFLAGS)"; \
		make -j $(make_threads) && \
		make install && \
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
# numpy
# ----------------------------------------------------------------------
numpy: installed_python installed_setuptools
if INSTALL_NUMPY
	$(FETCH_SCRIPT) "$(downloader)" numpy-$(NUMPY_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf numpy-$(NUMPY_VER).tar.gz
if WITH_NUMPY_BLASLAPACK
	$(CP) $(top_srcdir)/numpy_blaslapack.cfg numpy-$(NUMPY_VER)/site.cfg
endif
	cd numpy-$(NUMPY_VER) && \
		$(PYTHON) setup.py install --prefix=$(prefix_deps) && \
		touch $(abs_builddir)/installed_numpy

else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_numpy
endif

installed_numpy:
	$(MAKE) $(AM_MAKEFLAGS) numpy


# ----------------------------------------------------------------------
# six
# ----------------------------------------------------------------------
six: installed_python installed_setuptools
if INSTALL_SIX
	$(FETCH_SCRIPT) "$(downloader)" six-$(SIX_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf six-$(SIX_VER).tar.gz
	cd six-$(SIX_VER) && \
		$(PYTHON) setup.py install --prefix=$(prefix_deps) && \
		touch $(abs_builddir)/installed_six

else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_six
endif

installed_six:
	$(MAKE) $(AM_MAKEFLAGS) six


# ----------------------------------------------------------------------
# cftime
# ----------------------------------------------------------------------
cftime: installed_python installed_numpy
if INSTALL_CFTIME
	$(FETCH_SCRIPT) "$(downloader)" cftime-$(CFTIME_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf cftime-$(CFTIME_VER).tar.gz
	cd cftime-$(CFTIME_VER) && \
		$(PYTHON) setup.py install --prefix=$(prefix_deps) && \
		touch $(abs_builddir)/installed_cftime

else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_cftime
endif

installed_cftime:
	$(MAKE) $(AM_MAKEFLAGS) cftime


# ----------------------------------------------------------------------
# sqlite
# ----------------------------------------------------------------------
sqlite: installed_compilers
if INSTALL_SQLITE
	$(FETCH_SCRIPT) "$(downloader)" sqlite-autoconf-$(SQLITE_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf sqlite-autoconf-$(SQLITE_VER).tar.gz
	$(MKDIR_P) sqlite-build
	cd sqlite-build && \
		../sqlite-autoconf-$(SQLITE_VER)/configure \
			--prefix=$(prefix_deps) --enable-shared $(env_flags_deps) $(env_compilers) ; \
		make -j $(make_threads) && \
		make install && \
		touch $(abs_builddir)/installed_sqlite

else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_sqlite
endif

installed_sqlite:
	$(MAKE) $(AM_MAKEFLAGS) sqlite


# ----------------------------------------------------------------------
# proj
# ----------------------------------------------------------------------
# Disable parallel build to prevent internal compiler error when
# building some modules (Ubuntu 18,04 and 190.10).
proj: installed_compilers installed_sqlite
if INSTALL_PROJ
	$(FETCH_SCRIPT) "$(downloader)" proj-$(PROJ_VER).tar.gz $(DEPS_URL)
	$(FETCH_SCRIPT) "$(downloader)" proj-datumgrid-$(PROJ_DATUM_VER).zip $(DEPS_URL)
	$(TAR) -xf proj-$(PROJ_VER).tar.gz
	$(MKDIR_P) proj-build
	cd proj-build && \
		../proj-$(PROJ_VER)/configure \
			--prefix=$(prefix_deps) --with-jni=no \
			SQLITE3_CFLAGS=$(SQLITE3_INCLUDES) SQLITE3_LIBS="$(SQLITE3_LDFLAGS) -lsqlite3" \
			$(env_flags_deps) $(env_compilers); \
		$(UNZIP) -o $(abs_builddir)/proj-datumgrid-$(PROJ_DATUM_VER).zip -d $(abs_builddir)/proj-$(PROJ_VER)/data && \
		make -j $(make_threads) && \
		make install && \
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
	$(FETCH_SCRIPT) "$(downloader)" hdf5-$(HDF5_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf hdf5-$(HDF5_VER).tar.gz
	$(MKDIR_P) hdf5-build
	cd hdf5-build && \
		../hdf5-$(HDF5_VER)/configure \
			--enable-parallel --enable-shared --enable-unsupported \
			--disable-static --prefix=$(prefix_deps) $(hdf5_options) \
			$(env_flags_deps) $(env_mpicompilers); \
		make -j $(make_threads) && \
		make install && \
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
h5py: installed_hdf5 installed_numpy installed_six installed_cython
if INSTALL_H5PY
	$(FETCH_SCRIPT) "$(downloader)" h5py-$(H5PY_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf h5py-$(H5PY_VER).tar.gz
	cd h5py-$(H5PY_VER) && \
		$(PYTHON) setup.py configure --hdf5-libdir=$(HDF5_LIBDIR) --hdf5-includedir=$(HDF5_INCDIR) --hdf5-version=$(HDF5_VER) && \
		CC=mpicc $(env_flags_deps) CPPFLAGS="$(CPPFLAGS)" LDFLAGS="$(LDFLAGS)" $(PYTHON) setup.py build && \
		$(PYTHON) setup.py install --prefix=$(prefix_deps) && \
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
	$(FETCH_SCRIPT) "$(downloader)" netcdf-c-$(NETCDF_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf netcdf-c-$(NETCDF_VER).tar.gz
	$(MKDIR_P) netcdf-build
	cd netcdf-build && \
		../netcdf-c-$(NETCDF_VER)/configure \
			--prefix=$(prefix_deps) $(env_flags_deps) $(env_mpicompilers) \
			CPPFLAGS="$(CPPFLAGS) $(HDF5_INCLUDES)" LDFLAGS="$(LDFLAGS) $(HDF5_LDFLAGS)" \
			--enable-shared --disable-static --enable-netcdf-4 --disable-dap ; \
		sed -e "s/-l //g" libtool > libtool.tmp && mv -f libtool.tmp libtool; \
		make -j $(make_threads) && \
		make install && \
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
netcdfpy: installed_netcdf installed_numpy installed_cftime
if INSTALL_NETCDFPY
	$(FETCH_SCRIPT) "$(downloader)" netCDF4-$(NETCDFPY_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf netCDF4-$(NETCDFPY_VER).tar.gz
	cd netCDF4-$(NETCDFPY_VER) && \
		HDF5_INCDIR=$(HDF5_INCDIR) HDF5_LIBDIR=$(HDF5_LIBDIR) \
		NETCDF4_INCDIR=$(NETCDF_INCDIR) NETCDF_LIBDIR=$(NETCDF_LIBDIR) $(env_flags_deps) CPPFLAGS="$(CPPFLAGS)" LDFLAGS="$(LDFLAGS)" CC=mpicc $(PYTHON) setup.py install --prefix=$(prefix_deps) && \
		touch $(abs_builddir)/installed_netcdfpy
else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_netcdfpy
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
	cd ScientificPython-$(SCIENTIFICPYTHON_VER) && $(PYTHON) setup.py install --prefix=$(prefix_deps)
	$(FETCH_SCRIPT) "$(downloader)" FIAT-$(FIAT_VER).tar.gz $(DEPS_URL)
	$(TAR) -zxf FIAT-$(FIAT_VER).tar.gz
	cd FIAT-$(FIAT_VER) && $(PYTHON) setup.py install --prefix=$(prefix_deps) && touch $(abs_top_builddir)/installed_fiat

else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_top_builddir)/installed_fiat
endif

installed_fiat:
	$(MAKE) $(AM_MAKEFLAGS) fiat


# ----------------------------------------------------------------------
# setuptools
# ----------------------------------------------------------------------
setuptools: 
if INSTALL_SETUPTOOLS
	$(FETCH_SCRIPT) "$(downloader)" setuptools-$(SETUPTOOLS_VER).zip $(DEPS_URL)
	$(UNZIP) setuptools-$(SETUPTOOLS_VER).zip
	cd setuptools-$(SETUPTOOLS_VER) && $(PYTHON) setup.py install --prefix=$(prefix_deps) && touch $(abs_builddir)/installed_setuptools

else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_setuptools
endif

installed_setuptools:
	$(MAKE) $(AM_MAKEFLAGS) setuptools


# ----------------------------------------------------------------------
# cython
# ----------------------------------------------------------------------
cython: 
if INSTALL_CYTHON
	$(FETCH_SCRIPT) "$(downloader)" Cython-$(CYTHON_VER).tar.gz $(DEPS_URL)
	$(TAR) -xf Cython-$(CYTHON_VER).tar.gz
	cd Cython-$(CYTHON_VER) && $(PYTHON) setup.py install --prefix=$(prefix_deps) && touch $(abs_builddir)/installed_cython

else
	@echo "$@ already installed. Skipping installation."
	touch $(abs_builddir)/installed_cython
endif

installed_cython:
	$(MAKE) $(AM_MAKEFLAGS) cython


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
