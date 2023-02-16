"""
1. user introd din consola nume, an nasterii, luna, ziua, CNP
2. verificam daca useru e major - daca da se logheaza, daca nu il trimitem acas
3. daca e major - incercam sa extragem din cnp anul nasterii si sa verificam daca corespunde cu anul nasterii pe care l-a introdus
4. daca nu e ok - user nu e lasat sa intre pe site
5. daca da extragem pe baza prime cifre din CNP daca user e barbat sau femeie
6. daca e femeie se afiseaza un string de farfumuri si genti
7. daca e barbat un string cu ceasuri de mana
8. daca nu e barbat/ nici femeie - afiseaza ca esti un robot
"""

nume = input('Nume')
data_nasterii = input('Data nasterii in formatul dd/mm/yyyy ')
from datetime import datetime
varsta = datetime.strptime(data_nasterii, '%d/%m/%Y')
anul = varsta.year
if 2023 - anul > 17:
    print('esti major')
    cnp = input('CNP')
    if len(cnp) != 13:
        print('CNP-ul trebuie sa aiba 13 cifre')
        assert len(cnp) == 13
    an_din_cnp = int(str(cnp[1]) + str(cnp[2]))
    if an_din_cnp <= 5 or an_din_cnp >50:
        print('an nasterii = an din CNP')
        sex = int(cnp[0])
        if sex == 1:
            print('Acces la ceasuri de mana')
        elif sex == 2:
            print('Acces la genti')
        else:
            print('esti un robot')
    elif an_din_cnp > 5 and an_din_cnp < 49:
        print('nu ai varsta majoratului')
else:
    print('trebuie sa mai cresti')






