#!/usr/bin/bash
danglingImg=`docker image ls | grep httpsproxy | grep latest | awk {'print $3'} | uniq`
if [ -z "$danglingImg" ]
then
        echo "Empty Image!"
else
        printf "Images: $danglingImg \n=======\n"
        for word in $danglingImg
        do
                printf "Removing $word\n"
                cmd="docker image rm $word -f"
                echo $cmd
                $cmd
        done
fi

danglingImg2=`docker image ls | grep httpsproxy | awk {'print $3'} | uniq`
if [ -z "$danglingImg2" ]
then
        echo "Empty Image 2!"
else
        printf "Images: $danglingImg2 \n=======\n"
        for word2 in $danglingImg2
        do
                printf "Removing $word2\n"
                cmd2="docker image rm $word2 -f"
                echo $cmd2
                $cmd2
        done
fi

exit 0

