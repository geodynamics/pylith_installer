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
# Copyright (c) 2010 University of California, Davis
#
# See COPYING for license information.
#
# ----------------------------------------------------------------------
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.59)
AC_INIT([PyLith Installer], [1.6.3-0], [cig-short@geodynamics.org])
AC_CONFIG_AUX_DIR([./aux-config])
AC_CONFIG_MACRO_DIR([m4])
AM_INIT_AUTOMAKE([foreign])

# ----------------------------------------------------------------------
# SOFTWARE TO INSTALL
# ----------------------------------------------------------------------

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
AM_CONDITIONAL([GCC_FORTRAN_ONLY], [test "$gcc_languages" = fortran])

# PYTHON
AC_ARG_ENABLE([python],
    [AC_HELP_STRING([--enable-python],
        [install Python @<:@default=no@:>@])],
	[if test "$enableval" = yes ; then install_python=yes; else install_python=no; fi],
	[install_python=no])
AM_CONDITIONAL([INSTALL_PYTHON], [test "$install_python" = yes])

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

# CPPUNIT
AC_ARG_ENABLE([cppunit],
    [AC_HELP_STRING([--enable-cppunit],
        [install CppUnit @<:@default=yes@:>@])],
	[if test "$enableval" = yes ; then install_cppunit=yes; else install_cppunit=no; fi],
	[install_cppunit=yes])
AM_CONDITIONAL([INSTALL_CPPUNIT], [test "$install_cppunit" = yes])

# NUMPY
AC_ARG_ENABLE([numpy],
    [AC_HELP_STRING([--enable-numpy],
        [install numpy @<:@default=yes@:>@])],
	[if test "$enableval" = yes ; then install_numpy=yes; else install_numpy=no; fi],
	[install_numpy=yes])
AM_CONDITIONAL([INSTALL_NUMPY], [test "$install_numpy" = yes])

# PROJ4
AC_ARG_ENABLE([proj4],
    [AC_HELP_STRING([--enable-proj4],
        [install Proj4 @<:@default=yes@:>@])],
	[if test "$enableval" = "yes" ; then install_proj4=yes; else install_proj4=no; fi],
	[install_proj4=yes])
AM_CONDITIONAL([INSTALL_PROJ4], [test "$install_proj4" = yes])

# NETCDF
AC_ARG_ENABLE([netcdf],
    [AC_HELP_STRING([--enable-netcdf],
        [install NetCDF @<:@default=yes@:>@])],
	[if test "$enableval" = yes ; then install_netcdf=yes; else install_netcdf=no; fi],
	[install_netcdf=yes])
AM_CONDITIONAL([INSTALL_NETCDF], [test "$install_netcdf" = yes])

# HDF5
AC_ARG_ENABLE([hdf5],
    [AC_HELP_STRING([--enable-hdf5],
        [install HDF5 @<:@default=yes@:>@])],
	[if test "$enableval" = yes ; then install_hdf5=yes; else install_hdf5=no; fi],
	[install_hdf5=yes])
AM_CONDITIONAL([INSTALL_HDF5], [test "$install_hdf5" = yes])

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

# PCRE
AC_ARG_ENABLE([pcre],
    [AC_HELP_STRING([--enable-pcre],
        [install PCRE @<:@default=no@:>@])],
	[if test "$enableval" = "yes" ; then install_pcre=yes; else install_pcre=no; fi],
	[install_pcre=no])
AM_CONDITIONAL([INSTALL_PCRE], [test "$install_pcre" = yes])

# SWIG
AC_ARG_ENABLE([swig],
    [AC_HELP_STRING([--enable-swig],
        [install SWIG @<:@default=no@:>@])],
	[if test "$enableval" = "yes" ; then install_swig=yes; else install_swig=no; fi],
	[install_swig=no])
AM_CONDITIONAL([INSTALL_SWIG], [test "$install_swig" = yes])

# MERCURIAL
AC_ARG_ENABLE([mercurial],
    [AC_HELP_STRING([--enable-mercurial],
        [install mercurial @<:@default=no@:>@])],
	[if test "$enableval" = "yes" ; then install_mercurial=yes; else install_mercurial=no; fi],
	[install_mercurial=no])
