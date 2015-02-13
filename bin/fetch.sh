#~/bin/bash
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
# Copyright (c) 2010-2015 University of California, Davis
#
# See COPYING for license information.
#
# ----------------------------------------------------------------------

if [ $# != 3 ] ; then
    echo "usage: FETCH_PROGRAM FILE URL"
    exit -1
fi
fetch=$1
file=$2
url=$3

if [ ! -f $file ]; then
  if [ "$fetch" == "none" ]; then
    echo "No local copy of $file found and no downloader specified."
    exit -1
  else
    echo "Downloading $file from $url."
    $fetch $file $url/$file
  fi
else
    echo "Found local copy of $file."
fi 


# End of file
