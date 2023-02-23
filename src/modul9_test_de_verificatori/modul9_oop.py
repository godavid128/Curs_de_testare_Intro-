import time
import unittest
from selenium import webdriver

# Am importat din libraria 'unittest' doar 'TestCase'
class TestLogin(unittest.TestCase):
    # facem metoda de setUp
    def setUp(self) -> None:
        # creeam obiectul ns:
        self.driver = webdriver.Chrome()
        # apelam website
        self.driver.get('http://the-internet.herokuapp.com/login')
        self.driver.maximize_window()

    def test_invalid_login(self):
        self.assertEqual(self.driver.find_element(*self.text).text, 'This is where you can log into the secure area. ' \
                                                                    'Enter tomsmith for the username and SuperSecretPassword! for the password. ' \
                                                                    'If the information is wrong you should see error messages.')
        self.driver.find_element(*self.user).send_keys('David')
        self.driver.find_element(*self.pwd).send_keys('tot')
        self.driver.find_element(*self.button).click()
        self.driver.implicitly_wait(3)
        time.sleep(3)

    def test_valid_login(self):
        self.driver.find_element(*self.user).send_keys('tomsmith')
        self.driver.find_element(*self.pwd).send_keys('SuperSecretPassword!')
        self.driver.find_element(*self.button).click()
        self.driver.implicitly_wait(3)
        time.sleep(3)

    # Aici creem o metoda care face curat, apoi inchidem toata conexiunea cu driver.
    # dupa fiec test se curat mediul. un fel de 'cleanUp'
    def tearDown(self) -> None:
        self.driver.quit()

# todo 1. O clasa unde stocam locatori, apoi ii importam
#  locatorii sa fie intr-o clasa separat de metodele de testare (class login_locators)
#   2. Testele din to do sa le migram in modul oop
