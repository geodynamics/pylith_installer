# Overview of the installation process

The installer has two basic components: a `configure` script and a `Makefile`.
The `configure` script is used to select which dependencies to install, verify that any dependencies not selected are available, and create a shell script containing the appropriate environment variables to build and use PyLith.
The `Makefile` is used to download all of the source code, build it in the proper order, and install it to the desired location.
The following sections describe the default configuration and various common perturbations.

As part of the installation process, the installer will, by default, run some tests to make sure specific dependencies as well as PyLith were installed properly.

## Recommended directory structure

* `$HOME/src/pylith`: Directory where you will place and unpack the PyLith Installer tarball. This will contain the source code for the installer.
* `$HOME/build/pylith`: Directory where you will run `configure` script and the installer will build the software. The source code for all of the software downloaded by the installer will be placed in this directory.
* `$HOME/pylith`: Directory where PyLith and its dependencies will be installed.

:::{danger} We *STRONGLY* recommend that you run the configure script in a different directory from the PyLith Installer source code. This makes it easier to restart if you adjust your configuration.
:::

:::{danger}
We also *STRONGLY* recommend that you install PyLith and its dependencies to its own directory. This makes it easier to
start over should you encounter an error, in addition to managing multiple versions or different builds.
:::

:::{important}
If you need to rerun the `configure` script, then you should remove all of your build and install files *BEFORE* running configure. For example, `rm -fr $HOME/build/pylith $HOME/pylith`.
:::

These instructions are written assuming that you have downloaded the installer source code to `$HOME/Downloads` and use the directory structure described above.
If you choose to use different directories, then you will need to adjust the commands listed in the instructions to account for this change.

## Keeping track of the build process

The installer attempts to keep track of packages that it has installed by creating files with the syntax `installed_PACKAGE` where `PACKAGE` is mpi, netcdf, etc.
This permits you to stop the build process at any time and return at a later time and pick up from where you left off.
You can trigger a package to be rebuilt by removing the corresponding `PACKAGE-build` directory and the `installed_PACKAGE` file before running make.

## Compatibility of compiler, MPI, and Python

The default settings do not install a compiler suite, Python, or MPI.
In order for PyLith to work properly, Python and MPI must be built with the same compiler suite used by the PyLith installer to build all of the other dependencies and PyLith itself.


If you are using the Python and compiler suite provided by the operating system, these are guaranteed to be compatible.
The configure tests are relatively simple and detect only major incompatibilities; many small incompatibilities slip through and only show up during the testing phase of the build process.

### Checking the compiler used to build Python

You can see which compiler was used to build an installed version of Python by starting the Python interpreter (run `python3`) and examining the second line.
In the following example, we see from the second line that Python was built using clang provided by the macOS which is compatible with gcc 4.2.1.

```bash
python3

Python 3.8.3 (default, May 19 2020, 09:28:14)
[Clang 10.0.1 (clang-1001.0.46.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Likewise you can often identify which compiler an MPI version is using by running `mpicc -show`.
In the following example, we see that MPICH was compiled using clang and is installed in `/Users/johndoe/tools/mpich-3.3.2`.

```bash
mpicc -show

clang -Wl,-flat_namespace -I/Users/johndoe/tools/mpich-3.3.2/include -L/Users/johndoe/tools/mpich-3.3.2/lib -lmpi -lpmpi
```

