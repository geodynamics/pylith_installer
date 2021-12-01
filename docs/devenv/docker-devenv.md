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
| `PYTHON_VERSION`     |                 `2.7`                 | Python version                                          |
| `PYLITH_USER`        |             `pylith-dev`              | Username within container                               |
| `BASE_DIR`           |             `/opt/pylith`             | Top-level directory for development workspace           |
| `HOME`               |        `/home/${PYLITH_USER}`         | Home directory for user                                 |
| `INSTALL_DIR`        |       `${BASE_DIR}/dest/debug`        | Directory where code is installed                       |
| `TOPSRC_DIR`         |           `${BASE_DIR}/src`           | Top-level directory for source code                     |
| `TOPBUILD_DIR`       |       `${BASE_DIR}/build/debug`       | Top-level directory for building                        |
| `PYLITH_BUILDDIR`    |       `${TOPBUILD_DIR}/pylith`        | Top-level directory where we build PyLith [^vscode]     |
| `PYLITH_DIR`        |           `${INSTALL_DIR}`            | Directory containing CIG-related dependencies [^vscode] |
| `PYLITHDEPS_DIR`        |           `/opt/dependencies`            | Directory containing external dependencies [^vscode] |
| `PYTHON_INCDIR`      |       `/usr/include/python3.8`        | Directory containing Python header files [^vscode]      |
| `MPI_INCDIR`         | `/usr/include/x86_64-linux-gnu/mpich` | Directory containing MPI header files [^vscode]         |
| `PROJ_INCDIR`        |            `/usr/include`             | Directory containing Proj header files [^vscode]        |
| `CPPUNIT_INCDIR`     |            `/usr/include`             | Directory containing CppUnit header files [^vscode]     |

[^vscode]: Environment variables used in Visual Studio Code workspace settings.

## Setup

You only need to run these setup steps once.

:::{admonition} Requirements
:class: important

