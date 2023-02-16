# 1. Functie care prime o luna din an si return cate zile are luna
from calendar import monthrange


def luna_din_an(year, month):
    return monthrange(year, month)[1]


print('anul 2023')
print(f'Luna ianuarie', luna_din_an(2023, 1))
print(f'Luna februarie', luna_din_an(2023, month=2))
print(f'Luna martie', luna_din_an(2023, month=3))
print(f'Luna aprilie', luna_din_an(2023, month=4))


# 2. Functie calculator care return 4 valori: suma, diferenta, inmultirea, impartirea a 2 num.
#   In final vei putea face: a, b, c, d = calculator(10, 2)
#   print('summa:', a); print('dife:', a); print('imult:', a); print('imparti:', a);
# METODA 1
def calculator(num1, num2):  # Calculeaza cu cei 4 operatori: +, -, *, /
    a = num1 + num2
    b = num1 - num2
    c = num1 * num2
    d = num1 / num2
    return a, b, c, d


a, b, c, d = calculator(10, 5)
print('Suma:', a)
print('Diferenta:', b)
print('Inmultirea:', c)
print('Impartirea:', d)


# METODA 2
def suma(num1, num2):
    return num1 + num2


def diferenta(num1, num2):
    return num1 - num2


def inmultirea(num1, num2):
    return num1 * num2


def impartirea(num1, num2):
    return num1 / num2


print(f'Suma:', suma(10, 2))
print(f'Diferenta:', diferenta(10, 2))
print(f'Inmultirea:', inmultirea(10, 2))
print(f'Impartirea:', impartirea(10, 2))


# operator = input('Selecteaza un operator: +, -, * sau /: ')  # Calculator
# numar1 = int(input('Introdu 1-ul numar: '))
# numar2 = int(input('Introdu al 2-lea numar: '))
#
# if operator == '+':
#     print(numar1, '+', numar2, '=', suma(numar1, numar2))
# elif operator == '-':
#     print(numar1, '-', numar2, '=', diferenta(numar1, numar2))
# elif operator == '*':
#     print(numar1, '*', numar2, '=', inmultirea(numar1, numar2))
# elif operator == '/':
#     print(numar1, '/', numar2, '=', impartirea(numar1, numar2))
# else:
#     print('N-ai introdus un operator valid')

# 3. Functie care primeste o lista de cifre (adica doar 0-9). Ex: [1, 3, 1, 5, 7, 7, 5, 5]
#   Returneaza un DICT care ne spune de cate ori apare fiecare cifra
#   => dict {0: 0, 1: 2, 2: 0, 3: 1, 4: 0, 5: 3, 6: 0, 7: 2, 8: 0, 9: 0 }
# METODA 1
def numararea_fregventei(list1):
    fregventa = {}
    for n in list1:
        if (n in fregventa):
            fregventa[n] += 1
        else:
            fregventa[n] = 1
    for key, value in fregventa.items():
        print('% d: %d' % (key, value))


list1 = [1, 3, 1, 5, 7, 7, 5, 5]
numararea_fregventei(list1)


# METODA 2
def frecventa_num(listamea):
    dict = {}
    for i in listamea:
        dict[i] = dict.get(i, 1) + 1
    return dict


listamea = [1, 3, 1, 5, 7, 7, 5, 5]
print(frecventa_num(listamea))


# 4. Functie care primeste 3 numere. Return valoarea maxima dintre ele:
def numar_max(a, b, c):
    return max(a, b, c)


print(f'Numarul maxim este:', numar_max(2, 5, 10))


# 5. Functie care sa primeasca un numar si sa return suma tuturor num de la 0 la acel num
#   Ex: daca dam nr 3. Suma va fi 6 (0+1+2+3)
def suma_totala_numere(nr1):
    summ = 0
    while (nr1 > 0):
        summ += nr1
        nr1 -= 1
    return summ


print(f'Suma tuturor numerelor este: ', suma_totala_numere(10))
