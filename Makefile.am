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

default: all

all: gcc python mpi cppunit swig numpy proj4 netcdf hdf5 petsc nemesis spatialdata fiat

# ----------------------------------------------------------------------
# gcc
# ----------------------------------------------------------------------
gcc:
if INSTALL_GCC
	$(download) http://geodynamics.org/~buildbot/deps/gcc-4.5.2.tar.bz2
	$(download) http://geodynamics.org/~buildbot/deps/mpc-0.8.2.tar.gz
	$(download) http://geodynamics.org/~buildbot/deps/gmp-4.3.2.tar.gz
	$(doanload) http://geodynamics.org/~buildbot/deps/mpfr-2.4.2.tar.bz2
	tar -jxf gcc-4.5.2.tar.bz2
	cd gcc-4.5.2; \
		tar -zxf ../gmp-4.3.2.tar.gz; \
		ln -sf gmp-4.3.2/ gmp; \
		tar -zxf ../mpc-0.8.2.tar.gz; \
		ln -sf mpc-0.8.2/ mpc; \
		tar -jxf ../mpfr-2.4.2.tar.bz2; \
		ln -sf mpfr-2.4.2/ mpfr
	mkdir -p gcc-4.5.2-build
	cd gcc-4.5.2-build && \
		../gcc-4.5.2/configure --prefix=$(HOME)/install/$(BUILDBOT) \
			--enable-languages=c,c++,fortran && \
		make -j 4 && \
		make install

else
	@echo "Skipping gcc installation."
endif

# ----------------------------------------------------------------------
# python
# ----------------------------------------------------------------------
python:
if INSTALL_PYTHON

else
	@echo "Skipping Python installation."
endif

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
	@echo "Skipping MPI installation."
endif

# ----------------------------------------------------------------------
# openmpi
# ----------------------------------------------------------------------
openmpi:

# ----------------------------------------------------------------------
# mpich
# ----------------------------------------------------------------------
mpich:

# ----------------------------------------------------------------------
# cppunit
# ----------------------------------------------------------------------
cppunit:
if INSTALL_CPPUNIT

else
	@echo "Skipping CppUnit installation."
endif

# ----------------------------------------------------------------------
# swig
# ----------------------------------------------------------------------
swig:
if INSTALL_SWIG

else
	@echo "Skipping SWIG installation."
endif

# ----------------------------------------------------------------------
# numpy
# ----------------------------------------------------------------------
numpy:
if INSTALL_NUMPY

else
	@echo "Skipping Numpy installation."
endif

# ----------------------------------------------------------------------
# proj4
# ----------------------------------------------------------------------
proj4:
if INSTALL_PROJ4

else
	@echo "Skipping Proj4 installation."
endif

# ----------------------------------------------------------------------
# netcdf
# ----------------------------------------------------------------------
netcdf:
if INSTALL_NETCDF

else
	@echo "Skipping NetCDF installation."
endif

# ----------------------------------------------------------------------
# hdf5
# ----------------------------------------------------------------------
hdf5:
if INSTALL_HDF5

else
	@echo "Skipping HDF5 installation."
endif

# ----------------------------------------------------------------------
# petsc
# ----------------------------------------------------------------------
petsc:
if INSTALL_PETSC

else
	@echo "Skipping PETSc installation."
endif

# ----------------------------------------------------------------------
# spatialdata
# ----------------------------------------------------------------------
spatialdata:
if INSTALL_SPATIALDATA

else
	@echo "Skipping spatialdata installation."
endif

# ----------------------------------------------------------------------
# nemesis
# ----------------------------------------------------------------------
nemesis:
if INSTALL_NEMESIS

else
	@echo "Skipping nemesis installation."
endif

# ----------------------------------------------------------------------
# fiat
# ----------------------------------------------------------------------
fiat:
if INSTALL_FIAT

else
	@echo "Skipping FIAT installation."
endif


# ----------------------------------------------------------------------
# pylith
# ----------------------------------------------------------------------
pylith:


# End of file