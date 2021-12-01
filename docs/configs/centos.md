# CentOS

## CentOS 7

### Operating system packages

```bash
yum install -y \
    gcc \
    gcc-c++ \
    make \
    file \
    which \
    diffutils \
    gettext \
    automake \
    autoconf \
    libtool \
    curl \
    curl-devel \
    openssh \
    openssl \
    openssl-devel \
    zlib-devel \
    libffi-devel \
    unzip \
    bzip2 \
    git \
    ca-certificates \
    cmake
```

### Environment variables

```
export PYTHON_VERSION=2.7
PREFIX_DIR=$HOME/pylith
```

### Configure

```bash
$HOME/src/pylith/pylith-installer-2.2.2-2/configure \
    --prefix=$PREFIX_DIR \
    --with-fetch=curl \
    --with-fortran=no \
    --with-make-threads=$(nproc) \
    --disable-cmake \
    --enable-mpi=openmpi \
```


