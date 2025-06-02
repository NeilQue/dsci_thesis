from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from datetime import datetime
from datetime import timedelta
from time import sleep

# instantiate driver needed to interact with browser
options = webdriver.ChromeOptions()
options.headless = True
browser = webdriver.Chrome(service=Service(ChromeDriverManager(version='114.0.5735.90').install()), options=options)

# urls where data is contained
rainfall_url = "http://121.58.193.173:8080/rainfall/table.do"
waterlvl_url = "http://121.58.193.173:8080/water/table.do"

ignored_exceptions = [NoSuchElementException, ElementClickInterceptedException]

def wait_loading():
    sleep(0.1)
    WebDriverWait(browser, 20, ignored_exceptions=ignored_exceptions).until(
        expected_conditions.text_to_be_present_in_element_attribute(
            (By.ID, 'loading'), 'style', 'display: none;'
        )
    )

def type_into(date_time):
    '''
    Type Date and Time into webpage
    date_time is a datetime object parsed from input
    Also returns datetime object for data storage
    '''
    yr = browser.find_element(By.XPATH, 
        value='//*[@id="dtBox"]/div/div/div/div/div[2]/div[1]/div/input')
    mon = browser.find_element(By.XPATH, 
        value='//*[@id="dtBox"]/div/div/div/div/div[2]/div[2]/div/input')
    day = browser.find_element(By.XPATH,
        value='//*[@id="dtBox"]/div/div/div/div/div[2]/div[3]/div/input')
    hr = browser.find_element(By.XPATH,
        value='//*[@id="dtBox"]/div/div/div/div/div[2]/div[4]/div/input')
    min = browser.find_element(By.XPATH,
        value='//*[@id="dtBox"]/div/div/div/div/div[2]/div[5]/div/input')
        
    yr.click()
    yr.send_keys(str(date_time.year))
    mon.click()
    mon.send_keys(str(date_time.month))
    day.click()
    day.send_keys(str(date_time.day))
    hr.click()
    hr.send_keys(str(date_time.hour))
    min.click()
    min.send_keys(str(date_time.minute))
    yr.click()
    
    return date_time
    
def click_calendar():
    '''
    Click calendar icon for pop-up
    '''
    wait_loading()
    
    button = browser.find_element(By.XPATH, 
        value='//*[@id="content"]/div/div[1]/div[1]/div/span[1]/span'
    )
    button.click()

def click_increment(date_time):
    '''
    Click [-60] button for hourly intervals
    date_time obtained from previous iteration
    Returns new datetime by subtracting an hour
    '''
    wait_loading()
    
    button = browser.find_element(By.XPATH, 
        value='//*[@id="content"]/div/div[1]/div[1]/div/span[2]/a'
    )
    button.click()
    
    return date_time - timedelta(hours=1)
    
def click_set():
    '''
    Click [Set] button to set initial date
    '''
    button = browser.find_element(By.XPATH,
        value='//*[@id="dtBox"]/div/div/div/div/div[3]/a')
    button.click()
    
def click_search():
    '''
    Click search icon to update table
    '''
    button = browser.find_element(By.XPATH,
        value='//*[@id="content"]/div/div[1]/div[1]/div/span[1]/a')
    button.click()
  
def get_date():
    '''
    Get the date set on the webpage
    Use for testing for now
    '''
    date = browser.find_element(By.XPATH,
        value='//*[@id="dtBox"]/div/div/div/div/div[1]/div[2]').text
        
    return date
  
if __name__ == '__main__':
    pass
    # print((datetime.now().isoformat()))
    # browser.get("http://121.58.193.173:8080/rainfall/table.do")
    # print((datetime.now().isoformat()))
    # click_calendar()
    # date_time = type_into('06/26/23 17:20')
    # print(type(date_time.year), date_time.month, date_time.day, date_time.hour, date_time.minute)
    
# String to datetime
# datetime_name = datetime.strptime(string, format)
# cheatsheet: https://strftime.org/

# datetime to String
# datetime_name.strftime(format)