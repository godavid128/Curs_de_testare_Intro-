import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tema9_ex_oblig_class_Login import Login


class PasswordHacking(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com/login')

    # Completeaza user 'tomsmith'
    # Gaseste elementul '//h4'
    # Ia text de pe el si fa split dupa spatiu. Considera fiec cuv ca o potentia parola
    # Folos o struct iterativa, ca sa introd rand pe rand parol si sa apasi pe login
    # La final test trebuie sa imi printeze fie: 'Nu am reusit sa gasesc parola'
    #                                            'Parola secreta este [parola]'
    def test12_brute_force_pwd_hacking(self):
        x = self.driver.find_element(*Login.text1).text.split()
        for parola in x:
            self.driver.find_element(*Login.user).send_keys('tomsmith')
            self.driver.find_element(*Login.pwd).send_keys(parola)
            self.driver.find_element(*Login.button).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(Login.flash))
            if parola == 'SuperSecretPassword!':
                print(f'Parola secreta este {parola}')
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(Login.flash))
                time.sleep(2)
                break
        else:
            print('Nu am reusit sa gasesc parola')

    def tearDown(self) -> None:
        self.driver.quit()
