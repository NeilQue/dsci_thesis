import pandas as pd

rainfall_cols = ['datetime', 'station', '1hr', '3hr', '6hr', '12hr', '24hr']

rainfall_df = pd.read_csv('rf_data.csv', header=None, names=rainfall_cols, engine='pyarrow')
datetime_counts = rainfall_df['datetime'].value_counts()
print(datetime_counts[datetime_counts!=26])