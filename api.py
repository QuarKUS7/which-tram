from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import selenium.webdriver.chrome.service as service
import pandas as pd
import datetime

now = datetime.datetime.now()
now_mas = now + datetime.timedelta(hours=2, minutes = 11)
now_mas = now_mas.strftime('%H:%M')

now_bil = now + datetime.timedelta(hours=2, minutes = 9)
now_bil = now_bil.strftime('%H:%M')


def get_query(when, departure, arrival):
    options = Service.Service()
    #options.add_argument("--headless")
    driver = webdriver.Chrome("./geckodriver")
    driver.get("http://spojeni.dpp.cz/")
    inputElement = driver.find_element_by_id("ctlFrom_txtObject")
    inputElement.send_keys(departure)
    inputElement = driver.find_element_by_id("ctlTo_txtObject")
    inputElement.send_keys(arrival)
    driver.find_element_by_id("txtTime").clear()
    driver.find_element_by_id("txtTime").send_keys(when)
    driver.find_element_by_xpath("//input[@id='optChangesDirect']").click()
    inputElement.send_keys(Keys.ENTER)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    spans = soup.find_all('span', {'class' : 'date'})
    casy = [pd.to_datetime(span.get_text()) for span in spans]
    driver.close()
    return casy[0]

departure = 'Masarykovo nádraží'
arrival = 'Letenské náměstí'

mas = get_query(now_mas, departure, arrival)

departure = 'Bílá labuť'

bil = get_query(now_bil, departure, arrival)

if mas <  bil:
    print("Chod na Masaricku: {:d}:{:02d}".format(mas.time().hour, mas.time().minute))
else:
    print("Chod na Bielu labut: {:d}:{:02d}".format(bil.time().hour, bil.time().minute))
