from bsmLib import tcpServer
from time import sleep

tcpServer(port = '10002')

t = tcpServer()
t.listen()

def c_read():
    coords = t.recv()

    start = coords.find( '(' )
    end = coords.find( ')' )

    if start != -1 and end != -1:
        result = coords[start+1:end]

    lat1, long1 = result.split(',')
