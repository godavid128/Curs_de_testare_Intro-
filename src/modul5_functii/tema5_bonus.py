print('TEMA 5, EX BONUS')


# 1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
# numerele comune. Ex: list1 = [1, 1, 2, 3], list2 = [2, 2, 3, 4], Răspuns: {2, 3}
def intersectie(list1, list2):
    return set(list1).intersection(list2)


list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
print(intersectie(list1, list2))


# 2.. Funcție care să aplice o reducere de preț
# Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
# Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e invalidă.
def reducere(pret, soldes):
    pret_redus = pret - (pret * soldes) / 100
    if pret_redus >= pret_redus / 2:
        return pret_redus
    else:
        return f'Reducere invalida'


print(reducere(100, 10))
print(reducere(100, 50))
print(reducere(100, 90))
print(reducere(100, 99))
print(reducere(1000, 120))

# 2.1 Program python pt a calcula reducerea in functie de pretul de vanzare.
#   - daca valoare comenzii e m mare de 1000 - aplicam reducere de 20%
#   - daca valoare comenzii e m mare de 500 - aplicam reducere de 10%
#   - daca valoare comenzii e m mica de 500 - aplicam reducere de 5%
print('Calcularea reducerii in functie de pret')
rate = 100
quantity = 2  # float(input("Enter Quantity: "))
amount = rate * quantity  # rate-pret; amound-suma
print(f'Amount = {amount}')
if (amount >= 1000):
    discount = 20
elif (amount >= 500 and amount <= 999):
    discount = 10
else:
    discount = 5
discountAmount = (amount * discount) / 100
netAmt = amount - discountAmount

print('Discount = %d%% and Discount Amount = %.2f' % (discount, discountAmount))

print('Net Amount = ', netAmt)

# 3. Funcție care să afiș data și ora curentă din ro. (la fel si pt din China)

from datetime import datetime, timedelta
def data_ora_FR():
    return datetime.now()
print(data_ora_FR())


def china_time():
    print(f'Data actuala a Chinei este: {datetime.today()} + 6 ore ')
china_time()

# 4. Funcție care să afișeze câte zile mai sunt până la ziua ta
def calcul_nr_zile_birthday(data_azi, data_birth):
    zile_ramas = data_azi - data_birth
    return zile_ramas


data_azi = datetime.now()
data_birth = datetime(2023, 4, 4)
print(f'Until my Birthday is:', calcul_nr_zile_birthday(data_azi, data_birth))
data_birth = datetime(2023, 10, 10)
print(f'Until my wife is Birthday:', calcul_nr_zile_birthday(data_azi, data_birth))
data_birth = datetime(2024, 7, 17)
print(f'Pana la ziua lui Samy mai sunt:', calcul_nr_zile_birthday(data_azi, data_birth))
