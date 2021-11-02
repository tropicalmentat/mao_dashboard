import pandas as pd

data_path = "data/2M4AB301.csv"

df = pd.read_csv(data_path,header=1)

long_df = pd.melt(df,id_vars=["Geolocation","Commodity Description"],value_name="cpi")

new_cols = {'Geolocation':'location','Commodity Description':'commodity','variable':'month'}

long_df.rename(columns=new_cols,inplace=True)

long_df.to_csv(r'data/test.csv',index=False)
