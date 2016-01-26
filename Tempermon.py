import logging
logging.basicConfig(level=logging.DEBUG)

from time import sleep, strftime
import ownet

class TempBus:
    def __init__(self,host,port):
        self.connection = ownet.Connection(host,port)

    def thermometers(self):
        r = ownet.Sensor('/', host, port)
        sensors = r.sensorList()
        self.ds18s20s = []
        for sensor in sensors:
            if hasattr(sensor,'family'):
                if sensor.family == 10:
                    self.ds18s20s.append(sensor)
        return self.ds18s20s

    def temperatures(self):
        self.connection.write('/simultaneous/temperature',1)
        sleep(1.000)
        temps = []
        for ds18s20 in self.ds18s20s:
            temps.append( ds18s20.temperature)
        return temps

host = 'localhost'
port = 4304

bus = TempBus(host,port)
therms = bus.thermometers()

for i in range(10):
    logging.debug("\nIteration:%d",i)

    timestr = strftime('%Y%m%d %H:%M:%S')
    temps = bus.temperatures()
    for temp in temps:
        logging.debug( 'reading:%d, time:%s temp:%s',i,timestr, temp )


exit()

