# Creating pylith-devenv Docker image

## Setup

Create a multiple-architecture builder, `multiarch`.

```{code-block} bash
docker buildx create --name multiarch --driver docker-container --bootstrap
```

## Build Docker image

Build and push the Docker image.
This will create a docker image with layers for both architectures.
When a user pulls the image from the registry, only the layers for that computer's architecture are downloaded.

::::{tab-set}

:::{tab-item} No custom certificates

```{code-block} bash
# Select the multiarch builder
docker buildx use multiarch

# Build and push the image
docker buildx build --platform linux/amd64,linux/arm64 -t registry.gitlab.com/cig-pylith/pylith_installer/pylith-devenv --push -f docker/pylith-devenv .
```

:::

:::{tab-item} Using custom certificates

```{code-block} bash
# Select the multiarch builder
docker buildx use multiarch

# Build using DOI certs
docker buildx build --platform linux/amd64,linux/arm64 -t registry.gitlab.com/cig-pylith/pylith_installer/pylith-devenv --build-arg BUILD_ENV=certs-doi --push -f docker/pylith-devenv .
```

:::

::::