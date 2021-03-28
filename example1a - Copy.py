from stuff import *
df = pd.read_csv('dataRecordings.csv')

# fig = make_subplots(rows=3, cols=1)
# go.Figure(data = go.Scatter(x=df.index, y=df.loc[:, 3]), layout = go.Layout(title='wasup_bitch', yaxis_title='hueregeil', xaxis_title = 'waslosssjooo'))
# go.Figure(data = go.Scatter(x=df.time, y=df.phaseTmCorr), layout = go.Layout(title='wasup_bitch', yaxis_title='hueregeil', xaxis_title = 'waslosssjooo'))


import pandas as pd
import os, time
from datetime import datetime

from plotly.tools import mpl_to_plotly
from threading import Timer, Thread
time.strftime('%X %x %Z')
# os.environ['TZ'] = 'Geneva,Switzerland'
import plotly.io as pio
from plotly.matplotlylib import mplexporter, PlotlyRenderer
import plotly.graph_objs as go
from plotly.offline import plot
from plotly.subplots import make_subplots
df['time'] = pd.to_datetime(df['time'])
df = df.drop(['year', 'month', 'day'], axis=1)
# df['year'] = pd.to_datetime(df['year'])
# df['month'] = pd.to_datetime(df['month'])
# df['day'] = pd.to_datetime(df['day'])
pp(df.time.dt, 'd')
fig = make_subplots(rows=3, cols=1)
# go.Figure(data = go.Scatter(x=df.index, y=df.loc[:, 3]), layout = go.Layout(title='wasup_bitch', yaxis_title='hueregeil', xaxis_title = 'waslosssjooo'))
# go.Figure(data = go.Scatter(x=df.time, y=df.phaseTmCorr), layout = go.Layout(title='wasup_bitch', yaxis_title='hueregeil', xaxis_title = 'waslosssjooo'))
# df['time'] = pd.to_datetime(df['time'])
# df['year'] = pd.to_datetime(df['year'])
# df['month'] = pd.to_datetime(df['month'])
# df['day'] = pd.to_datetime(df['day'])
# pp(df.time)

print("das ist df.head")
print("das ist df.tail")

# traces =go.Figure(data = go.Scatter(x=df.index,  y = df.distance, name='distance'),layout=go.Layout(title='distance vs. time' , yaxis_title ='distance 1/[mm]'))
traces =go.Scatter(x=df.time.dt.strftime('%X %x %Z'),  y = df.distance, name='distance')
fig.add_trace(traces, row=1, col=1)
# traces =go.Scatter(x=df.time.dt.to_pydatetime(),  y = df.voltage, name='humidity')
# fig.add_trace(traces, row=2, col=1)
# traces =go.Scatter(x=df.time.dt.to_pydatetime(),  y = df.battery, name='temperature')
# fig.add_trace(traces, row=4, col=1)
traces =go.Scatter(x=df.time.dt.strftime('%X %x %Z'),  y = df.voltage, name='voltage')
fig.add_trace(traces, row=2, col=1)
traces =go.Scatter(x=df.time.dt.strftime('%X %x %Z'),  y = df.battery, name='battery')
fig.add_trace(traces, row=3, col=1)
pp(df.time.dt.strftime('%X %x %Z'))


# fig['layout']['xaxis']['title']='distance 1/[mm]'
# fig['layout']['xaxis2']['title']='humidity [pct]'
fig['layout']['xaxis3']['title']='time'
fig['layout']['yaxis']['title']='distance 1/[mm]'
# fig['layout']['yaxis2']['title']='humidity [pct]'
fig['layout']['yaxis2']['title']='voltage 1/[V]'
# fig['layout']['yaxis3']['title']='temperature 1/[°C]'
fig['layout']['yaxis3']['title']='battery [pct]'


fig['layout']['title']='Prototype Measurements'
fig['layout']['height'] = 1800
# fig.update_xaxes(type='date')

# fig.update_yaxes(autorange = True)
# windowMarg = 1
print([df['time'].min(),df['time'].max()])
fig['layout']['xaxis3']['range']=[df['time'].min(),df['time'].max()]

# diff = (np.max(df['battery'])-np.max(df['battery']))*windowMarg
# fig['layout']['yaxis3']['range']=[np.min(df['battery'])-diff,np.max(df['battery'])+diff]

# # diff = (np.max(df['temperature'])-np.max(df['temperature']))*windowMarg
# # fig['layout']['yaxis3']['range']=[np.min(df['temperature'])-diff,np.max(df['temperature'])+diff]

# diff = (np.max(df['voltage'])-np.max(df['voltage']))*windowMarg
# fig['layout']['yaxis2']['range']=[np.min(df['voltage'])-diff,np.max(df['voltage'])+diff]

# # diff = (np.max(df['humidity'])-np.max(df['humidity']))*windowMarg
# # fig['layout']['yaxis2']['range']=[np.min(df['humidity'])-diff,np.max(df['humidity'])+diff]

# diff = (np.max(df['distance'])-np.max(df['distance']))*windowMarg
# fig['layout']['yaxis']['range']=[np.min(df['distance'])-diff,np.max(df['distance'])+diff]
pio.show(fig)