import pandas as pd
from dotenv import load_dotenv
import pandas_gbq
import numpy as np


def wide_to_long(dataframe):
    pass


def convert_str_to_date(dataframe):

#    dataframe['month'] = dataframe.month + ' 01'

    dataframe['month'] = pd.to_datetime(dataframe.month,errors='coerce',format="%Y %b")

    print(dataframe.month)

def rename_columns(dataframe):
    pass


def remove_dots_location(dataframe):
    # remove "." from location field

    dataframe.iloc[:,0] = dataframe.iloc[:,0].str.replace(".","")


def remove_dots_cpi(dataframe):
    # remove ".." from cpi field
    # removing "." will remove the decimal point

    dataframe['cpi'] = pd.to_numeric(dataframe.cpi,errors='coerce')


def main():
    load_dotenv()
    
    data_path = "data/2M4AB301.csv"
    
    df = pd.read_csv(data_path,header=1)
    
    long_df = pd.melt(df,id_vars=["Geolocation","Commodity Description"],value_name="cpi")
    
    new_cols = {'Geolocation':'location','Commodity Description':'commodity','variable':'month'}
    
    long_df.rename(columns=new_cols,inplace=True)

    remove_dots_location(long_df)
    
    remove_dots_cpi(long_df)

    convert_str_to_date(long_df)
    
    pandas_gbq.to_gbq(long_df, "staging.test",project_id="mao-dw",if_exists="replace")


if __name__=="__main__":
    main()
