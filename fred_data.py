import pandas as pd
import pandas_datareader.data as web
from datetime import date
import datetime
import plotly.express as px

data_source='fred'
default_end_date=date.today()
default_start_date=default_end_date - datetime.timedelta(days=365*1)
# default_start_date_str=datetime.datetime.strftime(default_start_date,"%Y-%m-%d")
# default_end_date_str=datetime.datetime.strftime(default_end_date,"%Y-%m-%d")


class FredData:
    def __init__(self):
        self.data_source = 'fred'
    
    def get_data(self,name,series_id,start_date=default_start_date,end_date=default_end_date):
        self.name=name
        self.series_id = series_id
        self.start_date = start_date
        self.end_date = end_date
        self.data=web.DataReader(self.series_id,self.data_source,self.start_date,self.end_date).reset_index().dropna()
        self.data=self.data.rename(columns={"DATE":'Date',self.series_id:"Value"})
    
    def plot_data(self):
        fig = px.line(self.data,x='Date',y='Value')
        
        fig.update_layout(
            xaxis=dict(tickfont=dict(family='Goudy Old Style',color='#EEEEEE',size=14), tickformat='%Y-%m',showgrid=False),
            yaxis=dict(tickfont=dict(family='Goudy Old Style',color='#EEEEEE',size=14),showgrid=False),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            title=None,
            margin=dict(l=0, r=0, t=0, b=0, pad=0)
        )
        
        fig.update_traces(line=dict(color='#CF0A0A'))
        
        fig.update_xaxes(title='', showticklabels=True)
        fig.update_yaxes(title='', showticklabels=True)
        return fig
        
if __name__ == '__main__':
    fred=FredData()
    fred.get_data(name='NASDAQ',series_id='NASDAQCOM',start_date='2020-01-01')
    f=fred.plot_data()
    f.show()
    
