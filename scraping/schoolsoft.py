from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os
import json
import time

from selenium.webdriver.chrome.options import Options

import keys  #To use, make your own keys.py file with variables username and password

path = os.getcwd()

options = Options()
#options.binary_location = path + "/scraping/Chrome/Chrome.exe"
options.headless = True
options.disable_extensions = True
options.add_argument ('--no-sandbox')



driver = webdriver.Chrome(executable_path = path + "/scraping/chromedriver.exe", options = options)


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



html=driver.page_source



driver.stop_client()
driver.close()
driver.quit()

print(soup.find(id=''))


"""
soup = BeautifulSoup(html, "HTML.parser")
print(soup.find(id='accordion-group69500'))


main = soup.find(id='main')
news = main.find(id='news_con_content')

accordions = news.findAll("div", {"class": "accordion"})

lunchdiv = accordions[5]

accordioninner = lunchdiv.find(id='accordion-inner69500')

lunchlista = accordioninner.find("div", {"class": "accordion_inner_left"})

resturanger = lunchlista.findAll('p', {"class": "tinymce-p"})

print(lunchlista)

