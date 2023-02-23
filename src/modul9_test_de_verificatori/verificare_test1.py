import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# todo Cum gasim selector CSS in inspect?
#  Click dreapta => selectam copy => copy selector

text = (By.CLASS_NAME, 'subheader')
user = (By.ID, 'username')
pwd = (By.ID, 'password')
button = (By.CLASS_NAME, 'radius')

# creeam obiectul ns:
driver = webdriver.Chrome()
# apelam website
driver.get('http://the-internet.herokuapp.com/login')
driver.maximize_window()

# trasmitem un user/ pwd
# todo find_element - esti oblig sa-i trasmiti doar un locator, daca
#   nu-l gaseste => iti da eroare
#  find_elements - ii trim tot un locator, in schimb el o sa-ti
#   returneze o lista goala/ sau cu toate elementele.
#    - AJUTA LA: In cazul in care ai o lista cu mai multe rezultate, si toate
#    au acelasi locator, o sa vrei sa iei text de la ele. Ex. Pizza. - dupa i elem,
#     nu ti le mai da pe celelalte.
# * inseamna despachetare ex. user: 'By.Id' de 'username'
assert driver.find_element(*text).text == 'This is where you can log into the secure area. ' \
                                          'Enter tomsmith for the username and SuperSecretPassword! for the password. ' \
                                          'If the information is wrong you should see error messages.'
driver.find_element(*user).send_keys('David')
driver.find_element(*pwd).send_keys('tot')
driver.find_element(*button).click()
driver.implicitly_wait(3)
time.sleep(3)

driver.find_element(*user).send_keys('tomsmith')
driver.find_element(*pwd).send_keys('SuperSecretPassword!')
driver.find_element(*button).click()
driver.implicitly_wait(3)
time.sleep(3)

# todo 1 Sa integram explicit_wait pt butonul de login.
#  2. Sa incercam sa luam dinamic userul si parola din acel text field. Bagam textul
#     intr-o variabila si dupa sa extragem user/pwd
#  3. Sa verificam acele mesaje de succesfull login sau not
#  4. Un test de logout si intr-adevar ne-am logat cu succes



