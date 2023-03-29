import unittest
from selenium import webdriver


class BaseTests(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.maximize_window()


    def tearDown(self) -> None:
        self.driver.quit()
