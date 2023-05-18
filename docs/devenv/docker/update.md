# Updating the container

## Updating the Docker image

You can use the `docker pull` command to update your local PyLith development environment Docker container.
This is needed to get the latest operating system updates in the base image or to get updated versions of the dependencies.

:::{tab-set}

:::{tab-item} amd64 (Intel)

```{code-block} bash
docker pull registry.gitlab.com/cig-pylith/pylith_installer/pylith-devenv-amd64
```

:::

:::{tab-item} arm64 (Apple)

```{code-block} bash
docker pull registry.gitlab.com/cig-pylith/pylith_installer/pylith-devenv-arm64
```

:::

::::

:::{important}
Pulling the PyLith development environment Docker image does not update Pythia, Spatial Data, PETSc, or PyLith.
:::

## Updating PETSc or PyLith

See [Rebuilding PETSc and PyLith in the PyLith Developer Guide](https://pylith.readthedocs.io/en/v3.0.3/developer/contributing/rebuilding.html) for how to update PETSc and PyLith.
