python3 server.py &
SLEEP 1
pid=`ps -ef | grep server.py | grep -v grep | awk '{print $2}'`
python3 test.py
kill ${pid}