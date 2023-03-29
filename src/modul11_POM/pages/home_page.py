from src.modul11_POM.locators.home_locators import HomeLocators


class HomePage:
    def __init__(self, driver):
        self._driver = driver

    def go_to_alert_section(self):
        self._driver.find_element(*HomeLocators.BTN_ALERTS).click()
