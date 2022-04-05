#!/usr/bin/env python3
"""Update the docker images and containers for the test environment.

Run from the top-level source directory.
"""

import subprocess
import sys

sys.path.append("./docker")

from builder import DockerApp


ENVS = (
    ("debian:stable", "debian-stable"),
    ("debian:testing", "debian-testing"),
    ("ubuntu:18.04", "ubuntu-18.04"),
    ("ubuntu:20.04", "ubuntu-20.04"),
    ("ubuntu:21.10", "ubuntu-21.10"),
    ("ubuntu:22.04", "ubuntu-22.04"),
    ("fedora:34", "fedora-34"),
    ("fedora:35", "fedora-35"),
    ("fedora:36", "fedora-36"),
    ("centos:7", "centos-7"),
    ("rockylinux:8", "rockylinux-8"),
    )

app = DockerApp()
args = {
    "prefix": "registry.gitlab.com/cig-pylith/pylith_installer/testenv",
    "dockerfile": None,
    "build": True,
    "push": False,
    "build_env": "certs-doi",
    }
for base, dockerfile in ENVS:
    print(f"Updating {base}...")
    subprocess.run(["docker", "pull", base], check=True)
    args["dockerfile"] = f"docker/{dockerfile}"
    app.main(**args)
    
