#!/usr/bin/env python
"""
show how to add a matplotlib FigureCanvasGTK or FigureCanvasGTKAgg widget to a
gtk.Window
"""

import gtk

from matplotlib.figure import Figure
from numpy import arange, sin, cos, pi

# uncomment to select /GTK/GTKAgg/GTKCairo
# from matplotlib.backends.backend_gtk import FigureCanvasGTK as FigureCanvas
# from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas
from matplotlib.backends.backend_gtkcairo import FigureCanvasGTKCairo as FigureCanvas


win = gtk.Window()
win.connect("destroy", lambda x: gtk.main_quit())
win.set_default_size(800, 600)
win.set_title("Embedding in GTK")

box = gtk.VBox();

win.add(box)

f = Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111)

print f.get_axes()[0]

t = arange(0.0, 3.0, 0.01)
s = sin(2*pi*t)
a.plot(t, s)

s = cos(2*pi*t)
a.plot(t, s)

s = sin(2*pi*t)*cos(2*pi*t)
a.plot(t, s)

canvas = FigureCanvas(f)  # a gtk.DrawingArea

box.pack_start(canvas,expand=True,padding=10)

butt = gtk.Label("Here is a graph.")

box.pack_start(butt,expand=False,padding=10)

win.show_all()
gtk.main()