AM_CONDITIONAL([INSTALL_MERCURIAL], [test "$install_mercurial" = yes])


# PYTHIA
install_pythia=no
if test "$install_nemesis" = yes; then
  install_pythia=yes
fi
if test "$install_spatialdata" = yes; then
  install_pythia=yes
fi
AM_CONDITIONAL([INSTALL_PYTHIA], [test "$install_pythia" = yes])


# ----------------------------------------------------------------------
# OPTIONS
# ----------------------------------------------------------------------

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
        [enable Fortran options for packages @<:@default=yes@:>@])],
	[if test "$withval" = yes; then with_fortran=yes; else with_fortran=no; fi],
	[with_fortran=yes])
AM_CONDITIONAL([WITH_FORTRAN], [test "$with_fortran" = yes])

# NetCDF
if test "$install_netcdf" = yes ; then
  with_netcdf=yes
else
  with_netcdf=no
fi
AC_ARG_WITH([netcdf],
    [AC_HELP_STRING([--with-netcdf],
        [enable NetCDF (CUBIT) options for PyLith @<:@default=yes@:>@])],
	[if test "$withval" = yes; then with_netcdf=yes; else with_netcdf=no; fi],
	[with_netcdf=yes])
AM_CONDITIONAL([WITH_NETCDF], [test "$with_netcdf" = yes])

# HDF5
if test "$install_hdf5" = "yes"; then
  with_hdf5=yes
else
  with_hdf5=no
fi
AC_ARG_WITH([hdf5],
    [AC_HELP_STRING([--with-hdf5],
        [enable HDF5 options for PyLith @<:@default=no@:>@])],
	[if test "$withval" = yes; then with_hdf5=yes; else with_hdf5=no; fi],
	[with_hdf5=no])
AM_CONDITIONAL([WITH_HDF5], [test "$with_hdf5" = yes])

# PETSC options
AC_ARG_WITH([petsc-options],
    [AC_HELP_STRING([--with-petsc-options],
        [set optional PETSc configure options @<:@default=--download-chaco=1 --download-ml=1 --download-f-blas-lapack=1@:>@])],
	[petsc_options=$withval],
	[petsc_options="--download-chaco=1 --download-ml=1 --download-f-blas-lapack=1"])
AC_SUBST(petsc_options)

# pylith svn
AC_ARG_WITH([pylith-svn],
    [AC_HELP_STRING([--with-pylith-svn],
        [use PyLith from SVN repository (trunk, stable, BRANCH) @<:@default=no@:>@])],
	[pylith_svn=$withval],
	[pylith_svn=no])
if test "$pylith_svn" = yes ; then pylith_svn="trunk"; fi
if test "$pylith_svn" = stable ; then pylith_svn="branches/v1.6-stable"; fi
AC_SUBST(pylith_svn)
AM_CONDITIONAL([USE_PYLITH_SVN], [test "$pylith_svn" != no])

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
    downloader="$WGET -nd -r"
  fi
elif test "$with_fetch" = "curl" ; then
  AC_PATH_PROG(CURL, curl)
  if test -z "$CURL" ; then
    AC_MSG_FAILURE([cannot find 'curl' program.])
  else
    downloader="$CURL -O"
  fi
else
  AC_MSG_FAILURE([Error in configure logic for downloader.])
fi
AC_SUBST(downloader)

# svn/autoreconf
petsc_hg=no
if test "$pylith_svn" != no ; then
  # SVN
  AC_PATH_PROG(SVN, svn)
  if test -z "$SVN" ; then
    AC_MSG_FAILURE([cannot find 'svn' program.])
  fi
  # autoreconf 
  AC_PATH_PROG(AUTORECONF, autoreconf)
  if test -z "$AUTORECONF" ; then
    AC_MSG_FAILURE([cannot find 'autoreconf' program.])
  fi
  # HG
  if test "$install_mercurial" = yes; then
    echo "do nothing" >& /dev/null
  else
    AC_PATH_PROG(HG, hg)
    if test -z "$HG" ; then
      AC_MSG_FAILURE([cannot find 'hg' program.])
    fi
  fi
  petsc_hg=yes
