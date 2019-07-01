#!/usr/bin/bash
file="powerwall.txt"
while IFS=: read -r line 
do
	IP=`echo $line | cut -d ' ' -f1`
	PORT=`echo $line | cut -d ' ' -f2`
	cmd="nohup ./app.py $IP $PORT &>/var/log/powerwall/${PORT}_log &"
	echo $cmd
	nohup ./app.py $IP $PORT &>/var/log/powerwall/${PORT}_log &
done <"$file"
