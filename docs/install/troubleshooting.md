# Troubleshooting

In this section we show how to address common problems encountered when using the installer.

## Did you forget Step 3 (setting up your environment)?

If you added the PyLith environment variables to your shell setup (`.bashrc`), check to make sure the PyLith directory is listed before other directories in your `PATH`, `LD_LIBRARY_PATH` (for Linux), and `PYTHONPATH`.

```bash
echo $PATH
echo $PYTHONPATH

# Linux only
echo $LD_LIBRARY_PATH
```

## Did you change the compiler, environment, or configure options?

If you run into an error and change something (compiler, environment variable, etc), you should reconfigure and rebuild.

1. Remove the build and install directories (`$HOME/build/pylith` and `$HOME/pylith`).
2. Try again starting at Step 2 (running configure).

```bash
rm -r $HOME/build/pylith and $HOME/pylith
```

## Error during configure of a dependency

If the `configure` for one the dependencies fails, examine the `config.log` file in the build directory for that package. For example, `netcdf-build/config.log`. You will need to scroll up from the bottom to see why a test failed.

## Requesting help

If you get stuck and need help diagnosing a build failure, please use the [CIG community forum](https://community.geodynamics.org/c/pylith/). Be sure to include the following information:

  * Operating system, e.g., CentOS 6, Ubuntu 18.04
  * List system packages you are using
  * Attach `$HOME/build/pylith/config.log`
  * Attach `$HOME/build/pylith/make.log`
  * Attach `config.log` from the build directory in which the failure occurred, e.g., `$HOME/build/pylith/netcdf-build/config.log`.
