import time
from selenium import webdriver
from selenium.webdriver.common.by import By
print('EX: CAUTARE PE WEBSITE IN SEARCH BAR')
# Sa facem o cautare pe un website. Accesam link prin get. Cautam cu '.find_element.
# Trimitem cheia '.send_keys('lista scriitori'). trimitem prin '.submit()
driver = webdriver.Chrome()
driver.get('https://ro.wikipedia.org/wiki/Pagina_principal%C4%83')
time.sleep(2)
search1 = driver.find_element(By.NAME, 'search')
search1.send_keys('Lista de scriitori romani')  # ii trasmiti ms pe care vrei sa l faci pe google
search1.submit()  # simularea unui search enter. submit - trimite
time.sleep(5)