# if
piesa_faina = True
print('pornim radio')
if piesa_faina == True:
    print('dam mai tare')
    print('fredonam')
print('oprim radio')

#if else
# daca nr este par printam acest lucru
# altfel printam impar
nr = 2
# ce inseamna par? se imparte exact la 2
# ce inseamna ca se imparte la 2? ne da restul 0
if nr % 2 == 0:
    print('nr par')
else:
    print('impar')

# este un nr pozitiv?
if(nr > 1):
    print('pozitiv')
else:
    print('nr nu este pozitiv')

#daca utilizatorul are sub 18 ani, nu poate paria

# if, else if, else
# cum ne saluta robotelul in functie de ora?
# luam date de la tastatura
# ne asiguram ca sunt transformate din string in int
# ora  = int(input('Introdu ora'))
# if ora < 0:
#     print('ora invalida. ora negativa')
# elif ora <=11:
#     print('buna dimineata')
# elif ora <= 18:
#     print('buna ziua')
# elif ora <= 21:
#     print('buna seara')
# elif ora <= 24:
#     print('noapte buna')
# else:
#     print('ora invalida. ora mai mare decat 24')
    # else este iesire de pe autostrada
    # cum le comentam obtiunile, sau revenim ? prin CTRL +/

# robotel telefonic
obtiune = int(input('Alege o optiune'))
if obtiune == 0:
    print('meniu anterior')
elif obtiune == 1:
    print('ati ales ro')
elif obtiune == 2:
    print('ati ales eng')
else:
    print('nu am identificat optiunea, mai incearca')
