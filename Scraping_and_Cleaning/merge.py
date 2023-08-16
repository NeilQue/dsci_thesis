import pandas as pd

waterlevel_cols = ['datetime', 'water_level']
rainfall_cols = ['datetime', 'station', '1hr', '3hr', '6hr', '12hr', '24hr']
combined_cols = ['datetime', 'water_level', 'station', '1hr', '3hr', '6hr', '12hr', '24hr']

def merge_files(wl_file, rf_file, output_file):
    waterlevel_df = pd.read_csv(wl_file, header=None, names=waterlevel_cols, engine='pyarrow')
    rainfall_df = pd.read_csv(rf_file, header=None, names=rainfall_cols, engine='pyarrow')

    final_df = pd.merge(waterlevel_df, rainfall_df, on='datetime', how='left')
    final_df.to_csv(output_file, index=False)
    
def concat_files(file1, file2, file3):
    df_1 = pd.read_csv(file1, engine='pyarrow')
    df_2 = pd.read_csv(file2, engine='pyarrow')
    df_3 = pd.read_csv(file3, engine='pyarrow')
    
    data_2022 = pd.concat([df_1, df_2, df_3], ignore_index=True)
    data_2022.sort_values(by=['datetime', 'station'], inplace=True, ignore_index=True)
    data_2022.to_csv('data_2022.csv', index=False)
    
if __name__ == "__main__":
    concat_files('data_p1.csv', 'data_p2.csv', 'data_p3.csv')