# if
ferrari_prise = 50000000
varsta = int(input('majorat'))
sold = int(input('Sold:'))
cash = int(input('Cash:'))
apt_de_munca = True
if sold < cash:
    print('Sold insuficient')
    if varsta < 18:
        print('Cere bani la parinti')
    else:
        print('Bravo, este mare')
        if apt_de_munca:
            print('Angajeaza-te!')
elif sold == cash:
    print('Soldul va fi 0')
else:
    sold = sold - cash
    print(sold)
    if sold > ferrari_prise:
        print('Cumpara ferrari')
        sold = sold - ferrari_prise
        print(sold)
        ferrari_discount = ferrari_prise - ferrari_prise * 0.15
        if sold > ferrari_discount:
            print('Cumpara a 2-lea Ferrari')
    else:
        print('Ia-ti Dacia')


