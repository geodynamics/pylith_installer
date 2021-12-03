# -*- autoconf -*-
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
# Copyright (c) 2010-2021 University of California, Davis
#
# See COPYING for license information.
#
# ----------------------------------------------------------------------
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.59)
AC_INIT([PyLith Installer], [2.2.2-2], [https://community.geodynamics.org/c/pylith])
AC_CONFIG_AUX_DIR([./aux-config])
AC_CONFIG_MACRO_DIR([m4])
AM_INIT_AUTOMAKE([foreign tar-pax])

# ----------------------------------------------------------------------
# SETUP
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


# ----------------------------------------------------------------------
# SOFTWARE TO INSTALL
# ----------------------------------------------------------------------
# AUTOTOOLS
AC_ARG_ENABLE([autotools],
    [AC_HELP_STRING([--enable-autotools],
        [install GNU autotools @<:@default=no@:>@])],
	[if test "$enableval" != no ; then install_autotools=yes; else install_autotools=no; fi],
	[install_autotools=no])
AM_CONDITIONAL([INSTALL_AUTOTOOLS], [test "$install_autotools" = yes])


# CMAKE
AC_ARG_ENABLE([cmake],
    [AC_HELP_STRING([--enable-cmake],
        [install CMAKE @<:@default=yes@:>@])],
	[if test "$enableval" = yes ; then install_cmake=yes; else install_cmake=no; fi],
	[install_cmake=yes])
AM_CONDITIONAL([INSTALL_CMAKE], [test "$install_cmake" = yes])


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


# PYTHON
AC_ARG_ENABLE([python],
    [AC_HELP_STRING([--enable-python],
        [install Python @<:@default=yes@:>@])],
	[if test "$enableval" = yes ; then install_python=yes; else install_python=no; fi],
	[install_python=yes])
AM_CONDITIONAL([INSTALL_PYTHON], [test "$install_python" = yes])


# SETUPTOOLS
AC_ARG_ENABLE([setuptools],
    [AC_HELP_STRING([--enable-setuptools],
        [install setuptools @<:@default=yes@:>@])],
	[if test "$enableval" = yes ; then install_setuptools=yes; else install_setuptools=no; fi],
	[install_setuptools=yes])
AM_CONDITIONAL([INSTALL_SETUPTOOLS], [test "$install_setuptools" = yes])


# CYTHON
AC_ARG_ENABLE([cython],
    [AC_HELP_STRING([--enable-cython],
        [install cython @<:@default=yes@:>@])],
	[if test "$enableval" = yes ; then install_cython=yes; else install_cython=no; fi],
	[install_cython=yes])
AM_CONDITIONAL([INSTALL_CYTHON], [test "$install_cython" = yes])


# PKGCONFIG
AC_ARG_ENABLE([pkgconfig],
    [AC_HELP_STRING([--enable-pkgconfig],
        [install pkgconfig @<:@default=no@:>@])],
	[if test "$enableval" != no ; then install_pkgconfig=yes; else install_pkgconfig=no; fi],
	[install_pkgconfig=yes])
AM_CONDITIONAL([INSTALL_PKGCONFIG], [test "$install_pkgconfig" = yes])


# SIX
AC_ARG_ENABLE([six],
    [AC_HELP_STRING([--enable-six],
        [install six @<:@default=no@:>@])],
	[if test "$enableval" != no ; then install_six=yes; else install_six=no; fi],
	[install_six=yes])
AM_CONDITIONAL([INSTALL_SIX], [test "$install_six" = yes])


# NUMPY
AC_ARG_ENABLE([numpy],
    [AC_HELP_STRING([--enable-numpy],
        [install numpy @<:@default=yes@:>@])],
	[if test "$enableval" = yes ; then install_numpy=yes; else install_numpy=no; fi],
	[install_numpy=yes])
AM_CONDITIONAL([INSTALL_NUMPY], [test "$install_numpy" = yes])
AC_ARG_WITH([numpy-blaslapack],
    [AC_HELP_STRING([--with-numpy-blaslapack],
        [force numpy to build its own BLAS/LAPACK @<:@default=no@:>@])],
	[if test "$withval" = yes; then with_numpy_blaslapack=yes; else with_numpy_blaslapack=no; fi],
	[with_numpy_blaslapack=no])
AM_CONDITIONAL([WITH_NUMPY_BLASLAPACK], [test "$with_numpy_blaslapack" = yes])


# H5PY
AC_ARG_ENABLE([h5py],
    [AC_HELP_STRING([--enable-h5py],
        [install HDF5 @<:@default=yes@:>@])],
	[if test "$enableval" = yes ; then install_h5py=yes; else install_h5py=no; fi],
	[install_h5py=yes])
AM_CONDITIONAL([INSTALL_H5PY], [test "$install_h5py" = yes])


# NETCDFPY
AC_ARG_ENABLE([netcdfpy],
    [AC_HELP_STRING([--enable-netcdfpy],
        [install netCDF4 @<:@default=yes@:>@])],
	[if test "$enableval" = yes ; then install_netcdfpy=yes; else install_netcdfpy=no; fi],
	[install_netcdfpy=yes])
AM_CONDITIONAL([INSTALL_NETCDFPY], [test "$install_netcdfpy" = yes])


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


# pylith git
AC_ARG_WITH([pylith-git],
    [AC_HELP_STRING([--with-pylith-git],
        [use PyLith from GitHub repository (main, BRANCH) @<:@default=no@:>@])],
	[pylith_git=$withval],
	[pylith_git=no])
if test "$pylith_git" = yes ; then pylith_git="releases/v2.2"; fi
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


# SPATIALDATA
AC_ARG_ENABLE([spatialdata],
    [AC_HELP_STRING([--enable-spatialdata],
        [install spatialdata (CIG) @<:@default=yes@:>@])],
	[if test "$enableval" = yes ; then install_spatialdata=yes; else install_spatialdata=no; fi],
	[install_spatialdata=yes])
AM_CONDITIONAL([INSTALL_SPATIALDATA], [test "$install_spatialdata" = yes])


# NEMESIS
AC_ARG_ENABLE([nemesis],
    [AC_HELP_STRING([--enable-nemesis],
        [install nemesis (CIG) @<:@default=yes@:>@])],
	[if test "$enableval" = yes ; then install_nemesis=yes; else install_nemesis=no; fi],
	[install_nemesis=yes])
AM_CONDITIONAL([INSTALL_NEMESIS], [test "$install_nemesis" = yes])


# FIAT
AC_ARG_ENABLE([fiat],
    [AC_HELP_STRING([--enable-fiat],
        [install FIAT @<:@default=yes@:>@])],
	[if test "$enableval" = yes ; then install_fiat=yes; else install_fiat=no; fi],
	[install_fiat=yes])
AM_CONDITIONAL([INSTALL_FIAT], [test "$install_fiat" = yes])


# PYTHIA
install_pythia=no
if test "$install_nemesis" = yes; then
  install_pythia=yes
fi
if test "$install_spatialdata" = yes; then
  install_pythia=yes
fi
AM_CONDITIONAL([INSTALL_PYTHIA], [test "$install_pythia" = yes])


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
# Debugging
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
        [enable testing (requires cppunit) @<:@default=yes@:>@])],
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
  # GIT
  AC_PATH_PROG(GIT, git)
  if test -z "$GIT" ; then
    AC_MSG_FAILURE([cannot find 'git' program.])
  fi
