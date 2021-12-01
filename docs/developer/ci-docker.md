# Test environment Docker containers

The `docker` directory contains Dockerfiles for building containers for testing PyLith on several different Linux distributions.
These are used in the CI testing with GitLab Pipelines.
After building the containers, push them the GitLab registry.

## Building test environment images

```bash
# From the top-level source directory
docker/builder.py --dockerfile=$DOCKERFILE --build
```

### Debugging container setup

```bash
# Get id of container ($CONTAINER_ID) that failed
docker ps -a

# Save container state to 'debug' image
docker commit $CONTAINER_ID debug

# Run debug container
docker run --rm -ti debug /bin/bash
```

### Clean up

```bash
# Remove container
docker rm $CONTAINER_ID

# Remove `debug` image
docker rmi debug

# Remove stopped containers and orphan images
docker system prune
```
