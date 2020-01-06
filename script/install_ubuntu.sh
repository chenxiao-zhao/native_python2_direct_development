#!/bin/bash

INSTALL_NAME=native_python2_direct_development
INSTALL_PATH=/opt/personal/${INSTALL_NAME}

if [ "$TIME_ZONE" = "" ]
then
  TIME_ZONE="Asia/Shanghai"
fi

if [ "$LOG_LEVEL" = "" ]
then
  LOG_LEVEL="error"
fi

sed -i "s#@TIME_ZONE@#${TIME_ZONE}#g" ${INSTALL_PATH}/native_python2_direct_development.json

mkdir -p "/opt/personal/work"
appmgc reg -n native_python2_direct_development -c "${INSTALL_PATH}/native_python2_direct_development --${LOG_LEVEL} " -u root -w "${INSTALL_PATH}" -f 