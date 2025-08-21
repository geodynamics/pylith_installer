#!/usr/bin/env python3

import ssl
import certifi
import pathlib
import shutil

openssl_cafile = ssl.get_default_verify_paths().openssl_cafile
certifi_cafile = certifi.where()

# Remove `openssl_cafile`
openssl_filepath = pathlib.Path(openssl_cafile)
openssl_filepath.unlink(missing_ok=True)
openssl_filepath.parent.mkdir(parents=True, exist_ok=True)

# Copy `certifi_cafile` to `openssl_cafile`
shutil.copyfile(certifi_cafile, openssl_cafile)
