from selenium.webdriver.common.by import By
# locatori = selectori = elemente pe care le localizez din html
# Variabile = se pot modifica
# Constante = nu ar trebui sa se modifice. Sunt scrise cu litere mari


class AlertsLocators:
    JS_ALERT = (By.XPATH, '//*[@id="content"]/div/ul/li[1]/button')
    JS_CONFIRM = (By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')
    JS_PROMPT = (By.XPATH, '//*[@id="content"]/div/ul/li[3]/button')
    RESULT = (By.ID, 'result')

# todo in loc de variabile sa fie constante cu lit mari - FACUT
#   Sa creem un nou project - Pycharm