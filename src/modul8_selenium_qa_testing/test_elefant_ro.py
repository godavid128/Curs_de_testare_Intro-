import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestElefant(unittest.TestCase):
    accept_cookies = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    search_produs = (By.XPATH, '//input[@name="SearchTerm"]')
    button_search = (By.XPATH, '//button[@title="Începe căutarea"]')
    product_title = (By.CLASS_NAME, 'product-title')
    product_price = (By.CLASS_NAME, 'current-price ')

    button_cont = (By.XPATH, '//ul[@class="user-links"]/li/a[@href="#account-layer"]')
    button_cont_conectare = (By.XPATH, '//div[@id="account-layer"]//a[contains(text(),"Conectare")]')
    casuta_email = (By.ID, 'ShopLoginForm_Login')
    casuta_parola = (By.XPATH, '//*[@id="ShopLoginForm_Password"]')
    conectare = (By.XPATH, '/html/body/div[2]/div/div[9]/div[1]/div/div[1]/div/form/div[4]/div/button')
    eroare_login = (By.XPATH, '//div[@role="alert"]')
    button_cont_conectare1 = (By.XPATH, '//button[@value="Login"]')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.elefant.ro/')
        self.driver.implicitly_wait(2)
        # Test 1: Identificati butonul "accept cookies" si dai click pe el
        try:
            # self.driver.find_element(self.accept_cookies).click()
            accept_cookies = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")))
            accept_cookies.click()
        except:
            pass

    # Test 2: cautati un produs la alegere (iphone 14) si
    #  verificati ca s-au returnat cel putin 10 rezultate ([class="product-title"])
    def test2_cautare_produs(self):
        self.driver.find_element(*self.search_produs).send_keys('iphone 14')
        time.sleep(3)
        button_search = self.driver.find_elements(*self.button_search)
        button_search[0].click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.product_title))
        produse_returnate = self.driver.find_elements(*self.product_title)
        for i in range(len(produse_returnate)):
            print(f'Produsele sunt: {produse_returnate[i].text}')
        assert len(produse_returnate) >= 10, 'Error, nr de elemente returnate nu este corect'

    # Test 3: Extrageti din lista produsul cu pretul cel mai mic
    # [class="current-price "] -> //img[@class="product-image"]
    def test3_produs_pret_mic(self):
        self.driver.find_element(*self.search_produs).send_keys('iphone 14')
        time.sleep(3)
        button_search = self.driver.find_elements(*self.button_search)
        button_search[0].click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.product_price))
        produse_returnate = self.driver.find_elements(*self.product_title)
        pret_product = self.driver.find_elements(*self.product_price)
        dict_elements = {}
        for i in range(len(produse_returnate)):
            dict_elements[produse_returnate[i].text] = \
                pret_product[i].text.replace(".", "").replace(",", ".").replace(" lei", "")[:-3]
        pret_min = 10000
        produs_min = ''
        for key, value in dict_elements.items():
            if int(value) < int(pret_min):
                pret_min = value
                produs_min = key
        print(f'Produsul cu pret cel mai mic este: {produs_min} si are pret de: {pret_min} lei')

    # Test 4: Extrageti titlul paginii si verificati ca este corect
    def test4_titlu(self):
        titlle = self.driver.title
        if titlle == titlle:
            print(f'Titlul paginii este: {titlle}')
        assert titlle == 'elefant.ro - mallul online al familiei tale! • Branduri de top, preturi excelente • ' \
                         'Peste 500.000 de produse pentru tine!', 'Error, title is not correct'

    # Test 5: Intrati pe site, accesati butonul cont si click pe conectare.
    # Identificati elementele de tip user si parola si inserati valori incorecte (valori incorecte inseamna
    # oricare valori care nu sunt recunscute drept cont valid)
    # - Dati click pe butonul "conectare" si verificati urmatoarele:
    #             1. Faptul ca nu s-a facut logarea in cont
    #             2. Faptul ca se returneaza eroarea corecta
    def test5_accesare_cont_cu_valori_incorecte(self):
        self.driver.find_element(*self.button_cont).click()
        button_conectare = self.driver.find_element(*self.button_cont_conectare)
        # ActionChains(self.driver).context_click(self.driver.find_element(button_conectare)).perform()
        ActionChains(self.driver).move_to_element(button_conectare).click(button_conectare).perform()
        assert self.driver.current_url == 'https://www.elefant.ro/login'
        self.driver.find_element(*self.casuta_email).send_keys('iepure@gmail.com')
        self.driver.find_element(*self.casuta_parola).send_keys('12345')
        self.driver.find_element(*self.conectare).click()
        self.assertEqual(self.driver.find_element(*self.eroare_login).
                         text, 'Adresa dumneavoastră de email / Parola este incorectă. Vă rugăm să încercați din nou.'), \
            'Error, mesajul de eroare este incorect'
        self.assertTrue(
            self.driver.find_element(*self.button_cont_conectare1).is_displayed()), 'Error, logare fara cont valid'
        # Test 6: Stergeti valoarea de pe campul email si introduceti o valoare invalida (adica fara caracterul "@"),
        # fara sa introduceti si parola si verificati faptul ca butonul este dezactiva
        self.driver.find_element(*self.casuta_email).clear()
        self.driver.find_element(*self.casuta_email).send_keys('iepuregmail.com')
        time.sleep(3)
        self.assertFalse(self.driver.find_element(*self.button_cont_conectare1).is_enabled()), \
            'Error, login button is enabled'

    def tearDown(self) -> None:
        self.driver.quit()
