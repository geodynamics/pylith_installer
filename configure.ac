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
AC_INIT([PyLith Installer], [1.0.0], [cig-short@geodynamics.org])
AC_CONFIG_HEADER([portinfo])
AC_CONFIG_AUX_DIR([./aux-config])
AC_CONFIG_MACRO_DIR([m4])
AM_INIT_AUTOMAKE([foreign])

# ----------------------------------------------------------------------
# SOFTWARE TO INSTALL
# ----------------------------------------------------------------------

# GCC
AC_ARG_ENABLE([gcc],
    [AC_HELP_STRING([--enable-gcc],
        [install GNU compilers) @<:@default=no@:>@])],
	[install_gcc=yes],
	[install_gcc=no])
AM_CONDITIONAL([INSTALL_GCC], [test "$install_gcc" = yes])

# PYTHON
AC_ARG_ENABLE([python],
    [AC_HELP_STRING([--enable-python],
        [install Python) @<:@default=no@:>@])],
	[install_python=yes],
	[install_python=no])
AM_CONDITIONAL([INSTALL_PYTHON], [test "$install_python" = yes])

# MPI
AC_ARG_ENABLE([mpi],
    [AC_HELP_STRING([--enable-mpi],
        [install OpenMPI version of MPI) @<:@default=no@:>@])],
	[install_mpi=$enableval],
	[install_mpi=no])
AM_CONDITIONAL([INSTALL_MPI], [test "$install_mpi" != no])

# CPPUNIT
AC_ARG_ENABLE([cppunit],
    [AC_HELP_STRING([--enable-cppunit],
        [install GNU compilers) @<:@default=yes@:>@])],
	[install_cppunit=yes],
	[install_cppunit=no])
AM_CONDITIONAL([INSTALL_CPPUNIT], [test "$install_cppunit" = yes])

# SWIG
AC_ARG_ENABLE([swig],
    [AC_HELP_STRING([--enable-swig],
        [install SWIG) @<:@default=yes@:>@])],
	[install_swig=yes],
	[install_swig=no])
AM_CONDITIONAL([INSTALL_SWIG], [test "$install_swig" = yes])

# NUMPY
AC_ARG_ENABLE([numpy],
    [AC_HELP_STRING([--enable-numpy],
        [install numpy) @<:@default=yes@:>@])],
	[install_numpy=yes],
	[install_numpy=no])
AM_CONDITIONAL([INSTALL_NUMPY], [test "$install_numpy" = yes])

# PROJ4
AC_ARG_ENABLE([proj4],
    [AC_HELP_STRING([--enable-proj4],
        [install GNU compilers) @<:@default=yes@:>@])],
	[install_proj4=yes],
	[install_proj4=no])
AM_CONDITIONAL([INSTALL_PROJ4], [test "$install_proj4" = yes])

# NETCDF
AC_ARG_ENABLE([netcdf],
    [AC_HELP_STRING([--enable-netcdf],
        [install NetCDF) @<:@default=yes@:>@])],
	[install_netcdf=yes],
	[install_netcdf=no])
AM_CONDITIONAL([INSTALL_NETCDF], [test "$install_netcdf" = yes])

# HDF5
AC_ARG_ENABLE([hdf5],
    [AC_HELP_STRING([--enable-hdf5],
        [install HDF5) @<:@default=yes@:>@])],
	[install_hdf5=yes],
	[install_hdf5=no])
AM_CONDITIONAL([INSTALL_HDF5], [test "$install_hdf5" = yes])

# PETSC
AC_ARG_ENABLE([petsc],
    [AC_HELP_STRING([--enable-petsc],
        [install PETSc (development version)) @<:@default=yes@:>@])],
	[install_petsc=yes],
	[install_petsc=no])
AM_CONDITIONAL([INSTALL_PETSC], [test "$install_petsc" = yes])

# SPATIALDATA
AC_ARG_ENABLE([spatialdata],
    [AC_HELP_STRING([--enable-spatialdata],
        [install spatialdata (CIG)) @<:@default=yes@:>@])],
	[install_spatialdata=yes],
	[install_spatialdata=no])
AM_CONDITIONAL([INSTALL_SPATIALDATA], [test "$install_spatialdata" = yes])

# NEMESIS
AC_ARG_ENABLE([nemesis],
    [AC_HELP_STRING([--enable-nemesis],
        [install nemesis (CIG)) @<:@default=yes@:>@])],
	[install_nemesis=yes],
	[install_nemesis=no])
AM_CONDITIONAL([INSTALL_NEMESIS], [test "$install_nemesis" = yes])

# FIAT
AC_ARG_ENABLE([fiat],
    [AC_HELP_STRING([--enable-fiat],
        [install GNU compilers) @<:@default=yes@:>@])],
	[install_fiat=yes],
	[install_fiat=no])
