#!/usr/bin/env python3
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
# Copyright (c) 2010-2023 University of California, Davis
#
# See COPYING for license information.
#
# ----------------------------------------------------------------------

"""Application for building and pushing docker images.
"""

import os
import argparse
import subprocess
import pathlib

class DockerApp(object):
    """Application for building and pushing docker images.
    """

    def __init__(self, docker_file, registry="ghcr.io/geodynamics/pylith_installer", prefix="testenv"):
        self.docker_filename = docker_file
        self.registry = registry

        self.tag = self._get_tag(docker_file, registry, prefix)

    def build(self, build_env="certs-doi"):
        """Build image.
        """
        if build_env:
            cmd = f"docker build -t {self.tag} -f {self.docker_filename} --build-arg BUILD_ENV={build_env} ."
        else:
            cmd = f"docker build -t {self.tag} -f {self.docker_filename} ."
        self._run_cmd(cmd)

    def push(self):
        """Push docker image to registry.
        """
        cmd = f"docker push {self.tag}"
        self._run_cmd(cmd)

    def _get_tag(self, docker_file, registry, prefix):
        """Get image tag.
        """
        image = pathlib.Path(docker_file).name
        if prefix:
            tag = f"{registry}/{prefix}-{image}"
        else:
            tag = f"{registry}/{image}"
        return tag

    @staticmethod
    def _run_cmd(cmd):
        """Run shell command.
        """
        print("Running '%s'..." % cmd)
        subprocess.check_call(cmd.split())
        return


def cli():
    """Parse command line arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--dockerfile", action="store", dest="docker_file", required=True)
    parser.add_argument("--registry", action="store", dest="registry", default="ghcr.io/geodynamics/pylith_installer")
    parser.add_argument("--prefix", action="store", dest="prefix", default="testenv")
    parser.add_argument("--build", action="store_true", dest="build")
    parser.add_argument("--push", action="store_true", dest="push")
    parser.add_argument("--build-env", action="store", dest="build_env", default=None, choices=(None,"nocerts","certs-doi"))

    args = parser.parse_args()

    app = DockerApp(args.docker_file, args.registry, args.prefix)
    if args.build:
        app.build(args.build_env)
    if args.push:
        app.push()


# =================================================================================================
if __name__ == "__main__":
    cli()


# End of file
