
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie=driver.find_element(By.ID,"cookie")
cookie_sec=driver.find_element(By.CSS_SELECTOR,"#cps")
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids_list=[]

item_ids = [item.get_attribute("id") for item in items]






timeout = time.time()+5
timeout_start = time.time()
five_min=time.time()+60*1

while True:
      cookie.click()
      if time.time() > timeout:
         gifts = driver.find_elements(By.CSS_SELECTOR, "#store b")
         upgrades = []
         for gift in gifts:
             if gift.text !="":
                cost=int(gift.text.split("-")[1].strip().replace(",", ""))
                upgrades.append(cost)

         cookie_count = int(driver.find_element(By.ID, "money").text.replace(",", ""))

         cookie_upgrades = {}
         for n in range(len(upgrades)):
             cookie_upgrades[upgrades[n]]=item_ids[n]

         afforbale_upgrades = {}
         for cost, ids in cookie_upgrades.items():
                if cookie_count > cost:
                    afforbale_upgrades[cost] =ids
                    highest_price_affordable_upgrade =max(afforbale_upgrades)
                    to_purchase=afforbale_upgrades[highest_price_affordable_upgrade]
                    print(f"to_purchase:{to_purchase}")
         driver.find_element(By.ID,to_purchase).click()
         timeout=time.time()+5
      if time.time() > five_min:
                 cookie_per_s = driver.find_element(By.ID,"cps").text
                 print(cookie_per_s)
                 break






