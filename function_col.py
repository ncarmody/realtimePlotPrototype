# import portion as I
from time import strftime, sleep
from datetime import datetime, timedelta, date
import sys
import os
import logging
import inspect
from inspect import currentframe, getframeinfo
import copy
import matplotlib.pyplot as plt





#ifdef newman
#type: begin ignore
# print('ichwerdegeprinted')
try:
	from plotly.tools import mpl_to_plotly
	# from plotly.tools import mpl_to_plotly
	
	from plotly.matplotlylib import mplexporter, PlotlyRenderer
	import plotly.graph_objs as go
	from plotly.offline import plot
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
def pp(obj,arg=None,lineinfo='nd',cap='s',sc='nd'):
	if arg=='t':
		obj = type(obj)

	elif arg=='d':
		obj = dir(obj)
	else:
		pass
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



def fj(ser, bed,leftRight='l',  jumpV=4, valueToPlot=None, getFirst = True, plot=False):
	if leftRight=='r':
		getFirst=False

	# pp(ser.reset_index().query(bed).index.__iter__(), 'd')
	if getFirst:
		# pp(ser.describe())
		# pp(ser.reset_index())
		# pp(ser.reset_index().query(bed))
		# pp(ser.reset_index().query(bed).index.tolist())
		first = ser.reset_index().query(bed).index.tolist()[0]
		jumpV-=1
	jump=[]
	test = None
	# pp(ser.query(bed).index, 'd')
	checkMyList = ser.reset_index().query(bed).index.tolist()
	for end, i in enumerate(ser.reset_index().query(bed).index.__iter__()):
		if not test:
			start = i
			# pp(i)
			test = 0
			pp('start')
		jump.append(i-test)
		test = i
	# pp(jump)
	jumpTemp = jump.copy()
	jump.sort()
	# pp(jump)
	# pp(jump[-jumpV:]	, sc='ddd')
	# pp([jumpTemp.index(i) for i in jump[-jumpV:]]	, sc='ddd')
	
	if leftRight=='l':
		pp([checkMyList[jumpTemp.index(i)] for i in jump[-jumpV:]]	, sc='list')
		l = [checkMyList[jumpTemp.index(i)] for i in jump[-jumpV:]]
		l.insert(0, first)
		l.sort()
		if not valueToPlot:
			valueToPlot = bed.split('>')[1]
		if plot:
			a = ser[valueToPlot].plot(linewidth=0.5, color='red')
			ser['index'] = ser.index.values
			a = ser.query(bed).plot(ax = a, linewidth=0.5, color='green', y=valueToPlot,x ='index',  kind='scatter')
			a = ser.iloc[l].plot(ax = a, linewidth=0.5, color='blue', y=valueToPlot,x ='index',  kind='scatter')
			plt.show()
		# l.sort()
		l.reverse()
		return l

	elif leftRight=='r':
		pp([checkMyList[jumpTemp.index(i)-1] for i in jump[-jumpV:]]	, sc='list')
		l = [checkMyList[jumpTemp.index(i)-1] for i in jump[-jumpV:]]
		
		l.sort()
		if not valueToPlot:
			valueToPlot = bed.split('>')[1]
			pp(valueToPlot)
		if plot:
			a = ser[valueToPlot].plot(linewidth=0.5, color='red')
			ser['index'] = ser.index.values
			a = ser.query(bed).plot(ax = a, linewidth=0.5, color='green', y=valueToPlot,x ='index',  kind='scatter')
			a = ser.iloc[l].plot(ax = a, linewidth=0.5, color='blue', y=valueToPlot,x ='index',  kind='scatter')
			plt.show()
				
		# l.sort()
		l.reverse()
		return l

def invFunc(searchLambdaX, invF, searchInInvF, giveInInvF):
	# pp(invF, sc='dddd')
	# pp(invF.columns, sc='dddd')
	# pp(invF.iloc[(invF[search]-arg).abs().argsort()[:2]])
	# pp(invF.iloc[(invF[search]-arg).abs().argsort()[:2]][give].mean())
	# pp(invF.iloc[(invF[searchName]-searchArray).abs().argsort()[:2]])
	return invF.iloc[(invF[searchInInvF]-searchLambdaX).abs().argsort()[:2]][giveInInvF].mean()
def make_patch_spines_invisible(ax, bottomTop='bottom', shift=-0.04, color='blue', xOrY='x', labelpad=5):

		ax.spines[bottomTop].set_position(('axes', shift))
		ax.tick_params(axis=xOrY, colors=color)

		if xOrY=='x':
			ax.xaxis.label.set_color(color)

			ax.set_frame_on(True)
			ax.patch.set_visible(False)
			for sp in ax.spines.values():
				sp.set_visible(False)

			ax.spines[bottomTop].set_visible(True)
			ax.xaxis.set_label_position(bottomTop)
			ax.xaxis.set_ticks_position(bottomTop)
			ax.set_xlabel(ax.get_xlabel(), labelpad=labelpad, color=color)
		else:
			ax.yaxis.label.set_color(color)

			ax.set_frame_on(True)
			ax.patch.set_visible(False)
			for sp in ax.spines.values():
				sp.set_visible(False)

			ax.spines[bottomTop].set_visible(True)
			ax.yaxis.set_label_position(bottomTop)
			ax.yaxis.set_ticks_position(bottomTop)
			ax.set_ylabel(ax.get_ylabel(), labelpad=labelpad, color=color)


def iLocFinder(df, queryString, showRangeAroundTarget=0, printResult=False):
	
	
	loc = df.index.get_loc(df.query(queryString).iloc[0].name)
	# else:
	# 	if len(df.query(queryString).index.values)<5:
	# 		for i in df.query(queryString).index.values:
	# 			dfs = df.iloc
	if showRangeAroundTarget:
		if printResult:
			pp(df.iloc[loc-showRangeAroundTarget:loc+showRangeAroundTarget])
			pp(loc)
		return [df.iloc[loc-showRangeAroundTarget:loc+showRangeAroundTarget], loc]
	else:
		if printResult:
			pp(df.iloc[loc])
			pp(loc)
		return [df.iloc[loc], loc]