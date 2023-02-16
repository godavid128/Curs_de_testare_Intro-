# 1.Având lista: masini: Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for i in range(len(masini)):
    print(f'Masina mea preferata este {i}')
for masina in masini:
    print(f'Masina mea preferate e {masina}')
i = 0
while i < len(masini):
    print(masini[i])
    i +=1

# 2. Aceeasi lista: Foloseste un for else: In for - modif elem din lista astfel incat sa fie
#    cu majuscu, exceptand prim si ultim.  In else - print lista
masini_majuscule = ([])
for masina in masini:
    masini_majuscule.append(masina.upper())
else:
    masini_majuscule[0] = 'Audi'
    masini_majuscule[-1] = 'Opel'
    print(f'Masini cu majuscule sunt:', masini_majuscule)

# 3. Aceeași listă: Vine un cumpărător care dorește să cumpere un Mercedes.
#   Itereaza prin ea prin modalitatea aleasă de tine. Dacă mașina e mercedes:
#   Printează ‘am găsit mașina dorită de dvs’. Ieși din ciclu folosind un cuvânt cheie care face acest lucru
#   Altfel: Printează ‘Am găsit mașina X. Mai căutam‘
for masina_preferata in masini:
    if masina_preferata == 'Mercedes':
        print(f'am gasit dorita: {masina_preferata}')
        break
else:
    print('Mai cautam')

# 4. Aceași listă: Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
#   excepția Trabant și Lăstun. - Dacă mașina e Trabant sau Lăstun:
#   Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
#   - Printează S-ar putea să vă placă mașina x
for masina in masini:
    if masina == 'Lastun':
        continue
    if masina == 'Trabant':
        continue
    print(f'S-ar putea sa va placa: {masina}')

# 5. Modernizează parcul de mașini: ● Crează o listă goală, masini_vechi.
#   ● Itereaza prin mașini. ● Când găsesti Lăstun sau Trabant:
#       - Salvează aceste mașini în masini_vechi. - Suprascrie-le cu ‘Tesla’
#       (în lista inițială de mașini). ● Printează Modele vechi: x. ● Modele noi: x.
masini_vechi = []
for masina in masini:
    if masina == 'Lastun':
        masini.remove('Lastun')
        masini_vechi.append('Lastun')
        masini.remove('Trabant')
        masini_vechi.append('Trabant')
        print(masini_vechi)
        masini.append('Tesla')
        print(masini)

# 6. Având dict de mai jos:  Vine un client cu un buget de 15000 euro.
#   ● Prezi doar mași care se încad în acest buget.
#   ● Itereaza prin dict.items() și accesează mașina și prețul.
#   ● Print: pt un buget de sub 15000 euro puteți alege mașină xLastun ● Iterează prin listă.
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000}
for pret in pret_masini:
    print(f'Preturile la masini sunt: {pret_masini}')
    break
for i, v in enumerate(pret_masini):
    if pret_masini[v] <= 15000:
        print(f'Pentru un buget de sub 15000 puteti alege: {[v]}')

# 7. Având lista: numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#   ● Iterează prin ea.  ● Afișează de câte ori apare 3 (nu ai voie să folosești count).
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for numar3 in numere:
    if numar3 == 3:
        print(numar3)
# TODO nu reusesc sa afisaz numarul total insumat al lui 3

#  8. Aceeaai listă: ● Iterează prin ea. ● Calcu si afis suma num (nu folosi: sum).
x = 0
for totalul in numere:
    x += totalul
print(f'suma totala a numerelor este {x}')


#   9. Aceeași listă: ● Iterează prin ea. ● Afișază cel mai mare num (nu ai voie să folo max).
for numar_mare in numere:
    if numar_mare > 8:
        print(f'Numarul cel mai mare este {numar_mare}')

# 10. Aceeași listă: ● Iterează prin ea. ● Dacă num e pozitiv, înlocu cu valoarea lui negativă.
#      Ex: dacă e 3, să devină -3.   ● Afișază noua listă.
for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = -numere[i]
print(numere)
# TODO nu reusesc sa convertesc si pozitive si negative
for i in range(len(numere)):
    if numere[i] < 0:
        numere[i] = -numere[i]
print(numere)
