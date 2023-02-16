def cont_bancar(user, iban, pin, adresa, cont_economii, cont_credit):
    print(f'{user}')
    print(f'{iban}')
    print(f'{adresa}')
    print(f'{cont_economii}')
    print(f'{cont_credit}') # fara return print none
    return 'cont activ'


def log_in(user, password):
    print('Please enter your user name:', user)
    print('Please enter your password:', password)
    return 'successful log_in'


def generate_report(report):
    print(f'<h1>{report}</h1>')

# log_in('petre', 1234) # fara print, nu afisasa return din functia log_in
log_in_status = log_in('petre', 1234)
print(log_in_status)
generate_report(log_in_status) # continut luat de la o functie si trasm la alta
x = cont_bancar('david', 'RO100BTRL', 7777, 'str.Raiului nr.12', 'RO234BTRL', 'RO1300')
print(x)
