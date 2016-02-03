import gi
from time import sleep

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# class Handler:
#     def onDeleteWindow(self, *args):
#         Gtk.main_quit(*args)
#
#     def onButtonPressed(self, button):
#         print("Hello World!")

builder = Gtk.Builder()
builder.add_from_file("TryGlade.glade")
# builder.connect_signals(Handler())
window = builder.get_object("mainwindow")

labelsensornumbers = []
for isens in range(3):
    sensorgui = Gtk.Builder()
    sensorgui.add_from_file("TryGladeSensor.glade")
    sensorframe = sensorgui.get_object("sensorframe")
    labelsensornumber = sensorgui.get_object("countlabel")
    labelsensornumbers.append(labelsensornumber)
    labelsensornumber.set_label( str(isens) )
    sensorframe.set_name("sensorframe"+str(isens))

    boxgui = builder.get_object("sensorsbox")
    boxgui.pack_start(sensorframe, False, True, 0)

window.show_all()
Gtk.main()