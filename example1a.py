 -*- coding: utf-8 -*-
import dash_devices
from dash_devices.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

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
from function_col import pp, plotly_plot_data
import ast
import matplotlib.pyplot as plt
import matplotlib as mpl
import json
import numpy as np
# from example2a import returnRequest
# external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

import websocket
mpl.use('Agg')


import plotly.graph_objects as go
import plotly.io as pio

plotly_template = pio.templates["plotly_dark"]
print (plotly_template)
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
# pio.templates["plotly_dark_custom"] = pio.templates["plotly_dark"]

# pio.templates["plotly_dark_custom"].update({
#                                         #e.g. you want to change the background to transparent
#                                         'paper_bgcolor': 'rgba(0,0,0,0)',
#                                         'plot_bgcolor': 'rgba(0,0,0,0)'
#                                         })

# class returnRequest():
#     # def updatePlot(self):
#     #   pass

#     def rshift(self, val, n): return (val % 0x100000000) >> n

#     def PayloadDecoder(self, fullJson):



#         # print(request.content_encoding())
#         # v = {"cmd":"gw","seqno":103915,"EUI":"FFFFFFFFFFFFFFFA","ts":1606054046489,"fcnt":2,"port":1,"freq":868500000,"toa":56,"dr":"SF7 BW125 4/5","ack":false,"gws":[{"rssi":-71,"snr":10,"ts":1606054046489,"tmms":null,"time":"2020-11-22T14:07:26.485739Z","gweui":"647FDAFFFF007AFB","ant":0,"lat":47.40912537932723,"lon":8.549648523330688}],"sessionKeyId":null,"bat":255,"data":"01bbd70009d80010"}
#         # v = request.get_jason()
#         # v = v['data']

#         # toBeDecoded = bytearray.fromhex("01a93b0009e20010")
#         # toBeDecoded = bytearray.fromhex(toBeDecoded['data'])
#         # toBeDecoded = bytearray.fromhex("01bbd70009d80010")
#         # toBeDecoded = bytearray.fromhex(toBeDecoded)
#         print(fullJson)

#         toBeDecoded =  bytearray.fromhex(fullJson)
#         # toBeDecoded = fullJson.encode('utf-8')
#         print(toBeDecoded)
#         # toBeDecoded = fullJson

        
#         # toBeDecoded = 0x01bbd70009d80010
#         print(fullJson)
#         # for b in toBeDecoded:
#             # print(b)
#         i = 0
#         dataDict = {'distance':0.0, 'temperature': 0.0,'humidity': 0.0, 'time': "", 'year': None, 'month': None, 'day': None, 'date': None}
#         # dataDict = {'distance':0.0, 'temperature': 0.0,'humidity': 0.0, 'time': ""}
#         print(dataDict)
#         print('bis hier alles ok 1\n\n\n')
#         dataDict['distance'] = (self.rshift((toBeDecoded[i]<<16),0) + self.rshift((toBeDecoded[i+1]<<8),0) + toBeDecoded[i+2])/100
        
#         print('bis hier alles ok 2\n\n\n')
#         # print(dd)
#         print(dataDict)
#         i += 3
#         dataDict['temperature'] = (self.rshift((toBeDecoded[i]<<16),0) + self.rshift((toBeDecoded[i+1]<<8), 0) + toBeDecoded[i+2])/100
#         print(dataDict)
#         i += 3
#         dataDict['humidity'] = (self.rshift((toBeDecoded[i]<<16), 0) + self.rshift((toBeDecoded[i+1]<<8), 0))/100
#         # dataDict['time'] = pd.to_datetime(fullJson['gws'][0]['time'], infer_datetime_format=True)
#         # dataDict['date'] = pd.to_datetime(fullJson['gws'][0]['time'], infer_datetime_format=True).date
#         print('bis hier alles ok 3\n\n\n')
#         # dataDict['year'] = pd.to_datetime(fullJson['gws'][0]['time'], infer_datetime_format=True).year
#         # dataDict['month'] = pd.to_datetime(fullJson['gws'][0]['time'], infer_datetime_format=True).month
#         # dataDict['day'] = pd.to_datetime(fullJson['gws'][0]['time'], infer_datetime_format=True).day
#         # pd.to_datetime().min
#         dataDict['date'] = datetime.now()
#         dataDict['time'] = pd.to_datetime(datetime.now(), infer_datetime_format=True).min
#         dataDict['year'] = pd.to_datetime(datetime.now(), infer_datetime_format=True).year
#         dataDict['month'] = pd.to_datetime(datetime.now(), infer_datetime_format=True).month
#         dataDict['day'] = pd.to_datetime(datetime.now(), infer_datetime_format=True).day

