import pandas as pd
from dotenv import load_dotenv
import pandas_gbq
import numpy as np


def convert_str_to_date(dataframe):
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
    
    # TODO: Fix rounding of actual cpi values when uploaded to GBQ
    # probably caused by conversion of datatypes
    pandas_gbq.to_gbq(long_df, "staging.test",project_id="mao-dw",if_exists="replace")


if __name__=="__main__":
    main()
