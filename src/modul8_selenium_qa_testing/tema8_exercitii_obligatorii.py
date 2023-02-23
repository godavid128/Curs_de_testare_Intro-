import time

from selenium.webdriver.common.by import By
from datetime import datetime
print('EXERCITII OBLIGATORII')
"""
Alege-ți unuul sau mai multe din sugestiile de site-uri de mai jos
- https://www.phptravels.net/
- http://automationpractice.com/index.php
- https://formy-project.herokuapp.com/
- https://the-internet.herokuapp.com/
- https://www.techlistic.com/p/selenium-practice-form.html
- jules.app
Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
● Id  ● Link text  ● Parțial link text  ● Name  ● Tag*  ● Class name*
● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
observație:
- Probabil nu vei găsi un singur website care să cuprindă toate variantele
de mai sus, astfel că îți recomandăm să folosești mai multe site-uri
- Opțional: La tag și class name vei folosi find elementS! - salvează în listă.
Interactionează cu un element la alegere din listă.
- Pentru xpath identifică elemente după criteriile de mai jos:
● 3 după atribut valoare  ● 3 după textul de pe element
● 1 după parțial text  ● 1 cu SAU, folosind pipe |  ● 1 cu *
● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci
cu (xpath)[1]  ● 1 în care să folosești parent::
● 1 în care să folosești fratele anterior sau de după (la alegere)
● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu
ce element vreau să interacționez.
"""
# 1. https://www.phptravels.net/
from selenium import webdriver
# 1. Am navigat pe link de jos si am gasit elem dupa 'ID', apoi i-am trim key 'Gorodetchi'
# first_name = webdriver.Chrome()
# first_name.get('https://formy-project.herokuapp.com/form')
# first_name.find_element(By.ID, 'first-name').send_keys('Gorodetchi')
# time.sleep(3)
print('Navigam pe cateva link si gasim elem dupa: Id, Link_Text, Name, Tag, Class_name, CSS, Xpath')

# Vom accesa pagina web 'chrome'
driver = webdriver.Chrome()
# vom deschide website, vom gasi dupa 'id'
# driver.get('https://phptravels.net/')
# element1 = driver.find_element(By.ID, 'fadein')
# element1.click()
# element1.send_keys('27-02-2023')
# time.sleep(30)

# 7. Accesarea website prin elementul 'CSS_SELECTOR'
# driver.get('https://the-internet.herokuapp.com/')
# element2 = driver.find_element(By.CSS_SELECTOR, '#content > ul > li:nth-child(3) > a')
# element2.click()
# time.sleep(3)
# element2 = driver.find_element(By.CSS_SELECTOR, '#content > ul > li:nth-child(1) > a')
# element2.click()
# time.sleep(3)
driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
driver.find_element(By.NAME, 'firstname').send_keys('gorodetchi')
driver.find_element(By.NAME, 'lastname').send_keys('david')
driver.find_element(By.ID, 'sex-0').click()
driver.find_element(By.ID, 'exp-2').click()
driver.find_element(By.ID, 'datepicker').send_keys('2/20/2023')
driver.find_element(By.NAME, 'profession').click()
driver.find_element(By.XPATH, '//*[@id="tool-2"]').click()
driver.find_element(By.ID, 'continents').send_keys('Europe')
driver.find_element(By.ID, 'submit').click()
time.sleep(30)
driver.quit()
