# python package
import csv
import time
import random
import codecs

from .models import Rider

# selenium package
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# fonction pause
def pause():
    time_break = random.randint(1, 2)
    return time.sleep(time_break)


# options
# path_to_webdriver = "/Applications/chromedriver"
path_to_webdriver = "C:\\Users\\xgougat\\Desktop\\chromedriver"
options = webdriver.ChromeOptions()
options.add_argument("--kiosk")
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
# driver = webdriver.Chrome("/Applications/chromedriver", desired_capabilities=capa, chrome_options=options)
driver = webdriver.Chrome("C:\\Users\\xgougat\\Desktop\\chromedriver", desired_capabilities=capa, chrome_options=options)
wait = WebDriverWait(driver, 30)
pause()

# url de depart
lequipe_url = "https://www.procyclingstats.com/race/tour-de-pologne/2019/stage-4/startlist"

# aller sur lequipe
driver.get(lequipe_url)
images = wait.until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "img"))
            )

# scroller jusqu'en bas de page
scheight = .0
while scheight < 1.0:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight*%s);" % scheight)
    scheight += .2
    time.sleep(1)

# ouvrir csv
with codecs.open('pologne_startlist.csv', 'w', encoding="utf-8") as csvfile:
    fieldnames = ['rider']

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
    writer.writeheader()

    time.sleep(5)
    # bloc des teams participantes
    blocteam = driver.find_elements_by_css_selector("body > div.wrapper > div.content > div.statDivLeft > ul > li")
    for t in blocteam:
        team = t.find_elements_by_css_selector("div > a")

        for j in team:
            # scroll doucement
            driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'nearest'});",
                j)

            # rider
            try:
                rider = j.find_element_by_css_selector("span").text
            except NoSuchElementException:
                rider = ''
                pass

            try:
                riderInsert = Rider.objects.get(firstName__in=rider,
                                                lastName__in=rider)
            except Rider.DoesNotExist:
                riderInsert = None
            # write csv
            # writer.writerow({'rider': rider})
            print("-- SUCCESS : %s" % (riderInsert.fullName))
# fin
print("Scrap  terminé.")
driver.close()
