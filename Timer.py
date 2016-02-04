# from gi.repository import GObject.timeout_add
from gi.repository import Gtk
from gi.repository import GLib
class Timer:

    def __init__(self):
        print("init.")
        GLib.timeout_add(1000, self.timer )

    def timer(self):
        print("timer")
        return True

timr = Timer()
Gtk.main()
