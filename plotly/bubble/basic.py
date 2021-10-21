"""Basic bubble plots"""
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# create df
df = pd.read_csv('../Data/mpg.csv',na_values={'horsepower':'?'})

# data
data = [go.Scatter(x=df['horsepower'],
                    y=df['mpg'],
                    text=df['name'],
                    mode='markers',
                    marker=dict(
                        size=df['weight']/100, 
                        color=df['cylinders'],
                        showscale=True
                        ))]

# layout
layout = go.Layout(title='Bubble Chart')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='bubble.html')