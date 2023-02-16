import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://ro.wikipedia.org/wiki/Categorie:Liste_de_politicieni_rom%C3%A2ni%27')
time.sleep(5)

search_field = driver.find_element(By.NAME, 'search')

search_field.send_keys('Lista de primari romani')

search_field.submit()

driver.quit()
