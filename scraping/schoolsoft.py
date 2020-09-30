from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os
import json
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

import keys  # To use, make your own keys.py file with variables username and password

path = os.getcwd()

options = Options()
#options.binary_location = path + "/scraping/Chrome/Chrome.exe"
options.headless = True
options.disable_extensions = True
options.add_argument('--no-sandbox')


driver = webdriver.Chrome(executable_path=path +"/scraping/chromedriver.exe", options=options)


USERNAME = keys.username
PASSWORD = keys.password

driver.get("https://sms.schoolsoft.se/nti/sso")

btn = driver.find_elements_by_xpath("//*[@id='username']")[0]
btn.send_keys(USERNAME)
btn = driver.find_elements_by_xpath("//*[@id='password']")[0]
btn.send_keys(PASSWORD)
btn = driver.find_elements_by_xpath("//*[@class='form__button form__button--primary']")[0]
btn.click()

driver.get("https://sms.schoolsoft.se/nti/jsp/student/right_student_news.jsp?menu=news")
time.sleep(2)


element = driver.find_element_by_id("accordion-heading69500")
actions = ActionChains(driver)
actions.move_to_element(element).perform()


btn = driver.find_element_by_xpath('//a[@href="#collapse69500"]')
btn.click()

time.sleep(2)

html = driver.page_source


driver.stop_client()
driver.close()
driver.quit()


soup = BeautifulSoup(html, "lxml")
accordion = soup.find(id='accordion-inner69500')

lunchlista = accordion.findAll("div", {"class": "accordion_inner_left"})

resturanger = []

for i in lunchlista[0].find_all('p', {'class': "tinymce-p"})[6:]:
    if i.text == "\xa0":
        continue
    resturanger.append(i.text)

resturanger = resturanger[:-1]

resturanger2 = []
for i in resturanger:
    i = i.translate({ord('*'): None})
    i = i.translate({ord("'"): None})
    i = i.translate({ord('#'): None})
    i = i.translate({ord('´'): None})
    i = i.translate({ord(":"): None})
    i = i.translate({ord(";"): None})
    i = i.translate({ord("!"): None})
    i = i.replace('STOCKHOLM', '')
    i = i.replace('Stockholm', '')
    i = i.replace('stockholm', "")
    i = i.replace('sTOCKHOLM', '')
    i = i.replace(' - ', ',')
    resturanger2.append(i)

resturanger3 = []


class resturang(object):
    def __init__(self, name = 'N/A', location = 'N/A', annexet = 'N/A', craford = 'N/A', extra = 'N/A', review =  'N/A', description = 'N/A'):
        self.name = name
        self.location = location
        self.annexet = annexet
        self.craford = craford
        self.extra = extra
        self.review = review
        self.description = description

for i in resturanger2:
    tmp = i.split(',', 1)
    tmp2 = tmp[1].split(' NY', 1)
    tmp2 = tmp[1].split(' ny', 1)
    tmp2 = tmp[1].split(' Ny', 1)
    tmp2 = tmp[1].split(' Tillbaka', 1)
    tmp2 = tmp[1].split(' tillbaka', 1)
    tmp2 = tmp[1].split(' TILLBAKA', 1)


