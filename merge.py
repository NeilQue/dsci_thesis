import pandas as pd
import waterlevel_scraping as wls
import rainfall_scraping as rfs
import scrape_rf

waterlevel_df = wls.waterlevel_loop(23)
rainfall_df = rfs.rainfall_loop(23)

final_df = pd.merge(waterlevel_df, rainfall_df, on='datetime', how='left')
final_df.to_csv('data', index=False)
final_df.to_excel('data.xlsx', sheet_name='Sheet1')