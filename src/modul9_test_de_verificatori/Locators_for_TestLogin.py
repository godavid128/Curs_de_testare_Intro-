from selenium.webdriver.common.by import By

# class unde stocam locatori
class Locators:
    text = (By.CLASS_NAME, 'subheader')
    user = (By.ID, 'username')
    pwd = (By.ID, 'password')
    button = (By.CLASS_NAME, 'radius')
