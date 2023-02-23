import time
# 1. import webdriver
from selenium import webdriver
# 2. creem  obiectul webdriver. Putem sa-l num: driver, browser sau cum vrem noi
driver = webdriver.Chrome()
# 1. accesam google.com
driver.get('https://www.google.fr/')
time.sleep(3)
