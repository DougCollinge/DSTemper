import gobject, gtk

class TryTimer:

    def __init__(self):
        print("init.")
        gobject.timeout_add(1000, self.timer )

    def timer(self):
        print("timer")
        return True

timr = TryTimer()
gtk.main()
