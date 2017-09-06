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
# Copyright (c) 2010-2017 University of California, Davis
#
# See COPYING for license information.
#
# ----------------------------------------------------------------------
#
# Create docker images.

class DockerApp(object):

    def __init__(self, container):
        arch = "debian"
        pylithVersion = "2.2.1"
        buildVersion = "latest"

        baseenvTag = buildVersion
        binaryTag = "v[pver]-[btag]".replace("[pver]", pylithVersion).replace("[btag]", baseenvTag)
        self.container = container

        if container == "baseenv":
            self.config = arch + "-userenv"
            self.repo = "geodynamics/pylith-baseenv:" + baseenvTag
        elif container == "binary":
            self.config = arch + "-install"
            self.repo = "geodynamics/pylith:" + binaryTag
        elif container == "data":
            self.config = arch + "-data"
            self.repo = "geodynamics/pylith-data:" + baseenvTag
        return


    def build(self):
        cmd = "docker build -f %s -t %s ." % (self.config, self.repo)
        self._runCmd(cmd)
        return


    def run(self):
        cmd = "docker run -t -i %s /bin/bash" % self.repo
        self._runCmd(cmd)
        return


    def push(self):
        cmd = "docker push %s" % self.repo
        self._runCmd(cmd)
        return


    def _runCmd(self, cmd):
        print("Running '%s'..." % cmd)
        import subprocess
        subprocess.check_call(cmd.split())
        return

    
# ======================================================================
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--container", action="store", dest="container", choices=("baseenv","data","binary"), required=True)
    parser.add_argument("--build", action="store_true", dest="build")
    parser.add_argument("--run", action="store_true", dest="run")
    parser.add_argument("--push", action="store_true", dest="push")
    args = parser.parse_args()

    app = DockerApp(args.container)

    if args.build:
        app.build()

    if args.run:
        app.run()

    if args.push:
        app.push()
        
    
# End of file
