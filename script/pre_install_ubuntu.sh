#!/bin/bash

check_failed=0

if [ "$URL" = "" ]
then
  echo "error: url needed. Please export URL before install."
  check_failed=1
fi


if [ $check_failed = 1 ]
then
    exit 1
fi


if [ "$TIME_ZONE" = "" ]
then
  echo "warning: Use default timezone 'Asia/Shanghai'.Please export TIME_ZONE before install if you want to configure it."
fi


exit 0