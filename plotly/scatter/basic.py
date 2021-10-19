"""Scatter plots using plotly"""
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

# x,y
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

# scatter data
data = [go.Scatter(x=random_x,
                    y=random_y,
                    mode='markers',
                    marker=dict(
                        size= 5,
                        color= 'rgb(220,40,90)', # marker color
                        symbol= 'pentagon', # marker shape
                        line= {'width': 1.5} # marker border width
                    ))]

# layout
layout = go.Layout(title='Scatter Plot',
                    xaxis= dict(title= 'X Axis'),
                    yaxis= dict(title= 'Y Axis'),
                    hovermode= 'closest')
fig = go.Figure(data= data, layout= layout)

# plot and save at filename
pyo.plot(fig,filename='scatter.html')