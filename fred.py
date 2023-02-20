import pandas_datareader as pdr
import datetime

if __name__ == '__main__':
    #  Set start date
    start_date = datetime.date(2018, 1, 1)
    start_date_str = datetime.datetime.strftime(start_date, "%Y-%m-%d")

    #  Federal Reserve Economic Data Service
    data_source = 'fred'
    treasury_yield_code = 'DGS10' #  10-year Treasury Rate
    unemployment_rate_code = 'UNRATE'
    gdp_code = 'GDPC1'
    mortgage_code = 'MORTGAGE30US'
    snp_code = 'SP500'
    personal_savings_rate_code = 'PSAVERT'
    cpi_series = 'CPIAUCSL'

    #  Fetch data
    treasury_yield_df = pdr.DataReader(treasury_yield_code, data_source, start_date)
    unemployment_rate_df = pdr.DataReader(unemployment_rate_code, data_source, start_date)
    mortgate_data_df = pdr.DataReader(mortgage_code, data_source, start_date)
    snp_data_df = pdr.DataReader(snp_code, data_source, start_date)
    savings_df = pdr.DataReader(personal_savings_rate_code, data_source, start_date)
    cpi_df = pdr.DataReader(cpi_series, data_source, start_date)
    
    #  Return data
    print(treasury_yield_df)
