from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.options import Options
import pandas as pd
import datetime

def set_chromium():
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        return options

def set_driver(options):
    driver = webdriver.Chrome("/usr/lib/chromium/chromedriver", chrome_options=options)
    driver.get("http://spojeni.dpp.cz/")
    return driver

def get_times(when, departure, arrival, options):
    """ This function set up Selenium and visits url and returns desired times"""
    # Set up chromim and driver
    driver = set_driver(options)
    # Fill in the form
    inputElement = driver.find_element_by_id("ctlFrom_txtObject")
    inputElement.send_keys(departure)
    inputElement = driver.find_element_by_id("ctlTo_txtObject")
    inputElement.send_keys(arrival)
    driver.find_element_by_id("txtTime").clear()
    driver.find_element_by_id("txtTime").send_keys(when)
    driver.find_element_by_xpath("//input[@id='optChangesDirect']").click()
    # Send the form
    inputElement.send_keys(Keys.ENTER)
    # Waite 3 seconds for loading of the repsone page
    time.sleep(3)
    # Parse the response
    soup = BeautifulSoup(driver.page_source, "html.parser")
    # Search for time elements
    spans = soup.find_all('span', {'class' : 'date'})
    # Convert them to datetime
    casy = [pd.to_datetime(span.get_text()) for span in spans]
    # close the driver
    driver.close()
    # return times
    return casy[0] if casy else "Nenaslo sa ziadne spojenie!"
