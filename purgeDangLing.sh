#!/usr/bin/bash
danglingImg=`docker images -f 'dangling=true' | grep none | awk {'print $3'}`
if [ -z "$danglingImg" ]
then
        echo "Empty Dangling Image!"
        exit 0
else
        printf "Images: $danglingImg \n=======\n"
        for word in $danglingImg
        do
                printf "Removing $word\n"
                cmd="docker image rm $word"
                echo $cmd
                $cmd
        done
        exit 0
fi




