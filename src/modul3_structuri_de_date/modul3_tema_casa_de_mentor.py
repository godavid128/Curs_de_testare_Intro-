# TEMA PT ACASA
# 1.  TODO SA sortam lista 2 dupa penultimul litera din fiecare string
#      expected result = [mac, ipad, apple, iphone]
lista_1 = [1, 2, 3, 4, 5, 6]
lista_2 = ['Apple', 'mac', 'iphone', 'ipad', 'apple']
lista_3 = [1, True, '_', False, 5, 2]
lista_2.sort(key=lambda x: x[-2])
print(lista_2)
# exempl 2 pentru ex 2
# lista_4 = ['abcd', 'efgah', 'ijkl', 'mnoap']
# lista_4.sort(key=lambda x: x[-2])
# print(lista_4)
# lista_4.sort(key=lambda x: x[-1])
# print(lista_4)

# 2. # TODO count cate elem sunt intr-o lista mai multe decat o data =>
#       cu conditia ca: app le, app_le, Apple, app?le => apple
print('Numaram cate elemente sunt in lista de acelasi fel')
lista_2_1 = ['Apple ', 'mac', 'iphone', 'ipad', 'app.le', 'app le', 'app?le', 'app_le']
# Cum transformam Apple => apple prin lower si sa ramana in lista cu litera mica
def all_lower(lista_2_1):
    return [ x.lower() for x in lista_2_1]
print(all_lower(lista_2_1))
print([i for i in lista_2_1 if not i.isalnum()])
print(len([i for i in lista_2_1 if not i.isalnum()]))

# 3. TODO sa extragem din lista mare '_', ultimul 6, 2 din mijloc. folosesti if statement, if count
lista_matrice = [lista_1, lista_2, lista_3]
lista_mare = [lista_matrice, [0, 1, lista_1], ['a', 'b', 'c'], [lista_matrice], {}, True]
print('Extragem 2 din mijloc')
mijlocul_listei_mari = int((len(lista_mare)/2)-1)
print(mijlocul_listei_mari)
if mijlocul_listei_mari == 2:
    print('Mijlocul listei este 2')
else:
    print('Mijlocul listei nu este 2')
print('Extragem simbolul _')
# lista_mare = lista_mare[0]
# lista_mare[0] = lista_mare[2]
# print(lista_mare[2][2])
print(lista_mare[0][2][2])
print('Extragem ultimul 6')
# lista_mare = lista_mare[-3]
# print(lista_mare[0][0][5])
print(lista_mare[-3][0][0][5])

# 4. TODO display john and his email only his isActive is true. tr sa extragi status
#     creaza un dictionar mai complex cu date primite pt key,
#     pt valori: lista de ddictionare cu tuple, set, liste
print('TODO 4 dict')
anul_2023 = {
    'anotimpul': 'toamna este',
    'luna': 'ianuarie',
    'saptamana': 3,
    'sarbatori': {
        'iarna': ('nasterea Domnului Isus', 'anul nou', 2022-2023),
        'primavara': {'pastele', 'post', 30},
        'vara': ['ziua copiilor', 'vacanta mare', 3],
        'toamna1': {
            '1 zi de scoala': 'septemnbrie',
            'ziua multumirii': 'octombrie ',
            'luna 10': 'noiembrie'
        }
    }
}
print(anul_2023['anotimpul'], anul_2023['sarbatori']['toamna1'])
print(anul_2023['sarbatori'])

# 5. TODO Sa listam metodele de LISTE. sa incercam
print('Metode cu liste')
print(lista_1)
print(lista_1.index(1))
lista_1.extend('101')
print(lista_1)
lista_1.reverse()
print(lista_1)
lista_1.clear()
print(lista_1)

# 6. TODO Sa listam metodele de SETURI. sa incercam
print('Metode cu seturi')
my_set = {2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 0, 6, 7, }
print(my_set)
my_set.add(20)
my_set.add('sambata')
print(my_set)
print(my_set.pop())
print(my_set)
my_set.remove(7)
print(my_set)
my_set.discard(20)
print(my_set)

# 7. TODO Sa listam metodele de TULURI. sa incercam
print('Metode cu tupluri')
tuple = (1, 2, 5, 7, 3, 4, 6, 7, 8, 9, 10)
print(tuple.count(7))
print(tuple.index(4))
print(len(tuple))

