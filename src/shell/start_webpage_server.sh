export PYTHONIOENCODING=utf-8
echo "start webpage service!"
nohup python ./../webpage_server.py > webpage_output 2>&1 &

echo "ps -ef |grep python"
ps -ef |grep python
