process_status=$(ps -ef|grep python|grep tornado_server.py)

array=($process_status)

echo "stop tornado service!"

kill -9 ${array[1]}

echo "ps -ef |grep python"

ps -ef|grep python
