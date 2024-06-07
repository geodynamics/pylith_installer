#!/usr/bin/env python3
"""Update the docker images and containers for the test environment.

Run from the top-level source directory.
"""

import sys

sys.path.append("./docker")

from builder import DockerApp


class UpdateApp():

    ENVS = (
        ("debian:stable", "debian-stable"),
        ("debian:testing", "debian-testing"),
        ("ubuntu:20.04", "ubuntu-20.04"),
        ("ubuntu:22.04", "ubuntu-22.04"),
        ("ubuntu:24.04", "ubuntu-24.04"),
        ("fedora:38", "fedora-38"),
        ("fedora:39", "fedora-39"),
        ("centos:7", "centos-7"),
        ("rockylinux:8", "rockylinux-8"),
        ("rockylinux:9", "rockylinux-9"),
    )

    def update_images(self):
        import subprocess

        for base, _ in self.ENVS:
            print(f"Updating {base}...")
            subprocess.run(["docker", "pull", base], check=True)

    def build(self, build_env):
        for base, docker_file in self.ENVS:
            print(f"Building {base}...")
            app = DockerApp(f"docker/{docker_file}")
            app.build(build_env)
    

def cli():
    """Parse command line arguments.
    """
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--update-images", action="store_true", dest="update_images")
    parser.add_argument("--build", action="store_true", dest="build")
    parser.add_argument("--build-env", action="store", dest="build_env", default="certs-doi", choices=(None,"nocerts","certs-doi"))
    
    args = parser.parse_args()
    app = UpdateApp()
    if args.update_images:
        app.update_images()
    if args.build:
        app.build(args.build_env)


# =================================================================================================
if __name__ == "__main__":
    cli()
