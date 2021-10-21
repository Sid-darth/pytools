"""Stacked and horizontal bar charts"""
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# create DataFrame
df = pd.read_csv('../Data/mocksurvey.csv', index_col=0)

# create traces using a list comprehension
# vertical
data = [go.Bar(x=df.index, y=df[response], name=response) for 
                response in df.columns] 

# horizontal
data = [go.Bar(y=df.index, x=df[response], name=response, orientation='h') for 
                response in df.columns] 

# create layout
layout = go.Layout(title='Survey Results', barmode='stack')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig,filename='stack-bar-2.html')