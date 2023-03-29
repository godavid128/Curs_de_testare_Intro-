import time
import unittest

from selenium import webdriver
from selenium.common import NoAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

#
class TestContextMenu(unittest.TestCase):
    custom_btn = (By.XPATH, '//*[@id="content"]/ul/li[7]/a')
    alerta = (By.ID, 'hot-spot')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_2(self):
        self.driver.find_element(*self.custom_btn).click()
        ac = ActionChains(self.driver) # Este o class pt click
        ac.context_click(self.driver.find_element(*self.alerta)).perform() # perform e lansare click dreapta
        time.sleep(3)
        self.driver.switch_to.alert.accept() # E utilizarea unori proprietat a driver pt a da accept
        # todo Sa integram try except in partea de alerta 'NoAlertPresentException'
        # try:
        #     alert = self.driver.switch_to.alert.accept()
        #     alert = NoAlertPresentException
        # except
        #     pass
        time.sleep(3)



