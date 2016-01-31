from time import sleep, strftime
import ownet

class ThermometerBus:
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.connection = ownet.Connection(host,port)

    def thermometers(self):
        r = ownet.Sensor('/', self.host, self.port)
        sensors = r.sensorList()
        self.thermometers = []
        for sensor in sensors:
            if hasattr(sensor,'family'):
                if sensor.family == 10 or sensor.family == 28:
                    self.thermometers.append(sensor)
        return self.thermometers

    def temperatures(self):
        self.connection.write('/simultaneous/temperature',1)
        sleep(1.000)
        temps = []
        for thermometer in self.thermometers:
            if hasattr(thermometer,"temperature"):
                temps.append( thermometer.temperature )
            else:
                temps.append( None )
        return temps

# host = 'localhost'
# port = 4304
