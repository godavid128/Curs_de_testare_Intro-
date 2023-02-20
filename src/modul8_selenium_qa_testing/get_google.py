import time
# import webdriver
from selenium import webdriver
# creem  obiectul webdriver
driver = webdriver.Chrome()
# accesam google.com
driver.get('https://www.google.fr/')
time.sleep(3)
