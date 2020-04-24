# 3. Setting up your environment

Set up your environment variables (as indicated in the output of the
configure script).

**WARNING**: The `setup.sh` script works for terminals running the bash shell. If you are using a different shell, you
will need to modify the script to set the environment variables using the appropriate syntax.

```
bash> cd $HOME/build/pylith
bash> source setup.sh
```

**IMPORTANT**: You must run the `source setup.sh` script in each terminal you run configure *and* before each time you
run PyLith.

To avoid having to run `source setup.sh` each time, you can add the corresponding environment variables to your
`.bashrc` file (or equivalent for other shells).
