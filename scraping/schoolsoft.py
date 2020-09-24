from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os
import json

from selenium.webdriver.chrome.options import Options

import keys

options = Options()
options.headless = True

path = os.getcwd()


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
html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, "lxml")
print(soup.title.text)