1. You need to have [Docker](https://www.docker.com/products/docker-desktop) installed and running on your computer.
2. You need to have a [GitHub](https://github.com) account.
:::

### Fork repositories on GitHub

1. Log in to your [GitHub](https://github.com) account.

2. Fork the PyLith repository <https://github.com/geodynamics/pylith>.

This creates copies of the repositories in your GitHub account.

### Create Docker volume for persistent storage

On your local machine, create a Docker volume for persistent storage.

```{code-block} bash
docker volume create pylith-dev
```

### Start PyLith development Docker container

Running the command below will:

1. Start (run) the Docker container using the `pylith-devenv` Docker image and assign it the name `pylith-dev-workspace`.
2. Mount the docker volume with persistent storage at `/opt/pylith`. 
3. The `pylith-devenv` Docker image will be downloaded from the GitLab registry <registry.gitlab.com/cig-pylith/pylith_installer>.

```{code-block} bash
docker run --name pylith-dev-workspace --rm -it -v pylith-dev:/opt/pylith \
    registry.gitlab.com/cig-pylith/pylith_installer/pylith-devenv
```

:::{warning}
Closing the `pylith-dev-workspace` Docker container interactive shell (terminal) will stop the container. Simply run the command again to restart the container.
:::

### Setup directory structure

We will use the following directory structure for the persistent storage.

```{code-block} bash
/opt/pylith
    ├── src
    ├── build
    │   ├── debug
    │   └── opt
    └── dest
        ├── debug
        │   ├── bin
        │   ├── include
        │   ├── lib
        │   └── share
        └── opt
            ├── bin
            ├── include
            ├── lib
            └── share
```

We place the PyLith source code in `/opt/pylith/src`. You should not crate this directory as it will be created when you clone (download) the repository.

This directory structure is set up for both a debugging version for development (debug directory) and an optimized version for performance testing (opt directory).
For now, we will only setup the debugging version.

```{code-block} bash
cd /opt/pylith
mkdir -p ${TOPBUILD_DIR} && pushd ${TOPBUILD_DIR} && popd
mkdir -p ${INSTALL_DIR}
```

### Clone PyLith repository

This creates a local copy of the repository in the persistent storage volume of the PyLith development container.
These are your working copies of the repositories.

```{code-block} bash
cd /opt/pylith
git clone --recursive https://github.com/GITHUB_USERNAME/pylith.git
```

#### Set the upstream repository

The upstream repository is the central, community repository from which you will get updates.

```{code-block} bash
# PyLith repository (repeat for other repositories you forked)
cd /opt/pylith/src
git remote add upstream https://github.com/geodynamics/pylith.git
```

(sec-developer-fork-fix-m4-url)=
#### Fixing path to m4 submodule

For any of the repositories that you forked, you will encounter an error when it tries to clone the `m4` submodule, which has a relative link.
The error message will be similar to:

```{code-block} bash
Cloning into '/opt/pylith/src/m4'...
remote: Repository not found.
fatal: repository 'https://github.com/GITHUB_USERNAME/autoconf_cig.git/' not found
fatal: clone of 'https://github.com/GITHUB_USERNAME/autoconf_cig.git' into submodule path '/opt/pylith/src/pylith/m4' failed
Failed to clone 'm4'. Retry scheduled
```

The best workaround is to redirect your local clone to the geodynamics repository.
You only need to do this once after cloning.

```{code-block} bash
# Set URLs for submodules in `.git/config` to geodynamics repository (PyLith repository).
cd /opt/pylith/src
git config submodule.m4.url https://github.com/geodynamics/autoconf_cig.git
git config submodule.templates/friction/m4.url https://github.com/geodynamics/autoconf_cig.git
git config submodule.templates/materials/m4.url https://github.com/geodynamics/autoconf_cig.git

# Update submodules
git submodule update
```

:::{note}
We use a relative link so that the GitLab mirror works correctly.
The consequence of using a relative link is that your local clone will look for a corresponding fork of the `autoconf_cig` repository.
:::

### Configure and build PyLith for development

```{code-block} bash
cd ${TOPBUILD_DIR}/pylith
pushd ${TOPSRC_DIR}/pylith && autoreconf -if && popd
${TOPSRC_DIR}/pylith/configure --prefix=${PYLITH_DIR} \
    --enable-cubit --enable-hdf5 --enable-swig --enable-testing \
    --enable-test-coverage --with-python-coverage=coverage3 \
    CPPFLAGS="-I${HDF5_INCDIR} -I${PYLITHDEPS_DIR}/include -I${PYLITH_DIR}/include" \
    LDFLAGS="-L${HDF5_LIBDIR} -L${PYLITHDEPS_DIR}/lib -L${PYLITH_DIR}/lib --coverage" \
    CC=mpicc CFLAGS="-g -Wall" CXX=mpicxx CXXFLAGS="-g -Wall --coverage"
make install -j$(nproc)
make check -j$(nproc)
```

### Reset `ptrace` Flag

Attaching the debugger to a forked process can result in the following error:

```{code-block}
Could not attach to process. If your uid matches the uid of the target process, check the setting of /proc/sys/kernel/yama/ptrace_scope, or try again as the root user. For more details, see /etc/sysctl.d/10-ptrace.conf
ptrace: Operation not permitted.
```

The PyLith development environment Docker container sets up `/etc/sysctl.d/10-ptrace.conf` correctly, but the `ptrace_scope` variable is still usually `1`.
The fix is to run the container in privileged mode as root and restart the `procps` service.

```{code-block} bash
# Run docker image in privileged mode as root.
docker run -ti --privileged --rm -u root registry.gitlab.com/cig-pylith/pylith_installer/pylith-devenv /bin/bash

# Verify ptrace setting needs updating
cat /proc/sys/kernel/yama/ptrace_scope
# If output is 1, then continue, if 0 then no need to change anything.

# Verify ptrace setting is correct.
cat /etc/sysctl.d/10-ptrace.conf
# Output should be 0

# Restart the procps service.
service procps restart

# Verify ptrace setting has changed
cat /proc/sys/kernel/yama/ptrace_scope
# Output should be 0
```

### Install Visual Studio Code

1. Install [Visual Studio Code](https://code.visualstudio.com/) for your computer.
2. Install the following extensions:
    * Remote - Containers
    * C/C++ 
    * Docker
    * Live Share
    * Python
    * Uncrustify
    * Live Share

We recommend also installing the following extensions:

* GitHub Pull Requests and Issues
* GitLens -- Git supercharged
* Material Icon Theme
* autoconf
* Code Spell Checker
* Markdown all in One
* markdownlint
* MyST-Markdown
* Remote-SSH


## Running

### Start PyLith development Docker container

Whenever you need to restart the `pylith-dev-workspace` Docker container, simply run

```{code-block} bash
docker run --name pylith-dev-workspace --rm -it -v pylith-dev:/opt/pylith \
    registry.gitlab.com/cig-pylith/pylith_installer/pylith-devenv:2.2.2-2
```

:::{tip}
Make sure Docker is running before you start the container.
:::

### Attach VS Code to Docker container

1. Start VS Code.
2. Click on the Docker extension in the Activity Bar on the far left hand side as illustrated in the [screenshot](docker-attach-vscode).
3. Find the `pylith-dev-workspace` container. Verify that it is running.
4. Right-click on the container and select `Attach Visual Studio Code`. This will open a new window. You should see `Container registry.gitlab.com/cig-pylith...` at the left side of the status bar at the bottom of the window.

:::{figure-md} docker-attach-vscode
:class: myclass

<img src="figs/docker-attach-vscode.png" alt="Screenshot" class="bg-primary mb-1">

Screenshot showing how to attach VS Code to a running Docker container. 
:::
