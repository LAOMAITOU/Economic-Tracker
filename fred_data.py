import pandas as pd
import pandas_datareader.data as web
from datetime import date
import datetime
import plotly.express as px

data_source='fred'
default_end_date=date.today()
default_start_date=default_end_date - datetime.timedelta(days=365*10)
# default_start_date_str=datetime.datetime.strftime(default_start_date,"%Y-%m-%d")
# default_end_date_str=datetime.datetime.strftime(default_end_date,"%Y-%m-%d")


class FredData:
    def __init__(self, data_source='fred',series_id='SP500',start_date=default_start_date,end_date=default_end_date):
        self.data_source = data_source
        self.series_id = series_id
        self.start_date = start_date
        self.end_date = end_date
        self.data=pd.DataFrame()
    
    def get_data(self):
        self.data=web.DataReader(self.series_id,self.data_source,self.start_date,self.end_date).reset_index().dropna()
        self.data=self.data.rename(columns={"DATE":'Date',self.series_id:"Value"})
    
    def plot_data(self):
        fig = px.line(self.data,x='Date',y='Value',title=self.series_id)
        fig.show()
        
if __name__ == '__main__':
    fred=FredData(start_date='2020-01-01')
    fred.get_data()
    fred.plot_data()
    
