import pandas as pd
import numpy as np
from dash import Dash, html, dcc, Input, Output, dash_table, callback, State
import dash_bootstrap_components as dbc
from fred_data import FredData

app = Dash(__name__, external_stylesheets=['/assets/style.css'])

app.layout = html.Div(
    children=[
        html.H1('Economic Tracker', className='text'),
        html.H4(id='Name-Of-Graph', className='text'),
        dcc.Graph(id='Graph'),
        dcc.Interval(id='interval-component', interval=10*1000, n_intervals=0)
    ],
    className='background'
)


@app.callback(
    [Output('Name-Of-Graph', 'children'), Output('Graph', 'figure')],
    [Input('interval-component', 'n_intervals')]
)
def update_graph(n):
    fred_instance = FredData()
    fred_instance.get_data(name='S&P500', series_id='SP500')
    name_of_graph = fred_instance.name
    fig = fred_instance.plot_data()
    return name_of_graph, fig


if __name__ == '__main__':
    app.run_server(debug=True)
