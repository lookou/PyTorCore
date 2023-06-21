#!/bin/bash
SERVER="pytor_server.py"
for assetsuid in "`ps -ef | grep ${SERVER} |grep -v "grep"| awk '{print $2}'| sed -n '1'p`"
do
    kill -9 $assetsuid;
    echo $?>>/dev/null
done

if [ $? -lt 1 ]
then
    nohup  python3 ${SERVER} &
    echo "Restart Completion"
fi
