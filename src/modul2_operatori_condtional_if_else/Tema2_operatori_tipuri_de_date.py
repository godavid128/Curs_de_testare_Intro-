# 1. Cum functioneaza un if - else
#    Sunt conditii care bifurcheaza codul, if - daca indeplineste conditia, codul ruleaza pe aici, daca nu codul ruleaza prin else

# 2. Verifica si afiseaza daca x este numar natural sau nu (nr natural - nr intreg >0
x = int(input('Introdu un numar: '))
if x > 0:
    print('Numar natural')
else:
    print('Numar nenatural')

# 3. Verifica si afiseaza daca x este numar pozitiv, negativ, neutru
if x > 0:
    print('Numar pozitiv')
elif x < 0:
    print('Numar negativ')
else:
    print('Numar neutru')


# 4. Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval)
if x > -3 and x < 14:
    print('x este cuprins intre numerele -2 si 13')
else:
    print('x este in afara listei -2 si 13')

# 5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (dif inse cate numere
#    sunt intre x si y, nu rezultatul diferentei intre x si y).
#    Hint: Se va folosi functia abs
y = int(input('Introdu al 2 numar: '))
diferenta_xy = abs(x-y)
print(diferenta_xy)
if diferenta_xy < 5:
    print(f'Diferenta dintre {x} si {y} este mai mica 5 numere')
else:
    print(f'Diferenta dintre {x} si {y} este diferita de 5 numere')

# 6. Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)
#caz1
d = 28
if not (d < 5 or d > 27):
    print(f'{d} este intre 5 si 27')
else:
    print(f'{d} nu este intre 5 si 27')
#   caz2 cu functia not pt ex 6
e = 27
if not (5 <= e < 28):
    print(f'{e} este in afara lui 5 si 27')
else:
    print(f'{e} este in interiorul lui 5 si 27')

# caz 3 pt ex 6 - for i in range
a = 5
b = 27
numar = 28
for i in range(a,b+1):
    if numar == i:
        print(f'{numar} se afla in intervalul lui {a} si {b}')
        break
    if i == b:
        print(f'{numar} NU se afla in interval lui {a} si {b}')

# 7. Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale,
#    daca nu, afiseaza care din ele este mai mare
x1 = 5
y1 = 5
if y1 == x1:
    print(f'{x1} si {y1} sunt egale')
elif y1 > x1:
    print(f'{y1} > {x1}')
else:
    print(f'{y1} < {x1}')
assert y1 == x1

# 8. Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca
#   triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau
#   oarecare (nicio latura nu e egala).
x2 = 1
y2 = 2
z2 = 3
if x2 == y2 and y2 == z2 and z2 == x2:
    print(f'Triunghiul este echilateral')
elif x2 == y2 or y2 == z2 or z2 == x2:
    print(f'Triunghiul este isocel')
else:
    print(f'Triunghi oarecare')

# 9.  Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie!
#       Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.
litera = input('Introdu o litera: ')
if litera in 'aeiouAEIOU':
    print(f'Litera este o vocala')
else:
    print(f'Litera este o consoana')

# 10. Transforma si printeaza notele din sistem românesc in sistem american
nota = 7
if nota > 10 or nota < 1:
    print(f'Nota invalida')
elif nota >= 9:
    print(f'Nota este A')
elif nota >=8:
    print(f'Nota este B')
elif nota >=7:
    print(f'Nota este C')
elif nota >=6:
    print(f'Nota este D')
elif nota > 4:
    print(f'Nota este E')
elif nota <= 4:
    print(f'Nota este F')
else:
    print(f'0')
