# Overview

PyLith depends on several other libraries, some of which depend on other libraries.
As a result, building PyLith from source can be tricky and is fraught with potential pitfalls.
This installer attempts to eliminate these obstacles by providing a utility that builds all of the dependencies in the proper order with the required options in addition to PyLith itself.

The installer will download the source code for PyLith and all of the dependencies during the install process, so you do not need to do this yourself.
Additionally, the installer provides the option of checking out the PyLith and PETSc source code from the Git repositories (requires git be installed); only use this option if you need the bleeding edge versions and are willing to rebuild frequently.

:::{tip}
If you encounter trouble during the installation, see the [Troubleshooting](../install/troubleshooting.md) section.

Consult the [CIG community forum](https://community.geodynamics.org/c/pylith/) for additional help.
:::

```{toctree}
---
maxdepth: 2
---
release-notes.md
requirements.md
use-cases.md
packages.md
```

