# Updating the container

## Updating the Docker image

You can use the `docker pull` command to update your local PyLith development environment Docker container.
This is needed to get the latest operating system updates in the base image or to get updated versions of the dependencies.

```{code-block} bash
docker pull ghcr.io/geodynamics/pylith_installer/pylith-devenv
```

:::{warning}
Pulling the PyLith development environment Docker image does not update Pythia, SpatialData, PETSc, or PyLith.
:::

## Updating PETSc or PyLith

See [Rebuilding PETSc and PyLith in the PyLith Developer Guide](https://pylith.readthedocs.io/en/latest/developer/building/index.html) for how to update PETSc and PyLith.
