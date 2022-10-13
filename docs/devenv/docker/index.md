# PyLith development environment Docker image

The `pylith-devenv` Docker image provides all of the dependencies and defines the environment for PyLith development.
It is built using the Ubuntu 20.04 Linux distribution.
It is intended to be read only with a separate Docker volume for persistent storage of the PyLith development workspace.
We separate the development "environment" from the "workspace" so that we can update the development environment without affecting the workspace and easily maintain a persistent workspace while starting and stopping the Docker container that holds the development environment.

In addition to the PyLith dependencies, the Docker image includes the following development tools:

* gdb (debugger)
* valgrind (memory debugging tool)
* lcov (code coverage)
* uncrustify (C++ code formatter)
* autopep8 (Python code formatter)
* matplotlib (Python plotting) [TODO]
* Sphinx with MyST (documentation tools) [TODO]

The Docker image also defines the environment:

| Environment variable |                 Value                 | Decription                                              |
| :------------------- | :-----------------------------------: | :------------------------------------------------------ |
| `PYTHON_VERSION`     |                 `3.8`                 | Python version                                          |
| `PYLITH_USER`        |             `pylith-dev`              | Username within container                               |
| `BASE_DIR`           |             `/opt/pylith`             | Top-level directory for development workspace           |
| `HOME`               |        `/home/${PYLITH_USER}`         | Home directory for user                                 |
| `INSTALL_DIR`        |       `${BASE_DIR}/dest-debug`        | Directory where code is installed                       |
| `TOPSRC_DIR`         |           `${BASE_DIR}/src`           | Top-level directory for source code                     |
| `TOPBUILD_DIR`       |       `${BASE_DIR}/build-debug`       | Top-level directory for building                        |
| `PETSC_DIR`          |         `${TOPSRC_DIR}/petsc`         | Directory for PETSc                                     |
| `PETSC_ARCH`         |          `arch-pylith-debug`          | Build label for PETSc debugging configuration           |
| `PYLITH_BUILDDIR`    |       `${TOPBUILD_DIR}/pylith`        | Top-level directory where we build PyLith [^vscode]     |
| `PYLITH_DIR`        |           `${INSTALL_DIR}`            | Directory containing CIG-related dependencies [^vscode] |
| `PYLITHDEPS_DIR`        |           `/opt/dependencies`            | Directory containing external dependencies [^vscode] |
| `PYTHON_INCDIR`      |       `/usr/include/python3.8`        | Directory containing Python header files [^vscode]      |
| `MPI_INCDIR`         | `/usr/include/x86_64-linux-gnu/mpich` | Directory containing MPI header files [^vscode]         |
| `PROJ_INCDIR`        |            `/usr/include`             | Directory containing Proj header files [^vscode]        |
| `CPPUNIT_INCDIR`     |            `/usr/include`             | Directory containing CppUnit header files [^vscode]     |

[^vscode]: Environment variables used in Visual Studio Code workspace settings.

:::{toctree}
---
maxdepth: 1
---
setup.md
run.md
update.md
:::