fi
AM_CONDITIONAL([WITH_SWIG], [test "$pylith_svn" != no])
AC_SUBST(petsc_hg)

# ----------------------------------------------------------------------
# CHECK COMPATIBILITY OF OPTIONS
# ----------------------------------------------------------------------

# GCC
if test "$install_gcc" = yes ; then
  # Must have a C/C++ compiler to build gcc and run C++ configure checks.
  AC_PROG_CC
  AC_PROG_CXX
  if test "$with_fortran" = yes ; then
    FC=gfortran
    AC_SUBST(FC)
  fi
else
  # Must have a C++ compiler
  AC_PROG_CC
  AC_PROG_CXX
  if test "$with_fortran" = yes ; then
    AC_PROG_FC
  fi
fi

# Python
if test "$install_python" = yes ; then
  PYTHON=$prefix/bin/python
  AC_SUBST(PYTHON)
  AC_CHECK_HEADER([zlib.h], [], [
                AC_MSG_ERROR([Header file 'zlib.h' not found; maybe you don't have the zlib development package, e.g. 'zlib-dev', installed?])
                ])

else
  AM_PATH_PYTHON([2.4])
  CIT_PYTHON_SYSCONFIG
  CIT_CHECK_PYTHON_HEADER
  CIT_CHECK_PYTHON_SHARED
  CIT_PYTHON_MODULE([zlib])
fi

# MPI
if test "$install_mpi" != no ; then
  echo "do nothing" >& /dev/null
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
    CIT_CPPUNIT_HEADER
    CIT_CPPUNIT_LIB
  fi
fi

# PCRE
if test "$install_pcre" = yes ; then
  echo "do nothing" >& /dev/null
else
  if test "$install_swig" = yes ; then
    AC_LANG(C++)
    AC_CHECK_HEADER([pcre.h], [], [
      AC_MSG_ERROR([pcre header not found; try CPPFLAGS="-I<pcre include dir>"])
    ])dnl
    AC_LANG(C++)
    AC_MSG_CHECKING([for real_pcre in -lpcre])
    AC_REQUIRE_CPP
    AC_COMPILE_IFELSE(
      [AC_LANG_PROGRAM([[#include <pcre.h>]],
                       [[real_pcre value;]])],
      [AC_MSG_RESULT(yes)],
      [AC_MSG_RESULT(no)
      AC_MSG_ERROR([pcre library not found; try LDFLAGS="-L<pcre lib dir>"])
    ])dnl
    AC_PATH_PROG(PCRETEST, pcretest)
  fi
fi

# SWIG
if test "$install_swig" = yes ; then
  echo "do nothing" >& /dev/null
else
  if test "$pylith_svn" != no ; then
    AC_PROG_SWIG(1.3.33)
  fi
fi

# numpy
if test "$install_numpy" = yes ; then
  echo "do nothing" >& /dev/null
else
  CIT_NUMPY_PYTHON_MODULE
  CIT_NUMPY_INCDIR
fi

# proj4
if test "$install_proj4" = yes ; then
  echo "do nothing" >& /dev/null
else
  CIT_PROJ4_HEADER
  CIT_PROJ4_LIB
fi

# NETCDF
if test "$install_netcdf" = yes ; then
  echo "do nothing" >& /dev/null
else
  if test "$with_netcdf" = yes ; then
    CIT_NETCDF_HEADER
    CIT_NETCDF_LIB
  fi
fi

# HDF5
if test "$install_hdf5" = yes ; then
  # Need to account for PETSc option --download-hdf5=1.
  echo "do nothing" >& /dev/null
else
  if test "$with_hdf5" = yes ; then
    CIT_HDF5_HEADER
    CIT_HDF5_LIB
    CIT_HDF5_LIB_PARALLEL
  fi
fi

# PETSC
if test "$install_petsc" = yes ; then
  PETSC_DIR=$prefix
  AC_SUBST(PETSC_DIR)
  PETSC_ARCH=pylith_petsc_opt
  AC_SUBST(PETSC_ARCH)
else
  CIT_PATH_PETSC([3.1.0])
  CIT_HEADER_PETSC
  CIT_CHECK_LIB_PETSC
  CIT_CHECK_LIB_PETSC_SIEVE
fi

# nemesis
if test "$install_nemesis" = yes ; then
  echo "do nothing" >& /dev/null
else
  AC_PATH_PROG(NEMESIS, nemesis)
  if test -z $NEMESIS; then
    AC_MSG_FAILURE([cannot find 'nemesis' program.])
    NEMESIS=`echo "Error: nemesis is not installed properly." ; false`
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
  echo "do nothing" >& /dev/null
else
  CIT_SPATIALDATA_HEADER
  CIT_SPATIALDATA_LIB
  CIT_PYTHON_MODULE([spatialdata])
fi


# ----------------------------------------------------------------------
# Setup environment so dependencies are used in build

CPPFLAGS="-I$prefix/include $CPPFLAGS"
LDFLAGS="-L$prefix/lib $LDFLAGS"
AC_SUBST(CPPFLAGS)
AC_SUBST(LDFLAGS)


# Create setup.sh
echo "#!/bin/bash" > setup.sh

if test "X${PATH}" = X ; then
  echo "export PATH=$prefix/bin" >> setup.sh
else
  echo "export PATH=$prefix/bin:\${PATH}" >> setup.sh
fi

if test "X${LD_LIBRARY_PATH}" = X ; then
  echo "export LD_LIBRARY_PATH=$prefix/lib:$prefix/lib64" >> setup.sh
else
  echo "export LD_LIBRARY_PATH=$prefix/lib:$prefix/lib64:\${LD_LIBRARY_PATH}" >> setup.sh
fi

if test "X${PYTHONPATH}" = X ; then
  echo "export PYTHONPATH=$prefix/lib/python$PYTHON_VERSION/site-packages:$prefix/lib64/python$PYTHON_VERSION/site-packages" >> setup.sh
else
  echo "export PYTHONPATH=$prefix/lib/python$PYTHON_VERSION/site-packages:$prefix/lib64/python$PYTHON_VERSION/site-packages:\${PYTHONPATH}" >> setup.sh
fi

# ----------------------------------------------------------------------
AC_CONFIG_FILES([Makefile
		bin/Makefile
		])

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
echo ""
echo "PyLith dependencies to be installed:"
echo ""
echo "  gcc: $install_gcc, languages: $gcc_languages"
echo "  Python: $install_python"
echo "  mpi: $install_mpi"
echo "  cppunit: $install_cppunit"
echo "  proj4: $install_proj4"
echo "  netcdf: $install_netcdf"
echo "  hdf5: $install_hdf5"
echo "  pcre: $install_pcre"
echo "  swig: $install_swig"
echo "  nemesis: $install_nemesis"
echo "  numpy: $install_numpy"
echo "  fiat: $install_fiat"
echo "  spatialdata: $install_spatialdata"
echo "  mercurial: $install_mercurial"
echo "  petsc: $install_petsc, options: $petsc_options"
echo ""
if test "$pylith_svn" != no ; then
  echo "  Installing development version of PETSc from repository."
  echo "  Installing spatialdata from CIG SVN repository."
  echo "  Building PyLith from SVN repository '$pylith_svn'."
else
  echo "  Building PETSc, spatialdata, and PyLith from source tarballs."
fi
echo ""
echo "IMPORTANT"
echo ""
echo "  BEFORE running \"make\", setup your environment so that all of the "
echo "  dependencies are consistent. See the file setup.sh in this directory "
echo "  for how to set your variables for the bash shell. You can either run "
echo "  \"source setup.sh\" in this terminal (i.e., shell) where you will "
echo "  build PyLith and it dependencies or add these settings to your "
echo "  .bashrc or equivalent file and open a new terminal (i.e., shell)."
echo ""
echo "  Runing \"make\" will install PyLith and its dependencies to $prefix."
echo ""
echo "  AFTER running make, if you did not setup your .bashrc with the "
echo "  environment variables, be sure to run \"source setup.sh\" in the "
echo "  terminal (i.e., shell) BEFORE running PyLith."
echo ""


dnl end of configure.ac
