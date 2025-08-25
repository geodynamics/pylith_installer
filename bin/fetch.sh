#!/bin/bash
# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://geodynamics.org).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information. 
# =================================================================================================

if [ $# != 3 ] ; then
    echo "usage: CURL FILE URL"
    exit -1
fi
fetch=$1
file=$2
url=$3

if [ ! -f $file ]; then
  if [ "$fetch" == "none" ]; then
    echo "No local copy of $file found and no path to curl executable specified."
    exit -1
  else
    echo "Downloading $file from $url."
    curl -L -O $url/$file
  fi
else
    echo "Found local copy of $file."
fi 


# End of file
