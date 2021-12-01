# Intended uses for the PyLith Installer

* Installing PyLith on a cluster

    PyLith uses the Message Passing Interface for parallel processing.
    The implementation of this interface depends on the cluster hardware.
    As a result, we do not provide binary packages that run on clusters and you must build PyLith from source.
* User developers

    Anyone interested in contributing to PyLith development should build PyLith from source using the GitHub repositories.
    This makes it possible to contribute back to the main PyLith source code.

  :::{tip}
  The [PyLith Docker Development Environment](/devenv/docker-devenv.md) is an easy way to setup the PyLith development environment.
  :::
