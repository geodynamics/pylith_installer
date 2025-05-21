# Creating pylith-devenv Docker image

## Setup

Setup emulation libraries (taken from <https://docs.docker.com/build/building/multi-platform/>)

```{code-block} bash
# Install emulation packages
sudo apt install qemu qemu-user-static binfmt-support

# Install binfmt stuff
docker run --rm tonistiigi/binfmt --install all

# Verify the F flag is set
cat /proc/sys/fs/binfmt_misc/qemu/aarch64

# Try running container using emulation
docker run --rm -ti --platform=linux/arm64 ubuntu:24.04 /bin/bash
```

Create a multiple-architecture builder, `multiarch`.

```{code-block} bash
docker buildx create --name multiarch --driver docker-container --bootstrap
```

:::{note}
You may need `docker-credential-pass` in your `PATH`.
:::

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
docker buildx build --platform linux/amd64,linux/arm64 -t ghcr.io/geodynamics/pylith_installer/pylith-devenv --push -f docker/pylith-devenv .
```

:::

:::{tab-item} Using custom certificates

```{code-block} bash
# Select the multiarch builder
docker buildx use multiarch

# Build using DOI certs
docker buildx build --platform linux/amd64,linux/arm64 -t ghcr.io/geodynamics/pylith_installer/pylith-devenv --build-arg BUILD_ENV=certs-doi --push -f docker/pylith-devenv .
```

:::

::::