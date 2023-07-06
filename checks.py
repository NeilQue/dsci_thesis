import pandas as pd
import page_interact as pgi
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

def data_num():
    rainfall_cols = ['datetime', 'station', '1hr', '3hr', '6hr', '12hr', '24hr']

    rainfall_df = pd.read_csv('rf_data.csv', header=None, names=rainfall_cols, engine='pyarrow')
    datetime_counts = rainfall_df['datetime'].value_counts()
    print(datetime_counts[datetime_counts!=26])
    
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
    print(wait_test())