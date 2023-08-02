# pibuild
This repository contains all the necessary scripts, tools, and configurations for building the Pinect software from source.

- https://github.com/ser-mk/pilauncher

- https://github.com/ser-mk/mclient

- https://github.com/ser-mk/piball

- https://github.com/ser-mk/admin-dpc

It enables developers to easily build the software on android platforms.

## Prerequisites

* docker

## How build

1. Clone the repo:
```
git clone --recurse-submodules https://github.com/ser-mk/pibuild.git
```

2. Run docker contatiner:
```
docker pull sermkd/pibuild:1.0.0a
docker run --rm -it -v "$PWD/pibuild:/home/gradle/" sermkd/pibuild:1.0.0a python build.py
```
3. Built apks will be in $PWD/pibuild/build_archive/current/
```
$ ls pibuild/build_archive/current/
admin-dpc.apk  mclient.apk  piball.apk  pilauncher.apk
```

### Help
If you're building the Pinect software and you notice that not all of the APKs are being generated, one thing you can try is running the build command multiple times. Sometimes, issues with dependencies or missing files can cause the build process to fail, but running the command again can help resolve these issues:
```bash
$ docker run --rm -it -v "$PWD/pibuild:/home/gradle/" sermkd/pibuild:1.0.0a python build.py
...
$ ls pibuild/build_archive/current/
admin-dpc.apk  mclient.apk 

# rerun the build command
$ docker run --rm -it -v "$PWD/pibuild:/home/gradle/" sermkd/pibuild:1.0.0a python build.py
...
$ ls pibuild/build_archive/current/
admin-dpc.apk  mclient.apk  piball.apk  pilauncher.apk
```

