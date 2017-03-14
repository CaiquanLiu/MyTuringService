process_status=$(ps -ef|grep python|grep tornado_server.py)

array=($process_status)

echo "stop tornado service!"

#echo ${array[1]}

kill -9 ${array[1]}