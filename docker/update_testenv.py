#!/usr/bin/env python3
"""Update the docker images and containers for the test environment.

Run from the top-level source directory.
"""


import subprocess


ENVS = (
    ("debian:stable", "debian-stable"),
    ("debian:testing", "debian-testing"),
    ("ubuntu:18.04", "ubuntu-18.04"),
    ("ubuntu:20.04", "ubuntu-20.04"),
    ("ubuntu:21.04", "ubuntu-21.04"),
    ("fedora:33", "fedora-33"),
    ("fedora:34", "fedora-34"),
    ("centos:7", "centos-7"),
    ("centos:8", "centos-8"),
    )

TAG_TEMPLATE = "geodynamics/pylith-testenv-{env}"

def run_docker(cmd, verbose=True):
    """Run docker command.

    Args:
        cmd (str)
            Docker command to run.
        verbose (bool)
           Print command to stdout if True.
    """
    if verbose:
        print(f"docker {cmd}")
    subprocess.run(["docker"] + cmd.split(), check=True)


for base, dockerfile in ENVS:
    run_docker(f"pull {base}")

    tag = TAG_TEMPLATE.format(env=dockerfile)
    run_docker(f"build -t {tag} -f docker/{dockerfile} .")
