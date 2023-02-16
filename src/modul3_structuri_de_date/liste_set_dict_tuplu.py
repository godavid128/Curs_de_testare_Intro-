# Avem datele: lista, set, tuple, dictionar
data_type = 'tuple' # daca dam run cu lista va rula ramura liste
if data_type == 'lista':
    print('lista')
    # lista
    lista_1 = [1, 2, 3, 4, 5, 6]
    lista_2 = ['apple', 'mac', 'iphone', 'ipad', 'apple']
    lista_3 = [1, True, '_', False, 5, 2]
    print(lista_1[0], lista_1[len(lista_1) - 1])
    lista_1.reverse()
    print(lista_1)
    lista_1.sort()
    print(lista_1)
    lista_2.sort()
    print(lista_2)

    # TODO SA sortam lista 2 dupa penultimul litera din fiecare string, expected result = [mac, ipad, apple, iphone]
    # lista_3.sort()
    # print(lista_3) - nu se poate sorta aceste date
    print(lista_2.count('apple'))
    # TODO count cate elem sunt intr-o lista mai multe decat o data => cu conditia ca: app le, app_le, Apple, app?le = apple
    # sa listam metodele de liste. sa incercam
    print(sum(lista_1))
    print(lista_1 + lista_2)
    x = ['a', 'b', 'c', 'd']
    y = x.copy() # afisam in consola valorile lui x si y separat
    u = x[:]     # la fel afis in consol valor lui x si y separat
    y[0] ='E'
    print(x, y, u)
    print(id(x), id(y), id(u)) # id - aflam indetatea variabilei.
    if id(x) != id(y):
        print('sunt egale')
    if id(x) == id(y):
        print('nu sunt egale')
    lista_matrice = [lista_1, lista_2, lista_3]
    print(lista_matrice)
    lista_mare = [lista_matrice, [0, 1, lista_1], ['a', 'b', 'c'], [lista_matrice], {}, True]
    print(lista_mare) # sa vedem linia 32
    print(lista_mare[0]) # vrem sa vede lista mare[0]
    print(lista_mare[0][0])
    print(lista_matrice[0][0][1])
    # TODO sa extragem din lista mare '_', ultimul 6, 2 din mijloc. folosesti if statement, if count
elif data_type == 'set':
    print('set')
    # SET TODO DE testat celelalte metode din seturi
    my_set = {2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7,}
    print(my_set)
    my_list = [1, 1, 1, 1]
    print(list(set(my_list)))
    second_set = {1, 2, 3, 8, 20, 5, 7}
    print(my_set.difference(second_set), my_set.intersection(second_set))
    second_set.difference_update(my_set)
    print(my_set)
elif data_type == 'tuple':
    print('tuple')
    # tuple TODO de facut tot ce facem la liste
    tuple = (1, 2, 5, 7)
    print(tuple[0], tuple[-1])
    a = (1,)
    print(type(a))
    print((a)[:])
elif data_type == 'dictionar':
    print('dictionar')
    # TODO display john and his email only his isActive is true. tr sa extragi status
    # creaza un dictionar mai complex cu date primite pt key, pt valori lista de ddictionare cu tuple, set, listei
    dictionar = {
        'user1': 'admin',
        'user2': 'petre',
        'user3': {
            'name': 'john',
            'email': 'john@jahn.com',
            'isActive': True
        }
    }
    print(dictionar['user2'], dictionar['user3']['email'])
    print(dictionar['user3']['isActive'])