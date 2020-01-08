# native_python2_direct_development

# Features

  - Native python directly develops the deb package

# Build

```sh
$ sudo -s
$ git clone https://github.com/chenxiao-zhao/native_python2_direct_development.git
$ cd native_python2_direct_development/
$ make
or
$ wget http://file.achang.tech/Package/last/native_python2_direct_development/native-python2-direct-development_2.2_amd64.deb 
```
  - install package is **native_python2_direct_development_2.2_amd64.deb**
  
# Prerequirements

Installing the environment requires [Application Manager](https://github.com/laoshanxi/app-manager).

# Install

```sh
$ sudo -s
$ export URL="http://localhost"
$ export TIME_ZONE="Asia/Shanghai"
$ export LOG_LEVEL="error"
$ apt-get install ./native-python2-direct-development_2.2_amd64.deb
```

# Verify

```sh
$ appc query | grep native_python2_direct_development
2  root  start  21470 0      native_python2_direct_development       /opt/personal/native_python2_direct_development/native_python2_direct_development --error
```

# Uninstall

```sh
$ sudo apt-get remove native-python2-direct-development
```