export PYTHONIOENCODING=utf-8
echo "start wechat service!"
nohup python ./../wechat_server.py > wechat_output 2>&1 &

echo "ps -ef |grep python"
ps -ef |grep python
