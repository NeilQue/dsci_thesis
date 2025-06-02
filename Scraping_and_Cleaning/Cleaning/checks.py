import pandas as pd
import page_interact as pgi
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from datetime import datetime
from scrape import data_loaded

waterlevel_cols = ['datetime', 'water_level']
rainfall_cols = ['datetime', 'station', '1hr', '3hr', '6hr', '12hr', '24hr']

def check_col_types_wl(wl_file):
    df = pd.read_csv(wl_file, header=None, names=waterlevel_cols, engine='pyarrow')
    print(df.info())

def check_col_types_rf(rf_file):
    df = pd.read_csv(rf_file, header=None, names=rainfall_cols, engine='pyarrow')
    print(df.info())
    
def check_col_types(file):
    df = pd.read_csv(file, engine='pyarrow')
    print(df.info())

def data_num_rf(rf_file):
    rainfall_df = pd.read_csv(rf_file, header=None, names=rainfall_cols, engine='pyarrow')
    datetime_counts = rainfall_df['datetime'].value_counts()
    print(datetime_counts[datetime_counts!=26])
    # for row in rainfall_df.datetime.unique():
        # print(row)
    
def data_num_wl(wl_file):
    waterlevel_df = pd.read_csv(wl_file, header=None, names=waterlevel_cols, engine='pyarrow')
    datetime_counts = waterlevel_df['datetime'].value_counts() 
    print(waterlevel_df)

def wait_test():
    pgi.browser.get(pgi.waterlvl_url)
    # pgi.browser.get(pgi.rainfall_url)
    ignored_exceptions = [NoSuchElementException, StaleElementReferenceException]
    data = WebDriverWait(pgi.browser, 5, ignored_exceptions=ignored_exceptions).until(
        lambda d: d.find_element(By.XPATH, value='//*[@id="11104201"]/td[1]/span').text
    )
    # data = WebDriverWait(pgi.browser, 5, ignored_exceptions=ignored_exceptions).until(
        # lambda d: d.find_element(By.XPATH, '//*[@id="11303101"]/td[7]/span').text
    # )
    return data
    
def get_ids():
    pgi.browser.get(pgi.rainfall_url)
    data_table = pgi.browser.find_element(By.XPATH, value='//*[@id="tblList"]')
    rows = data_table.find_elements(By.TAG_NAME, 'tr')
    
    for row in rows:
        print(row.get_attribute('id'))
    
def check_functionality():
    pgi.browser.get(pgi.rainfall_url)
    ignored_exceptions = [NoSuchElementException, StaleElementReferenceException]
    
    id = 11204101
    
    for i in range(3, 8):
        data = WebDriverWait(pgi.browser, 10, ignored_exceptions=ignored_exceptions).\
            until(data_loaded(f'//*[@id="{id}"]/td[{i}]/span'))
        print(data)

if __name__ == "__main__":
    check_col_types('data_2022.csv')