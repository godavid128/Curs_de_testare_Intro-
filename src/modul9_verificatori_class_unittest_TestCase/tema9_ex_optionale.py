import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators_for_tests_tema9 import LocatorsTema9


class PasswordHacking(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://the-internet.herokuapp.com/login')
        self.driver.implicitly_wait(3)

    # Completeaza user 'tomsmith'
    # Gaseste elementul '//h4'
    # Ia text de pe el si fa split dupa spatiu. Considera fiec cuv ca o potentia parola
    # Folos o struct iterativa, ca sa introd rand pe rand parol si sa apasi pe login
    # La final tests trebuie sa imi printeze fie: 'Nu am reusit sa gasesc parola'
    #                                            'Parola secreta este [parola]'
    def test12_brute_force_pwd_hacking(self):
        parola = self.driver.find_element(*LocatorsTema9.text2).text.split()
        logged_in = False
        for i in range(len(parola)):
            self.driver.find_element(*LocatorsTema9.user).send_keys('tomsmith')
            self.driver.find_element(*LocatorsTema9.pwd).send_keys(parola[i])
            self.driver.find_element(*LocatorsTema9.button).click()
            # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(Locators_Tema9.flash))
            login_confirmation = self.driver.find_element(*LocatorsTema9.text1_login_page).text
            if login_confirmation == 'Secure Area':
                logged_in = True
                print(f'Parola secreta este {parola[i]}')
                break
        else:
            print('Nu am reusit sa gasesc parola')
        assert logged_in == True

    def tearDown(self) -> None:
        self.driver.quit()
