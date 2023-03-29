'''
1. deschidem link
2.
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin(unittest.TestCase):
    basic_auth = (By.XPATH, '//*[@id="content"]/ul/li[3]/a')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_1(self):
        self.driver.find_element(*self.basic_auth).click()
        user = 'admin'
        parola = 'admin'
        self.driver.get('https://' + user + ':' + parola + '@the-internet.herokuapp.com/basic_auth')
        # Pentru a respecta ordinea lui Baze_auth punem ':' intre user si parola
        mssg = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/p').text
        assert mssg == 'Congratulations! You must have the proper credentials.'

