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

"""Application for building and pushing docker images.
"""

import os
import argparse
import subprocess

class DockerApp(object):
    """Application for building and pushing docker images.
    """

    def __init__(self):
        self.docker_filename = None
        self.tag = None

    def main(self, **kwargs):
        """Main entry point
        """
        args = argparse.Namespace(**kwargs) if kwargs else self._parse_command_line()
        self.initialize(args)

        if args.build:
            self.build()

        if args.push:
            self.push()

    def initialize(self, args):
        """Initialize builder.
        """
        self.docker_filename = args.dockerfile
        self.tag = "-".join([args.prefix, os.path.split(args.dockerfile)[-1]])
        return

    def build(self):
        """Build docker image.
        """
        cmd = "docker build -t {tag} -f {dockerfile} .".format(tag=self.tag, dockerfile=self.docker_filename)
        self._run_cmd(cmd)

    def push(self):
        """Push docker image to Docker Hub.
        """
        cmd = "docker push {tag}".format(tag=self.tag)
        self._run_cmd(cmd)
        return

    @staticmethod
    def _parse_command_line():
        """Parse command line arguments.
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("--dockerfile", action="store", dest="dockerfile", required=True)
        parser.add_argument("--prefix", action="store", dest="prefix", default="registry.gitlab.com/cig-pylith/pylith_installer/testenv")
        parser.add_argument("--build", action="store_true", dest="build")
        parser.add_argument("--push", action="store_true", dest="push")
        return parser.parse_args()

    @staticmethod
    def _run_cmd(cmd):
        """Run shell command.
        """
        print("Running '%s'..." % cmd)
        subprocess.check_call(cmd.split())
        return


# ======================================================================
if __name__ == "__main__":
    DockerApp().main()


# End of file
