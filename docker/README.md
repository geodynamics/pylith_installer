# Building Docker containers

This directory holds Docker container build instructions, aka Dockerfiles.
The images are stored in the geodynamics GitHub container registry with the URL `ghcr.io/geodynamics/pylith_installer`.

To set the visibility of container images, go to `github.com/geodynamics` -> `packages` (tab) -> `settings` (right side); the visibility setting is near the bottom.

## Containers

- **pylith-devenv**: Linux developer environment for PyLith (contains only dependencies)
- **pylith-binaryenv**: Linux environment for creating Linux binary package
- **Test environments**:
  - **debian-stable**: Python 3.11, gcc 12.2
  - **debian-testing**: Python 3.12, gcc 14.2
  - **debian-11**: EOL Aug 2026, Python 3.9, gcc 10.2
  - **debian-12**: EOL Jun 2028, Python 3.11, gcc 12.2
  - **debian-13**: EOL Jun 2030, Python 3.13, gcc 14.2
  - **fedora-41**: EOL TBD, Python 3.13, gcc 14.3
  - **fedora-42**: EOL TBD, Python 3.13, gcc 15.2
  - **rockylinux-8**: EOL May 2029, Python 3.8, gcc 8.5
  - **rockylinux-9**: EOL May 2032, Python 3.9, gcc 11.4
  - **ubuntu-22.04**: LTS EOL April 2027, Python 3.10, gcc 11.4
  - **ubuntu-24.04**: LTS EOL April 2029, Python 3.12, gcc 13.2
  - **ubuntu-25.04**: EOL Jan 2026, Python 3.13, gcc 14.2
  - **ubuntu-25.10**: EOL TBD, Python 3.13, gcc 15.1

%  - **ubuntu-20.04**: LTS EOL April 2025, Python 3.8, gcc 9.4
%  - **ubuntu-24.10**: EOL Jul 2025, Python 3.12, gcc 14.2
%  - **fedora-39**: EOL Nov 2024, Python 3.12, gcc 13.3 
%  - **fedora-40**: EOL May 2025, Python 3.12, gcc 14.2


## Building images

```bash
cd $SRC
docker/build.py --dockerfile=docker/ubuntu-22.04 --build --build-env=certs-doi
```

## Push images

:::{admonition} Prerequisites
1. Install `pass`
2. Install `docker-credential-helper` from GitHub
3. Edit `~/.docker/config.json`
  ```
  {
	"auths": {
		"ghcr.io": {}
	},
	"credsStore": "pass"
  }
  ```
4. Login to container repository `docker login ghcr.io -u USERNAME`.
  This will place the credentials in the password store.
  Run `pass` to view the credentials.
:::

```bash
# Linux
pass -c PATH_TO_TOKEN
docker push IMAGE_URL
```
