# Running the container

## Start the Docker container

Whenever you need to restart the `pylith-dev-workspace` Docker container, simply run

::::{tab-set}

:::{tab-item} No GUI applications

```{code-block} bash
---
caption: Run development environment _without_ support for GUI applications.
---
docker run --name pylith-dev-workspace --rm -it -v pylith-dev:/opt/pylith \
    ghcr.io/geodynamics/pylith_installer/pylith-devenv
```

:::

:::{tab-item} With GUI applications

```{code-block} bash
---
caption: Run development environment _with_ support for GUI applications.
---
xhost +$(hostname).local
docker run --name pylith-dev-workspace --rm -it -e DISPLAY=host.docker.internal:0 \
    -v pylith-dev:/opt/pylith \
    ghcr.io/geodynamics/pylith_installer/pylith-devenv
```

:::

::::

:::{important}
Make sure Docker is running before you start the container.
:::

## Attach VS Code to the Docker container

1. Start VS Code.
2. Click on the Docker extension in the Activity Bar on the far left hand side as illustrated in the [screenshot](docker-attach-vscode).
3. Find the `pylith-dev-workspace` container. Verify that it is running.
4. Right-click on the container and select `Attach Visual Studio Code`. This will open a new window. You should see `Container ghcr.io/geodynamics/pylith_installer` at the left side of the status bar at the bottom of the window.
5. Open the PyLith source code by selecting `File` -> `Open Folder...` and navigating to `/opt/pylith/src/pylith`. 

:::{figure-md} docker-attach-vscode
:class: myclass

<img src="figs/docker-attach-vscode.png" alt="Screenshot" class="bg-primary mb-1">

Screenshot showing how to attach VS Code to a running Docker container.
:::
