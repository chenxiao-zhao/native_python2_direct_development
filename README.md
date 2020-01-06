# native_python2_direct_development

# Features

  - Process the continuous data output from the AI box and convert it into statistics every 5 minutes

# Build

```sh
$ sudo -s
$ git clone https://github.com/chenxiao-zhao/native_python2_direct_development.git
$ cd native_python2_direct_development/
$ make
```
  - install package is **native_python2_direct_development_2.2_amd64.deb**

# Install

```sh
$ sudo -s
$ export URL="http://localhost"
$ export TIME_ZONE="Asia/Shanghai"
$ export LOG_LEVEL="error"
$ apt-get install ./native_python2_direct_development_2.2_amd64.deb
```

# Verify

```sh
$ appc query | grep native_python2_direct_development
2  root  start  21470 0      native_python2_direct_development       /opt/personal/native_python2_direct_development/native_python2_direct_development
```

# Uninstall

```sh
$ sudo apt-get remove native_python2_direct_development
```