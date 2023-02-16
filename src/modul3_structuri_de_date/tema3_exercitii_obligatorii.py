''' 1.
Declara o lista note_muzicale in care sa pui do re mi etc pana la do
a. Afiseaz-o.
b. Inversează ordinea folosind slicing si suprascrie aceasta lista,
apoi printeaza varianta actuala (inversata).
c. Pe aceasta lista, aplica o metoda care banuiesti ca face același lucru, adica sa ii
inverseze ordinea (Nu trebuie sa o suprascrii în acest caz, deoarece metoda face
asta automat) si apoi printeaza varianta actuala a listei. Practic ai ajuns înapoi la
varianta inițială
Concluzii: slicing e temporar, dacă vrei sa pastrezi noua varianta va trebuie sa
suprascrii lista sau sa o salvezi intr-o listă nouă. Metoda gasita de tine face
suprascrierea automat și permanentizeaza aceste modificări. Ambele variante își
găsesc utilitatea în funcție de ce ne dorim in acel moment.
'''
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)
note_muzicale.reverse()
note_invers = note_muzicale
print(note_invers)
note_invers.reverse()
print(note_muzicale)

# 2. afiseaza pe ecran de cate ori apare nota 'do' in lista
print(note_muzicale.count('do'))

# 3. avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]. gaseste 2 variante sa le unesti intr-o sing lista
lista_1 = [3, 1, 0, 2]
lista_2 = [6, 5, 4]
varianta_1 = lista_1 + lista_2
print(varianta_1)
varianta_2 = [*lista_1, *lista_2]
print(varianta_2)

# 4. sorteaza si afiseaza lista generala la ex anterior. Sterge nr 0 din lista folos o functie si apoi afis din nou lista
varianta_2.sort()
print(varianta_2)
varianta_2.pop(0)
print(varianta_2)

# 5. folosind un if, verifica lista generala la ex.3 si afis pe fiecare ramura urm:
# - lista este goala (if);   - lista nu este goala (else)
varianta_2.clear()
if varianta_2 == varianta_2.clear():
    print('Lista este goala')
else:
    print('Lista nu este goala')

# 6. folos o functie care sa goleasca lista de la ex 3
lista_1.clear()
print(lista_1)

# 7. rescrie if-ul de la ex 5 si verifica inca o data rezultatul. acum ar trebui sa se afiseze ca lista e goala
if varianta_2 != varianta_2.clear():
    print('Lista este goala')
else:
    print('Lista nu este goala')

# 8. avand dictionarul dict = {'Ana':8, 'Gigel': 10, 'Dorel': 5}, folos o functie ca sa afisezi elevii (cheile)
elevii = {'Ana':8, 'Gigel': 10, 'Dorel': 5}
print(elevii.keys())

# 9. printeaza cei 3 elevi din dict din ex 8 si respectiv notele lor.
# ex.'Ana a luat nota {x}'; Doar nota o vei lua folosindu-te de cheie
print(f'Ana a luat nota: ', elevii['Ana'])
print(f'Gigel a luat nota: ', elevii['Gigel'])
print(f'Dorel a luat nota: ', elevii['Dorel'])

# 10. Imagineaza-ti ca Dorel a facut contestatie si a primit nota 6
# - Modifica nota lui Dorel in 6. - Printeaza nota dupa modificare
elevii['Dorel'] = 6
print(elevii)

# 11. Imagineaza-ti ca Gigel se transfera din clasa. - Cauta o functie care sa il stearga.
#  - Vine un coleg nou. - Adaug pe Ionel cu nota 9. Print dict cu noi elevi
elevii.pop('Gigel')
print(elevii)
elevii.update({'Ionel': 9})
print(elevii)

# 12. Ai urm seturi:
#   zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
#   weekend = {'sambata', 'duminica'}
# - Incearca sa adaugi in setul zilele_sapt ziua de ‘luni’ si observa ce se intampla.
# - Afiseaza setul zile_sapt si constata rezultatul adaugarii anterioare.
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('Luni')
print(zile_sapt)

# 13. Foloseste un if si verifica daca:
#   Weekend este un subset al zilelor din sapt (adica daca elementele din setul weekend se
#   regasesc intre elementele din setul zile_sapt)
#   - Weekend nu este un subset al zilelor din sapt
#   Hint: Va puteti folosi fie de  operatorul de comparatie fie de o functie.
#   Rezultatul fiecarui punct de mai sus va fi un boolean
weekend1 = weekend.intersection(zile_sapt)
print(weekend1)
if weekend1 == weekend:
    print('Zilele din weekend se regasesc in zilele saptamanii')
else:
    print('Zilele din weekend nu se regasesc in zilele saptamanii')

# 4. Afiseaza dif dintre aceste 2 seturi (adica elementele care sunt in zile_sapt si nu
#   sunt in weekend si invers)
diferenta = zile_sapt - weekend
print(diferenta)
diferenta1 = weekend - zile_sapt
print(diferenta1)

# 15. Afiseaza intersectia elementelor din aceste 2 seturi (adica elementele care exista in
# ambele seturi). Hint: Va puteti folosi de o functie
weekend1 = weekend.intersection(zile_sapt)
print(weekend1)






