# todo ce facem cu alertele ? in pages o alta clasa care sa trateze alerte
#    - alerts_pages_handling si ce metode ar trebui sa aiba. metode:
#    1.accept, 2. dismiss, 3.send_keys
from datetime import time

from src.modul11_POM.locators.alerts_locators import AlertsLocators


class AlertsPagesHandling:
    def __init__(self, driver):
        self._driver = driver

    def accept(self):
        self._driver.switch_to.alert.accept()

    def dismiss(self):
        self._driver.switch_to.alert.dismiss()

    def send_keys(self):
        my_input = 'dada'
        self._driver.switch_to.alert.send_keys(my_input)
        self._driver.switch_to.alert.accept()
        assert my_input in self._driver.find_element(*AlertsLocators.RESULT).text

