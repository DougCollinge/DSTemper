from time import sleep, strftime
import random

class Thermometer:
    def __init__(self,type,family,id,temperature):
        self.type = type
        self.family = family
        self.id = id
        self.temperature = temperature

class ThermometerBus:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        # self.connection = ownet.Connection(host,port)

    def thermometers(self):
        # r = ownet.Sensor('/', self.host, self.port)
        # sensors = r.sensorList()
        self.thermometers = [
            Thermometer("DSFAKE","10","xxxxxxxxxxxx",0),
            Thermometer("DSFAKE","28","yyyyyyyyyyyy",0)
        ]


        # for sensor in sensors:
        #     if hasattr(sensor,'family'):
        #         if sensor.family == 10 or sensor.family == 28:
        #             self.thermometers.append(sensor)
        return self.thermometers

    def simultaneousTemperatures(self):
        # self.connection.write('/simultaneous/temperature',1)
        sleep(1.000)
        temps = []
        for thermometer in self.thermometers:
            if hasattr(thermometer, "temperature"):
                # temps.append( thermometer.temperature )
                temps.append(random.random() * 100)
            else:
                temps.append(None)
        return temps

# host = 'localhost'
# port = 4304
