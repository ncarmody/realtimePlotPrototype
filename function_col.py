# import portion as I
from time import strftime, sleep
from datetime import datetime, timedelta, date
import sys
import os
import logging
import inspect
from inspect import currentframe, getframeinfo
import copy




#ifdef newman
#type: begin ignore
# print('ichwerdegeprinted')
try:
	from plotly.tools import mpl_to_plotly
	# from plotly.tools import mpl_to_plotly

	from plotly.matplotlylib import mplexporter, PlotlyRenderer
	import plotly.graph_objs as go
	from plotly.offline import plot
	from plotly.subplots import make_subplots
	def plotly_plot_data(fig):


	    ax_list = fig.axes
	    
	    for ax in ax_list:
	    	if ax.get_legend():
	
		        ax.get_legend().remove()

	    plotly_fig = mpl_to_plotly(fig)
	    
	    legend = go.layout.Legend(
	        x=0.05,
	        y=0.95
	    )
	    plotly_fig.update_layout(showlegend=True, legend=legend)
	    return plotly_fig
	    # plotly.offline.plot(plotly_fig, filename="plotly_strain.html")
	   	# print("plotly_conversion_function is available")
except:
		pass
#type: end ignore

def combine_interval(intervals, element_to_search_for):

	return [1 for i, element in enumerate(intervals) if element_to_search_for in element]

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# printpropertiefunction->pp
def pp(obj,lineinfo='nd',cap='s',sc='nd'):
	
	# yield getframeinfo(currentframe())
	# frameinfo = getframeinfo(currentframe())

	# print(frameinfo.filename, frameinfo.lineno)
	# print('lineifo:::',lineinfo)
	obj_name=retrieve_name(obj)
	if sc=='nd':
		sc=''
	if lineinfo=='nd':
		lineinfo = ''

	# try:	
	# 	raise Exception
	# except:
	# 	line = int(sys.exc_info()[2].tb_lineno)+3
	string = "line: " +'\n'+5*sc+':---> ' +obj_name+': ----> '
	string = '\n'+5*sc+':---> ' +obj_name+': ----> \n'
	if cap == 'b':
		string = string.upper()

	print(string,obj)

# adress = str(sys.path.insert(0,os.path.relpath('../CsvData')))
# adress = str(os.path.relpath('../CsvData'))
# adress = str(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'CsvData')))
# adress = str(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '', 'CsvData')))

# print(adress)
def relPath(folder, operation = '..'):
	# either .. for prev. folder
	# or foldername to go further for operation
	# folder sollte bei operation=none ein filename sein
	# print(os.getcwd())
	# print(os.path.abspath(os.path.join(os.path.dirname( __file__ ), operation, folder)))

	print(os.path.abspath(os.path.join(os.path.dirname( __file__ ), operation, folder)))
	sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname( __file__ ), operation, folder)))		
	return str(os.path.abspath(os.path.join(os.path.dirname( __file__ ), operation, folder)))

def retrieve_name(var):
        """
        Gets the name of var. Does it from the out most frame inner-wards.
        :param var: variable to get name from.
        :return: string
        """
        for fi in reversed(inspect.stack()):
            names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
            if len(names) > 0:
                return names[0]
# d={'k':1}

# def li():
# 	return getframeinfo(currentframe())



