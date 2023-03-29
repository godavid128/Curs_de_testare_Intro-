'''
1. deschidem link
2.
'''
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAlerts(unittest.TestCase):
    btn_alerts = (By.XPATH, '//*[@id="content"]/ul/li[29]/a')
    js_alert = (By.XPATH, '//*[@id="content"]/div/ul/li[1]/button')
    js_confirm = (By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')
    js_prompt = (By.XPATH, '//*[@id="content"]/div/ul/li[3]/button')

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_3(self):
        # Accesam pagina javascript Alerts
        self.driver.find_element(*self.btn_alerts).click()
        # Accesam butoanele prin click
        self.driver.find_element(*self.js_alert).click()
        self.driver.switch_to.alert.accept()

        self.driver.find_element(*self.js_confirm).click()
        self.driver.switch_to.alert.dismiss()

        self.driver.find_element(*self.js_prompt).click()
        my_imput = 'da da'
        self.driver.switch_to.alert.send_keys(my_imput)
        self.driver.switch_to.alert.accept()

        assert my_imput in self.driver.find_element(By.ID, 'result').text
        time.sleep(5)


