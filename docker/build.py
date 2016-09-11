#!/usr/bin/env python
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
# Copyright (c) 2010-2016 University of California, Davis
#
# See COPYING for license information.
#
# ----------------------------------------------------------------------
#
# Create PyLith binary package.
#
# Run from the top-level PyLith build dir.
#
# Usage: make_package.py

PYLITH_VER=2.1.3x
ARCH=ubuntu
ARCH_VER=16.04
ENV_VER=1

BUILDENV_VER=$(PYLITH_VER)-$(ARCH)-$(ARCH_VER)-$(ENV_VER)
BINARY_VER=$(PYLITH_VER

buildenv-build: $(ARCH)-buildenv
	docker build -f $< -t geodynamics/pylith-buildenv:$(BUILDENV_VER) .

buildenv-irun: $(ARCH)-buildenv
	docker run -t -i geodynamics/pylith-buildenv:$(BUILDENV_VER)

buildenv-push: $(ARCH)-buildenv
	docker push geodynamics/pylith-buildenv:$(BUILDENV_VER)

binary-build: $(ARCH)-binary
	docker build -f $< -t geodynamics/pylith:$(BINARY_VER) .

binary-irun: $(ARCH)-binary
	docker run -t -i geodynamics/pylith:$(BINARY_VER) .

binary-push: $(ARCH)-binary
	docker push geodynamics/pylith:$(BINARY_VER) .


# End of file
