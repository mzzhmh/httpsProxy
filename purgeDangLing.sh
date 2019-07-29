#!/usr/bin/bash
danglingImg=`docker images -f 'dangling=true' | grep none | awk {'print $3'}`
echo $danglineImg




