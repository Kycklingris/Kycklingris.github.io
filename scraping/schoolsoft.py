from selenium import webdriver
from bs4 import BeautifulSoup
import os
import json
import time
import copy
import string
import sys
import codecs
import googlemaps
import responses

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

import keys  # To use, make your own keys.py file with variables username and password

path = os.getcwd()

options = Options()
#options.binary_location = path + "/scraping/Chrome/Chrome.exe"
options.headless = True
options.disable_extensions = True
options.add_argument('--no-sandbox')


driver = webdriver.Chrome(executable_path=path +
                          "/scraping/chromedriver.exe", options=options)

gmaps = googlemaps.Client(key=keys.apikey)

USERNAME = keys.username
PASSWORD = keys.password

driver.get("https://sms.schoolsoft.se/nti/sso")

btn = driver.find_elements_by_xpath("//*[@id='username']")[0]
btn.send_keys(USERNAME)
btn = driver.find_elements_by_xpath("//*[@id='password']")[0]
btn.send_keys(PASSWORD)
btn = driver.find_elements_by_xpath(
    "//*[@class='form__button form__button--primary']")[0]
btn.click()

driver.get(
    "https://sms.schoolsoft.se/nti/jsp/student/right_student_news.jsp?menu=news")
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

tmpresturanger = []

lunchlista = lunchlista[0]

for i in lunchlista.findAll('a', href=True):
    i.extract()

for i in lunchlista.find_all('p', {'class': "tinymce-p"})[6:]:
    if i.text == "\xa0":
        continue
    tmpresturanger.append(i.text)


new = False
old = []

with codecs.open('scraping/old.txt', 'r', encoding="utf8") as f:
    for i in f:
        tmp = i[:-1]
        old.append(tmp)

if tmpresturanger == old:
    new = False
else:
    new = True


with codecs.open('scraping/old.txt', 'w', encoding="utf8") as f:
    for i in tmpresturanger:
        f.writelines("%s\n" % i)

# use if bypassing previous check is needed.
new = True

if new == False:
    sys.exit()

tmpresturanger = tmpresturanger[:-1]

tmpresturanger2 = []
for i in tmpresturanger:
    i = i.lower()
    i = i.translate({ord('*'): None})
    i = i.translate({ord('.'): None})
    i = i.translate({ord("'"): None})
    i = i.translate({ord('#'): None})
    i = i.translate({ord('´'): None})
    i = i.translate({ord(":"): None})
    i = i.translate({ord(";"): None})
    i = i.translate({ord("!"): None})
    i = i.replace('stockholm', "")
    i = i.replace(' - ', ',')
    i = i.replace(' ny', ' tmp  ny')
    i = i.replace(' tillbaka', ' tmp  tillbaka')

    tmpresturanger2.append(i)

failure = True
resturanger = []

for i in tmpresturanger2:
    tmp = i.split(',', 1)
    if len(tmp) == 1:
        continue

    tmp2 = tmp[1]
    tmp3 = tmp2.split(' tmp ', 1)

    name = tmp[0]
    if len(tmp3) == 2:
        location = tmp3[0]
        extra = tmp3[1]
    else:
        location = tmp[1]
        extra = ""

    while True:
        if name.startswith(" ") or name.startswith(","):
            name = name[1:]
        elif name.endswith(" ") or name.endswith(","):
            name = name[:-1]
        elif "/" in name:
            tmpname = name.split("/", 1)
            name = tmpname[0]
        elif location.startswith(" ") or location.startswith(","):
            location = location[1:]
        elif location.endswith(" ") or location.endswith(","):
            location = location[:-1]
        elif extra.startswith(" ") or extra.startswith(","):
            extra = extra[1:]
        elif extra.endswith(" ") or extra.endswith(","):
            extra = extra[:-1]
        else:
            break

    name = string.capwords(name)
    location = string.capwords(location)
    extra = string.capwords(extra)
    while True:
        try:
            geocode_result = gmaps.geocode(location + ' Stockholm')
        except:
            time.sleep(2)
            continue
        else:
            break

    street_number = geocode_result[0]["address_components"][0]["short_name"]
    street_name = geocode_result[0]["address_components"][1]["short_name"]

    mapsaddress = street_name + " " + street_number

    latitude = geocode_result[0]["geometry"]["location"]["lat"]
    longitude = geocode_result[0]["geometry"]["location"]["lng"]

    a = False
    b = False

    while a == False and b == False:
        try:
            directions_result_annexet = gmaps.directions(mapsaddress + "," + "Stockholm", "59.341667,18.049201", mode="walking")
        except:
            time.sleep(2)
            continue
        else:
            a = True
        try:
            directions_result_craford = gmaps.directions(mapsaddress + "," + "Stockholm", "59.337579,18.046180", mode="walking")
        except:
            time.sleep(2)
            continue
        else:
            b = True
        

    walking_time_annexet = directions_result_annexet[0]["legs"][0]['duration']['text']
    walking_time_craford = directions_result_craford[0]["legs"][0]['duration']['text']


    tmpdict = {"name": name, "location": mapsaddress, "extra": extra, "lon": longitude,"lat": latitude, "annexet": walking_time_annexet, "craford": walking_time_craford}
    resturanger.append(copy.deepcopy(tmpdict))


with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(resturanger, f, ensure_ascii=False, indent=4)
