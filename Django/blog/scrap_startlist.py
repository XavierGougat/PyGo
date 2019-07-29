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
lequipe_url = "https://www.procyclingstats.com/race/tour-de-france/2019/stage-20/startlist/roster"

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
with codecs.open('lequipe_etape.csv', 'w') as csvfile:
    fieldnames = ['Team', 'Rider']

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
    writer.writeheader()

    # bloc d'éléments 1
    bloc1 = driver.find_elements_by_css_selector("ul.startlist > li")
    # boucle 2
    for j in bloc1:

        # scroll doucement
        driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'nearest'});",
            j)

        #team
        try:
            team = j.find_element_by_css_selector("h4 > a").text
        except NoSuchElementException:
            team = ''
            pass
        
        bloc2 = j.find_elements_by_css_selector(".riders > a")

        for i in bloc2:
            # rider
            try:
                rider = i.find_element_by_css_selector("span").text
            except NoSuchElementException:
                rider = ''
                pass
            # write csv
            writer.writerow({'Team': team, 'Rider': rider})
            print("-- SUCCESS : %s - %s" % (team, rider))

# fin
print("Scrap  terminé.")
driver.close()