import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import *
import numpy as np  # (*) numpy for math functions and arrays
import datetime
import time
import logging
logging.basicConfig(level=logging.DEBUG)

from ThermometerBus import ThermometerBus

host = 'localhost'
port = 4304

bus = ThermometerBus(host,port)
therms = bus.thermometers()
logging.debug("Number of thermometers:%d",len(therms))

stream_ids = ["d7hhv34d32","jfh75d1vr1","tz0nz3779t","j359lsu1rh","vut4dqvvlz","aml29ioq5v"]

# Make instance of stream id object
streams = []
traces = []
npoints = 60*60

for i in range(len(therms)):
    streams.append( Stream(
        token=stream_ids[i],  # (!) link stream id to 'token' key
        maxpoints=npoints
        )
    )

    traces.append(
        Scatter(
            # name="Sensor "+str(i+1),
            name = therms[i].id,
            x=[],
            y=[],
            mode='lines',
            stream=streams[i]         # (!) embed stream id, 1 per trace
        )
    )

data = Data(traces)

# Add title to layout object
layout = Layout(
    title='Thermolog',
    yaxis={
        "range":[0,40],
        "type":"linear",
        "title":"Temperature (C)",
        "autorange":False,
        "gridcolor":"rgb(204, 204, 204)",
        "tickmode":"linear",
        "dtick":1,
        "side":"right"
    },
    xaxis={
        "title":"Time",
        "type":"date",
        "autorange":True,
        "tickangle":90
    },
)

# Make a figure object
fig = Figure(data=data, layout=layout)

# (@) Send fig to Plotly, initialize streaming plot, open new tab
unique_url = py.plot(fig, filename='thermolog',fileopt="overwrite",auto_open=False,sharing="public")

for i in range(len(streams)):
    streams[i] = py.Stream(stream_ids[i])
    streams[i].open()

# (@) Open the stream


N = 24*60*60  # number of points to be plotted

# Delay start of stream by 5 sec (time to switch tabs)
time.sleep(5)

i = 0    # a counter
while i<N:
    i += 1   # add to counter
    temps = bus.simultaneousTemperatures()
    gnow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    for j in range(len(temps)):
        # Current time on x-axis, random numbers on y-axis
        x = gnow
        y = temps[j]
        # y = 60+10*np.random.randn(1)[0]

        # (-) Both x and y are numbers (i.e. not lists nor arrays)

        # (@) write to Plotly stream!
        streams[j].write(dict(x=x, y=y))

        # (!) Write numbers to stream to append current data on plot,
        #     write lists to overwrite existing data on plot (more in 7.2).

    # time.sleep(0.08)  # (!) plot a point every 80 ms, for smoother plotting

for i in range(len(streams)):
# (@) Close the stream when done plotting
    streams[i].close()