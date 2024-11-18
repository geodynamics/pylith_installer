# Binary packaging

Binary version is distributed via tarballs that are generated using
the build.py script.

## Linux

`export SSL_CERT_FILE="$CERT_PATH/$CERT_FILE"  REQUESTS_CA_BUNDLE="$CERT_PATH/$CERT_FILE"`

1. `docker volume create pylith-binary`
2. `docker build -t pylith_installer/pylith-binaryenv -f docker/pylith-binaryenv  --build-arg BUILD_ENV=certs-doi .`
3. `docker run --name pylith-binary-workspace --rm -t -v pylith-binary:/opt/pylith pylith_installer/pylith-binaryenv &`
4. `docker exec -it  pylith-binary-workspace /bin/bash`
   1. `mkdir src dist build && cd src`
   2. `git clone --recursive https://github.com/geodynamics/pylith_installer.git`
   3. `src/pylith_installer/packager/build.py --base-dir=/opt/pylith --make-threads=40 --setup`

## macOS

`export SSL_CERT_FILE="$CERT_PATH/$CERT_FILE"  REQUESTS_CA_BUNDLE="$CERT_PATH/$CERT_FILE"`
`export PYLITH_INSTALLER_PATH=${SW_DIR}/autotools/${COMPILER_VERSION}/bin`
`module purge`

1. `cd ~/scratch/build/pylith-binary`
2. `mkdir src && pushd src && ln -s $HOME/src/cig/pylith_installer && popd`
3. x86_64: `src/pylith_installer/packager/build.py --base-dir=`pwd` --make-threads=8 --macos-target=11.0 --setup`
4. arm64: `src/pylith_installer/packager/build.py --base-dir=`pwd` --make-threads=32 --macos-target=12.0 --setup`
