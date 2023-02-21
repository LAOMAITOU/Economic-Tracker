import pandas_datareader as pdr
import streamlit as st
import plotly.express as px
import datetime

if __name__ == '__main__':
    # Data Source
    data_source='fred'
    
    # Ask user to input a date
    default_end_date=datetime.today()
    start_date=st.date_input("Select a start date")
    start_date_str = datetime.datetime.strftime(start_date, "%Y-%m-%d")
    end_date=st.date_input("Select a end date",value=default_end_date)
    end_date_str = datetime.datetime.strftime(end_date, "%Y-%m-%d")
    metrics=st.text_input("What are you interested in?", value='SP500')

    #  Fetch data
    df = pdr.DataReader(metrics, data_source, start_date_str,end_date_str)
    
    def plot():
        y_index=snp_data_df.columns[0]
        fig = px.line(df, x=df.index, y=y_index)
        fig.update_layout(
        title=y_index,
        xaxis_title="Date",
        yaxis_title="Value"
        )
        return fig
    
    
    st.title("US Economic Dashboard")
    st.plotly_chart(plot)
