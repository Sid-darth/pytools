"""Line chart showing US Census Bereau"""
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# read a .csv file into a pandas dataframe:
df = pd.read_csv('Data/population.csv')

# create traces
traces = [go.Scatter(
    x = df.columns,
    y = df.loc[name],
    mode = 'markers+lines',
    name = name
) for name in df.index]

layout = go.Layout(
    title = 'Population estimates of the six New England states'
)

fig = go.Figure(data=traces, layout=layout)
pyo.plot(fig, filename='line2.html')