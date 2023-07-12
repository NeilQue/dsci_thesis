import pandas as pd

waterlevel_cols = ['datetime', 'water_level']
rainfall_cols = ['datetime', 'station', '1hr', '3hr', '6hr', '12hr', '24hr']

waterlevel_df = pd.read_csv('wl_data.csv', header=None, names=waterlevel_cols, engine='pyarrow')
rainfall_df = pd.read_csv('rf_data_new.csv', header=None, names=rainfall_cols, engine='pyarrow')

final_df = pd.merge(waterlevel_df, rainfall_df, on='datetime', how='left')
final_df.to_csv('data', index=False)