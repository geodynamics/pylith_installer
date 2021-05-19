(sec-developer-helper)=
# Developer-helper utility

The `developer_helper.py` Python script provides developers with a quick reference to commands related to managing the PyLith development environment created by the installer or with the PyLith Development Docker image.
The script shows the commands to run for configuring and building pythia, spatialdata, PETSc, and PyLith and Git commands for keeping the local clones in sync with the upstream repositories.

## Setup

The `developer_helper.py` script requires a configuration file to specify locations of the source, build, and install directories as well as which repositories to use.
The top-level source directory is where the source code for pythia, spatialdata, PETSc, and PyLith will be downloaded.
PETSc is built in a subdirectory within the source tree.
The top-level build directory will contain the builds for pythia, spatialdata, and PyLith.

```{code-block} ini
---
caption: Example configuration file for the `developer_helper.py` Python script.
---
# Basic information
[base]
# top-level source directory.
src_dir = /opt/pylith/src

# top-level build directory.
build_dir = /opt/pylith/build

# Install directory.
install_dir = /opt/pylith/dest

# Directory containing dependencies installed by the PyLith installer utility.
deps_dir = /opt/dependencies

# Build with debugging flags?
debug = True

# Number of make threads to use when compiling source code.
build_threads = 8

# For each software package, we specify the URL of the repository to clone and default branch to use.
# If the repository to clone is a fork, then we use `upstream` to specify the main repository.
# We assume only the PyLith repository is a fork.

[pythia]
repo_url = https://github.com/geodynamics/pythia.git
upstream = False
branch = main

[spatialdata]
repo_url = https://github.com/geodynamics/spatialdata.git
upstream = False
branch = main

[petsc]
repo_url = https://gitlab.com/petsc/petsc.git
upstream = False
branch = knepley/pylith

[pylith]
repo_url = https://github.com/GITHUB_USERNAME/pylith.git
upstream = https://github.com/geodynamics/pylith.git
branch = main
```

## Running `developer-helper.py`

The script will print commands to run in a terminal shell based on the specified configuration and command line arguments.

### Required command line arguments

* **`--config=FILENAME`** Get the configuration settings from file `FILENAME`.
* **`--package=PACKAGE`** Get help related to software package `PACKAGE`, where `PACKAGE` is one of `pythia`, `spatialdata`, `petsc`, and `pylith`.

### Optional command line arguments

The optional command line arguments correspond to tasks that the user wants to run.

* **`--git-clone`** How to clone (download) the repository.
* **`--git-set-upstream`** How to set the origin for a forked repository (where updates will come from and where pull requests should be made).
* **`--git-sync-fork`** Steps for updating the main branch in a fork with the current upstream repository.
* **`--git-set-branch`** How to set the current branch.
* **`--git-new-branch`** How to create a new branch from the current branch.
* **`--git-delete-branch`** How to delete a branch from the local clone.
* **`--git-fetch`** How to fetch from the repository while pruning deleted branches.
* **`--git-rebase`** Basic instructions for rebasing.
* **`--git-replace-branch`** How to replace a local branch after it has been force pushed from another clone.
* **`--configure`** How to run `configure` for the software package.
* **`--build`** Command to run to build the software package.
* **`--test`** Command to run to test the software package.
* **`show-config`** Show the configuration file.

### Order of commands for installing the software

The software packages should be installed in the following order:

1. pythia
2. spatialdata
3. PETSc
4. PyLith

When installing each package, the commands should be run in the following order:

1. `--git-clone`
2. `--configure`
3. `--build`
4. `--test`

The remaining commands are used to update the software.
