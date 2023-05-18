# ----------------------------------------------------------------------
#
# Brad T. Aagaard, U.S. Geological Survey
# Charles A. Williams, GNS Science
# Matthew G. Knepley, University at Buffalo
#
# This code was developed as part of the Computational Infrastructure
# for Geodynamics (http://geodynamics.org).
#
# Copyright (c) 2010-2023 University of California, Davis
#
# See LICENSE.md for license information.
#
# ----------------------------------------------------------------------
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.59)
AC_INIT([PyLith Installer], [3.0.3-0], [https://community.geodynamics.org/c/pylith/])
AC_CONFIG_AUX_DIR([./aux-config])
AC_CONFIG_MACRO_DIR([m4])
AM_INIT_AUTOMAKE([foreign tar-pax])

# ----------------------------------------------------------------------
# SOFTWARE TO INSTALL
# ----------------------------------------------------------------------
AC_ARG_WITH([cert-path],
    [AC_HELP_STRING([--with-cert-path],
        [absolute path to SSL certificates @<:@default=no@:>@])],
	[cert_path=$withval],
	[cert_path=no])
AC_SUBST(cert_path)
AC_ARG_WITH([cert-file],
    [AC_HELP_STRING([--with-cert-file],
        [name of SSL certificate file @<:@default=no@:>@])],
	[cert_file=$withval],
	[cert_file=no])
AC_SUBST(cert_file)
AM_CONDITIONAL([WITH_CERT], [test "$cert_path" != no])

# FORCE INSTALLATION
AC_ARG_ENABLE([force-install],
    [AC_HELP_STRING([--enable-force-install],
        [Force installation of software, overriding warnings about existing versions@<:@default=no@:>@])],
	[if test "$enableval" != no ; then force_install=yes; else force_install=no; fi],
	[force_install=no])

# GCC
AC_ARG_ENABLE([gcc],
    [AC_HELP_STRING([--enable-gcc],
        [install GNU compilers (no, c,c++,fortran)@<:@default=no@:>@])],
	[if test "$enableval" != no ; then install_gcc=yes; gcc_languages=$enableval; else install_gcc=no; fi],
	[install_gcc=no])
if test "$gcc_languages" = yes ; then
  gcc_languages=c,c++,fortran
fi
AC_SUBST(gcc_languages)
AM_CONDITIONAL([INSTALL_GCC], [test "$install_gcc" = yes])

# CMAKE
AC_ARG_ENABLE([cmake],
    [AC_HELP_STRING([--enable-cmake],
        [install CMAKE @<:@default=yes@:>@])],
	[if test "$enableval" = yes ; then install_cmake=yes; else install_cmake=no; fi],
	[install_cmake=yes])
AM_CONDITIONAL([INSTALL_CMAKE], [test "$install_cmake" = yes])

# MPI
AC_ARG_ENABLE([mpi],
    [AC_HELP_STRING([--enable-mpi],
        [install MPI (no | openmpi | mpich) @<:@default=no@:>@])],
	[if test "$enableval" != no ; then install_mpi=$enableval; else install_mpi=no; fi],
	[install_mpi=no])
AM_CONDITIONAL([INSTALL_MPI], [test "$install_mpi" != no])
AM_CONDITIONAL([INSTALL_OPENMPI], [test "$install_mpi" = openmpi])
AM_CONDITIONAL([INSTALL_MPICH], [test "$install_mpi" = mpich])
if test "$install_mpi" = mpich ; then
  mpich_sharedarch=gcc
  case $host_os in
    darwin*)
      mpich_sharedarch=osx-gcc ;;
  esac
fi
AC_SUBST(mpich_sharedarch)
AC_ARG_WITH([mpich-options],
    [AC_HELP_STRING([--with-mpich-options],
        [MPICH configure options @<:@default=@:>@])],
	[mpich_options=$withval],
	[mpich_options=""])
AC_SUBST(mpich_options)


# GIT
AC_ARG_ENABLE([git],
    [AC_HELP_STRING([--enable-git],
        [install Git @<:@default=no@:>@])],
	[if test "$enableval" != no ; then install_git=yes; else install_git=no; fi],
	[install_git=no])
AM_CONDITIONAL([INSTALL_GIT], [test "$install_git" = yes])

# AUTOTOOLS
AC_ARG_ENABLE([autotools],
    [AC_HELP_STRING([--enable-autotools],
        [install GNU autotools @<:@default=no@:>@])],
	[if test "$enableval" != no ; then install_autotools=yes; else install_autotools=no; fi],
	[install_autotools=no])
AM_CONDITIONAL([INSTALL_AUTOTOOLS], [test "$install_autotools" = yes])

# PCRE
AC_ARG_ENABLE([pcre],
    [AC_HELP_STRING([--enable-pcre],
        [install PCRE @<:@default=no@:>@])],
	[if test "$enableval" = "yes" ; then install_pcre=yes; else install_pcre=no; fi],
	[install_pcre=no])
AM_CONDITIONAL([INSTALL_PCRE], [test "$install_pcre" = yes])
AC_ARG_WITH([pcre-incdir],
    [AC_HELP_STRING([--with-pcre-incdir],
        [location of pcre header files @<:@default=no@:>@])],
	[with_pcre_incdir=$withval],
	[with_pcre_incdir=no])
AC_SUBST(with_pcre_incdir)
AC_ARG_WITH([pcre-libdir],
    [AC_HELP_STRING([--with-pcre-libdir],
        [location of pcre library @<:@default=no@:>@])],
	[with_pcre_libdir=$withval],
	[with_pcre_libdir=no])
AC_SUBST(with_pcre_libdir)

# SWIG
AC_ARG_ENABLE([swig],
    [AC_HELP_STRING([--enable-swig],
        [install SWIG @<:@default=no@:>@])],
	[if test "$enableval" = "yes" ; then install_swig=yes; else install_swig=no; fi],
	[install_swig=no])
AM_CONDITIONAL([INSTALL_SWIG], [test "$install_swig" = yes])

# OPENSSL
AC_ARG_ENABLE([openssl],
    [AC_HELP_STRING([--enable-openssl],
        [install OpenSSL @<:@default=no@:>@])],
	[if test "$enableval" != no ; then install_openssl=yes; else install_openssl=no; fi],
	[install_openssl=no])
AM_CONDITIONAL([INSTALL_OPENSSL], [test "$install_openssl" = yes])

# CURL
AC_ARG_ENABLE([curl],
    [AC_HELP_STRING([--enable-curl],
        [install curl @<:@default=no@:>@])],
	[if test "$enableval" != no ; then install_curl=yes; else install_curl=no; fi],
	[install_curl=no])
AM_CONDITIONAL([INSTALL_CURL], [test "$install_curl" = yes])

# libFFI
AC_ARG_ENABLE([libffi],
    [AC_HELP_STRING([--enable-libffi],
        [install libffi @<:@default=no@:>@])],
	[if test "$enableval" != no ; then install_libffi=yes; else install_libffi=no; fi],
	[install_libffi=no])
AM_CONDITIONAL([INSTALL_LIBFFI], [test "$install_libffi" = yes])

# PYTHON
AC_ARG_ENABLE([python],
    [AC_HELP_STRING([--enable-python],
        [install Python @<:@default=no@:>@])],
	[if test "$enableval" = yes ; then install_python=yes; else install_python=no; fi],
	[install_python=no])
AM_CONDITIONAL([INSTALL_PYTHON], [test "$install_python" = yes])

# DEVELOPER
AC_ARG_ENABLE([developer],
    [AC_HELP_STRING([--enable-developer],
        [install Python packages for PyLith development @<:@default=no@:>@])],
	[if test "$enableval" != no ; then install_developer=yes; else install_developer=no; fi],
	[install_developer=no])
AM_CONDITIONAL([INSTALL_DEVELOPER], [test "$install_developer" = yes])

# PYQT
AC_ARG_ENABLE([pyqt],
    [AC_HELP_STRING([--enable-pyqt],
        [install pyqt Python package @<:@default=no@:>@])],
	[if test "$enableval" != no ; then install_pyqt=yes; else install_pyqt=no; fi],
	[install_pyqt=no])
AM_CONDITIONAL([INSTALL_PYQT], [test "$install_pyqt" = yes])

# MATPLOTLIB
AC_ARG_ENABLE([matplotlib],
    [AC_HELP_STRING([--enable-matplotlib],
        [install matplotlib Python package @<:@default=no@:>@])],
	[if test "$enableval" != no ; then install_matplotlib=yes; else install_matplotlib=no; fi],
	[install_matplotlib=no])
AM_CONDITIONAL([INSTALL_MATPLOTLIB], [test "$install_matplotlib" = yes])

# GMSH
AC_ARG_ENABLE([gmsh],
    [AC_HELP_STRING([--enable-gmsh],
        [install Gmsh Python package @<:@default=no@:>@])],
	[if test "$enableval" != no ; then install_gmsh=yes; else install_gmsh=no; fi],
	[install_gmsh=no])
AM_CONDITIONAL([INSTALL_GMSH], [test "$install_gmsh" = yes])

# CPPUNIT
AC_ARG_ENABLE([cppunit],
    [AC_HELP_STRING([--enable-cppunit],
        [install CppUnit @<:@default=yes@:>@])],
	[if test "$enableval" = yes ; then install_cppunit=yes; else install_cppunit=no; fi],
	[install_cppunit=yes])
AM_CONDITIONAL([INSTALL_CPPUNIT], [test "$install_cppunit" = yes])
AC_ARG_WITH([cppunit-incdir],
    [AC_HELP_STRING([--with-cppunit-incdir],
        [location of cppunit header files @<:@default=no@:>@])],
	[with_cppunit_incdir=$withval],
	[with_cppunit_incdir=no])
AC_SUBST(with_cppunit_incdir)
AC_ARG_WITH([cppunit-libdir],
    [AC_HELP_STRING([--with-cppunit-libdir],
        [location of cppunit library @<:@default=no@:>@])],
	[with_cppunit_libdir=$withval],
	[with_cppunit_libdir=no])
AC_SUBST(with_cppunit_libdir)

# CATCH2
AC_ARG_ENABLE([catch2],
    [AC_HELP_STRING([--enable-catch2],
        [install Catch2 @<:@default=yes@:>@])],
	[if test "$enableval" = yes ; then install_catch2=yes; else install_catch2=no; fi],
	[install_catch2=yes])
AM_CONDITIONAL([INSTALL_CATCH2], [test "$install_catch2" = yes])
AC_ARG_WITH([catch2-incdir],
    [AC_HELP_STRING([--with-catch2-incdir],
        [location of Catch2 header files @<:@default=no@:>@])],
	[with_catch2_incdir=$withval],
	[with_catch2_incdir=no])
AC_SUBST(with_catch2_incdir)
AC_ARG_WITH([catch2-libdir],
    [AC_HELP_STRING([--with-catch2-libdir],
        [location of Catch2 library @<:@default=no@:>@])],
	[with_catch2_libdir=$withval],
	[with_catch2_libdir=no])
AC_SUBST(with_catch2_libdir)

# SQLITE
AC_ARG_ENABLE([sqlite],
    [AC_HELP_STRING([--enable-sqlite],
        [install Sqlite @<:@default=yes@:>@])],
	[if test "$enableval" = "yes" ; then install_sqlite=yes; else install_sqlite=no; fi],
	[install_sqlite=yes])
AM_CONDITIONAL([INSTALL_SQLITE], [test "$install_sqlite" = yes])
AC_ARG_WITH([sqlite-incdir],
    [AC_HELP_STRING([--with-sqlite-incdir],
        [location of sqlite header files @<:@default=no@:>@])],
	[with_sqlite_incdir=$withval],
	[with_sqlite_incdir=no])
AC_SUBST(with_sqlite_incdir)
AC_ARG_WITH([sqlite-libdir],
    [AC_HELP_STRING([--with-sqlite-libdir],
        [location of sqlite library @<:@default=no@:>@])],
	[with_sqlite_libdir=$withval],
	[with_sqlite_libdir=no])
AC_SUBST(with_sqlite_libdir)

# TIFF
AC_ARG_ENABLE([tiff],
    [AC_HELP_STRING([--enable-tiff],
        [install Tiff @<:@default=yes@:>@])],
	[if test "$enableval" = "yes" ; then install_tiff=yes; else install_tiff=no; fi],
	[install_tiff=no])
AM_CONDITIONAL([INSTALL_TIFF], [test "$install_tiff" = yes])
AC_ARG_WITH([tiff-incdir],
    [AC_HELP_STRING([--with-tiff-incdir],
        [location of tiff header files @<:@default=no@:>@])],
	[with_tiff_incdir=$withval],
	[with_tiff_incdir=no])
AC_SUBST(with_tiff_incdir)
AC_ARG_WITH([tiff-libdir],
    [AC_HELP_STRING([--with-tiff-libdir],
        [location of tiff library @<:@default=no@:>@])],
	[with_tiff_libdir=$withval],
	[with_tiff_libdir=no])
AC_SUBST(with_tiff_libdir)

# PROJ
AC_ARG_ENABLE([proj],
    [AC_HELP_STRING([--enable-proj],
        [install Proj @<:@default=yes@:>@])],
	[if test "$enableval" = "yes" ; then install_proj=yes; else install_proj=no; fi],
	[install_proj=yes])
AM_CONDITIONAL([INSTALL_PROJ], [test "$install_proj" = yes])
AC_ARG_WITH([proj-incdir],
    [AC_HELP_STRING([--with-proj-incdir],
        [location of proj header files @<:@default=no@:>@])],
	[with_proj_incdir=$withval],
	[with_proj_incdir=no])
AC_SUBST(with_proj_incdir)
AC_ARG_WITH([proj-libdir],
    [AC_HELP_STRING([--with-proj-libdir],
        [location of proj library @<:@default=no@:>@])],
	[with_proj_libdir=$withval],
	[with_proj_libdir=no])
AC_SUBST(with_proj_libdir)

# HDF5
AC_ARG_ENABLE([hdf5],
    [AC_HELP_STRING([--enable-hdf5],
        [install HDF5 @<:@default=yes@:>@])],
	[if test "$enableval" = yes ; then install_hdf5=yes; else install_hdf5=no; fi],
	[install_hdf5=yes])
AM_CONDITIONAL([INSTALL_HDF5], [test "$install_hdf5" = yes])
AC_ARG_WITH([hdf5-incdir],
    [AC_HELP_STRING([--with-hdf5-incdir],
        [location of hdf5 header files @<:@default=no@:>@])],
	[with_hdf5_incdir=$withval],
	[with_hdf5_incdir=no])
AC_SUBST(with_hdf5_incdir)
AC_ARG_WITH([hdf5-libdir],
    [AC_HELP_STRING([--with-hdf5-libdir],
        [location of hdf5 library @<:@default=no@:>@])],
	[with_hdf5_libdir=$withval],
	[with_hdf5_libdir=no])
AC_SUBST(with_hdf5_libdir)

# H5PY
AC_ARG_ENABLE([h5py],
    [AC_HELP_STRING([--enable-h5py],
        [install HDF5 @<:@default=yes@:>@])],
	[if test "$enableval" = yes ; then install_h5py=yes; else install_h5py=no; fi],
	[install_h5py=yes])
AM_CONDITIONAL([INSTALL_H5PY], [test "$install_h5py" = yes])

# NETCDF
AC_ARG_ENABLE([netcdf],
    [AC_HELP_STRING([--enable-netcdf],
        [install NetCDF @<:@default=yes@:>@])],
	[if test "$enableval" = yes ; then install_netcdf=yes; else install_netcdf=no; fi],
	[install_netcdf=yes])
AM_CONDITIONAL([INSTALL_NETCDF], [test "$install_netcdf" = yes])
AC_ARG_WITH([netcdf-incdir],
    [AC_HELP_STRING([--with-netcdf-incdir],
        [location of netcdf header files @<:@default=no@:>@])],
	[with_netcdf_incdir=$withval],
	[with_netcdf_incdir=no])
AC_SUBST(with_netcdf_incdir)
AC_ARG_WITH([netcdf-libdir],
    [AC_HELP_STRING([--with-netcdf-libdir],
        [location of netcdf library @<:@default=no@:>@])],
	[with_netcdf_libdir=$withval],
	[with_netcdf_libdir=no])
AC_SUBST(with_netcdf_libdir)

# NETCDFPY
AC_ARG_ENABLE([netcdfpy],
    [AC_HELP_STRING([--enable-netcdfpy],
        [install netCDF4 @<:@default=yes@:>@])],
	[if test "$enableval" = yes ; then install_netcdfpy=yes; else install_netcdfpy=no; fi],
	[install_netcdfpy=yes])
AM_CONDITIONAL([INSTALL_NETCDFPY], [test "$install_netcdfpy" = yes])

# PYTHIA
AC_ARG_ENABLE([pythia],
    [AC_HELP_STRING([--enable-pythia],
        [install pythia (CIG) @<:@default=yes@:>@])],
	[if test "$enableval" = yes ; then install_pythia=yes; else install_pythia=no; fi],
	[install_pythia=yes])
AM_CONDITIONAL([INSTALL_PYTHIA], [test "$install_pythia" = yes])
AC_ARG_WITH([pythia-repo],
    [AC_HELP_STRING([--with-pythia-repo],
        [URL for Pythia Git repository @<:@default=https://github.com/geodynamics/pythia.git@:>@])],
	[pythia_repo="$withval"],
	[pythia_repo=https://github.com/geodynamics/pythia.git])
AC_SUBST(pythia_repo)

# SPATIALDATA
AC_ARG_ENABLE([spatialdata],
    [AC_HELP_STRING([--enable-spatialdata],
        [install spatialdata (CIG) @<:@default=yes@:>@])],
	[if test "$enableval" = yes ; then install_spatialdata=yes; else install_spatialdata=no; fi],
	[install_spatialdata=yes])
AM_CONDITIONAL([INSTALL_SPATIALDATA], [test "$install_spatialdata" = yes])
AC_ARG_WITH([spatialdata-repo],
    [AC_HELP_STRING([--with-spatialdata-repo],
        [URL for Spatialdata Git repository @<:@default=https://github.com/geodynamics/spatialdata.git@:>@])],
	[spatialdata_repo="$withval"],
	[spatialdata_repo=https://github.com/geodynamics/spatialdata.git])
AC_SUBST(spatialdata_repo)

# pylith git
AC_ARG_WITH([pylith-git],
    [AC_HELP_STRING([--with-pylith-git],
        [use PyLith from GitHub repository (main, BRANCH) @<:@default=no@:>@])],
	[pylith_git=$withval],
	[pylith_git=no])
if test "$pylith_git" = yes ; then pylith_git="main"; fi
AC_SUBST(pylith_git)
AM_CONDITIONAL([USE_PYLITH_GIT], [test "$pylith_git" != no])
AC_ARG_WITH([pylith-repo],
    [AC_HELP_STRING([--with-pylith-repo],
        [URL for PyLith Git repository @<:@default=https://github.com/geodynamics/pylith.git@:>@])],
	[pylith_repo="$withval"],
	[pylith_repo=https://github.com/geodynamics/pylith.git])
AC_SUBST(pylith_repo)

# PETSC
AC_ARG_ENABLE([petsc],
    [AC_HELP_STRING([--enable-petsc],
        [install PETSc (development version) @<:@default=yes@:>@])],
	[if test "$enableval" = "yes" ; then install_petsc=yes; else install_petsc=no; fi],
	[install_petsc=yes])
AM_CONDITIONAL([INSTALL_PETSC], [test "$install_petsc" = yes])
AC_ARG_WITH([petsc-options],
    [AC_HELP_STRING([--with-petsc-options],
        [set optional PETSc configure options @<:@default=--download-chaco=1 --download-f2cblaslapack=1@:>@])],
	[petsc_options=$withval],
	[petsc_options="--download-chaco=1 --download-f2cblaslapack=1 --download-ml=1"])
AC_SUBST(petsc_options)
AC_ARG_WITH([petsc-tarball],
    [AC_HELP_STRING([--with-petsc-tarball],
        [Force use of PETSc tarball even if using PyLith from repository @<:@default=no@:>@])],
	[force_petsc_tarball=$withval],
	[force_petsc_tarball=no])
AC_SUBST(force_petsc_tarball)
AM_CONDITIONAL([PETSC_TARBALL], [test "$pylith_git" = no || test "$force_petsc_tarball" = yes])

# PARAMTERSGUI (PYLITH-PARAMETERS)
AC_ARG_ENABLE([parametersgui],
    [AC_HELP_STRING([--enable-pylith-parameters],
        [install parametersgui @<:@default=yes@:>@])],
	[if test "$enableval" = "yes" ; then install_parametersgui=yes; else install_parametersgui=no; fi],
	[install_parametersgui=yes])
AM_CONDITIONAL([INSTALL_PARAMETERSGUI], [test "$install_parametersgui" = yes])


# ----------------------------------------------------------------------
# OPTIONS
# ----------------------------------------------------------------------
# debugging
AC_ARG_WITH([debugging],
    [AC_HELP_STRING([--with-debugging],
        [Generate debugging symbols and use low-level optimization for spatialdata, PETSc, and PyLith builds. @<:@default=no@:>@])],
	[if test "$withval" = yes; then with_debugging=yes; else with_debugging=no; fi],
	[with_debugging=no])
AM_CONDITIONAL([WITH_DEBUGGING], [test "$with_debugging" = yes])

# TESTING
if test "$install_cppunit" = yes ; then
  with_testing=yes
fi
AC_ARG_WITH([testing],
    [AC_HELP_STRING([--with-testing],
        [enable testing (requires CppUnit) @<:@default=yes@:>@])],
	[if test "$withval" = yes; then with_testing=yes; else with_testing=no; fi],
	[with_testing=yes])
AM_CONDITIONAL([WITH_TESTING], [test "$with_testing" = yes])

# FORTRAN
AC_ARG_WITH([fortran],
    [AC_HELP_STRING([--with-fortran],
        [enable Fortran options for packages @<:@default=no@:>@])],
	[if test "$withval" = yes; then with_fortran=yes; else with_fortran=no; fi],
	[with_fortran=no])
AM_CONDITIONAL([WITH_FORTRAN], [test "$with_fortran" = yes])

# fetch tool
AC_ARG_WITH([fetch],
    [AC_HELP_STRING([--with-fetch],
        [set tool for downloading tarballs @<:@default=wget@:>@])],
	[with_fetch=$withval],
	[with_fetch=wget])

# parallel builds
AC_ARG_WITH([make-threads],
    [AC_HELP_STRING([--with-make-threads],
        [set number of threads to use in parallel builds @<:@default=1@:>@])],
	[make_threads=$withval],
	[make_threads=1])
AC_SUBST(make_threads)

# ----------------------------------------------------------------------
# BASIC TOOLS
# ----------------------------------------------------------------------
AC_PROG_LIBTOOL
AC_PROG_MKDIR_P
AC_PROG_LN_S

# cp
AC_PATH_PROG(CP, cp)
if test -z "$CP" ; then
  AC_MSG_FAILURE([cannot find 'cp' program.])
  CP=`echo "Error: cp is not installed." ; false`
fi

# tar
AC_PATH_PROG(TAR, tar)
if test -z "$TAR" ; then
  AC_MSG_FAILURE([cannot find 'tar' program.])
  TAR=`echo "Error: tar is not installed." ; false`
fi

# wget/curl
downloader=none
if test "$with_fetch" = "wget" ; then
  AC_PATH_PROG(WGET, wget)
  if test -z "$WGET" ; then
    AC_MSG_FAILURE([cannot find 'wget' program.])
  else
    downloader="$WGET -nd -r -O"
  fi
elif test "$with_fetch" = "curl" ; then
  AC_PATH_PROG(CURL, curl)
  if test -z "$CURL" ; then
    AC_MSG_FAILURE([cannot find 'curl' program.])
  else
    downloader="$CURL -L -O -o"
  fi
else
  AC_MSG_FAILURE([Error in configure logic for downloader.])
fi
AC_SUBST(downloader)

# autoreconf/git
petsc_git=no
if test "$pylith_git" != no; then
  # autoreconf
  if test "$enable_autotools" = no; then
    AC_PATH_PROG(AUTORECONF, autoreconf)
    if test -z "$AUTORECONF" ; then
      AC_MSG_FAILURE([cannot find 'autoreconf' program.])
    fi
  else
    AUTORECONF=autoreconf
  fi
  if test "$install_git" = no; then
    # GIT
    AC_PATH_PROG(GIT, git)
    if test -z "$GIT" ; then
      AC_MSG_FAILURE([cannot find 'git' program.])
    fi
  else
    GIT=$prefix/bin/git
    AC_SUBST(GIT)
  fi
  petsc_git=yes
  petsc_repo="https://gitlab.com/petsc/petsc.git"
  AC_SUBST(petsc_repo)

fi
AM_CONDITIONAL([WITH_SWIG], [test "$pylith_git" != no])
AC_SUBST(petsc_git)

# ----------------------------------------------------------------------
# CHECK COMPATIBILITY OF OPTIONS
# ----------------------------------------------------------------------

AC_PROG_CC
AC_PROG_CPP
AC_PROG_CXX
AC_PROG_CXXCPP

# GCC
if test "$install_gcc" = yes ; then
  if test "$install_mpi" = no ; then
    AC_MSG_WARN([Building GCC requires building MPI as well. Adding installation of MPICH.])
  fi
  install_mpi=mpich

  if test "$with_fortran" = yes ; then
    FC=gfortran
    AC_SUBST(FC)
  fi
else
  # Save raw compiler settings
  save_cc=$CC
  save_cxx=$CXX
  AX_CXX_COMPILE_STDCXX(14)
  CC=$save_cc
  CXX=$save_cxx
  if test "$with_fortran" = yes ; then
    AC_PROG_FC
  fi
fi
AC_SUBST(CC)
AC_SUBST(CXX)

# Python
if test "$install_python" = yes ; then
  PYTHON=$prefix/bin/python3
  PYTHON_VERSION=3.10
  AC_SUBST(PYTHON)
  AC_CHECK_HEADER([zlib.h], [], [
                AC_MSG_ERROR([Building Python requires zlib. Header file 'zlib.h' not found; maybe you don't have the zlib development package, e.g. 'zlib-dev', installed?])
                ])
  if test "$install_openssl" != yes ; then
    AC_CHECK_HEADER([openssl/ssl.h], [], [
                  AC_MSG_ERROR([Building Python requires openssl. Header file 'openssl/ssl.h' not found; maybe you don't have the openssl development package, e.g. 'openssl-dev', installed?])
                ])
  fi

  # install pythia
  if test "$install_pythia" != yes ; then
    AC_MSG_WARN([Building Python requires building pythia/pyre as well. Adding installation of pythia/pyre.])
  fi
  install_pythia=yes

  # install spatialdata
  if test "$install_spatialdata" != yes ; then
    AC_MSG_WARN([Building Python requires building spatialdata as well. Adding installation of spatialdata.])
  fi
  install_spatialdata=yes
else
  AM_PATH_PYTHON([3.7])
  CIT_PYTHON_SYSCONFIG
  CIT_CHECK_PYTHON_HEADER
  CIT_CHECK_PYTHON_SHARED
  CIT_PYTHON_MODULE([zlib])
  # Python will be installed as virtual environment to $prefix
  PYTHON=$prefix/bin/python3
  AC_SUBST(PYTHON)
fi
AC_CHECK_LIB([z], [deflate], 
  [],
  [AC_MSG_ERROR([Compression library '-lz' not found; maybe you don't have the zlib development package, e.g., 'zlib-dev', installed])
])dnl

# MPI
if test "$install_mpi" != no ; then
  AC_PATH_PROG(existing_mpi, mpirun)
  AC_SUBST(existing_mpi)
else
  AC_PATH_PROG(MPICC, mpicc)
  if test -z "$MPICC"; then
    AC_MSG_FAILURE([cannot find 'mpicc' program.])
    MPICC=`echo "Error: MPI is not installed properly." ; false`
  fi
  AC_PATH_PROG(MPICXX, mpicxx)
  if test -z "$MPICXX"; then
    AC_MSG_FAILURE([cannot find 'mpicxx' program.])
    MPICXX=`echo "Error: MPI is not installed properly." ; false`
  fi
  if test "$with_fortran" = yes ; then
    AC_PATH_PROG(MPIF90, mpif90)
    if test -z "$MPIF90"; then
      AC_MSG_FAILURE([cannot find 'mpif90' program.])
      MPIF90=`echo "Error: MPI is not installed properly." ; false`
    fi
  fi
fi

# cppunit
if test "$install_cppunit" = yes ; then
  echo "do nothing" >& /dev/null
else
  if test "$with_testing" = yes ; then
    if test "$with_cppunit_incdir" != no; then
      CPPUNIT_INCLUDES="-I$with_cppunit_incdir"
    fi
    if test "$with_cppunit_libdir" != no; then
      CPPUNIT_LDFLAGS="-L$with_cppunit_libdir"
    fi
    CIT_CPPUNIT_HEADER
    CIT_CPPUNIT_LIB
  fi
fi
AC_SUBST(CPPUNIT_INCLUDES)
AC_SUBST(CPPUNIT_LDFLAGS)

# catch2
if test "$install_catch2" = yes ; then
  echo "do nothing" >& /dev/null
else
  if test "$with_testing" = yes ; then
    if test "$with_catch2_incdir" != no; then
      CATCH2_INCLUDES="-I$with_catch2_incdir"
    fi
    if test "$with_catch2_libdir" != no; then
      CATCH2_LDFLAGS="-L$with_catch2_libdir"
    fi
    CIT_CATCH2_HEADER
    CIT_CATCH2_LIB
  fi
fi
AC_SUBST(CATCH2_INCLUDES)
AC_SUBST(CATCH2_LDFLAGS)

# PCRE
if test "$install_pcre" = yes ; then
  echo "do nothing" >& /dev/null
else
  if test "$install_swig" = yes ; then
    if test "$with_pcre_incdir" != no; then
      PCRE_INCLUDES="-I$with_pcre_incdir"
    fi
    if test "$with_pcre_libdir" != no; then
      PCRE_LDFLAGS="-L$with_pcre_libdir"
    fi
    CIT_PCRE_HEADER
    CIT_PCRE_LIB
  fi
fi
AC_SUBST(PCRE_INCLUDES)
AC_SUBST(PCRE_LDFLAGS)

# SWIG
if test "$install_swig" = yes ; then
  echo "do nothing" >& /dev/null
else
  if test "$pylith_git" != no ; then
    AC_PROG_SWIG([4.0.0])
  fi
fi

# sqlite
if test "$install_sqlite" = yes ; then
  AC_PATH_PROG(existing_sqlite, sqlite)
  AC_SUBST(existing_sqlite)
  SQLITE3_INCLUDES="-I$prefix/include"
  SQLITE3_LDFLAGS="-L$prefix/lib"
else
  if test "$with_sqlite_incdir" != no; then
    SQLITE3_INCDIR="$with_sqlite_incdir"
  fi
  if test "$with_sqlite_libdir" != no; then
    SQLITE3_LIBDIR="$with_sqlite_libdir"
  fi
  CIT_SQLITE3_HEADER
  CIT_SQLITE3_LIB
fi
AC_SUBST(SQLITE3_INCDIR)
AC_SUBST(SQLITE3_LIBDIR)

# proj
if test "$install_proj" = yes ; then
  AC_PATH_PROG(existing_proj, proj)
  AC_SUBST(existing_proj)

  # Installing Proj requires tiff
  if test "$install_tiff" = yes ; then
    AC_PATH_PROG(existing_tiff, tiff)
    AC_SUBST(existing_tiff)
    TIFF_INCLUDES="-I$prefix/include"
    TIFF_LDFLAGS="-L$prefix/lib"
  else
    if test "$with_tiff_incdir" != no; then
      TIFF_INCDIR="$with_tiff_incdir"
    fi
    if test "$with_tiff_libdir" != no; then
      TIFF_LIBDIR="$with_tiff_libdir"
    fi
    CIT_TIFF_HEADER
    CIT_TIFF_LIB
  fi
  AC_SUBST(TIFF_INCDIR)
  AC_SUBST(TIFF_LIBDIR)
else
  if test "$with_proj_incdir" != no; then
    PROJ_INCLUDES="-I$with_proj_incdir"
  fi
  if test "$with_proj_libdir" != no; then
    PROJ_LDFLAGS="-L$with_proj_libdir"
  fi
  CIT_PROJ6_HEADER
  CIT_PROJ6_LIB
fi
AC_SUBST(PROJ_INCLUDES)
AC_SUBST(PROJ_LDFLAGS)

# HDF5
if test "$install_hdf5" = yes ; then
  # Need to account for PETSc option --download-hdf5=1.
  AC_PATH_PROG(existing_hdf5, h5dump)
  AC_SUBST(existing_hdf5)
  HDF5_INCDIR=$prefix/include
  HDF5_LIBDIR=$prefix/lib
  HDF5_INCLUDES="-I$prefix/include"
  HDF5_LDFLAGS="-L$prefix/lib"
else
  if test "$with_hdf5_incdir" != no; then
    HDF5_INCDIR="$with_hdf5_incdir"
    HDF5_INCLUDES="-I$with_hdf5_incdir"
  fi
  if test "$with_hdf5_libdir" != no; then
    HDF5_LIBDIR="$with_hdf5_libdir"
    HDF5_LDFLAGS="-L$with_hdf5_libdir"
  fi
  CC_SAVE=$CC
  CC=mpicc
  CIT_HDF5_HEADER
  CIT_HDF5_LIB
  CIT_HDF5_LIB_PARALLEL
  CC=$CC_SAVE
fi
AC_SUBST(HDF5_INCDIR)
AC_SUBST(HDF5_LIBDIR)
AC_SUBST(HDF5_INCLUDES)
AC_SUBST(HDF5_LDFLAGS)

# H5PY
if test "$install_h5py" = yes ; then
  x=1
else
  if test "$with_h5py" = yes ; then
    CIT_PYTHON_MODULE([h5py],[3.0.0])
  fi
fi

# NETCDF
if test "$install_netcdf" = yes ; then
  AC_PATH_PROG(existing_netcdf, ncdump)
  AC_SUBST(existing_netcdf)
  NETCDF_INCDIR="$prefix/include"
  NETCDF_LIBDIR="$prefix/lib"
else
  if test "$with_netcdf_incdir" != no; then
    NETCDF_INCDIR="$with_netcdf_incdir"
    NETCDF_INCLUDES="-I$with_netcdf_incdir"
  fi
  if test "$with_netcdf_libdir" != no; then
    NETCDF_LIBDIR="$with_netcdf_libdir"
    NETCDF_LDFLAGS="-L$with_netcdf_libdir"
  fi
  CIT_NETCDF_HEADER
  CIT_NETCDF_LIB
fi
AC_SUBST(NETCDF_INCDIR)
AC_SUBST(NETCDF_LIBDIR)
AC_SUBST(NETCDF_INCLUDES)
AC_SUBST(NETCDF_LDFLAGS)

# NETCDF4 (python)
if test "$install_netcdfpy" = yes ; then
  if test "$install_python" = yes ; then
    if test "$install_cftime" != yes ; then
      AC_MSG_WARN([Building Python requires building cftime (for NetCDF4) as well. Adding installation of cftime.])
    fi
    install_cftime=yes
  fi
  if test "$install_cftime" = !yes ; then
    CIT_PYTHON_MODULE([cftime],[1.0.0])
  fi
fi

# PETSC
if test "$install_petsc" = yes ; then
  if test -n "$PETSC_DIR"; then
    existing_petsc=$PETSC_DIR
  fi
  AC_SUBST(existing_petsc)

  AC_ARG_VAR(PETSC_DIR, [location of PETSc installation])
  AC_ARG_VAR(PETSC_ARCH, [PETSc configuration])
  if test "$install_developer" = yes ; then
    PETSC_DIR="$(pwd)/cig/petsc-pylith"
  else
    PETSC_DIR=$prefix
  fi
  AC_SUBST(PETSC_DIR)
  PETSC_ARCH=arch-pylith
  AC_SUBST(PETSC_ARCH)
else
  AC_LANG(C)
  CIT_PATH_PETSC([3.18.2])
  CIT_HEADER_PETSC
  CIT_CHECK_LIB_PETSC
fi

# pythia
if test "$install_pythia" = yes ; then
  AC_PATH_PROG(existing_nemesis, nemesis)
  AC_SUBST(existing_nemesis)
else
  AC_PATH_PROG(NEMESIS, nemesis)
  if test -z $NEMESIS; then
    AC_MSG_FAILURE([cannot find 'nemesis' program.])
    NEMESIS=`echo "Error: Pythia/pyre is not installed properly." ; false`
  fi
fi

# spatialdata
if test "$install_spatialdata" = yes ; then
  AC_PATH_PROG(existing_spatialdata, gensimpledb.py)
  AC_SUBST(existing_spatialdata)
else
  CIT_SPATIALDATA_HEADER
  CIT_SPATIALDATA_LIB
  CIT_PYTHON_MODULE([spatialdata])
fi

# ----------------------------------------------------------------------
# Warning of existing installation
AC_PATH_PROG(existing_pylith, pylith)
AC_SUBST(existing_pylith)

existing_fail=false
printf "\n"
printf "Examining test results for existing versions of software...\n"

# MPI
if test -n "$existing_mpi"; then
  printf "WARNING: Existing version of MPI installed. Found $existing_mpi\n"
  if test "$force_install" != yes ; then
    existing_fail=yes
  fi
fi

# SQLITE
if test -n "$existing_sqlite"; then
  printf "WARNING: Existing version of SQLITE installed. Found $existing_sqlite\n"
  if test "$force_install" != yes ; then
    existing_fail=yes
  fi
fi

# TIFF
if test -n "$existing_tiff"; then
  printf "WARNING: Existing version of TIFF installed. Found $existing_tiff\n"
  if test "$force_install" != yes ; then
    existing_fail=yes
  fi
fi

# PROJ
if test -n "$existing_proj"; then
  printf "WARNING: Existing version of PROJ installed. Found $existing_proj\n"
  if test "$force_install" != yes ; then
    existing_fail=yes
  fi
fi

# HDF5
if test -n "$existing_hdf5"; then
  printf "WARNING: Existing version of HDF5 installed. Found $existing_hdf5\n"
  if test "$force_install" != yes ; then
    existing_fail=yes
  fi
fi

# NETCDF
if test -n "$existing_netcdf"; then
  printf "WARNING: Existing version of NetCDF installed. Found $existing_netcdf\n"
  if test "$force_install" != yes ; then
    existing_fail=yes
  fi
fi

# NEMESIS
if test -n "$existing_nemesis"; then
  printf "WARNING: Existing version of nemesis installed. Found $existing_nemesis\n"
  if test "$force_install" != yes ; then
    existing_fail=yes
  fi
fi

# PETSC
if test -n "$existing_petsc"; then
  printf "WARNING: Existing version of PETSc installed. Found $existing_petsc\n"
  if test "$force_install" != yes ; then
    existing_fail=yes
  fi
fi

# SPATIALDATA
if test -n "$existing_spatialdata"; then
  printf "WARNING: Existing version of spatialdata installed. Found $existing_spatialdata\n"
  if test "$force_install" != yes ; then
    existing_fail=yes
  fi
fi

# PYLITH
if test -n "$existing_pylith"; then
  printf "WARNING: Existing version of PyLith installed. Found $existing_pylith\n"
  if test "$force_install" != yes ; then
    existing_fail=yes
  fi
fi

if test "$existing_fail" = yes ; then
  printf "\n"
  AC_MSG_ERROR(["Configure failed due to conflict with existing software. Existing software may interfere with proper installation of PyLith, may be configured incorrectly for use with PyLith, or may have been built with incompatible compilers. Remove existing software (RECOMMENDED) or reconfigure with --enable-force-install to override error message. "])
fi


# ----------------------------------------------------------------------
AC_CANONICAL_HOST
# Setup environment so dependencies are used in build
CPPFLAGS="-I$prefix/include $CPPFLAGS"

case $host_os in
  darwin*)
    LDFLAGS="-L$prefix/lib $LDFLAGS"
    ;;
  *)
    LDFLAGS="-L$prefix/lib -L$prefix/lib64 $LDFLAGS"
  ;;
esac
AC_SUBST(CPPFLAGS)
AC_SUBST(LDFLAGS)

# Create setup.sh
echo "#!/bin/bash" > setup.sh
TEMP_BINDIR="$prefix/bin"
echo "if [[ -d $TEMP_BINDIR ]]; then" >> setup.sh
echo "  source ${TEMP_BINDIR}/activate" >> setup.sh
echo "else" >> setup.sh
if test "X${PATH}" = X ; then
  echo "export PATH=${TEMP_BINDIR}" >> setup.sh
else
  echo "export PATH=${TEMP_BINDIR}:\${PATH}" >> setup.sh
fi
TEMP_PATH="$prefix/lib/python$PYTHON_VERSION/site-packages:$prefix/lib64/python$PYTHON_VERSION/site-packages"
if test "X$PYTHONPATH" = X ; then
  echo "export PYTHONPATH=${TEMP_PATH}" >> setup.sh
else
  echo "export PYTHONPATH=${TEMP_PATH}:\${PYTHONPATH}" >> setup.sh
fi
echo "fi" >> setup.sh

case $host_os in
  darwin*)
    ;;
  *)
    TEMP_PATH="$prefix/lib:$prefix/lib64"
    if test "$install_developer" = "yes"; then
     TEMP_PATH="${TEMP_PATH}:${PETSC_DIR}/${PETSC_ARCH}/lib"
    fi
    if test "X${LD_LIBRARY_PATH}" = X ; then
      echo "export LD_LIBRARY_PATH=${TEMP_PATH}" >> setup.sh
    else
      echo "export LD_LIBRARY_PATH=${TEMP_PATH}:\${LD_LIBRARY_PATH}" >> setup.sh
    fi
    ;;
esac


# ----------------------------------------------------------------------
AC_CONFIG_FILES([Makefile dependencies/Makefile cig/Makefile])

AC_OUTPUT

# ----------------------------------------------------------------------
# Write summary.
printf "\n"
printf "Build info:\n"
printf "  Using $downloader to download tarballs.\n"
printf "  Using $make_threads thread(s) when running make in parallel.\n"
printf "  Languages enabled: "
if test "$with_fortran" = yes ; then
  printf "C,C++,Fortran\n"
else
  printf "C,C++\n"
fi
printf "  Debugging: $with_debugging\n\n"
printf "PyLith dependencies to be installed:\n\n"
printf "  gcc: $install_gcc"
if test "$install_gcc" = yes ; then
  printf ", languages: $gcc_languages, flags: $gcc_flags\n"
else
  printf "\n"
fi
printf "  cmake: $install_cmake\n"
printf "  mpi: $install_mpi"
if test "$install_mpi" != "mpich" ; then
  printf "\n"
else
  printf ", options: $mpich_options\n"
fi
printf "  git: $install_git\n"
printf "  autotools: $install_autotools\n"
printf "  pcre: $install_pcre\n"
printf "  swig: $install_swig\n"
printf "  cppunit: $install_cppunit\n"
printf "  catch2: $install_catch2\n"
printf "  openssl: $install_openssl\n"
printf "  curl: $install_curl\n"
printf "  libffi: $install_libffi\n"
printf "  Python: $install_python\n"
printf "  Python packages\n"
printf "    h5py: $install_h5py\n"
printf "    netCDF4 (python): $install_netcdfpy (optional; post-processing)\n"
printf "    sphinx: $install_sphinx (optional; generate documentation)\n"
printf "  sqlite: $install_sqlite\n"
printf "  tiff: $install_tiff\n"
printf "  proj: $install_proj\n"
printf "  hdf5: $install_hdf5\n"
printf "  netcdf: $install_netcdf\n"
printf "  pythia: $install_pythia\n"
printf "  spatialdata: $install_spatialdata\n"
printf "  petsc: $install_petsc, options: $petsc_options\n"
printf "  pylith-parameters GUI: $install_parametersgui\n"
printf "\n"
if test "$pylith_git" != no ; then
  if test "$force_petsc_tarball" == yes ; then
    printf "  Using PETSc tarball from PyLith release.\n"
  else
    printf "  Using PETSc from Git repo: $petsc_repo.\n"
  fi
  printf "  Using spatialdata from Git repo: $spatialdata_repo.\n"
  printf "  Using PyLith from Git repo: $pylith_repo.\n"
  printf "  Building PyLith branch '$pylith_git'.\n"
else
  printf "  Building PETSc, spatialdata, and PyLith from source tarballs.\n"
fi
printf "\n"
printf "IMPORTANT\n\n"
printf "  Step 1\n"
printf "  BEFORE running \"make\", setup your environment so that all of the \n"
printf "  dependencies are consistent. See the file setup.sh in this directory \n"
printf "  for how to set your variables for the bash shell. You can either run \n"
printf "  \"source setup.sh\" in this terminal (i.e., shell) where you will \n"
printf "  build PyLith and it dependencies or add these settings to your \n"
printf "  .bashrc or equivalent file and open a new terminal (i.e., shell).\n"
printf "\n"
printf "  Step 2\n"
printf "  Running \"make\" will install PyLith to $prefix.\n"
printf "\n"
printf "  Step 3\n"
printf "  If you did not setup your .bashrc with the environment variables, be sure \n"
printf "  to run \"source setup.sh\" every time you open a new terminal (i.e., shell) \n"
printf "  BEFORE running PyLith.\n"
printf "\n"


dnl end of configure.ac
