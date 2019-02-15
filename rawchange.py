from gps import GPS
from time import sleep
from bsmLib import tcpClient
from time import sleep
#r = '$GPRMC,154633.000,A,4457.4413,N,09320.5487,W,0.19,0.07,011118,,,A*7B'

tcpClient(host = '192.168.21.153', port = '10002')
t = tcpClient()
t.connect()

while True:
    sleep (2)

    g = GPS()
    r = g.read()

    start = r.find('$GPRMC')
    end = r.find(',0.', start)
    log = r[start:end]

    start2 = log.find('A')
    end2 = log.find('W', start2)
    log2 = log[start2:end2]

    start3 = log2.find('44')
    end3 = log2.find(',N', start3)
    lat = log2[start3:end3]

    start4 = log2.find('09')
    end4 = log2.find(',W,', start4)
    lon = log2[start4:end4]

    f = open('gData.txt', 'w')
    #sample = ('4457.4413', '09320.5487')
    dlat = ((float(lat) - 4400) / 60) + 44
    dlon = (((float(lon) - 9300) / 60) + 93) * -1
    coords = dlat, dlon
    f.write(str(coords))
    f.close

    sleep(2)

    f = open('gData.txt', 'r')
    data = r.read()
    t.send(str(data))
