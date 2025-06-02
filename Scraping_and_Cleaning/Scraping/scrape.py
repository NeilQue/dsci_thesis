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

def data_loaded(xpath):
    def return_value(driver):
        try:
            data = driver.find_element(By.XPATH, value=xpath).text
            if data is None:
                return False
            return data
        except StaleElementReferenceException:
            return False
            
    return return_value

def scrape_wl(date_time, data_dict):
    '''
    Scrape data from waterlevel webpage and store it in dictionary
    '''
    data = WebDriverWait(pgi.browser, 10, ignored_exceptions=ignored_exceptions).until(
        data_loaded('//*[@id="11104201"]/td[1]/span')
    )
    
    data_dict['datetime'].append(date_time)
    data_dict['water_level'].append(data)
    
def scrape_rf(date_time, data_dict):
    '''
    Scrape data from rainfall webpage and store it in dictionary
    '''
    ids = [11204101, 11105301, 11103105, 11103103, 11101101, 11203102, 11302102, 11302301,
        11102103, 11202102, 11103107, 11103104, 11101102, 11102102, 11103106, 11201101,
        11303102, 11201301, 11102105, 11204301, 11103101, 11302101, 11203101, 11102101,
        11105101, 11303101]
    
    for id in ids:
        station_name = WebDriverWait(pgi.browser, 10, ignored_exceptions=ignored_exceptions).\
            until(data_loaded(f'//*[@id="{id}"]/th/span'))
        data_list = []
            
        for i in range(3, 8):
            data = WebDriverWait(pgi.browser, 10, ignored_exceptions=ignored_exceptions).\
                until(data_loaded(f'//*[@id="{id}"]/td[{i}]/span'))
            data_list.append(data)
            
        data_dict['datetime'].append(date_time)
        data_dict['station'].append(station_name)
        data_dict['1hr'].append(data_list[0])
        data_dict['3hr'].append(data_list[1])
        data_dict['6hr'].append(data_list[2])
        data_dict['12hr'].append(data_list[3])
        data_dict['24hr'].append(data_list[4])
    
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