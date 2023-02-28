from dash import Dash, html, dcc, Input, Output, dash_table, callback, State
import dash_bootstrap_components as dbc

def market_tab():
    content = html.Div(
        [
            html.H1('Economic Tracker',className='title'),
            html.Div(
              dbc.Row(
                  [
                      dbc.Col(
                        html.Div(
                            [
                                html.P(id='Name-Of-Graph-1', className='para'),
                                dcc.Graph(id='Graph-1', className='graph'),
                                dcc.Interval(id='interval-component',
                                             interval=10*1000, n_intervals=0)
                            ]
                        ), width=4
                    ),
                    dbc.Col(
                        html.Div(
                            [
                                html.P(id='Name-Of-Graph-2', className='para'),
                                dcc.Graph(id='Graph-2', className='graph'),
                                dcc.Interval(id='interval-component',
                                             interval=10*1000, n_intervals=0)
                            ]
                        ), width=4
                    ),
                    dbc.Col(
                        html.Div(
                            [
                                html.P(id='Name-Of-Graph-3', className='para'),
                                dcc.Graph(id='Graph-3', className='graph'),
                                dcc.Interval(id='interval-component',
                                             interval=10*1000, n_intervals=0)
                            ]
                        ), width=4
                    )
                  ]
              ) 
            )
        ],
        className='background'
    )
    
    return content
