'''
Declara si initializeaza in limbajul de programare python cate o
variabila din fiecare din urmatoarele tipuri: string, integer, float,
boolean
'''
# string
obiect_1 = 'Casuta noastra'
obiect_2 = 'are acoperisul gri'
print(obiect_1 + ' ' + obiect_2)

# integer
numar_ferestre = 4
numar_usa = 1
print(numar_ferestre + numar_usa)

# float
valoarea = 50000
print(valoarea)

# boolean
se_vede_din_satelit = False
print(se_vede_din_satelit)
print('-------------------------')

# treceti valorile de start si finis intre paranteze
for i in range (1, 20, 3):
    print(i)

print('----------------------------------')
fructe = 'exoctice'
legume = 'naturale'
print(f'{fructe} {legume}')
numar_fructe = 1000
numar_legume = 500
print(f'{numar_fructe} {numar_legume}')
pret_fructe = 'mic'
pret_legume = 150.50
print(f'{pret_fructe} {pret_legume}')
fructele_sunt_coapte = True
print(f'{fructele_sunt_coapte}')
