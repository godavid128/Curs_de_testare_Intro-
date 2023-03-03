import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login(unittest.TestCase):
    text0 = (By.CSS_SELECTOR, 'h2')
    text1 = (By.CLASS_NAME, 'subheader')
    text1_xpath = (By.XPATH, '//*[@id="content"]/div/h2')
    button = (By.CLASS_NAME, 'radius')
    link_css = (By.CSS_SELECTOR, '#page-footer > div > div > a')
    link_xpath = (By.XPATH, '//*[@id="page-footer"]/div/div/a')
    error_login = (By.ID, 'flash')
    user = (By.ID, 'username')
    pwd = (By.ID, 'password')
    close_x = (By.LINK_TEXT, '×')
    label_username = (By.CSS_SELECTOR, '.row:nth-child(1) label')
    label_pwd = (By.CSS_SELECTOR, '.row:nth-child(2) > .large-6 > label')
    flash = (By.ID, 'flash')
    flash_succes = (By.CLASS_NAME, 'flash success')
    button_logout = (By.CSS_SELECTOR, ".icon-2x")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.find_element(By.LINK_TEXT, 'Form Authentication').click()
        self.driver.maximize_window()

    # def test1(self):
    #     # verifica daca noul url e corect
    #     self.assertEqual(self.driver.current_url, 'https://the-internet.herokuapp.com/login')
    #
    # def test2(self):
    #     # verifica daca page title e corect
    #     self.assertEqual(self.driver.find_element(*self.text0).text, 'Login Page')
    #
    # def test3(self):
    #     # verifica text de pe elementul 'xpath=//h2' e corect
    #     # self.assertEqual(self.driver.find_element(*self.text1_xpath).text, 'Login Page')
    #     self.driver.find_element(*self.text1_xpath).is_displayed()
    #
    #
    # def test4(self):
    #     # verifica daca butonul de login este displayed
    #     self.driver.find_element(*self.button).is_displayed()
    #
    # def test5(self):
    #     # verifica daca atrubutul 'href' al linkului 'Elemental Selenium' e corect
    #     print(self.driver.find_element(*self.link_css).get_attribute('hraef'), True)
    #     print(self.driver.find_element(*self.link_xpath).get_attribute('href'), True)
    #     WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.link_css))
    #
    # def test6(self):
    #     # Lasa goale user si pass. Click login. Verifica daca eroarea e displayed
    #     self.driver.find_element(*self.button).click()
    #     self.driver.find_element(*self.error_login).is_displayed()
    #
    # def test7(self, actual=None):
    #     # Complet cu user si pass invalide. Click login. Verifica daca ms de pe eroare
    #     # e corect. Este si un 'x' pus acolo extra, asa ca vom folosi soluti de m jos:
    #     # - expected = 'Your username is invalid!'
    #     # - self.assertTrue(expected in actual, 'Error message text is incorrect')
    #     self.driver.find_element(*self.user).send_keys('david')
    #     self.driver.find_element(*self.pwd).send_keys('12345')
    #     self.driver.find_element(*self.button).click()
    #     expected = 'Your username is invalid!'
    #     self.assertTrue(self.driver.find_element(*self.error_login), expected)
    #
    # def test8(self):
    #     # Lasa goale user si pwd. Click login.
    #     # Apasa x la eroare. Verifica daca eroarea a disparut
    #     self.driver.find_element(*self.button).click()
    #     self.driver.find_element(*self.close_x).click()
    #     self.assertTrue(self.driver.find_element(*self.error_login).is_enabled())
    #     time.sleep(1)
    #
    # def test9(self):
    #     # Ia ca o lista toate //label. Verifica textul ca textul de pe ele sa fie
    #     # cel asteptat (Username si Password). Aici e ok sa avem 2 assert-uri
    #     self.assertEqual(self.driver.find_element(*self.label_username).text, 'Username')
    #     self.assertEqual(self.driver.find_element(*self.label_pwd).text, 'Password')
    #     # todo N-AM STIUT CUM SA IAU CA O LISTA TOATE //LABEL-URILE???
    #
    def test10(self):
        # Complet user si pwd valide. Click login.
        self.driver.find_element(*self.user).send_keys('tomsmith')
        self.driver.find_element(*self.pwd).send_keys('SuperSecretPassword!')
        self.driver.find_element(*self.button).click()
        #  Verifica ca noul url Contine/secure.
        print(self.driver.current_url)
        self.assertEqual(self.driver.current_url, 'https://the-internet.herokuapp.com/secure')
        #  Folos un 'explicit wait' pt elem cu clasa 'flash succes'.
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.flash))
        # todo N-am reusit sa verific dupa CLASS_NAME, ci dupa ID
        #  Verifica daca elemen cu clasa='flash succes' este displayed
        self.driver.find_element(*self.flash).is_displayed()
        # todo nu reusesc sa fac!
        #  Verifica daca mesajul de pe acest element CONTINE textul 'secure area!'
        self.assertEqual(self.driver.find_element(*self.flash).text, 'You logged into a secure area!\n×')

    # def test11(self):
    #     # Completeaza cu user si pass valide. Click login.
    #     self.driver.find_element(*self.user).send_keys('tomsmith')
    #     self.driver.find_element(*self.pwd).send_keys('SuperSecretPassword!')
    #     self.driver.find_element(*self.button).click()
    #     # Click logout.
    #     self.driver.find_element(*self.button_logout).click()
    #     # Verifica daca ai ajuns pe https://the-internet.herokuapp.com/login
    #     self.assertEqual(self.driver.current_url, 'https://the-internet.herokuapp.com/login')


    def tearDown(self) -> None:
        self.driver.quit()

# 1. todo CUM STIM CE FUNCTIE FOLOSIM DUPA 'EC.'??????
#     2. Practic, cum ne dam seama ca am facut un test corect?