AM_CONDITIONAL([INSTALL_FIAT], [test "$install_fiat" = yes])

# TESTING
AC_ARG_ENABLE([fiat],
    [AC_HELP_STRING([--enable-fiat],
        [install GNU compilers) @<:@default=yes@:>@])],
	[install_fiat=yes],
	[install_fiat=no])
AM_CONDITIONAL([INSTALL_FIAT], [test "$install_fiat" = yes])


# ----------------------------------------------------------------------
# OPTIONS
# ----------------------------------------------------------------------

# TESTING
AC_ARG_ENABLE([testing],
    [AC_HELP_STRING([--enable-testing],
        [enable testing (requires cppunit) @<:@default=yes@:>@])],
	[enable_testing=yes],
	[enable_testing=no])
AM_CONDITIONAL([ENABLE_TESTING], [test "$enable_testing" = yes])

# FORTRAN
AC_ARG_ENABLE([fortran],
    [AC_HELP_STRING([--enable-fortran],
        [enable Fortran options for packages @<:@default=yes@:>@])],
	[enable_fortran=yes],
	[enable_fortran=no])
AM_CONDITIONAL([ENABLE_FORTRAN], [test "$enable_fortran" = yes])

# PETSC options
AC_ARG_WITH([petsc-options],
    [AC_HELP_STRING([--with-petsc-options],
        [set PETSc configure options @<:@default=none@:>@])],
	[petsc_options=$withval],
	[petsc-options=none])

# :TODO: Add option to use/not use NETCDF, HDF5

# :TODO: Add option to use SVN for CIG code and PETSc. Use enableval
# to switch between stable release and trunk for PyLith.

# ----------------------------------------------------------------------
# CHECK COMPATIBILITY OF OPTIONS
# ----------------------------------------------------------------------

# GCC
if test "$install_gcc" = "yes" ; then
  # Must have a C compiler to build gcc
  AC_PROG_CC
else
  # Must have a C++ compiler
  AC_PROG_CXX  
  if test "$enable_fortran" = "yes" ; then
    AC_PROG_FC
  fi
fi

# Python
if test "$install_python" = "yes" ; then
  echo "do nothing" >& /dev/null
else
  AM_PATH_PYTHON([2.3])
  CIT_PYTHON_SYSCONFIG
fi

# MPI
if test "$install_mpi" = "yes" ; then
  echo "do nothing" >& /dev/null
else
  AC_PATH_PROG(MPICXX, mpicxx)
fi

# cppunit
if test "$install_cppunit" = "yes" ; then
  echo "do nothing" >& /dev/null
else
  CIT_CPPUNIT_HEADER
  CIT_CPPUNIT_LIB
fi

# SWIG
if test "$install_swig" = "yes" ; then
  echo "do nothing" >& /dev/null
else
  AC_PROG_SWIG(1.3.33)
fi

# numpy
if test "$install_numpy" = "yes" ; then
  echo "do nothing" >& /dev/null
else
  CIT_NUMPY_PYTHON_MODULE
  CIT_NUMPY_INCDIR
fi

# proj4
if test "$install_proj4" = "yes" ; then
  echo "do nothing" >& /dev/null
else
  CIT_PROJ4_HEADER
  CIT_PROJ4_LIB
fi

# NETCDF
if test "$install_proj4" = "yes" ; then
  echo "do nothing" >& /dev/null
else
  CIT_NETCDF_HEADER
  CIT_NETCDF_LIB
fi

# HDF5
if test "$install_hdf5" = "yes" ; then
  echo "do nothing" >& /dev/null
else
  # Need to account for PETSc option --download-hdf5=1.
  #CIT_HDF5_PETSC_HEADER
  #CIT_HDF5_PETSC_LIB
fi

# PETSC
if test "$install_hdf5" = "yes" ; then
  echo "do nothing" >& /dev/null
else
  CIT_PATH_PETSC([3.1.0])
  CIT_HEADER_PETSC
  CIT_CHECK_LIB_PETSC
  CIT_CHECK_LIB_PETSC_SIEVE
fi


# spatialdata
if test "$install_proj4" = "yes" ; then
  echo "do nothing" >& /dev/null
else
  CIT_SPATIALDATA_HEADER
  CIT_SPATIALDATA_LIB
fi

# nemesis
if test "$install_nemesis" = "yes" ; then
  echo "do nothing" >& /dev/null
else
  AC_PATH_PROG(NEMESIS, nemesis)
fi

# fiat
if test "$install_proj4" = "yes" ; then
  echo "do nothing" >& /dev/null
else
  CIT_PYTHON_MODULE([FIAT],[0.9.9])
fi


# ----------------------------------------------------------------------
AC_CONFIG_FILES([Makefile
		])

AC_OUTPUT


dnl end of configure.ac
