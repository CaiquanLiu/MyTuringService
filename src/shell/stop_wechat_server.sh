process_status=$(ps -ef|grep python|grep wechat_server.py)

array=($process_status)

echo "stop wechat service!"

kill -9 ${array[1]}

echo "ps -ef |grep python"

ps -ef|grep python
