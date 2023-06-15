# Docker quick reference

## Copy files to/from container

```{code-block} bash
# Copy file to `/opt/pylith/src` in container `pylith-dev-workspace`
docker cp myfile.txt pylith-dev-workspace:/opt/pylith/src

# Copy file from `/opt/pylith/src` in container `pylith-dev-workspace` to current directory
docker cp pylith-dev-workspace:/opt/pylith/src/myfile.txt .
```

## Attach to container as root

```{code-block} bash
# Attach to running container `pylith-dev-workspace` as root
docker exec -it -u root pylith-dev-workspace /bin/bash
```
