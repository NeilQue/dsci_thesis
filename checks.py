import pandas as pd
import page_interact as pgi
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from datetime import datetime

waterlevel_cols = ['datetime', 'water_level']
rainfall_cols = ['datetime', 'station', '1hr', '3hr', '6hr', '12hr', '24hr']

def check_col_types_wl():
    df = pd.read_csv('wl_data.csv', header=None, names=waterlevel_cols, engine='pyarrow')
    print(df.info())

def check_col_types_rf():
    df = pd.read_csv('rf_data.csv', header=None, names=rainfall_cols, engine='pyarrow')
    print(df.info())

def data_num_rf():
    rainfall_df = pd.read_csv('rf_data.csv', header=None, names=rainfall_cols, engine='pyarrow')
    # datetime_counts = rainfall_df['datetime'].value_counts()
    print(type(rainfall_df.datetime.unique()[-1]))
    
def data_num_wl():
    waterlevel_df = pd.read_csv('wl_data.csv', header=None, names=waterlevel_cols, engine='pyarrow')
    # datetime_counts = rainfall_df['datetime'].value_counts()
    print(waterlevel_df.datetime.unique())    

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
    
if __name__ == "__main__":
    # print(wait_test())
    # data_num_rf()
    # print(type(datetime.strptime('11/05/22 11:00', '%m/%d/%y %H:%M')))
    data_num_rf()