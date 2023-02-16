# listele in python pot sa cuprinda elemente de tipuri dif
# au dimensiunea dinammica
fructe  = ['mar', 'banana', 'portocala', 3, True, 3]

# afisam o lista
print(fructe)

# accesam un element in functie de index
print(fructe[1])

# adaugam un element nou  # a adauga java=add, python=append !!!
fructe.append('avocado')

# suprascriem un element
fructe[0] = 'para'

# afisam o lista
print(fructe)

# aflam dimensiunea
print(len(fructe))

# scoate si ne returneaza ultimul element
last = fructe.pop()
print('lista', fructe)
print('ultimul elem', last)

# de cate ori apare un element
print(fructe.count(3))

# extindem lista
fructe_exoctice = ['ananas', 'kiwi']
fructe.extend(fructe_exoctice)
print(fructe)

