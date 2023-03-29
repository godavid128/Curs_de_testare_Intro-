from selenium.webdriver.common.by import By


class LocatorsTema9:
    form_Authentication = (By.LINK_TEXT, 'Form Authentication')
    text1_login_page = (By.XPATH, '//h2')
    # todo in inspect 'h4 sau //h4. Cum e mai corect???
    #  am gasit acelasi '//h2' in pagini separate. E ok
    text2 = (By.XPATH, '//h4')
    button = (By.XPATH, '//button[@type="submit"]')
    # am gasit selector unic si dupa CSS_selector si dupa XPATH
    elemental_selenium1 = (By.CSS_SELECTOR, '#page-footer > div > div > a')
    elemental_selenium2 = (By.XPATH, '//*[@id="page-footer"]/div/div/a')
    user = (By.ID, 'username')
    pwd = (By.ID, 'password')
    flash = (By.XPATH, '//div[@id="flash-messages"]')
    error_login = (By.ID, 'flash-messages')
    close_x = (By.XPATH, '//a[normalize-space()="×"]')
    label_username = (By.XPATH, '//label')
    flash_succes = (By.XPATH, '//*[@id="flash"]')
    button_logout = (By.CSS_SELECTOR, '.icon-2x')