"""Line charts using plotly"""
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(56)

# x and y values
x_values = np.linspace(0,1,100)
y_values = np.random.randn(100) # random normal distribution

# data tracing
trace0 = go.Scatter(x=x_values, y=y_values+5, 
                    mode='markers', name='markers')

trace1 = go.Scatter(x=x_values,y=y_values,
                    mode='lines',name='mylines')

trace2 = go.Scatter(x=x_values,y=y_values-5,
                    mode='lines+markers',name='mylines_has_markers')

data = [trace0,trace1,trace2]

# layout
layout = go.Layout(title= 'Line charts')

# plot and save
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='line.html')
