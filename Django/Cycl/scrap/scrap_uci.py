# python package
import csv
import time
import random
import codecs

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
path_to_webdriver = "/Applications/chromedriver"
options = webdriver.ChromeOptions()
options.add_argument("--kiosk")
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
driver = webdriver.Chrome("/Applications/chromedriver", desired_capabilities=capa, chrome_options=options)
wait = WebDriverWait(driver, 30)
pause()

# url de depart
lequipe_url = "https://www.uci.org/road/teams"

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
with codecs.open('csv/team_astana_riders.csv', 'w') as csvfile:
    fieldnames = ['rider', 'birthDate', 'nation']

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
    writer.writeheader()

    time.sleep(5)
    # bloc des teams
    blocteam = driver.find_elements_by_css_selector("#team-grid > table > tbody > tr")
    for t in blocteam:
        team = t.find_element_by_css_selector("td:nth-child(1) > a")
        team.click()

        time.sleep(5)
        # bloc d'éléments 1
        bloc1 = driver.find_elements_by_css_selector("#grid-riders > table > tbody > tr")
        # boucle 2
        for j in bloc1:

            # scroll doucement
            driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'nearest'});",
                j)

            # rider
            try:
                rider = j.find_element_by_css_selector("td.fixNameCol > a").text
            except NoSuchElementException:
                rider = ''
                pass

            # birthDate
            try:
                birthDate = j.find_element_by_css_selector("td:nth-child(2)").text
            except NoSuchElementException:
                birthDate = ''
                pass

            # nation
            try:
                nation = j.find_element_by_css_selector("td:nth-child(3) > div > div:nth-child(2)").text
            except NoSuchElementException:
                nation = ''
                pass

            # write csv
            writer.writerow({'rider': rider, 'birthDate': birthDate, 'nation': nation})
            print("-- SUCCESS : %s - %s - %s" % (rider, birthDate, nation))
        # url de depart
        lequipe_url = "https://www.uci.org/road/teams"

        # aller sur lequipe
        driver.get(lequipe_url)

# fin
print("Scrap  terminé.")
driver.close()