#         print('bis hier alles ok 4\n\n\n')

#         return [dataDict, list(dataDict.keys())]
def encondeFunction(hexArray):
    c = bytearray.fromhex(hexArray)
    print(c)
    c = json.loads(c)
    # c['date_time'] = pd.to_datetime(c['datetime'].apply(lambda x: x.strftime('%x, %X')), infer_datetime_format=True)
    c['time'] = pd.to_datetime(datetime.now().strftime('%x, %X'), infer_datetime_format=True)

    # c['time'] = pd.to_datetime(datetime.now(), infer_datetime_format=True).min
    c['year'] = pd.to_datetime(datetime.now(), infer_datetime_format=True).year
    c['month'] = pd.to_datetime(datetime.now(), infer_datetime_format=True).month
    c['day'] = pd.to_datetime(datetime.now(), infer_datetime_format=True).day
    return [c, list(c.keys())]


app = dash_devices.Dash(__name__,external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True

websocket.enableTrace(True)

# rr = returnRequest()

try:
    df = pd.read_csv('dataRecordings.csv')
    # print(df)
    # f, (a1, a2, a3) = plt.subplots(3, figsize=(14,round(18*0.8)))
    # a1 = df.set_index('time')[['distance']].plot(title='Distance',ax= a1, xlabel='time', grid=True, ylabel='Distance')
    # a2 = df.set_index('time')[['humidity']].plot(title='Temperature & Humidity' , ax= a2, xlabel='time', grid=True, ylabel='Humidity')
    # a3 = df.set_index('time')[['temperature']].plot(ax= a3, xlabel='time', grid=True, ylabel='Temperature')
    fig = make_subplots(rows=3, cols=1)
    # go.Figure(data = go.Scatter(x=df.index, y=df.loc[:, 3]), layout = go.Layout(title='wasup_bitch', yaxis_title='hueregeil', xaxis_title = 'waslosssjooo'))
    # go.Figure(data = go.Scatter(x=df.time, y=df.phaseTmCorr), layout = go.Layout(title='wasup_bitch', yaxis_title='hueregeil', xaxis_title = 'waslosssjooo'))
    df['time'] = pd.to_datetime(df['time'], infer_datetime_format=True)
    df['year'] = pd.to_datetime(df['year'], infer_datetime_format=True)
    df['month'] = pd.to_datetime(df['month'], infer_datetime_format=True)
    df['day'] = pd.to_datetime(df['day'], infer_datetime_format=True)

    # traces =go.Figure(data = go.Scatter(x=df.index,  y = df.distance, name='distance'),layout=go.Layout(title='distance vs. time' , yaxis_title ='distance 1/[mm]'))
    traces =go.Scatter(x=df.date,  y = df.distance, name='distance')
    fig.add_trace(traces, row=1, col=1)
    traces =go.Scatter(x=df.date,  y = df.temperature, name='humidity')
    fig.add_trace(traces, row=2, col=1)
    traces =go.Scatter(x=df.date,  y = df.humidity, name='temperature')
    fig.add_trace(traces, row=3, col=1)
    # fig['layout']['xaxis']['title']='distance 1/[mm]'
    # fig['layout']['xaxis2']['title']='humidity [pct]'
    fig['layout']['xaxis3']['title']='time'
    fig['layout']['yaxis']['title']='distance 1/[mm]'
    fig['layout']['yaxis2']['title']='humidity [pct]'
    fig['layout']['yaxis3']['title']='temperature 1/[°C]'

    fig['layout']['title']='Prototype Measurements'
    fig['layout']['height'] = 1800
    # fig.update_xaxes(type='date')

    # fig.update_yaxes(autorange = True)
    windowMarg = 1
    print([df['time'].min(),df['time'].max()])
    fig['layout']['xaxis3']['range']=[df['time'].min(),df['time'].max()]
    diff = (np.max(df['temperature'])-np.max(df['temperature']))*windowMarg
    fig['layout']['yaxis3']['range']=[np.min(df['temperature'])-diff,np.max(df['temperature'])+diff]
    diff = (np.max(df['humidity'])-np.max(df['humidity']))*windowMarg
    fig['layout']['yaxis2']['range']=[np.min(df['humidity'])-diff,np.max(df['humidity'])+diff]
    diff = (np.max(df['distance'])-np.max(df['distance']))*windowMarg
    fig['layout']['yaxis']['range']=[np.min(df['distance'])-diff,np.max(df['distance'])+diff]
    fig.update_xaxes(type = 'date')
    
    # fig.add_trace(go.Scatter(y=df.distance,x=df.index,, mode="lines"), row=1, col=1)
    # fig.add_trace(go.Bar(y=df.humidity), row=2, col=1)


    # f.tight_layout()
    # figure = plotly_plot_data(f)
    # figure.update_xaxes(type = 'date')
    # fig.update_layout(xaxis= {'autorange': True }, yaxis= {'autorange': True})
    # fig.update_yaxes(range=)

    dcc.Graph(id='temp_graph', figure=fig)
except Exception as e:
    print(e)
    pass





def on_message(ws, message):

    message = json.loads(message)

    print('bis hier alles ok 5\n\n\n')
    print(message)
    print('bis hier alles ok 5\n\n\n')
    message = message['data']
    # [message, keyList] = rr.PayloadDecoder(message['data'])
    # [message, keyList] = encondeFunction(message)
    message, keyList = encondeFunction(message)
    print(message)
    print('bis hier alles ok 6\n\n\n')
    try:
        df = pd.read_csv('dataRecordings.csv')
        print('bis hier alles ok 7\n\n\n')
        print(df)
        df = df.append(pd.DataFrame(message, columns=keyList, index=[0]), ignore_index=True )
        df['time'] = pd.to_datetime(df['time'], infer_datetime_format=True)
        df['year'] = pd.to_datetime(df['year'], infer_datetime_format=True)
        df['month'] = pd.to_datetime(df['month'], infer_datetime_format=True)
        df['day'] = pd.to_datetime(df['day'], infer_datetime_format=True)
        print('bis hier alles ok 8\n\n\n')
    except:
        df = pd.DataFrame(message, columns=keyList, index = [0])
        print('bis hier alles ok 9.5\n\n\n')
        # print(df)
    try:
        # print('bis hier alles ok 10\n\n\n')
        # f, (a1, a2, a3) = plt.subplots(3, sharex=True, figsize=(14,round(18*0.8)))
        # # f, (a1, a2, a3) = plt.subplots(3, sharex=True)
        # a1 = df.set_index('time')[['distance']].plot(title='Distance',ax= a1, xlabel='time', grid=True, ylabel='Distance')
        # a2 = df.set_index('time')[['humidity']].plot(title='Temperature & Humidity' , ax= a2, xlabel='time', grid=True, ylabel='Humidity')
        # a3 = df.set_index('time')[['temperature']].plot(ax= a3, xlabel='time', grid=True, ylabel='Temperature')
        # print('bis hier alles ok 11\n\n\n')
        # # # traces =go.Scatter(x=df['time']  y = df['distance'], name='FirstPlot',layout=dict(xaxis=dict(title='Measured distance vs. time' )), yaxis = dict(title='distance 1/[mm]'))


        # f.tight_layout()
        # print('bis hier alles ok 12\n\n\n')
        # figure = plotly_plot_data(f)
        fig = make_subplots(rows=3, cols=1)

        traces =go.Scatter(x=df.time,  y = df.distance, name='distance')
        fig.add_trace(traces, row=1, col=1)
        traces =go.Scatter(x=df.time,  y = df.humidity, name='humidity')
        fig.add_trace(traces, row=2, col=1)
        traces =go.Scatter(x=df.time,  y = df.temperature, name='temperature')
        fig.add_trace(traces, row=3, col=1)
        fig['layout']['xaxis3']['title']='time'
        fig['layout']['yaxis']['title']='distance 1/[mm]'
        fig['layout']['yaxis2']['title']='humidity [pct]'
        fig['layout']['yaxis3']['title']='temperature 1/[°C]'
        fig['layout']['title']='Prototype Measurements'
        fig['layout']['height'] = 1800
        print('bis hier alles ok 13\n\n\n')
        # figure.update_xaxes(type = 'date')
        print('bis hier alles ok 14\n\n\n')
        # fig.update_xaxes(autorange=True,type = 'date')
        # fig.update_yaxes(autorange = True)
        windowMarg = 1
        print([df['time'].min(),df['time'].max()])
        fig['layout']['xaxis3']['range']=[df['time'].min(),df['time'].max()]
        diff = (np.max(df['temperature'])-np.max(df['temperature']))*windowMarg
        fig['layout']['yaxis3']['range']=[np.min(df['temperature'])-diff,np.max(df['temperature'])+diff]
        diff = (np.max(df['humidity'])-np.max(df['humidity']))*windowMarg
        fig['layout']['yaxis2']['range']=[np.min(df['humidity'])-diff,np.max(df['humidity'])+diff]
        diff = (np.max(df['distance'])-np.max(df['distance']))*windowMarg
        fig['layout']['yaxis']['range']=[np.min(df['distance'])-diff,np.max(df['distance'])+diff]
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(type = 'date')
        # fig.add_trace(go.Scatter(y=df.distance,x=df.index,, mode="lines"), row=1, col=1)
        # fig.add_trace(go.Bar(y=df.humidity), row=2, col=1)


        # f.tight_layout()
        # figure = plotly_plot_data(f)
        # fig.update_xaxes(type = 'date')
        # fig.update_layout(xaxis= {'autorange': True }, yaxis= {'autorange': True})

        

        # pio.template['plotly_dark']
        app.push_mods({
            'temp_graph': {'figure': fig}
        })


        # plt.close()
        print("in try and push figure")
        df.to_csv('dataRecordings.csv', index=False)

            
    except Exception as e:
        print('hier nicht ok weil: e')
        print(e)




def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")
def on_open(ws):
    print("opened the websocket")
html.Div()


app.layout = html.Div([

    html.Div([
            html.Div(dcc.Markdown("__general information about the project__")),
            dcc.Input(id="shared_input_no_output", type="text", value='')],style={'width' : '150%', 'marginLeft': 130 , 'marginTop' : 140 ,'minWidth' : 1000 ,  'template': 'plotly_dark' }),
     html.Div([       
           dcc.Input(
                    id = 'size',
                    type='text',
                    value='',
                    style={'width':'100%', 'template': 'plotly_dark'}
            )],style={'marginLeft': 130 , 'marginTop' : 20 ,'minWidth' : 1000,  'template': 'plotly_dark' }
            ),   
    html.Div(id='temp'),
    dcc.Graph(id='temp_graph',animate=True), 
    html.Div('Server rebooting'),

    # html.Div("Shared slider no output"),
    # dcc.Slider(id='shared_slider_no_output', value=5, min=0, max=10, step=1, updatemode='drag'),

    # html.Div("Shared slider with output"),
    # dcc.Slider(id='shared_slider_output', value=5, min=0, max=10, step=1, updatemode='drag'),
    # html.Div(id='shared_slider_output_output'),

    # html.Div("Regular slider"),
    # dcc.Slider(id='regular_slider', value=5, min=0, max=10, step=1, updatemode='drag'),
    # html.Div(id='regular_slider_output'),


    # html.Div("Shared input with output"),
    # dcc.Input(id="shared_input_output", type="text", value=''), 
    # html.Div(id='shared_input_output_output'),

    # html.Div("Regular input"),
    # dcc.Input(id="regular_input", type="text", value=''), 
    # html.Div(id='regular_input_output'),
], style={'backgroundColor': colors['background'], 'color': colors['text'], 'height':'100vh', 'width':'100%', 'height':'100%', 'top':'0px', 'left':'0px'})


# @app.callback_shared(None, [Input('shared_slider_no_output', 'value')])
# def func(value):
#     print('Shared slider no output', value)

# @app.callback_shared(Output('shared_slider_output_output', 'children'), [Input('shared_slider_output', 'value')])
# def func(value):
#     return value

# @app.callback(Output('regular_slider_output', 'children'), [Input('regular_slider', 'value')])
# def func(value):
#     return value

@app.callback_shared(None, [Input('shared_input_no_output', 'value')])
def func(value):
    print('Shared input no output', value)

@app.callback_shared(None, [Input('size', 'value')])
def func(value):
    print('size', value)

@app.callback_shared(Output('shared_input_output_output', 'children'), [Input('shared_input_output', 'value')])
def func(value):
    return value

@app.callback(Output('regular_input_output', 'children'), [Input('regular_input', 'value')])
def func(value):
    return value

ws = websocket.WebSocketApp("wss://eu1.loriot.io/app?token=vnoi7QAAAA1ldTEubG9yaW90Lmlvq0PCtX4ipfqgsIUngoB5DA=",
                  on_message = on_message,
                  on_error = on_error,
                  on_close = on_close,
                    on_open = on_open)

# @app.push_mods_coro

if __name__ == '__main__':

    tws = Thread(target=ws.run_forever)
    tws.daemon = True
    tws.start()
    print("run server")
    app.run_server(debug=True, host='0.0.0.0', port=8765)