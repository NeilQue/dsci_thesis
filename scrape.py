from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import page_interact as pgi
from datetime import datetime
from pprint import pprint
from time import sleep
import pandas as pd
from random import uniform

rainfall_data = {
    'datetime': [],
    'station': [],
    '1hr': [],
    '3hr': [],
    '6hr': [],
    '12hr': [],
    '24hr': []
}

ignored_exceptions = [NoSuchElementException, StaleElementReferenceException]

def scrape_wl(date_time, data_dict):
    '''
    Scrape data from waterlevel webpage and store it in dictionary
    '''
    data = WebDriverWait(pgi.browser, 5, ignored_exceptions=ignored_exceptions).until(
        lambda d: d.find_element(By.XPATH, value='//*[@id="11104201"]/td[1]/span').text
    )
    
    data_dict['datetime'].append(date_time)
    data_dict['water_level'].append(data)
    
def scrape_rf(date_time, data_dict):
    '''
    Scrape data from rainfall webpage and store it in dictionary
    '''
    WebDriverWait(pgi.browser, 5, ignored_exceptions=ignored_exceptions).until(
        lambda d: d.find_element(By.XPATH, '//*[@id="11303102"]/td[4]/span').text
    )
    sleep(uniform(0.25, 0.5))
    data_table = pgi.browser.find_element(By.XPATH, value='//*[@id="tblList"]')
    rows = data_table.find_elements(By.TAG_NAME, 'tr')
    
    for row in rows:
        station_container = row.find_element(By.TAG_NAME, 'th')
        station_name = station_container.find_element(By.TAG_NAME, 'span').text
        data_list = []
        data = row.find_elements(By.TAG_NAME, 'td')
        
        for point in data:
            content = point.find_element(By.TAG_NAME, 'span').text
            data_list.append(content)
            
        data_dict['datetime'].append(date_time)
        data_dict['station'].append(station_name)
        data_dict['1hr'].append(data_list[2])
        data_dict['3hr'].append(data_list[3])
        data_dict['6hr'].append(data_list[4])
        data_dict['12hr'].append(data_list[5])
        data_dict['24hr'].append(data_list[6])
    
if __name__ == '__main__':
    print(datetime.now().isoformat())
    pgi.browser.get("http://121.58.193.173:8080/rainfall/table.do")
    print(datetime.now().isoformat())
    pgi.click_calendar()
    # wait.until(
        # expected_conditions.visibility_of_element_located(
            # (By.XPATH, '//*[@id="dtBox"]/div/div/div/div')
        # )
    # )
    # print(pgi.get_date())
    date_time = pgi.type_into('06/26/23 17:20')
    pgi.click_set()
    # pgi.click_calendar()
    # wait.until(
        # expected_conditions.visibility_of_element_located(
            # (By.XPATH, '//*[@id="dtBox"]/div/div/div/div')
        # )
    # )
    # print(pgi.get_date())
    pgi.click_search()
    sleep(1)
    scrape_rf(date_time, rainfall_data)
    print(datetime.now().isoformat())
    date_time = pgi.click_increment(date_time)
    sleep(1)
    scrape_rf(date_time, rainfall_data)
    print(datetime.now().isoformat())
    print(pd.DataFrame(rainfall_data))
    print(datetime.now().isoformat())