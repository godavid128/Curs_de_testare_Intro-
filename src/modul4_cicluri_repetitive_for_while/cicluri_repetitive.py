mylist = ['unu', 2, 3, 4, True, dict(name='john'), set(), 5, {'key1': 1, 'key2': 2, 'key3': 3}]
# for numar in mylist:
#     print(numar)

# for i in range(len(mylist)): # afisam lista dupa index
#     print(i, mylist[i])

# for i in mylist:
#     if isinstance(i, str): # isinstantce - este instanta de int. este clasa de integer
#         print(i)           # isinstantce - e o masura de preventie. sa vezi exact ce este
#     elif isinstance(i, int):
#         print(i)
#     elif isinstance(i, dict):
#         print(i['name'])
#     else:
#         print(('print alceva'))

# for i, v in enumerate(mylist): # index pe I coloana, si valoarea - II coloana
#     print(i, v)              # i = index; v = valoarea
#     print(mylist[i])

# for i in range(len(mylist)):  # afisam dupa index
#     print(mylist[i])

# for i in range(len(mylist)):    # afisam dict: obtinem keile si valorile
#     if isinstance(mylist[i], dict):
#         print(mylist[i].keys(), mylist[i].values())

# for i in range(len(mylist)):
#     if isinstance(mylist[i], dict):
#         for k, v in mylist[i].items():   # afisam content de la cheia 3
#             if k == 'key3' and v == 3:
#                 print(k, v)
#
# for i in range(10, 0, -1):  # afiseaza in ordinea inversa
#     print(i)

# 1. TODO declaram o lista ce contine doar numere si aflam suma num, prin 4 metode:
#   for, for dupa index, while
# 1. Metoda 'sum'
lista_numere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 33]
# 1. Metoda 'sum'
x = sum(lista_numere)
print(f'Am aflat suma prin metoda sum: {x}')
# 2. Metoda 'for'
suma = 0
for i in lista_numere:
    suma += i
print(f'Am aflat suma prin metoda for, care este: {suma}')
# 3. Metoda 'for dupa index'
suma_totala = 0
for i in range(len(lista_numere)):
    suma_totala = suma_totala + lista_numere[i]
print(f'Am aflat suma prin metoda for dupa index, care este {suma_totala}')
# 4. Metoda 'while'
total = 0
lungimea_listei = len(lista_numere)
repetitia = 0                           # Aflam cate repetari face 'loop control'
while repetitia < lungimea_listei:
    total = total + lista_numere[repetitia]
    repetitia +=1
print(f'Am aflat suma prin metoda while {total}')
print(f'Aflam numar de repetari a loop control', repetitia)

# 2. TODO sa aflu cel mai mare nr par
par = []
for i in lista_numere:
    if i % 2 == 0:
        par.append(i)
nr_par_max = max(par)
print(f'Cel mai mare numar par este:', nr_par_max)

# 3. TODO sa goasim duplicatele dintr-o lista - sa afisez doar duplicatele
from collections import Counter

tema_list = ['ion', 'ion', 'mihai', 'mihai', 'ion', 'radu']
# dublicate = tema_list.count('ion')
# dublicate1 = tema_list.count('mihai')
# print(F'Numarul dublicatelor sunt ion:', dublicate, 'si mihai',  dublicate1)

lista_noua = []
dup_list = []
for i in tema_list:
    if i not in lista_noua:
        lista_noua.append(i)
    else:
        dup_list.append(i)
print(f'Lista duplicate', dup_list)
print(f'Lista fara dublicat', lista_noua)
