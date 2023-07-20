import pandas as pd

waterlevel_cols = ['datetime', 'water_level']
rainfall_cols = ['datetime', 'station', '1hr', '3hr', '6hr', '12hr', '24hr']

def parse_datetime_col():
    rainfall_df = pd.read_csv('rf_data.csv', header=None, names=rainfall_cols, engine='pyarrow')
    rainfall_df['datetime'] = pd.to_datetime(rainfall_df['datetime'], format='mixed', dayfirst=True)
    rainfall_df.sort_values(by=['datetime'], ascending=False, inplace=True, ignore_index=True)
    rainfall_df.to_csv('rf_data_new.csv', index=False, header=False, mode='w')
    
if __name__ == "__main__":
    parse_datetime_col()
    print('yay')