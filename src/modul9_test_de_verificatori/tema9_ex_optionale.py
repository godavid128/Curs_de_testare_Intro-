import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from tema9_ex_oblig_class_Login import Login


class PasswordHacking(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com/login')

    def test12_brute_force_pwd_hacking(self):
        # Completeaza user 'tomsmith'
        self.driver.find_element(*Login.user).send_keys('tomsmith')
        self.driver.find_element(*Login.pwd).send_keys()
        self.driver.find_element(*Login.button).click()

        # Gaseste elementul '//h4'
        x = self.driver.find_element(*Login.text1)
        for parola in x:
            if
            self.driver.find_element(*Login.button).click()
            print(f'Parola secreta este {parola}')
        else:
            print('Nu am reusit sa gasesc parola')
        # Ia text de pe el si fa split dupa spatiu. Considera fiec cuv ca o potentia parola
        # Folos o struct iterativa, ca sa introd rand pe rand parol si sa apasi pe login
        # La final test trebuie sa imi printeze fie: 'Nu am reusit sa gasesc parola'
        #                                            'Parola secreta este [parola]'


    def tearDown(self) -> None:
        self.driver.quit()
