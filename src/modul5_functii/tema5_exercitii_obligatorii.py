# 1. Functie care sa calc si return suma a 2 num
def suma_2_numere(a, b):
    suma = a + b
    return suma


print(f'Suma a 2 numere este', suma_2_numere(2, 5))
print(f'Suma a 2 numere este', suma_2_numere(10, -5))


# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
def numar_par_impar(numar):
    return numar % 2 == 0


print(numar_par_impar(355))
print(numar_par_impar(22))


# 3. Funcție care retur num total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)
def lungime_nume(nume):
    return len(nume)


print('Lungimea numelui integral e', lungime_nume('gorodetchi david go'))
print('Lungimea numelui integral e', lungime_nume('ion-mic grecu'))


# 4. Functie care return aria dreptunghiului
def aria_dreptunghiului(a, b):
    aria_drep = a * b
    return aria_drep


print('Aria dreptunghiului e', aria_dreptunghiului(3, 7))
print('Aria dreptunghiului e', aria_dreptunghiului(6, 10))


# 5. Functie care return aria cercului
def aria_cercului(PI, R):
    aria_cerc = PI * R * R
    return aria_cerc


print('Aria cercului este', aria_cercului(3.14, 4))
print('Aria cercului este', aria_cercului(3.14, 10))


# 6. Funcție care return True dacă un caracter x se găsește într-un string dat
#   și False dacă nu găsește.
def caracterul_r():
    caracter = 'Iar venir iarna, afara iar e frig '
    litera_r = 'a'
    #    litera_r = 'Z'
    if litera_r in caracter:
        return True
    else:
        return False


print(caracterul_r())


# 7. Functie fara return, primeste un string si print:
#   - Nr de caractere lower case e x; - Nr de caract upper case e y
# metoda 1 la ex 7
def litere_mari_mici(litere):
    mari_mici = {'litere_mari': 0, 'litere_mici': 0}
    for l in litere:
        if l.isupper():
            mari_mici['litere_mari'] += 1
        if l.islower():
            mari_mici['litere_mici'] += 1
    print(mari_mici)


litere_mari_mici('Astazi este o Zi Insorita')


# metoda 2 la ex 7
def litere_mari_mici(litere):
    mari = 0
    mici = 0
    for l in litere:
        if l.isupper():
            mari += 1
        if l.islower():
            mici += 1
    print(f'Litere mari sunt', mari, 'Litere mici sunt', mici)


litere_mari_mici('Am reusit sa Gasesc Litere MARI si MICI')


# 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu num pozitive
# metoda 1 a ex 8
def lista_numere(*numere):
    numere = [2, -2, 4, -5, 9, 10, 22]
    numar = 0
    lista1 = []
    for n in numere:
        if n >= 0:
            numar += 1
    lista1.append(numar)
    return lista1


print(f'Avem {lista_numere()} numere pozitive')


# metoda 2 a ex. 8
def lista_nr_pozitive(lista1, lista2):
    if lista1 == len(lista2):  # conditia de baza
        return
    if lista2[lista1] >= 0:
        print(lista2[lista1], end=" ")  # end= '' - listeaza num pe aceeasi linie
    lista_nr_pozitive(lista1 + 1, lista2)  # apelul functiei recursive


lista2 = [2, -2, 4, -4, 10, 11]  # lista cu numere
print('Numerele pozitive sunt:')
lista_nr_pozitive(0, lista2)  # apelarea functie
print(end='\n')


# 9. Functie care nu returneaza nimic. Primeste 2 num si print:
#   - x > y; - y > x; numerele sunt egale
def doua_numere(x, y):
    if x > y:
        print(f'{x} este mai mare decat {y}')
    elif y > x:
        print(f'{y} este mai mare decat {x}')
    else:
        print(f'{x} e egal cu {y}')


doua_numere(3, 9)
doua_numere(-5, 2)
doua_numere(2, 2)


# 10 Functie care primeste un num si un set de numere. - Print: 'am adaugat num nou in set'
#   + return True. Print: 'nu am adaugat num in set. Aceasta exista deja' + return False
def functia_numar_set(numar, set):
    if numar in set:
        print(f'Nu am adaugat numarul {numar}, pentru ca exista deja')
        print(set, end=' ')
        return False
    else:
        set.add(numar)
        print('Am adaugat un numar nou in set')
        print(set, end=' ')
        return True


print(functia_numar_set(1, {2, 3, 4}))
print(functia_numar_set(3, set={2, 3, 4}))


# aflam patratul nr trasm din exterior
def patrat(numar):
    return numar ** 2




print('Patratul numarului dat este:', patrat(4))
