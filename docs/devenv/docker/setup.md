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
    │   ├── debug
    │   │   ├── pythia
    │   │   ├── spatialdata
    │   │   └── pylith
    │   └── opt
    │       ├── pythia
    │       ├── spatialdata
    │       └── pylith
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

All of the source code will be placed under `/opt/pylith/src`. You only need to create the top-level source directory as the subdirectories will be created when you clone (download) the repositories.

This directory structure is set up for both a debugging version for development (debug directory) and an optimized version for performance testing (opt directory).
For now, we will only setup the debugging version.

```{code-block} bash
cd /opt/pylith
mkdir src
mkdir -p ${TOPBUILD_DIR} && pushd ${TOPBUILD_DIR} && mkdir pythia spatialdata pylith && popd
mkdir -p ${INSTALL_DIR}
```

## Clone repositories

This creates a local copy of the repositories in the persistent storage volume of the PyLith development container.
These are your working copies of the repositories.

:::{tip}
Starting at this step, you can use the `developer-helper.py` Python script (see {ref}`sec-developer-helper`) to show the exact commands to run.
This script and the default configuration file are in the `/opt/pylith-devenv` directory.
:::

```{code-block} bash
cd /opt/pylith/src
git clone --recursive https://github.com/geodynamics/pythia.git
git clone --recursive https://github.com/geodynamics/spatialdata.git
git clone --recursive https://github.com/GITHUB_USERNAME/pylith.git
git clone --branch knepley/pylith https://gitlab.com/petsc/petsc.git
```

### Set the upstream repository

For the PyLith repository and any other repositories that you forked, you should set the upstream repository.
The upstream repository is the central, community repository from which you will get updates.

```{code-block} bash
# PyLith repository (repeat for other repositories you forked)
cd /opt/pylith/src/pylith
git remote add upstream https://github.com/geodynamics/pylith.git
```

(sec-developer-fork-fix-m4-url)=
### Fixing path to m4 submodule

For any of the repositories that you forked, you will encounter an error when it tries to clone the `m4` submodule, which has a relative link.
The error message will be similar to:

```{code-block} bash
Cloning into '/opt/pylith/src/pylith/m4'...
remote: Repository not found.
fatal: repository 'https://github.com/GITHUB_USERNAME/autoconf_cig.git/' not found
fatal: clone of 'https://github.com/GITHUB_USERNAME/autoconf_cig.git' into submodule path '/opt/pylith/src/pylith/m4' failed
Failed to clone 'm4'. Retry scheduled
```

The best workaround is to redirect your local clone to the geodynamics repository.
You only need to do this once after cloning.

```{code-block} bash
# Set URLs for submodules in `.git/config` to geodynamics repository (PyLith repository).
cd /opt/pylith/src/pylith
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

Pythia, Spatialdata, and PETSc are not include in the Docker image, because they may need to be updated as part of PyLith development.

:::{tip}
To speed up the build process, we set the number of make threads to the number of cores `-j$(nproc)`.
You can often find speedup with up to twice as many threads as the number of cores.
:::

### Pythia

```{code-block} bash
cd ${TOPBUILD_DIR}/pythia
pushd ${TOPSRC_DIR}/pythia && autoreconf -if && popd
${TOPSRC_DIR}/pythia/configure --prefix=${PYLITH_DIR} --enable-testing \
    CC=mpicc CXX=mpicxx CFLAGS="-g -Wall" CXXFLAGS="-g -Wall"
make install
make check
```

### Spatialdata

```{code-block} bash
cd ${TOPBUILD_DIR}/spatialdata
pushd ${TOPSRC_DIR}/spatialdata && autoreconf -if && popd
${TOPSRC_DIR}/spatialdata/configure --prefix=${PYLITH_DIR} \
    --enable-swig --enable-testing --enable-test-coverage \
    --with-python-coverage=coverage3 \
	CPPFLAGS="-I${PYLITHDEPS_DIR}/include -I${PYLITH_DIR}/include" \
	LDFLAGS="-L${PYLITHDEPS_DIR}/lib -L${PYLITH_DIR}/lib --coverage" \
	CXX=mpicxx CXXFLAGS="-g -Wall --coverage"
make install -j$(nproc)
make check -j$(nproc)
```

### PETSc

```{code-block} bash
cd ${TOPSRC_DIR}/petsc
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
