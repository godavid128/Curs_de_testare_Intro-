'''
POM - Partea practica. Aranjarea proiectului. Se face in 3 nivele:
                        1.Difinirea locatorilor pt o pagina website
                        2.Actiunile pe care le putem face cu locatorii respectivi. ex: click, enable, vizibile
                        3.Teste - alegem ce actiuni folosim si doar le apelezi. Aici putem sa apelam propriile metode
BDD si POM - pot functiona impreuna? da, pt ca BDD ne ofera o structura fff simpla prin care pot sa faci un mic freemork
de automation, dar cand ajungi sa ai o pagin fff mare (ex.website cu super m functiona) - practic toti pasii pe care ii
immplemen in python, vor fi foarte multi => si ar fi o practica gresita sa-i pastram in fuctie, insa folosindu-ne de
POM - ii putem sparge si mai bine => organizare mai buna
'''
import time
from src.modul11_POM.pages.alerts_page import AlertPage
from src.modul11_POM.pages.alerts_pages_handling import AlertsPagesHandling
from src.modul11_POM.pages.home_page import HomePage
from src.modul11_POM.tests.base_test import BaseTests


class TestAlert(BaseTests):

    def test3(self):
        # POM
        # Facem instante de ce clase avem nevoie. Facem un obiect 'home_page' si 'alert_page'.
        home_page = HomePage(self.driver)
        alert_page = AlertPage(self.driver)
        alert_page_handling = AlertsPagesHandling(self.driver)

        home_page.go_to_alert_section()

        alert_page_handling.accept()
        alert_page.page_alert()

        alert_page.page_confirm()
        alert_page_handling.dismiss()

        alert_page.page_prompt()
        alert_page_handling.send_keys()
# TODO  PT CELElalte teste din modul 10 sa facem la fel???
