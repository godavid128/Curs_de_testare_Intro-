import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from locators_for_tests_tema9 import LocatorsTema9
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.find_element(*LocatorsTema9.form_Authentication).click()
        self.driver.maximize_window()

    def test1(self):
        # verifica daca noul url e corect
        self.assertEqual(self.driver.current_url, 'https://the-internet.herokuapp.com/login')

    def test2(self):
        # verifica daca page title e corect
        title = self.driver.title
        assert title == 'The Internet'

    def test3(self):
        # verifica text de pe elementul 'xpath=//h2' e corect
        self.assertEqual(self.driver.find_element(*LocatorsTema9.text1_login_page).text, 'Login Page')
        self.driver.find_element(*LocatorsTema9.text1_login_page).is_displayed()


    def test4(self):
        # verifica daca butonul de login este displayed
        self.driver.find_element(*LocatorsTema9.button).is_displayed()

    def test5(self):
        # verifica daca atrubutul 'href' al linkului 'Elemental Selenium' e corect
        print(self.driver.find_element(*LocatorsTema9.elemental_selenium1).get_attribute('hraef'), True)
        print(self.driver.find_element(*LocatorsTema9.elemental_selenium2).get_attribute('href'), True)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsTema9.elemental_selenium1))

    def test6(self):
        # Lasa goale user si pass. Click login. Verifica daca eroarea e displayed
        self.driver.find_element(*LocatorsTema9.button).click()
        self.driver.find_element(*LocatorsTema9.error_login).is_displayed()

    def test7(self, actual=None):
        # Complet cu user si pass invalide. Click login. Verifica daca ms de pe eroare
        # e corect. Este si un 'x' pus acolo extra, asa ca vom folosi soluti de m jos:
        # - expected = 'Your username is invalid!'
        # - self.assertTrue(expected in actual, 'Error message text is incorrect')
        self.driver.find_element(*LocatorsTema9.user).send_keys('david')
        self.driver.find_element(*LocatorsTema9.pwd).send_keys('12345')
        self.driver.find_element(*LocatorsTema9.button).click()
        expected = 'Your username is invalid!'
        self.assertTrue(self.driver.find_element(*LocatorsTema9.error_login), expected)

    def test8(self):
        # Lasa goale user si pwd. Click login.
        # Apasa x la eroare. Verifica daca eroarea a disparut
        self.driver.find_element(*LocatorsTema9.button).click()
        self.driver.find_element(*LocatorsTema9.close_x).click()
        self.assertTrue(self.driver.find_element(*LocatorsTema9.error_login).is_enabled())
        time.sleep(1)

    def test9(self):
        # Ia ca o lista toate //label. Verifica textul ca textul de pe ele sa fie
        # cel asteptat (Username si Password). Aici e ok sa avem 2 assert-uri
        label = self.driver.find_elements(*LocatorsTema9.label_username)
        self.assertEqual(label[0].text, 'Username')
        self.assertEqual(label[1].text, 'Password')

    def test10(self):
        # Complet user si pwd valide. Click login.
        self.driver.find_element(*LocatorsTema9.user).send_keys('tomsmith')
        self.driver.find_element(*LocatorsTema9.pwd).send_keys('SuperSecretPassword!')
        self.driver.find_element(*LocatorsTema9.button).click()
        #  Verifica ca noul url Contine/secure.
        print(self.driver.current_url)
        self.assertEqual(self.driver.current_url, 'https://the-internet.herokuapp.com/secure')
        #  Folos un 'explicit wait' pt elem cu clasa 'flash succes'.
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LocatorsTema9.flash))
        #  Verifica daca elemen cu clasa='flash succes' este displayed
        self.driver.find_element(*LocatorsTema9.flash).is_displayed()
        #  Verifica daca mesajul de pe acest element CONTINE textul 'secure area!'
        self.assertEqual(self.driver.find_element(*LocatorsTema9.flash).text, 'You logged into a secure area!\n×')

    def test11(self):
        # Completeaza cu user si pass valide. Click login.
        self.driver.find_element(*LocatorsTema9.user).send_keys('tomsmith')
        self.driver.find_element(*LocatorsTema9.pwd).send_keys('SuperSecretPassword!')
        self.driver.find_element(*LocatorsTema9.button).click()
        # Click logout.
        self.driver.find_element(*LocatorsTema9.button_logout).click()
        # Verifica daca ai ajuns pe https://the-internet.herokuapp.com/login
        self.assertEqual(self.driver.current_url, 'https://the-internet.herokuapp.com/login')
        time.sleep(1)

    def tearDown(self) -> None:
        self.driver.quit()

# 1. todo CUM STIM CE FUNCTIE FOLOSIM DUPA 'EC.'??????
#     2. Practic, cum ne dam seama ca am facut un tests corect?
