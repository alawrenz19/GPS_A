import bsmLib.RPL as RPL
from bsmLib.vector import vector
from server import c_read
from time import sleep
from bsmLib import tcpServer


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

lat2 = raw_input("Latuitude: ")
long2 = raw_input("Longitude: ")

c_read()

p1 = [lat1, long1]
p2 = [lat2,long2]

L = 0
R = 1

global distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

def drive_forward():
    while True:
        sleep(2)
        c_read()
        while distance > 20:
            RPL.servoWrite(L, 2000)
            RPL.servoWrite(R, 1000)
            if distance < 20:
                break
        while distance < 20:
            RPL.servoWrite(L, 0)
            RPL.servoWrite(R, 0)
            if distance > 20:
                break

drive_forward()
