# PyLith development environment using Docker

## What is Docker?

From https://www.docker.com/what-docker:

> "Docker containers wrap a piece of software in a complete filesystem that contains everything needed to run: code, runtime, system tools, system libraries – anything that can be installed on a server.
> This guarantees that the software will always run the same, regardless of its environment.
>
> LIGHTWEIGHT
>
> Containers running on a single machine share the same operating system kernel; they start instantly and use less RAM.
> Images are constructed from layered filesystems and share common files, making disk usage and image downloads much more efficient."

# PyLith development Docker image

The `pylith-devenv` Docker image provides all of the dependencies and defines the environment for PyLith development.
It is built using the Ubuntu 22.04 Linux distribution.
It is intended to be read only with a separate Docker volume for persistent storage of the PyLith development workspace.
We separate the development "environment" from the "workspace" so that we can update the development environment without affecting the workspace and easily maintain a persistent workspace while starting and stopping the Docker container that holds the development environment.

In addition to the PyLith dependencies, the Docker image includes the following development tools:

* gdb (debugger)
* valgrind (memory debugging tool)
* lcov (code coverage)
* uncrustify (C++ code formatter)
* autopep8 (Python code formatter)
* Sphinx with MyST (documentation tools)
* matplotlib (Python plotting)
* gmsh (Mesh generation; not available for arm64)

:::{important}
Docker images use the Linux operating system, and most Python packages that require platform specific libraries are built only for the x86_64 architecture (Intel processors).
Consequently, we cannot provide Gmsh within the Docker container for the arm64 architecture.
You will need to run Gmsh _outside_ the container or use the amd64 (x86_64) container (runs in emulation mode and is significantly slower).
Alternatively, you can use the installer utility; this will allow you to install Python packages using the macOS arm64 architecture.
Similarly, matplotlib cannot be used interactively within the Docker container, because the libraries for the interactive matplotlib backends are not available.
:::

The Docker image also defines the environment:

| Environment variable |                 Value                 | Decription                                              |
| :------------------- | :-----------------------------------: | :------------------------------------------------------ |
| `PYTHON_VERSION`     |                 `3.10`                | Python version                                          |
| `PYLITH_USER`        |             `pylith-dev`              | Username within container                               |
| `DEV_DIR`            |             `/opt/pylith`             | Top-level directory for development workspace           |
| `HOME`               |        `/home/${PYLITH_USER}`         | Home directory for user                                 |
| `ARCH_LIBPATH`       |  `x86_64-linux-gnu` or `aarch64-linux-gnu` | Architecture dependent path                        |
| `INSTALL_DIR`        |       `${DEV_DIR}/dest-debug`         | Directory where code is installed                       |
| `TOP_SRCDIR`         |           `${DEV_DIR}/src`            | Top-level directory for source code                     |
| `TOP_BUILDDIR`       |       `${DEV_DIR}/build`              | Top-level directory for building                        |
| `PETSC_DIR`          |         `${TOPSRC_DIR}/petsc`         | Directory for PETSc                                     |
| `PETSC_ARCH`         |          `arch-pylith-debug`          | Build label for PETSc debugging configuration           |
| `PYLITH_BUILDDIR`    |       `${TOPBUILD_DIR}/pylith-debug`  | Top-level directory where we build PyLith [^vscode]     |
| `PYLITH_DIR`         |           `${INSTALL_DIR}`            | Directory containing CIG-related dependencies [^vscode] |
| `PYLITHDEPS_DIR`     |           `/opt/dependencies`         | Directory containing external dependencies [^vscode]    |
| `PYTHON_INCDIR`      |       `/usr/include/python3.10`       | Directory containing Python header files [^vscode]      |
| `MPI_INCDIR`         | `/usr/include/${ARCH_LIBPATH}/mpich`  | Directory containing MPI header files [^vscode]         |
| `PROJ_INCDIR`        |            `/usr/include`             | Directory containing Proj header files [^vscode]        |
| `CATCH_INCDIR`       |            `/usr/include`             | Directory containing Catch2 header files [^vscode]      |

[^vscode]: Environment variables used in Visual Studio Code workspace settings.

:::{toctree}
---
maxdepth: 1
---
setup.md
run.md
update.md
gmsh.md
quickref.md
:::
