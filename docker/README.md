# Building Docker containers

This directory holds Docker container build instructions, aka Dockerfiles.
The images are stored in the geodynamics GitHub container registry with the URL `ghcr.io/geodynamics/pylith_installer`.

To set the visibility of container images, go to `github.com/geodynamics` -> `packages` (tab) -> `settings` (right side); the visibility setting is near the bottom.

## Containers

- **pylith-devenv**: Linux developer environment for PyLith (contains only dependencies)
- **pylith-binaryenv**: Linux environment for creating Linux binary package
- **Test environments**:
  - **centos-7**: EOL June 2024
  - **debian-stable**:
  - **debian-testing**:
  - **fedora-38**:
  - **fedora-39**:
  - **rockylinux-8**:
  - **rockylinux-9**:
  - **ubuntu-20.04**: LTS
  - **ubuntu-22.04**: LTS
  - **ubuntu-23.04**:
  - **ubuntu-23.10**:

## Building images

```bash
cd $SRC
docker/build.py --dockerfile=docker/ubuntu-22.04 --build --build-env=certs-doi
```

## Push images

```bash
# Linux
pass -c PATH_TO_TOKEN
docker push IMAGE_URL
```
