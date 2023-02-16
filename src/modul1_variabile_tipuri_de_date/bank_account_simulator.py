'''
1. Declaram expected results - user, password, sold
2. Introducem un username
3. Verificam corectitudinea userului
4. introducem p parola valida
5. verificam corectitudinea parolei
6. if all ok = simulat press enter to login
7. afisam mesaj string in care afisam 'expected sold'
8. intampinam userul cu un ms: cat ches doriti sa transferati
9. afisam in consola daca tranzactia are loc cat sold ii ramane
10. extragem lungimea parolei
11.If lungim parolel <5 codul va da 'error' (assert)
12. Afisam in consola username-ul, dar parola sa fie inlocuita cu stelute in loc de caractere propriuzise
'''
# 1 declaram user, password, sold
user: str = 'david'
password: str = 'abc123'
sold: int= 5000


# 2 introd username => imput (introduce de la tastatura)
actual_user = input('Introducem username: ').lower() # lower = litere mici
print(actual_user)
# 3 verificam corectitudinea user prin TODO'assert'= afirma
assert user == actual_user

# 4 introd parola
actual_password = input('Introducem parola: ').strip()  # strip scoate spatiile din ce intr la tastatura
print(actual_password)                                   # lstrip elimin spatiu din left, rstrip - elim spat din dreapta
# 5 verific corectitudinea parolei
assert password == actual_password
print (f'Parola introdusa este ok')
# 12  parola sa fie inlocuita cu stelute in loc de caractere
print('******')
print('-------------------------------------')

# 6 if all ok - simularea 'press enter to login'
input('Press Enter to login')
# 7 afisam mes string: TODO'expected sold'= soldul curent
print(f'Soldul este: {sold}')

# 8 intimpinam user (client) cu urm ms: 'ce suma doresti sa extragi'?
cash_suma = int(input('Ce suma doresti sa retragi? '))

# 9 afisam in consola daca tranzictia are loc si cat sold ii ramane
assert sold - cash_suma >= 0
sold = sold - cash_suma
# dam update la sold
print(f'Noul sold este: {sold}')

# 10 extragem lungimea parolei
print(len(password))
len_password = len(password)
# 11 daca lungimea parolei < 5 codul va da 'error' (assert)
assert len_password >= 5
print (f'Parola introdusa este ok')


# TODO chetul de parolade la 11 sal mutam sus sa il mutam la inceput
# daca am introdus un spatiu nu mai e corecr = sa eliminam orice spatiu fie ca e la inceput
# sa verificam c a ea contin macar o litere si un caracrett special (parola
# 12 tema

a, b, c, d = '!', '@', '#', '$'
assert a in password or b in password or c in password or d in password


