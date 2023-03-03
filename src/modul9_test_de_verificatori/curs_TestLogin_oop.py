import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Locators_for_TestLogin import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Am importat din libraria 'unittest' doar 'TestCase'
class TestLogin(unittest.TestCase):

    # facem metoda de setUp
    def setUp(self) -> None:
        # creeam obiectul ns:
        self.driver = webdriver.Chrome()
        # apelam website
        self.driver.get('http://the-internet.herokuapp.com/login')
        self.driver.maximize_window()

    # def test_invalid_login(self):
    #     self.assertEqual(self.driver.find_element(*Locators.text).text, 'This is where you can log into the secure area. ' \
    #                                                                 'Enter tomsmith for the username and SuperSecretPassword! for the password. ' \
    #                                                                 'If the information is wrong you should see error messages.')
    #     self.driver.find_element(*Locators.user).send_keys('David')
    #     self.driver.find_element(*Locators.pwd).send_keys('tot')
    #     self.driver.find_element(*Locators.button).click()
    #     self.driver.implicitly_wait(3)
    #     time.sleep(3)

    def test_valid_login(self):
        self.driver.find_element(*Locators.user).send_keys('tomsmith')
        self.driver.find_element(*Locators.pwd).send_keys('SuperSecretPassword!')
        self.driver.find_element(*Locators.button).click()
        # 3. Sa integram explicit_wait pt butonul de login.
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.button))
        # self.driver.implicitly_wait(3)
        # time.sleep(3)

    # Aici creem o metoda care face curat, apoi inchidem toata conexiunea cu driver.
    # dupa fiec test se curat mediul. un fel de 'cleanUp'
    def tearDown(self) -> None:
        self.driver.quit()

# todo 1. O clasa unde stocam locatori, apoi ii importam - FACUT
#    locatorii sa fie intr-o clasa separat de metodele de testare (class login_locators)
#  2. Testele din to do sa le migram in modul oop - FACUT
#  3.  Sa integram explicit_wait pt butonul de login. - FACUT
#  4. Sa incercam sa luam dinamic userul si parola din acel text field. Bagam textul
#     intr-o variabila si dupa sa extragem user/pwd
#  5. Sa verificam acele mesaje de succesfull login sau not
#  6. Un test de logout si intr-adevar ne-am logat cu succes
