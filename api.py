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

def get_times(when, departure, arrival):
    """ This function set up Selenium and visits url and returns desired times"""
    # Set up chromim and driver
    options = set_chromium()
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
    # Waite 5 seconds for loading of the repsone page
    time.sleep(5)
    # Parse the response
    soup = BeautifulSoup(driver.page_source, "html.parser")
    # Search for time elements
    spans = soup.find_all('span', {'class' : 'date'})
    # Convert them to datetime
    casy = [pd.to_datetime(span.get_text()) for span in spans]
    # close the driver
    driver.close()
    # return times
    return casy[0]


if __name__ == '__main__':

    now = datetime.datetime.now()
    now_mas = now + datetime.timedelta(hours=2, minutes = 11)
    now_mas = now_mas.strftime('%H:%M')

    now_bil = now + datetime.timedelta(hours=2, minutes = 9)
    now_bil = now_bil.strftime('%H:%M')

    masar = 'Masarykovo nádraží'
    bila = 'Bílá labuť'
    arrival = 'Letenské náměstí'

    mas = get_times(now_mas, masar, arrival)
    bil = get_times(now_bil, bila, arrival)

    if mas <  bil:
        print("Chod na Masaricku: {:d}:{:02d}".format(mas.time().hour, mas.time().minute))
    else:
        print("Chod na Bielu labut: {:d}:{:02d}".format(bil.time().hour, bil.time().minute))
