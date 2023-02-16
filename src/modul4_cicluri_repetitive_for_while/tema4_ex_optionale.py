
print('EXERCITII OPTIONALE TEMA 4')
# 1.  Itereaza prin listă alte_numere. Populează corect cele liste. Afiș cele 4 liste la final
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for numere in alte_numere:
    if numere % 2 == 0:
        numere_pare.append(numere)
    if numere % 2 != 0:
        numere_impare.append(numere)
    if numere > 0:
        numere_pozitive.append(numere)
    if numere < 0:
        numere_negative.append(numere)
print(f'Numere pare sunt:', numere_pare)
print(f'Numere impare sunt:', numere_impare)
print(f'Numere pozitive sunt:', numere_pozitive)
print(f'Numere negative sunt:', numere_negative)

# 2. Aceeași listă: Ordonează crescător lista fară să folosești sort.
#   Te poți inspira vizual de aici. https://www.youtube.com/watch?v=lyZQPjUT5B4
for i in range(len(alte_numere)):
    for n in range(i + 1, len(alte_numere)):
        if alte_numere[i] > alte_numere[n]:
            alte_numere[i], alte_numere[n] = alte_numere[n], alte_numere[i]
print(alte_numere)

# 3. Ghicitoare de număr:  numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None. Folosind un while. User alege un număr
# Programul îi spune: ● Nr secret e mai mare ● Nr secret e mai mic ● Felicitări! Ai ghicit!
import random
num_secret = random.randint(1, 30)
incercari = 0  # numaram cate incercari am avut de a ghici
ghici = 0
while ghici != num_secret:
    ghici = eval(input('Ghiceste un numar de la 1-30: ')) # eval = evalueaza dinamic elemente
    incercari += 1
    if ghici == num_secret:
        print('Felicitari! Dupa', incercari, 'incercari, ai ghicit!')
        print(f'Nr secret este', num_secret)
        break
    elif ghici < num_secret:
        print('Nr secret e mai mare!')
    else:
        print('Nr secret e mai mic!')

# 4. Alege un număr de la tastatură
# Ex: 4. Scrie un program care să genereze în consolă următoarea piramidă
# 1
# 22
# 333
# 4444
piramida = int(input('Introdu un numar pentru piramida: '))
for i in range(piramida +1):
    for j in range(i):
        j += 1
        print(i, end=' ')
    print()
# 5.Iterează prin listă 2d. Print ‘Cifra curentă este x’. (hint: nested for - adică for în for)
tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for lista in tastatura_telefon:
    for lista1 in tastatura_telefon:
        print(f'Cifra curenta este {lista} {lista1}')

# repetarea unei liste 1D
data = [0, 1, 4]
for i in range(len(data)):
    print(data[i], end=' ') # end= afiseaza elementele pe aceeasi linie orinzotala
