class BankAccount:
    bank_name = 'banca transilvania'

    #  CONSTRUCTORUL TB SA FIE TOT PRIMA METODA IN LISTA
    # REGULA - CAND UN PARAMETRU APARE MAI MULT DE 2 ORI, POATE FI PUS IN CONSTRUCTOR
    def __init__(self, user, pwd):
        self._user = user
        self._pwd = pwd

    def cont_bancar(self, iban, adresa, cont_economii, cont_credit):
        print(f'Hi: {self._user}, Iban dv: {iban}, Pin: {self._pwd}, Adres: {adresa},'
              f'Cont1: {cont_economii}, Con2: {cont_credit}')

        return 'cont activ'

    def log_in(self):
        print(self.bank_name)
        print(BankAccount.bank_name)
        return f'{self._user} log_in with {self._pwd}'

    def interogare_sold(self, sold):
        status_log_in = self.log_in()
        if status_log_in == 'john log_in with 1111':
            print(f'soldul {self._user} este {sold}')
        else:
            print(f'user inexistent')
            # este un decorator, ne permite sa avem acel curs valutar

    @staticmethod # @ e decorator, ce decor functia care permite sa avem metod curs val, fara 'self.
    def curs_valutar(moneda):   # O face sa fie independenta de instantierea clasei
        if moneda == 'Euro':
            print('4,94')
        elif moneda == 'Usd':
            print('4,5')
        else:
            print('curs inexistent pt aceasta moneda')


# user = input('Please enter your username: ')
# pwd = input('Please enter your pwd: ')
bank_account_john = BankAccount('john', '1111')  # am creeat obiectul
bank_account_ion = BankAccount('ion', '2222')  # am creeat obiectu
# AICI APELAM
# dupa ce creeam obiectul, accesam metodele
bank_account_john.cont_bancar('0RO100BTRL', 'str.Raiului nr.12', 'RO234BTRL', 'RO1300')
bank_account_ion.cont_bancar('0RO100BTRd', 'str.iasului nr.12', 'RO24BTRL', 'RO300')
log_in_status = bank_account_john.log_in()  #
print(log_in_status)
bank_account_john.interogare_sold('20 RON')
bank_account_john.curs_valutar('Euro')



