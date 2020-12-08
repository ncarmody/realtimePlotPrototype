import dash_devices
from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from function_col import pp, relPath
from dash_devices.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from threading import Timer
import socket
import sys
import sockettest
sys.path.insert(0,"C:/Users/nicol/Desktop/python/dashDevices/dash_devices/sockettest")
app = Flask(__name__)
app.layout = html.Div([
    sockettest.sockettest(),
    html.Progress(id='progress', max=10, value=0), 
	dcc.Slider(id='slider', value=0, min=0, max=10, step=1),
    html.Div(id='divspace')
])


def change(id, val):
	socket.emit('call', {'id': id, 'val': val})


def timerCallback():
	Timer(1.0, timerCallback).start()
	change('slider', {'value': timerCallback.i})
	change('progress', {'value': timerCallback.i})
	change('divspace', {'children': 'hello ' + str(timerCallback.i)})
	timerCallback.i += 1;
	if timerCallback.i>10:
		timerCallback.i = 0


timerCallback.i = 0

if __name__ == '__main__':
	timerCallback()
	socket.run(server, debug=False, port=5000, host='0.0.0.0')