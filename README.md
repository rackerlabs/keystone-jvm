Keystone JVM
============

This project demonstrates how to run a large python application on the JVM using Jython.

Source
------
This project uses a git submodule for Jython.
To pull the submodule source execute the commands:

```
git submodule init
git submodule update
```

Build
-----
This project creates a keystone jar.
It requires pyenv to be installed.

It uses CPython to download all dependencies and gradle to package them into a jar.

To build execute the following commands:

```
./install.sh
./gradlew build
```

Deploy
------
To run keystone execute the following command:

`java -jar keystone.jar`

By default keystone will search for the config files under ./etc
A different configuration directory can be specified by the config_dir property:

`java -Dconfig_dir=<dir> keystone.jar`

Backend
-------
This project includes a mysql Dockerfile to build a docker mysql image.

Build:

`docker build -t mysql mysql`

Run:

`docker run -d -p 3306:3306 mysql`
