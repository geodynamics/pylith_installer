# Sample Configurations

For most current Linux distributions the default Python version is 3.x.
PyLith v2.2.2 uses Python version 2.7, so we recommend having the PyLith installer build Python (default behavior); this will trigger the installer to build all of the Python modules PyLith needs as well.

:::{important}
All of these sample configurations assume you do not have alternative versions of the PyLith dependencies already installed.
The best way to avoid conflicts is to setup your environment so that PATH only points to operating system directorys and PYTHONPATH and LD_LIBRARY_PATH (Linux only) are not set.
:::

```{toctree}
clusters.md
ubuntu.md
centos.md
macos.md
```
