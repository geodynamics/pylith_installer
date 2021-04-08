# 4. Running make

Running `make` will build all of the required dependencies and then PyLith. You do not need to run `make install`, because the installer includes this step in the make process.

```bash
make
```

Depending on the speed and memory of your machine and the number of dependencies and which ones need to be built, the build process can take anywhere from about ten minutes to several hours. As discussed above you can interrupt the build process and continue at a later time from where you left off.

:::{tip}
We usually prefer capturing the output of running `make` to make it
easier to troubleshoot any problems. If you ask for help using the
installer, we will ask you to provide the log file.

```bash
# Capture the output to `make.log`
make >& make.log &

# Show the real-time updates to `make.log`
tail -f make.log
```
:::
