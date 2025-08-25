#!/usr/bin/env python3

from dataclasses import dataclass
import tarfile
import pathlib

import requests

GNU_TEMPLATE = "https://ftp.gnu.org/pub/gnu/{name}/{name}-{version}.tar.gz"
TAR_FILENAME = "pylith-dependencies-4.2.1-0.tar.gz"


@dataclass
class PackageInfo:
    """Package information"""

    name: str
    url: str
    version: str

    def tarball_filename(self):
        return f"{self.name}-{self.version}.tar.gz"


COMPILER_PACKAGES = (
    PackageInfo(
        name="gcc",
        version="14.2.0",
        url="https://ftp.gnu.org/pub/gnu/{name}/{name}-{version}/{name}-{version}.tar.gz",
    ),
    PackageInfo(name="mpc", version="1.3.1", url=GNU_TEMPLATE),
    PackageInfo(name="gmp", version="6.3.0", url=GNU_TEMPLATE),
    PackageInfo(name="mpfr", version="4.2.2", url=GNU_TEMPLATE),
)

PACKAGES = (
    PackageInfo(name="m4", version="1.4.20", url=GNU_TEMPLATE),
    PackageInfo(name="autoconf", version="2.72", url=GNU_TEMPLATE),
    PackageInfo(name="automake", version="1.17", url=GNU_TEMPLATE),
    PackageInfo(name="libtool", version="2.5.4", url=GNU_TEMPLATE),
    PackageInfo(
        name="mpich",
        version="4.2.3",
        url="https://www.mpich.org/static/downloads/{version}/{name}-{version}.tar.gz",
    ),
    PackageInfo(
        name="openmpi",
        version="5.0.7",
        url="https://download.open-mpi.org/release/open-mpi/v5.0/{name}-{version}.tar.gz",
    ),
    PackageInfo(
        name="openssl",
        version="3.4.1",
        url="https://github.com/openssl/openssl/releases/download/{name}-{version}/{name}-{version}.tar.gz",
    ),
    PackageInfo(
        name="libxcrypt",
        version="4.4.38",
        url="https://github.com/besser82/libxcrypt/releases/download/v{version}/{name}-{version}.tar.xz",
    ),
    PackageInfo(
        name="libffi",
        version="3.4.8",
        url="https://github.com/libffi/libffi/releases/download/v{version}/{name}-{version}.tar.gz",
    ),
    PackageInfo(
        name="curl",
        version="8.13.0",
        url="https://curl.se/download/{name}-{version}.tar.gz",
    ),
    PackageInfo(
        name="cmake",
        version="4.0.2",
        url="https://github.com/Kitware/CMake/releases/download/v{version}/{name}-{version}.tar.gz",
    ),
    PackageInfo(
        name="Python",
        version="3.12.10",
        url="https://www.python.org/ftp/python/{version}/{name}-{version}.tgz",
    ),
    PackageInfo(
        name="pcre2",
        version="10.45",
        url="https://github.com/PCRE2Project/pcre2/releases/download/{name}-{version}/{name}-{version}.tar.gz",
    ),
    PackageInfo(
        name="swig",
        version="4.3.1",
        url="https://sourceforge.net/projects/swig/files/swig/{name}-{version}/{name}-{version}.tar.gz/download",
    ),
    PackageInfo(
        name="Catch2",
        version="3.8.1",
        url="https://github.com/catchorg/{name}/archive/refs/tags/v{version}.tar.gz",
    ),
    PackageInfo(
        name="sqlite-autoconf",
        version="3490200",
        url="https://sqlite.org/2025/{name}-{version}.tar.gz",
    ),
    PackageInfo(
        name="tiff",
        version="4.7.0",
        url="https://download.osgeo.org/libtiff/{name}-{version}.tar.gz",
    ),
    PackageInfo(
        name="proj",
        version="9.6.0",
        url="https://download.osgeo.org/{name}/{name}-{version}.tar.gz",
    ),
    PackageInfo(
        name="hdf5",
        version="1.14.6",
        url="https://github.com/HDFGroup/hdf5/releases/download/{name}_{version}/{name}-{version}.tar.gz",
    ),
    PackageInfo(
        name="netcdf-c",
        version="4.9.3",
        url="https://downloads.unidata.ucar.edu/{name}/{version}/{name}-{version}.tar.gz",
    ),
)

failures = 0

for package in COMPILER_PACKAGES + PACKAGES:
    url = package.url.format(name=package.name, version=package.version)
    filename = package.tarball_filename()
    if pathlib.Path(filename).exists():
        print(f"{filename} already downloaded.")
        continue
    else:
        print(f"Fetching {url}...")

    MB = 2**20
    session = requests.Session()
    response = session.get(url, stream=True, allow_redirects=True)
    if response.status_code != requests.codes.OK:
        print(f"ERROR: Could not fetch {url}. {response.reason}")
        failures += 1
        continue
    with open(filename, "wb") as fout:
        for chunk in response.iter_content(chunk_size=4 * MB):
            fout.write(chunk)

if not failures:
    print(f"Creating tarball {TAR_FILENAME}")
    tfile = tarfile.open(TAR_FILENAME, mode="w:gz")
    for package in COMPILER_PACKAGES + PACKAGES:
        filename = package.tarball_filename()
        tfile.add(filename)
    tfile.close()
