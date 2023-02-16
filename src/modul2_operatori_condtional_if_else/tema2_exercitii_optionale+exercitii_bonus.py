# 1. Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre
a = 1234
lungimea_a = len((str(a)))
if lungimea_a >= 4:
    print(f'{a} are minim 4 cifre')
else:
    print(f'{a} nu are minim 4 cifre')

# 2. Verifica daca x are 6 cifre:
b= 123456
lungimea_b = len(str(b))
if lungimea_b == 6:
    print(f'{b} are exact 6 cifre')
else:
    print(f'{b} nu are 6 cifre')

# 3. verifica daca x este numar par sau impar
c = 5
if c % 2 == 0:
    print(f'{c} este par')
else:
    print(f'{c} este impar')

# 4. Avand trei variabile x, y, z (toate int) afiseaza in consola care este cel mai mare dintr
x = 89
y = 46
z = 45
print(f'Cel mai mare numar este: {max(x, y, z)}')

# 5. x, y, z => laturile unui triunghi. verifica si afiseaza daca triunghiul este valid sau nu
#    un triunghi e valid daca suma tuturor unghiurilor = 180 grade
#    sau suma lungim a oricare 2 laturi > lungimea a celei de-a 3 latura
if x != 0 and y != 0 and z != 0 and (x + y + z) == 180:
    if x < (y + z) and y < (z + x) and z < (x + y):
        print(f'Triunghi valid')
    else:
        print(f'Triunghi invalid')
else:
    print(f'Triunghi invalid')

# 6. avand str: 'Coral is either the stupidest animal or the smartest rock'
#    citeste de la tastatura un numar x de tip int si afise str fara ultimele x caractere.
#    ex: daca ati ales 7 se va afisa urm string: 'Coral is either the stupidest animal or the smarte'
fraza =  'Coral is either the stupidest animal or the smartest rock'
fraza_taiata = int(input('Introdu un numar: '))
print(fraza[:-fraza_taiata])

# 7. Din stringul ex.6, declaram un string nou care sa fie format din primele 5 caractere + ultimele 5
fraza_5_5_caractere = fraza[:5] + fraza[-5:]
print(fraza_5_5_caractere)

# 8. Din stringul ex.6, salveaza intr-o variabila si afiseaza indexul de start al cuvant 'rock'
#                       adica pozitia in string la care incepe cuvant 'rock'
#    hint: este o functie care te ajuta. Folosind aceasta variabila + slicing, afiseaza tot string
#    pana la acest cuvant.
fraza_rock = fraza.index('rock')
print(fraza_rock)
# caz 1 de rezolvare pt ex 8
fraza_fara_rock = fraza.replace('rock', ' ')
print(fraza_fara_rock)
# caz 2 de rezolvare pt ex 8
d = slice(-4)
print(fraza[d])

# 9. citeste de la tastatu un string si verifica cu 'assert daca I si ultim caracter sunt la fel.
#    se doreste ca program sa fie case insensitive, adica 'apA' e acceptat ca un string
#    hint: te poti folosi de o functie pt a face string => case insensitive
nume = input('Introdu un nume: ')
nume1 = nume.lower()
nume2 = nume1[0] == nume1[-1]
assert nume2 == True
print(nume2)

# 10. avand stringul '0123456789' afiseaza doar num pare si apoi doar num impare.
#     hint: folos 'slicing'  si controleaza afisarea in slicing cu slicing step
numere = '0123456789'
par = slice(0, 10, 2)
print(numere[par])
impar = slice(1, 9, 2)
print(numere[impar])

print(f'EXERCITII BONUS')
'''
1. Creem o aplicatie pt achizit bilete de avion care sa prim drept inputuri urm info:
    varsta; insotit de mama; insot de tata; passaport; act permesiune mama; act perm tata
    conditii de imbarcare: 1.daca are varsta > 18 ani si are pasaport
                           2. daca varsta < 18 ani, are pasaport si e insotit de ambii parinti
                           3. daca varsta < 18 ani, are pasaport si e insotit de un parinte si are perm celuilalt parinte
Scrie cod care implem conditii de imbarca de mai sus si testeaz cu toate variant.
Genereaza scenarii de testare cu 'expected result si apoi run cod pt a verific daca 'expected result == actual result
Scenarii de testare:
1. Varsta 20 ani, are pasaport => calatorie placuta.
2. Varsta 20 ani, nu are pasaport => nu poti fi imbarcat fara pasaport. 
3. Varsta 17 ani, are pasaport, ambii barinti => calatorie validata
4. Varsta 12 ani, are pasaport, cu tata => Nu te poti imbarca
5. Varsta 12 ani, are pasaport, cu mama => Nu te poti imbarca
6. Varsta 12 ani, are pasaport, cu mama + Procura tata => calatorie fericita cu tata
7. Varsta 12 ani, are pasaport, cu tata + Procura mama => calatorie fericita cu mama
8. Varsta 12 ani, are pasaport, cu tata + Procura tata => Nu te poti imbarca
9. Varsta 12 ani, are pasaport, cu mama + Procura mama => Nu te poti imbarca
'''
varsta = int(input('Introdu varsta ta: '))
passaport = str(input('Ai passaport? Raspunde da sau nu: ')).lower().strip()
if varsta >= 18 and passaport == 'da':
    print('Calatorie placuta')
elif varsta >= 18 and passaport == 'nu':
    print('Nu poti fi imbarcat fara pasaport')
else:
    print('Mai trebuie ceva acte')
    tata = str(input('Esti insotit de tata? Raspunde cu da sau nu: ')).lower().strip()
    mama = str(input('Esti insotit de mama? Raspunde cu da sau nu: ')).lower().strip()
    if varsta <= 18 and passaport and tata == 'da' and mama == 'da':
        print('Calatorie validata')
    else:
        print('Inca ceva')
        procura_t = str(input('Ai act permesiune tata? Raspunde cu da sau nu: ')).lower().strip()
        procura_m = str(input('Ai act permesiune mama? Raspunde cu da sau nu: ')).lower().strip()
        if varsta <= 18 and passaport and procura_m == 'da' and tata == 'da':
            print('Calatorie fericita cu tata')
        elif varsta <= 18 and passaport and (procura_t == 'da' and mama == 'da'):
            print('Calatorie fericita cu mama')
        else:
            print('Nu te poti imbarca')

# 2. joc de noroc: vezi cum se genereaza un nr radom. Dai cu zarul si salvezi acest nr intr-o variab.
#    Nr.salvat va fi generat random. Utiliz introdu un nr de la tastatu. Verifica si afiseaz daca utiliz a ghicit nr.
#    vor exista 3 optiuni: 1. Ai pierdut. Ai ales un nr <. Ai ales x dar a fost y
#                          2. Ai pierdut. Ai ales un nr >. Ai ales x dar a fost y
#                          3. Ai ghicit. Felicitari. Ai ales x si zarul a fost y
import random
dice_roll = int(random.randint(1, 6))
numar = int(input('Introdu un numar de la 1-6: '))
if numar < dice_roll:
    print(f'Ai pierdut. A fost {numar} < {dice_roll}')
elif numar > dice_roll:
    print(f'Ai pierdut. A fost {numar} > {dice_roll}')
elif numar == dice_roll:
    print(f'Ai ghicit. Ai ales {numar} si zarul a fost {dice_roll}')
