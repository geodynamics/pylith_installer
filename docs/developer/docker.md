# Docker images

The `docker` directory contains Dockerfiles for building containers for testing PyLith on several different Linux
distributions. These are used in the CI testing done with Travis CI. After building the containers, push them to Docker
Hub.

## Building test environment images

```
docker build -t $IMAGE_NAME -f docker/$DOCKERFILE .
```

### Debugging

```
# Get id of container that failed
docker ps -a

# Save container state to 'debug' image
docker commit debug

# Run debug container
docker run -ti debug /bin/bash
```

### Clean up

```
# Remove container
docker rm $CONTAINER_ID

# Remove image
docker rmi $IMAGE_ID

# Remove stopped containers and orphan images
docker system prune
```
