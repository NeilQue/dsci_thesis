import page_interact as pgi
import scrape
# from time import sleep
# from random import uniform
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from datetime import datetime
from pprint import pprint

rainfall_data = {
    'datetime': [],
    'station': [],
    '1hr': [],
    '3hr': [],
    '6hr': [],
    '12hr': [],
    '24hr': []
}

ignored_exceptions = [NoSuchElementException, ElementClickInterceptedException]

def rainfall_loop(start, end):
    '''
    Conducts the process for scraping hourly rainfall data from start to end.
    start should be a later date than end.
    start and end should be in the format 09(month)/13(day)/23(year) 13:45
    Starts with opening the webpage for rainfall,
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
    
    pgi.browser.get(pgi.rainfall_url)
    pgi.click_calendar()
    date_time = pgi.type_into(start_date) # returns this datetime
    pgi.click_set()
    pgi.click_search()
    scrape.scrape_rf(date_time, rainfall_data)
    
    try:
        for i in range(num_hours):
            date_time = pgi.click_increment(date_time)
            scrape.scrape_rf(date_time, rainfall_data)
    except Exception as e:
        print(f'{type(e)}: {e}\nstopped at {date_time}')
    finally:
        pgi.browser.quit()
        return pd.DataFrame(rainfall_data)
	
if __name__ == "__main__":
    print(datetime.now().isoformat())
    rainfall_df = rainfall_loop('12/26/22 13:00', '12/26/22 13:00')
    rainfall_df.to_csv('rf_data.csv', index=False, header=False, mode='a')
    print(datetime.now().isoformat())
        
    # for 24 days worth of data: 6mins
    # for almost 3.5 days: 5mins
    # for ~5 days: 17mins
    # ~2days: 2mins
    # for ~5 days: ~13mins 
    # for 6-7 days: ~16mins