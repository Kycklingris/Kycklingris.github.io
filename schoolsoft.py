from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import keys

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options)


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

nyheter = BeautifulSoup(html)

print(nyheter)