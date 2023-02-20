import streamlit as st
import os
import pandas as pd
import yfinance as yf
import datetime
import requests
import plotly.graph_objects as go
from pandas_datareader import data as wb
import pandas_datareader as pdr
import datetime
import requests

# Today=datetime.date.today()
# start_date=datetime.date(2000,01,01)
# diff=start_date-Today
Start='2000-01-01'

VIX=wb.DataReader('^VIX', data_source='yahoo', start=Start)
VIX['Returns']=VIX['Close'].pct_change()

st.title('Economic Tracking Monitor')
option=st.sidebar.selectbox("Select a Dashboard:",('VIX','S&P'),0)

if option=='VIX':
    st.header('VIX')
    st.write('This dashboard screens VIX')
    fig1=go.Figure()
    fig1.add_trace(go.Scatter(x=VIX.index, y=VIX['Close'],mode='lines',name='VIX'))
    fig1.update_layout(height=600,width=400)
    st.plotly_chart(fig1,use_container_width=True)
    
    st.dataframe(VIX)
    st.write('Source: Yahoo Finance')