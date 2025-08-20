# 1. Download the installer

## Download the installer from the CIG website

  <https://geodynamics.org/resources/pylith>

  We assume the tarball `pylith-installer-4.2.1-0.tgz` is downloaded to `$HOME/Downloads`. We will place the installer source code in the directory `$HOME/src/pylith`.

## Unpack the installer source code:

```bash
mkdir -p $HOME/src/pylith
cd $HOME/src/pylith
mv $HOME/Downloads/pylith-installer-4.2.1-0.tgz $HOME/src/pylith/
tar -xf pylith-installer-4.2.1-0.tgz
```
