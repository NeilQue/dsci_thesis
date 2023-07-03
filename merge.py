import pandas as pd

waterlevel_cols = ['datetime', 'water_level']
rainfall_cols = ['datetime', 'station', '1hr', '3hr', '6hr', '12hr', '24hr']

waterlevel_df = pd.read_csv('wl_data.csv', header=None, names=waterlevel_cols)
rainfall_df = pd.read_csv('rf_data.csv', header=None, names=rainfall_cols)

final_df = pd.merge(waterlevel_df, rainfall_df, on='datetime', how='left')
final_df.to_csv('data', index=False)
final_df.to_excel('data.xlsx', sheet_name='Sheet1')