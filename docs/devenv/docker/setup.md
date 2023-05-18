# Setup the container

You only need to run these setup steps once.

:::{admonition} Requirements
:class: important

1. You need to have [Docker](https://www.docker.com/products/docker-desktop) installed and running on your computer.
2. You need to have a [GitHub](https://github.com) account.
:::

## Fork repositories on GitHub

1. Log in to your [GitHub](https://github.com) account.

2. Fork the following repositories:

* <https://github.com/geodynamics/pythia> (optional, not recommended)
* <https://github.com/geodynamics/spatialdata> (optional, not recommended)
* <https://github.com/geodynamics/pylith>

This creates copies of the repositories in your GitHub account.

## Create Docker volume for persistent storage

On your local machine, create a Docker volume for persistent storage.

```{code-block} bash
docker volume create pylith-dev
```

## Start PyLith development Docker container

Running the command below will:

1. Start (run) the Docker container using the `pylith-devenv` Docker image and assign it the name `pylith-dev-workspace`.
2. Mount the docker volume with persistent storage at `/opt/pylith`. 
3. The `pylith-devenv` Docker image will be downloaded from the GitLab registry <registry.gitlab.com/cig-pylith/pylith_installer>.

```{code-block} bash
docker run --name pylith-dev-workspace --rm -it -v pylith-dev:/opt/pylith \
    registry.gitlab.com/cig-pylith/pylith_installer/pylith-devenv
```

:::{note}
The `pylith-devenv` Docker image is a multiple architecture image supporting both the `amd64` (Intel) and `arm64` (Apple M processor) architectures.
Docker will automatically download the portion of the image appropriate for your architecture.
In either case, the image uses the Linux Ubuntu 22.04 operating system.
:::

:::{warning}
Closing the `pylith-dev-workspace` Docker container interactive shell (terminal) will stop the container. Simply run the command again to restart the container.
:::

## Setup directory structure

We will use the following directory structure for the persistent storage.

```{code-block} bash
/opt/pylith
    ├── src
    │    ├── pythia
    │    ├── spatialdata
    │    ├── petsc
    │    └── pylith
    ├── build
    │   ├── pythia-debug
    │   ├── pythia-opt (optional)
    │   ├── spatialdata-debug
    │   ├── spatialdata-opt (optional)
    │   ├── pylith-debug
    │   └── pylith-opt (optional)
    ├── dest-debug
    │   ├── bin
    │   ├── include
    │   ├── lib
    │   └── share
    └── dest-opt (optional)
        ├── bin
        ├── include
        ├── lib
        └── share
```

All of the source code will be placed under `/opt/pylith/src`. You only need to create the top-level source directory as the subdirectories will be created when you clone (download) the repositories.

This directory structure is set up for both a debugging version for development (`*-debug` directories) and an optimized version for performance testing (`*-opt` directories).
For now, we will only setup the debugging version.

```{code-block} bash
cd ${DEV_DIR}
mkdir src
mkdir -p ${TOP_BUILDDIR} && pushd ${TOP_BUILDDIR} && mkdir pythia-debug spatialdata-debug pylith-debug && popd
mkdir -p ${INSTALL_DIR}
```

## Clone repositories

This creates a local copy of the repositories in the persistent storage volume of the PyLith development container.
These are your working copies of the repositories.

```{code-block} bash
cd ${TOP_SRCDIR}
git clone --recursive https://github.com/geodynamics/pythia.git
git clone --recursive https://github.com/geodynamics/spatialdata.git
git clone --recursive https://github.com/GITHUB_USERNAME/pylith.git
git clone --branch knepley/pylith https://gitlab.com/petsc/petsc.git
```

### Set the upstream repository

For the PyLith repository and any other repositories that you forked, you should set the upstream repository.
The upstream repository is the central, community repository from which you will get updates.
We also recommend **never** using the `main` branch in your fork; instead, set your local `main` branch to the `upstream/main` branch.
This simplifies keeper your local repository in sync with the community repository.

```{code-block} bash
# PyLith repository (repeat for other repositories you forked)
cd ${TOP_SRCDIR}/pylith
git remote add upstream https://github.com/geodynamics/pylith.git
git fetch upstream

# Checkout the `upstream` main branch
git checkout -b upstream/main --track upstream/main
# Remove the local `main` from your fork
git branch -D main
# Rename your `upstream/main` to `main`
git branch -m upstream/main main
```

## Setup Python virtual environment

We use a Python virtual environment, so that we can install Python modules using the Pip module.
The Docker container explicitly sets the environment variables to make use of this virtual environment, so you do not need to manually activate it.

```{code-block} bash
python3 -m venv ${PYLITH_DIR}
```

## Configure and build PyLith for development

We build 3 CIG-related dependencies and PyLith:

1. Pythia
2. Spatialdata
3. PETSc
4. PyLith

Pythia, Spatialdata, and PETSc are not include in the Docker image, because they need to be updated as part of PyLith development.

:::{tip}
To speed up the build process, we set the number of make threads to the number of cores `-j$(nproc)`.
You can often find speedup with up to twice as many threads as the number of cores.
:::

### Pythia

```{code-block} bash
cd ${TOP_BUILDDIR}/pythia-debug
pushd ${TOP_SRCDIR}/pythia && autoreconf -if && popd
${TOP_SRCDIR}/pythia/configure --prefix=${PYLITH_DIR} --enable-testing \
    CC=mpicc CXX=mpicxx CFLAGS="-g -Wall" CXXFLAGS="-g -Wall"
make install
make check
```

### Spatialdata

```{code-block} bash
cd ${TOP_BUILDDIR}/spatialdata-debug
pushd ${TOP_SRCDIR}/spatialdata && autoreconf -if && popd
${TOP_SRCDIR}/spatialdata/configure --prefix=${PYLITH_DIR} \
    --enable-swig --enable-testing \
	CPPFLAGS="-I${PYLITHDEPS_DIR}/include -I${PYLITH_DIR}/include" \
	LDFLAGS="-L${PYLITHDEPS_DIR}/lib -L${PYLITH_DIR}/lib --coverage" \
	CXX=mpicxx CXXFLAGS="-g -Wall --coverage"
make install -j$(nproc)
make check -j$(nproc)
```

### PETSc

```{code-block} bash
cd ${TOP_SRCDIR}/petsc
python3 ./configure --with-c2html=0 --with-lgrind=0 --with-fc=0 \
    --with-x=0 --with-clanguage=C --with-mpicompilers=1 \
    --with-shared-libraries=1 --with-64-bit-points=1 --with-large-file-io=1 \
    --with-hdf5=1 --download-chaco=1 --download-ml=1 \
    --download-f2cblaslapack=1 --with-debugging=1 CFLAGS="-g -O -Wall" \
    CPPFLAGS="-I${HDF5_INCDIR} -I${PYLITHDEPS_DIR}/include" \
    LDFLAGS="-L${HDF5_LIBDIR} -L${PYLITHDEPS_DIR}/lib"
make 
make check
```

### PyLith

```{code-block} bash
cd ${TOP_BUILDDIR}/pylith-debug
pushd ${TOP_SRCDIR}/pylith && autoreconf -if && popd
${TOP_SRCDIR}/pylith/configure --prefix=${PYLITH_DIR} \
    --enable-cubit --enable-hdf5 --enable-swig --enable-testing \
    --enable-test-coverage --with-python-coverage=coverage3 \
    CPPFLAGS="-I${HDF5_INCDIR} -I${PYLITHDEPS_DIR}/include -I${PYLITH_DIR}/include" \
    LDFLAGS="-L${HDF5_LIBDIR} -L${PYLITHDEPS_DIR}/lib -L${PYLITH_DIR}/lib --coverage" \
    CC=mpicc CFLAGS="-g -Wall" CXX=mpicxx CXXFLAGS="-g -Wall --coverage"
make install -j$(nproc)
make check -j$(nproc)
```

## Reset `ptrace` Flag

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

## Install Visual Studio Code

1. Install [Visual Studio Code](https://code.visualstudio.com/) for your computer.
2. Install the following extensions:
    * Dev Containers
    * C/C++
    * Docker
    * Live Share
    * Python
    * Uncrustify
    * Live Share
    * C++ TestMate
    * Test Explorer UI

We recommend also installing the following extensions:

* autoconf
* Code Spell Checker
* Markdown all in One
* markdownlint
* Material Icon Theme
* MyST-Markdown
* Remote-SSH
