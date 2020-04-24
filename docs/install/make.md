# 4. Running make

Running `make` will build all of the required dependencies and then PyLith. You do not
need to run `make install`, because the installer includes this step
in the make process.

```[bash]
bash> make
```

Depending on the speed and memory of your machine and the number of dependencies and which ones need to be built, the
build process can take anywhere from about ten minutes to several hours. As discussed above you can interrupt the build
process and continue at a later time from where you left off.
