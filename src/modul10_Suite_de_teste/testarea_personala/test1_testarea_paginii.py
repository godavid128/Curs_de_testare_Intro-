import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestPersonal(unittest.TestCase):
    reclame = (By.XPATH, '//*[@id="ez-video-ez-stuck-close"]')
    reclame1 = (By.XPATH, '//*[@id="ezmob-footer-close"]')
    input_first_name = (
    By.XPATH, '//*[@id="post-body-3077692503353518311"]/div[1]/div/div/h2[2]/div[1]/div/div[2]/input')
    input_last_name = (
    By.XPATH, '//*[@id="post-body-3077692503353518311"]/div[1]/div/div/h2[2]/div[1]/div/div[5]/input')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
        self.driver.maximize_window()
        try:
            self.driver.find_element(*self.reclame).click()
            self.driver.find_element(*self.reclame1).click()
        except:
            pass

    def tearDown(self) -> None:
        self.driver.quit()

    def test_1(self):
        self.driver.find_element(*self.input_first_name).send_keys('go')
        time.sleep(3)
        self.driver.find_element(*self.input_last_name).send_keys('david')
        time.sleep(3)