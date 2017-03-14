echo "start tornado service!"
nohup python tornado_server.py > tornado_output 2>&1 &

echo "ps -ef |grep python"
ps -ef |grep python
