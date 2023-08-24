import preprocessing
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = preprocessing.run("../data/Iris.csv", 0.3)
indexes = [i for i in range(df.shape[0])]

fig = px.scatter(df, x=indexes, y="SepalLengthCm")

app.layout = html.Div(children=[
    html.H1(children='A simple Scatter Plot - Dataset Iris'),
    html.Div(children='''
        Dataset download here: https://www.kaggle.com/datasets/uciml/iris?resource=download
    '''),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
