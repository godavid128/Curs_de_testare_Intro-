
from src.modul11_POM.locators.alerts_locators import AlertsLocators


class AlertPage:
    def __init__(self, driver):
        self._driver = driver

    def page_alert(self):
        self._driver.find_element(*AlertsLocators.JS_ALERT).click()

    def page_confirm(self):
        self._driver.find_element(*AlertsLocators.JS_CONFIRM).click()

    def page_prompt(self):
        self._driver.find_element(*AlertsLocators.JS_PROMPT).click()

    # def get_text_for_result(self):
    #     return self._driver.find_element(*AlertsLocators.RESULT).text


# todo ce facem cu alertele ? in pages o alta clasa care sa trateze alerte
#    - alerts_pages_handling si ce metode ar trebui sa aiba. metode:
#    1.accept, 2. dismiss, 3.send_keys  => FACUT