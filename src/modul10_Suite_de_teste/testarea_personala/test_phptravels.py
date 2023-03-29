import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestTravels(unittest.TestCase):
    # locatori pt setare limba site si curs valutar
    setare_limba = (By.XPATH, '//*[@id="languages"]/i')
    lang_fr = (By.XPATH, '//*[@id="fadein"]/header/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/ul/li[7]/a')
    curs_valuta = (By.XPATH, '//*[@id="currency"]/i')
    curs_euro = (By.XPATH, '//*[@id="fadein"]/header/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/ul/li[4]/a')

    # locatori pt acces cont invalide
    acces_compte = (By.XPATH, '//*[@id="ACCOUNT"]/i')
    client_conection = (
        By.XPATH, '//*[@id="fadein"]/header/div/div/div/div/div/div[2]/div/div[2]/div[3]/div/ul/li[1]/a')
    input_email = (By.XPATH, '//*[@id="fadein"]/div[4]/div/div[2]/div[2]/div/form/div[1]/div/input')
    input_mot_de_passe = (By.XPATH, '//*[@id="fadein"]/div[4]/div/div[2]/div[2]/div/form/div[2]/div[1]/input')
    button_conection = (By.XPATH, '//*[@id="fadein"]/div[4]/div/div[2]/div[2]/div/form/div[3]/button')
    mesaj_error = (By.CLASS_NAME, 'message')

    # locatori pt rezervare bilet avion
    button_flights = (By.XPATH, '//*[@id="flights-tab"]')
    flying_from = (By.XPATH, '//*[@id="autocomplete"]')
    flying_destination = (By.XPATH, '//*[@id="autocomplete2"]')
    departure_date = (By.XPATH, '//*[@id="departure"]')
    passengers = (By.XPATH, '//*[@id="onereturn"]/div[3]/div/div/div/a')
    adults = (By.XPATH, '//*[@id="fadults"]')

    button_search = (By.XPATH, '//*[@id="flights-search"]')
    mesaj_error_flights = (By.XPATH, '//*[@id="fadein"]/div[6]/img')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://phptravels.net/')
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    '''
    Accesam pagina 'https://phptravels.net/'
    1.  - Schimbam limba franceza pentru site.
        - Alegem valuta euro
        - Accesam pe contul de client.
        - Introducem email si parola invalida.
        - Facem click pe 'Conection'
        - Verificam daca mesajul de error este 'Identifiants erronés. réessayez !'
    2.  - Accesam 'Flights
        - Selectam From - Destination - Departure - pasagerii - search
    '''

    def test1_lang_curs_compte_invalide(self):
        self.driver.find_element(*self.setare_limba).click()
        self.driver.find_element(*self.lang_fr).click()
        time.sleep(3)
        self.driver.find_element(*self.curs_valuta).click()
        self.driver.find_element(*self.curs_euro).click()
        time.sleep(3)
        self.driver.find_element(*self.acces_compte).click()
        self.driver.find_element(*self.client_conection).click()
        self.driver.find_element(*self.input_email).send_keys('david@gmail.com')
        self.driver.find_element(*self.input_mot_de_passe).send_keys('12345')
        self.driver.find_element(*self.button_conection).click()
        time.sleep(3)
        self.assertEqual(self.driver.find_element(*self.mesaj_error).text, 'Identifiants erronés. réessayez !')
        self.driver.find_element(*self.mesaj_error).is_displayed()

    def test2_rezervare_flights(self):
        self.driver.find_element(*self.button_flights).click()
        time.sleep(3)
        self.driver.find_element(*self.flying_from).send_keys('KIV')
        time.sleep(3)
        self.driver.find_element(*self.flying_destination).send_keys('PAR')
        time.sleep(3)
        self.driver.find_element(*self.departure_date).clear()
        self.driver.find_element(*self.departure_date).send_keys('01-04-2023')
        self.driver.find_element(*self.passengers).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.adults))
        self.driver.find_element(*self.adults).clear()
        time.sleep(3)
        self.driver.find_element(*self.adults).send_keys('2')
        time.sleep(3)
        self.driver.find_element(*self.button_search).click()
        self.driver.find_element(*self.mesaj_error_flights).is_displayed()
        time.sleep(3)
