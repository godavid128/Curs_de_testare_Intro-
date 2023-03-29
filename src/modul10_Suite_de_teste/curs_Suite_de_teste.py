import unittest
import HtmlTestRunner

from curs_Test3_alerts import TestAlerts
from curs_Test2_Context_Menu import TestContextMenu
from curs_test1_autentificare import TestLogin


class MyTestSuite(unittest.TestCase):
    def test_suite(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            report_title='report1', report_name='Smoke Test', combine_reports=True
        )
        runner.run(smoke_test)

# todo Sa integram try except in partea de alerta 'NoAlertPresentException'

# QUESTION 1. De ce folosim 2 ori HtmlTestRunner la runner?
# QUESTION 2. Ce ins runner
# Question 3. Cum integram locatorii intr-o suite din alt python package
# Question 4. De ce uneori ruleaza doar un tests, in loc de toate???



