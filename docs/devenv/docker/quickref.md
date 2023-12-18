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

## Docker images

```{code-block} bash
# List local images
docker images

# Remove docker image using id
docker rmi IMAGE_ID

# Remove docker image using tag
docker rmi IMAGE_TAG
```

## Docker containers

```{code-block} bash
# List all docker containers
docker ps -a

# List running docker containers
docker ps

# Remove docker container
docker rm CONTAINER_ID
```
