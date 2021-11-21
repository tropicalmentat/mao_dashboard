import pandas as pd
from dotenv import load_dotenv
import pandas_gbq
import numpy as np


def convert_str_to_date():
    pass

def remove_dots_location(dataframe):
    # remove "." from location field
    dataframe.iloc[:,0] = dataframe.iloc[:,0].str.replace(".","")


def remove_dots_cpi(dataframe):
    # remove ".." from cpi field
    # removing "." will remove the decimal point

    dataframe.iloc[:,3] = dataframe.iloc[:,3].str.replace("..",np.nan)
    
def main():
    load_dotenv()
    
    data_path = "data/2M4AB301.csv"
    
    df = pd.read_csv(data_path,header=1)
    
    long_df = pd.melt(df,id_vars=["Geolocation","Commodity Description"],value_name="cpi")
    
    new_cols = {'Geolocation':'location','Commodity Description':'commodity','variable':'month'}
    
    long_df.rename(columns=new_cols,inplace=True)

    print(long_df.dtypes)
    
    print(long_df)

    remove_dots(long_df)
    
#    long_df.to_csv(r'data/test.csv',index=False)
    
    print(long_df)
#    pandas_gbq.to_gbq(long_df, "staging.test",project_id="mao-dw",if_exists="replace")


if __name__=="__main__":
    main()