fi
AM_CONDITIONAL([WITH_SWIG], [test "$pylith_git" != no])


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
  if test "$with_fortran" = yes ; then
    AC_PROG_FC
  fi
fi


# PYTHON
if test "$install_python" = yes ; then
  PYTHON=$prefix/bin/python2
  PYTHON_VERSION=2.7
  AC_SUBST(PYTHON)
  AC_CHECK_HEADER([zlib.h], [], [
                AC_MSG_ERROR([Header file 'zlib.h' not found; maybe you don't have the zlib development package, e.g. 'zlib-dev', installed?])
                ])
  if test "$install_openssl" != yes ; then
    AC_CHECK_HEADER([openssl/ssl.h], [], [
                  AC_MSG_ERROR([Building Python requires openssl. Header file 'openssl/ssl.h' not found; maybe you don't have the openssl development package, e.g. 'openssl-dev', installed?])
                ])
  fi
  if test "$install_numpy" != yes ; then
    AC_MSG_WARN([Incompatible configure options. Building Python requires building numpy as well. Adding installation of numpy.])
  fi
  install_numpy=yes
  if test "$install_fiat" != yes ; then
    AC_MSG_WARN([Incompatible configure options. Building Python requires building FIAT as well. Adding installation of FIAT.])
  fi
  install_fiat=yes
  if test "$install_nemesis" != yes ; then
    AC_MSG_WARN([Incompatible configure options. Building Python requires building nemesis as well. Adding installation of nemesis.])
  fi
  install_pythia=yes
  install_nemesis=yes
  if test "$install_spatialdata" != yes ; then
    AC_MSG_WARN([Incompatible configure options. Building Python requires building spatialdata as well. Adding installation of spatialdata.])
  fi
  install_spatialdata=yes
else
  AM_PATH_PYTHON([2.7])
  CIT_PYTHON_SYSCONFIG
  CIT_CHECK_PYTHON_HEADER
  CIT_CHECK_PYTHON_SHARED
  CIT_PYTHON_MODULE([zlib])
fi
AC_CHECK_LIB([z], [deflate], 
  [],
  [AC_MSG_ERROR([Compression library '-lz' not found; maybe you don't have the zlib development package, e.g., 'zlib-dev', installed])
])dnl


# MPI
if test "$install_mpi" != no ; then
  if test "$install_python" != yes ; then
    AC_MSG_WARN([Potentially incompatible configure options. System Python with installer-built MPI is error prone. If build fails you should try reconfiguring with --enable-python or use system MPI.])
  fi
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


# CPPUNIT
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
    AC_PROG_SWIG([2.0.4], [3.0.2])
  fi
fi


# PROJ
if test "$install_proj" = yes ; then
  AC_PATH_PROG(existing_proj, proj)
  AC_SUBST(existing_proj)
  # Installing datums requires unzip
  AC_PATH_PROG(UNZIP, unzip)
  if test -z "$UNZIP" ; then
    AC_MSG_FAILURE([cannot find 'unzip' program.])
    UNZIP=`echo "Error: unzip is not installed." ; false`
  fi
else
  if test "$with_proj_incdir" != no; then
    PROJ_INCLUDES="-I$with_proj_incdir"
  fi
  if test "$with_proj_libdir" != no; then
    PROJ_LDFLAGS="-L$with_proj_libdir"
  fi
  CIT_PROJ4_HEADER
  CIT_PROJ4_LIB
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
  if test "$install_python" = yes ; then
    if test "$install_six" != yes ; then
      AC_MSG_WARN([Building Python requires building six (for h5py) as well. Adding installation of six.])
    fi
    install_six=yes
    AM_CONDITIONAL([INSTALL_SIX], [test "$install_six" = yes])
    if test "$install_pkgconfig" != yes ; then
      AC_MSG_WARN([Building Python requires building pkgconfig (for h5py) as well. Adding installation of pkgconfig.])
    fi
    install_pkgconfig=yes
    AM_CONDITIONAL([INSTALL_PKGCONFIG], [test "$install_pkgconfig" = yes])
    if test "$install_cython" != yes ; then
      AC_MSG_WARN([Building Python requires building cython (for h5py) as well. Adding installation of cython.])
    fi
    install_cython=yes
    AM_CONDITIONAL([INSTALL_CYTHON], [test "$install_cython" = yes])
  fi
  if test "$install_python" = no ; then
    AM_PATH_PYTHON([2.7])
  fi
else
  if test "$with_h5py" = yes ; then
    CIT_PYTHON_MODULE([h5py],[2.0.0])
  fi
fi


# NetCDF
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
else
  if test "$with_netcdfpy" = yes ; then
    CIT_PYTHON_MODULE([netCDF4],[1.0])
  fi
fi


# PETSC options
AC_ARG_WITH([petsc-options],
    [AC_HELP_STRING([--with-petsc-options],
        [set optional PETSc configure options @<:@default=--download-chaco=1 --download-ml=1 --download-f2cblaslapack=1@:>@])],
	[petsc_options=$withval],
	[petsc_options="--download-chaco=1 --download-ml=1 --download-f2cblaslapack=1"])
AC_SUBST(petsc_options)


# numpy
if test "$install_numpy" = yes ; then
  echo "do nothing" >& /dev/null
else
  CIT_NUMPY_PYTHON_MODULE
  CIT_NUMPY_INCDIR
fi


# PETSC
if test "$install_petsc" = yes ; then
  if test -n "$PETSC_DIR"; then
    existing_petsc=$PETSC_DIR
  fi
  AC_SUBST(existing_petsc)

  AC_ARG_VAR(PETSC_DIR, [location of PETSc installation])
  AC_ARG_VAR(PETSC_ARCH, [PETSc configuration])
  PETSC_DIR=$prefix
  AC_SUBST(PETSC_DIR)
  PETSC_ARCH=arch-pylith
  AC_SUBST(PETSC_ARCH)
else
  AC_LANG(C)
  CIT_PATH_PETSC([3.5.3])
  CIT_HEADER_PETSC
  CIT_CHECK_LIB_PETSC
fi

# nemesis
if test "$install_nemesis" = yes ; then
  AC_PATH_PROG(existing_nemesis, nemesis)
  AC_SUBST(existing_nemesis)
else
  AC_PATH_PROG(NEMESIS, nemesis)
  if test -z $NEMESIS; then
    AC_MSG_FAILURE([cannot find 'nemesis' program.])
    NEMESIS=`echo "Error: nemesis is not installed properly." ; false`
  fi
fi

# setuptools
if test "$install_setuptools" = yes ; then
  # Installing setuptools requires unzip
  AC_PATH_PROG(UNZIP, unzip)
  if test -z "$UNZIP" ; then
    AC_MSG_FAILURE([cannot find 'unzip' program.])
    UNZIP=`echo "Error: unzip is not installed." ; false`
  fi
fi

# fiat
if test "$install_fiat" = yes ; then
  echo "do nothing" >& /dev/null
else
  CIT_PYTHON_MODULE([FIAT],[0.9.9])
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
echo ""
echo "Examining test results for existing versions of software..."

# MPI
if test -n "$existing_mpi"; then
  echo "WARNING: Existing version of MPI installed. Found $existing_mpi"
  if test "$force_install" != yes ; then
    existing_fail=yes
  fi
fi

# PROJ
if test -n "$existing_proj"; then
  echo "WARNING: Existing version of PROJ installed. Found $existing_proj"
  if test "$force_install" != yes ; then
    existing_fail=yes
  fi
fi

# HDF5
if test -n "$existing_hdf5"; then
  echo "WARNING: Existing version of HDF5 installed. Found $existing_hdf5"
  if test "$force_install" != yes ; then
    existing_fail=yes
  fi
fi

# NETCDF
if test -n "$existing_netcdf"; then
  echo "WARNING: Existing version of NetCDF installed. Found $existing_netcdf"
  if test "$force_install" != yes ; then
    existing_fail=yes
  fi
fi

# NEMESIS
if test -n "$existing_nemesis"; then
  echo "WARNING: Existing version of nemesis installed. Found $existing_nemesis"
  if test "$force_install" != yes ; then
    existing_fail=yes
  fi
fi

# PETSC
if test -n "$existing_petsc"; then
  echo "WARNING: Existing version of PETSc installed. Found $existing_petsc"
  if test "$force_install" != yes ; then
    existing_fail=yes
  fi
fi

# SPATIALDATA
if test -n "$existing_spatialdata"; then
  echo "WARNING: Existing version of spatialdata installed. Found $existing_spatialdata"
  if test "$force_install" != yes ; then
    existing_fail=yes
  fi
fi

# PYLITH
if test -n "$existing_pylith"; then
  echo "WARNING: Existing version of PyLith installed. Found $existing_pylith"
  if test "$force_install" != yes ; then
    existing_fail=yes
  fi
fi

if test "$existing_fail" = yes ; then
  echo ""
  AC_MSG_ERROR(["Configure failed due to conflict with existing software. Existing software may interfere with proper installation of PyLith, may be configured incorrectly for use with PyLith, or may have been built with incompatible compilers. Remove existing software (RECOMMENDED) or reconfigure with --enable-force-install to override error message. "])
fi


# ----------------------------------------------------------------------
# Setup environment so dependencies are used in build
CPPFLAGS="-I$prefix/include $CPPFLAGS"
LDFLAGS="-L$prefix/lib -L$prefix/lib64 $LDFLAGS"
AC_SUBST(CPPFLAGS)
AC_SUBST(LDFLAGS)

# Create setup.sh
echo "#!/bin/bash" > setup.sh

TEMPVAR="$prefix/bin"
if test "X${PATH}" = X ; then
  echo "export PATH=$TEMPVAR" >> setup.sh
else
  echo "export PATH=$TEMPVAR:\${PATH}" >> setup.sh
fi

AC_CANONICAL_HOST
case $host_os in
  darwin*)
    ;;
  *)
    TEMPVAR="$prefix/lib:$prefix/lib64"
    if test "X${LD_LIBRARY_PATH}" = X ; then
      echo "export LD_LIBRARY_PATH=$TEMPVAR" >> setup.sh
    else
      echo "export LD_LIBRARY_PATH=$TEMPVAR:\${LD_LIBRARY_PATH}" >> setup.sh
    fi
    ;;
esac

TEMPVAR="$prefix/lib/python$PYTHON_VERSION/site-packages:$prefix/lib64/python$PYTHON_VERSION/site-packages"
if test "X$PYTHONPATH" = X ; then
  echo "export PYTHONPATH=$TEMPVAR" >> setup.sh
else
  echo "export PYTHONPATH=$TEMPVAR:\${PYTHONPATH}" >> setup.sh
fi

# ----------------------------------------------------------------------
AC_CONFIG_FILES([Makefile docs/Makefile])

AC_OUTPUT

# ----------------------------------------------------------------------
# Write summary.
echo ""
echo "Build info:"
echo "  Using $downloader to download tarballs."
echo "  Using $make_threads thread(s) when running make in parallel."
echo -n "  Languages enabled: "
if test "$with_fortran" = yes ; then
  echo "C,C++,Fortran"
else
  echo "C,C++"
fi
echo "  Debugging: $with_debugging"
echo ""
echo "PyLith dependencies to be installed:"
echo ""
echo "  autotools: $install_autotools"
echo "  gcc: $install_gcc, languages: $gcc_languages"
echo "  openssl: $install_openssl"
echo "  mpi: $install_mpi"
echo "  cppunit: $install_cppunit"
echo "  proj: $install_proj"
echo "  hdf5: $install_hdf5"
echo "  netcdf: $install_netcdf"
echo "  cmake: $install_cmake"
echo "  Python: $install_python"
echo "    setuptools: $install_setuptools"
echo "    cython: $install_cython"
echo "    pkgconfig: $install_pkgconfig"
echo "    six: $install_six"
echo "    numpy: $install_numpy  w/own blas/lapack: $with_numpy_blaslapack"
echo "    h5py: $install_h5py"
echo "    cftime: $install_cftime"
echo "    netCDF4 (python): $install_netcdfpy (optional; post-processing)"
echo "  pcre: $install_pcre"
echo "  swig: $install_swig"
echo "  nemesis: $install_nemesis"
echo "  fiat: $install_fiat"
echo "  spatialdata: $install_spatialdata"
echo "  petsc: $install_petsc, options: $petsc_options"
echo "  pyre/pythia: $install_pythia"
echo "  pylith-parameters GUI: $install_parametersgui"
echo ""
echo "  Building PETSc and spatialdata from source tarballs."
if test "$pylith_git" != no ; then
  echo "  Using PyLith from Git repo: $pylith_repo."
  echo "  Building PyLith branch '$pylith_git'."
else
  echo "  Building PyLith from source tarball."
fi
echo ""
echo "IMPORTANT"
echo ""
echo "  Step 1"
echo "  BEFORE running \"make\", setup your environment so that all of the "
echo "  dependencies are consistent. See the file setup.sh in this directory "
echo "  for how to set your variables for the bash shell. You can either run "
echo "  \"source setup.sh\" in this terminal (i.e., shell) where you will "
echo "  build PyLith and it dependencies or add these settings to your "
echo "  .bashrc or equivalent file and open a new terminal (i.e., shell)."
echo ""
echo "  Step 2"
echo "  Running \"make\" will install PyLith and its dependencies to $prefix."
echo ""
echo "  Step 3"
echo "  If you did not setup your .bashrc with the environment variables, be sure "
echo "  to run \"source setup.sh\" every time you open a new terminal (i.e., shell) "
echo "  BEFORE running PyLith."
echo ""


dnl end of configure.ac
