# Creeam o suite cu tests de la tema9 + testele de la intalnirea 10. Generati raportul
import unittest
import HtmlTestRunner

from src.modul10_Suite_de_teste.curs_Test2_Context_Menu import TestContextMenu
from src.modul10_Suite_de_teste.curs_Test3_alerts import TestAlerts
from src.modul10_Suite_de_teste.curs_test1_autentificare import TestLogin
from src.modul9_verificatori_class_unittest_TestCase.tema9_ex_oblig_class_Login import Login
from src.modul9_verificatori_class_unittest_TestCase.tema9_ex_optionale import PasswordHacking


class MyTestSuite(unittest.TestCase):
    def test_suite(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(PasswordHacking),

            unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            report_title='report1', report_name='Smoke Test', combine_reports=True
        )
        runner.run(smoke_test)
