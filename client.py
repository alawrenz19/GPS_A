from bsmLib import tcpClient
from time import sleep

tcpClient(host = '192.168.21.153', port = '10002')
t = tcpClient()
t.connect()

f = open('gData.txt', 'r')

while True:
    sleep(2)
    data = f.read()
    t.send(str(data))
