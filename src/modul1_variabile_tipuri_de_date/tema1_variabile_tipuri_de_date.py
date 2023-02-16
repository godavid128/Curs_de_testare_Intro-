# 1. Variabile - este o cutie din memorie, unde stocam date
# 2. Declarare si initializare
# import rock as rock

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

# 3 Utilizare functiei 'type'
print(type(fructe))
print(type(numar_fructe))
print(type(pret_fructe))
print(type(pret_legume))
print(type(fructele_sunt_coapte))

# 4. Rotunjeste 'float'-ul folosind functia round() si suprascrie aceasta variabila
pret_legume = 150.50
print(f'{pret_legume}')
pret_legume = round(pret_legume)
print(pret_legume)

# 5. Foloseste print() si printeaza in consola 4 propozitii folosind cele 4 variabile
print(f'Am fost la cumparaturi si am cumparat fructe {fructe} si {legume}')
print(f'In numar de: {numar_fructe} si {numar_legume}')
print(f'La pret de: {pret_fructe} + {pret_legume}')
print(f'care erau foarte coapte! {fructele_sunt_coapte}')

# 6. Citeste de la tastatura: num, prenumele => afis: 'Numele complect are X caractere
numele: str = 'gorodetchi'
prenumele: str = 'david'
numele = input('introdu numele: ')
print(numele)
prenumele = input('introdu prenumele: ')
print(prenumele)
print(f'Numele complet are {len(numele)} caractere')

# 7. Citeste de la tastatura: lungimea, latimea; afiseaza: 'aria dreptunghiului este x'
a= int(input("Lungimea este egala cu:"))
b = int(input('Latimea este egala cu:'))
print(f'Aria dreptunghiului este egala cu: {a * b}')

# 8. si 9 Având stringul: 'Coral is either the stupidest animal or the smartest rock' - afiseaza de cate ori apare cuv 'the'
coral = 'Coral is either the stupidest animal or the smartest rock'
coral = coral.count('the')
print(f'Cuvantul "the" apare de {coral} ori')

# 10. folosind 'assert' afiseaza daca stringul ex 8 contine doar numere
coral = 'Coral is either the stupidest animal or the smartest rock'
print(coral.isnumeric())
assert coral.isnumeric() == False
coral1 = '3333344'
assert coral1.isnumeric() ==True
print(coral1.isnumeric())
