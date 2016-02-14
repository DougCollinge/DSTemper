import gi
from gi.repository import GObject
from gi.repository import GLib
from time import sleep
import datetime
import os

import ownet
from ThermometerBus import ThermometerBus
from DSSettings import DSSettings

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

host = 'localhost'
port = 4304

# settings = {
#     "samplePeriod": 2.3
# }

# class Handler:
#     def onDeleteWindow(self, *args):
#         Gtk.main_quit(*args)
#
#     def onButtonPressed(self, button):
#         print("Hello World!")

tbus = ThermometerBus(host,port)
thermometers = tbus.thermometers()

builder = Gtk.Builder()
builder.add_from_file("DSTemperMain.glade")
dateTimeLabel = builder.get_object("dateTimeLabel")
# builder.connect_signals(Handler())
window = builder.get_object("mainwindow")
window.connect("destroy", lambda x: Gtk.main_quit())

labelsensornumbers = []
temperaturelabels = []

for isens in range(len(thermometers)):
    sensorgui = Gtk.Builder()
    sensorgui.add_from_file("DSTemperThermometer.glade")
    sensorframe = sensorgui.get_object("sensorframe")

    labelsensornumber = sensorgui.get_object("countlabel")
    labelsensornumbers.append(labelsensornumber)
    labelsensornumber.set_label( str(isens) )
    sensorframe.set_name("sensorframe"+str(isens))

    sensoridlabel = sensorgui.get_object("sensorIdLabel")
    sensoridlabel.set_label( thermometers[isens].id )

    sensortypelabel = sensorgui.get_object("sensorTypeLabel")
    sensortypelabel.set_label( thermometers[isens].type )

    boxgui = builder.get_object("sensorsbox")
    boxgui.pack_start(sensorframe, False, True, 0)


    sensorTemperatureLabel = sensorgui.get_object("sensorTemperatureLabel")
    temperaturelabels.append( sensorTemperatureLabel )

def on_periodSpinButton_value_changed(src):
    settings.set("samplePeriod", src.get_value())

def on_enableCheckButton_toggled(src):
    if src.get_active() :
        # print "not active"
        sampleTemperature()

builder.connect_signals(
    {
        'on_periodSpinButton_value_changed': (on_periodSpinButton_value_changed),
        'on_enableCheckButton_toggled': (on_enableCheckButton_toggled)
    }
)



def sampleTemperature():
    checkbutton = builder.get_object("enableCheckButton")
    if not checkbutton.get_active() :
        return False
    GLib.timeout_add_seconds(settings.get("samplePeriod"), sampleTemperature )

    temps = tbus.simultaneousTemperatures()
    gnow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    dateTimeLabel.set_label( gnow )
    for isens in range(len(temps)):
        ntemp = temps[isens]
        if ntemp != None :
            stemp = "{0:6.2f}".format(ntemp)
        else :
            stemp = "---.--"
        # print stemp
        temperaturelabels[isens].set_label( stemp )
        temperaturelabels[isens].queue_draw()


settings = DSSettings(os.path.expanduser("~/.DSTemper.settings"))
builder.get_object("periodSpinButton").set_value( settings.get("samplePeriod") )

# sampleTemperature()
window.show_all()

Gtk.main()


