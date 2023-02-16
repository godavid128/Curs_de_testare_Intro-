print('EXERCITII OPTIONALE')
# 1. Citeste de la tastatura un string de dimensiune impare
numar = int(input('Introdu un numar'))
if numar % 2 ==0:
    print('nr par')
else:
    print('nr impar')
# 1a. Afiseaza caracterul din mijloc
culoare = 'Opera 1 este de culoarea albastra '
len_culoare = len(culoare)
mijloc = int (len_culoare / 2)
print(culoare[round(mijloc)])

# 2. foloseste assert, ca sa verifici daca un string este palindrom
palindrom = input('Introdu un palindrom: ')
assert palindrom == palindrom[::-1]
print(palindrom)


# 3. Folosind o singura linie de cod:
#       - citeste un string de la tastatura; - salveaza fiecare cuvant intr-o variabila;
#       - printeaza ambele variabile pt verificare
iarna, vara = input(f'iarna e: '), input('vara e: '); print(f'{iarna} \n{vara}')

# 4. Citeste un string de la tastatura; - salv I caracter intr-o variabila -
#       - capitalizeaza acest caracter peste tot, mai putin pt I si ultimul caracter
fructe = 'alabala portocala'
fructe_1caracter = fructe[0]
print(fructe_1caracter)
fructe_1 = fructe.replace('a', 'A', 5)
fructe_2 = fructe_1.replace('A', 'a', 1)
print(fructe_2)

# 5. Citeste un user de la tastatura; si o parola;
#    Afiseaza: 'parola pt user x este **** si are x caractere';
#    **** se va calcula dinamic, indiferent de dimens parolei, treb sa afiseze corect
user = input('Introdu userul tau ')
parola = input('Introdu parola ')
lungimea_parolei = len(parola) * '*'
print(f'Parola pentru userul {user} este {lungimea_parolei} si are {len(parola)} caractere')

