import page_interact as pgi
import scrape
from time import sleep
from random import uniform
import pandas as pd
from datetime import datetime
from pprint import pprint

# The dictionary of lists where data would initially be stored after scraping
waterlevel_data = {
    'datetime': [],
    'water_level': []
}

def waterlevel_loop(start, end):
    '''
    Conducts the process for scraping hourly water level data from start to end.
    start should be a later date than end.
    start and end should be in the format 09(month)/13(day)/23(year) 13:45
    Starts with opening the webpage for water level,
    then interacts with the page to get the initial data,
    then obtaining the data.
    The interaction with the webpage and obtaining of data is done in a loop.
    A sleep period is used to allow the webpage to load the data after interaction.
    The length of the sleep period is randomized to avoid bot detection.
    The data is stored in a dictionary of lists which would be converted into a DataFrame.
    '''
    start_date = datetime.strptime(start, '%m/%d/%y %H:%M')
    end_date = datetime.strptime(end, '%m/%d/%y %H:%M')
    diff = start_date - end_date
    num_hours = diff.days*24 + diff.seconds//3600
    
    pgi.browser.get(pgi.waterlvl_url)
    pgi.click_calendar()
    date_time = pgi.type_into(start_date) # returns this datetime
    pgi.click_set()
    pgi.click_search()
    scrape.scrape_wl(date_time, waterlevel_data)
    
    try:
        for i in range(num_hours):
            date_time = pgi.click_increment(date_time)
            scrape.scrape_wl(date_time, waterlevel_data)
    except Exception as e:
        print(f'{type(e)}: {e}\nstopped at {date_time}')
    finally:
        pgi.browser.quit()        
        return pd.DataFrame(waterlevel_data)

if __name__ == "__main__":
    print(datetime.now().isoformat())
    waterlevel_df = waterlevel_loop('11/01/22 00:00', '09/01/22 01:00')
    waterlevel_df.to_csv('wl_data.csv', index=False, header=False, mode='a')
    print(datetime.now().isoformat())
        
    # for 24hours worth of data: 28s, 19s. 20s
    # 1 week data: ~1min, ~2mins