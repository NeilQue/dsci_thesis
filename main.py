import page_interact as pgi
import scrape
from time import sleep
from random import uniform
import pandas as pd

# The dictionary of lists where data would initially be stored after scraping
waterlevel_data = {
    'datetime': [],
    'water_level': []
}
rainfall_data = {
    'datetime': [],
    'station': [],
    '1hr': [],
    '3hr': [],
    '6hr': [],
    '12hr': [],
    '24hr': []
}

def waterlevel_loop(n):
    '''
    Conducts the process for scraping water level data with n+1 data points.
    Starts with opening the webpage for water level,
    then interacts with the page to get the initial data,
    then obtaining the data.
    The interaction with the webpage and obtaining of data is done in a loop.
    A sleep period is used to allow the webpage to load the data after interaction.
    The length of the sleep period is randomized to avoid bot detection.
    The data is stored in a dictionary of lists which would be converted into a DataFrame.
    '''
    pgi.browser.get(pgi.waterlvl_url)
    pgi.click_calendar()
    date_time = pgi.type_into('06/13/23 00:00') # returns this datetime
    pgi.click_set()
    pgi.click_search()
    sleep(1)
    scrape.scrape_wl(date_time, waterlevel_data)
    
    for i in range(n):
        date_time = pgi.click_increment(date_time)
        sleep(uniform(1, 2))
        scrape.scrape_wl(date_time, waterlevel_data)
    
    pgi.browser.quit()
    
    return pd.DataFrame(waterlevel_data)

def rainfall_loop(n):
    '''
    Conducts the process for scraping rainfall data with n+1 data points.
    Starts with opening the webpage for rainfall,
    then interacts with the page to get the initial data,
    then obtaining the data.
    The interaction with the webpage and obtaining of data is done in a loop.
    A sleep period is used to allow the webpage to load the data after interaction.
    The length of the sleep period is randomized to avoid bot detection.
    The data is stored in a dictionary of lists which would be converted into a DataFrame.
    '''
    pgi.browser.get(pgi.rainfall_url)
    pgi.click_calendar()
    date_time = pgi.type_into('06/13/23 00:00') # returns this datetime
    pgi.click_set()
    pgi.click_search()
    sleep(1)
    scrape.scrape_rf(date_time, rainfall_data)
    
    for i in range(n):
        date_time = pgi.click_increment(date_time)
        sleep(uniform(1, 2))
        scrape.scrape_rf(date_time, rainfall_data)
    
    pgi.browser.quit()
    
    return pd.DataFrame(rainfall_data)
    
if __name__ == '__main__':
    waterlevel_df = waterlevel_loop(50)
    rainfall_df = rainfall_loop(50)
    
    final_df = pd.merge(waterlevel_df, rainfall_df, on='datetime', how='left')
    final_df.to_csv('data', index=False)
    final_df.to_excel('data.xlsx', sheet_name='Sheet1')