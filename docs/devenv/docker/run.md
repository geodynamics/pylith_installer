# Running the container

## Start the Docker container

Whenever you need to restart the `pylith-dev-workspace` Docker container, simply run

```{code-block} bash
docker run --name pylith-dev-workspace --rm -it -v pylith-dev:/opt/pylith \
    registry.gitlab.com/cig-pylith/pylith_installer/pylith-devenv
```

:::{important}
Make sure Docker is running before you start the container.
:::

## Attach VS Code to the Docker container

1. Start VS Code.
2. Click on the Docker extension in the Activity Bar on the far left hand side as illustrated in the [screenshot](docker-attach-vscode).
3. Find the `pylith-dev-workspace` container. Verify that it is running.
4. Right-click on the container and select `Attach Visual Studio Code`. This will open a new window. You should see `Container registry.gitlab.com/cig-pylith...` at the left side of the status bar at the bottom of the window.

:::{figure-md} docker-attach-vscode
:class: myclass

<img src="figs/docker-attach-vscode.png" alt="Screenshot" class="bg-primary mb-1">

Screenshot showing how to attach VS Code to a running Docker container. 
:::
