import page_interact as pgi
import scrape
from time import sleep
from random import uniform
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
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

wait = WebDriverWait(pgi.browser, 5).until_not(
    expected_conditions.visibility_of_element_located(
        (By.ID, 'loading')
    )
)

def rainfall_loop(n):
    '''
    Conducts the process for scraping rainfall data worth n+1 hours.
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
    date_time = pgi.type_into('12/31/22 00:00') # returns this datetime
    pgi.click_set()
    pgi.click_search()
    wait
    sleep(uniform(0.5, 1))
    scrape.scrape_rf(date_time, rainfall_data)
    print('1')
    
    for i in range(n):
        date_time = pgi.click_increment(date_time)
        wait
        sleep(uniform(0.5, 1))
        scrape.scrape_rf(date_time, rainfall_data)
        print(f"{i+2}")
    
    pgi.browser.quit()
    
    return pd.DataFrame(rainfall_data)
	
if __name__ == "__main__":
    rainfall_df = rainfall_loop(23)
    pprint(rainfall_df)