import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://ro.wikipedia.org/wiki/Pagina_principal%C4%83')
time.sleep(2)

# todo Sa incercam sa dam click pe accept si si sa facem o cautare dupa politicieni din Romania
#   indetifici dupa location search bar
search1 = driver.find_element(By.NAME, 'search')
search1.send_keys('Lista de scriitori romani')  # ii trasmiti ms pe care vrei sa l faci pe google
search1.submit()  # simularea unui search enter
time.sleep(5)