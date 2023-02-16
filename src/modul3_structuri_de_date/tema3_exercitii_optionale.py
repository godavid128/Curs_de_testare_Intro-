'''
1. Ne imaginam o echipa de fotbal in timpul meciului. Sunt permise maxim 3 schimbari.
- Declara o lista cu 5 jucatori: lista_jucatori_teren
- Declara o lista cu 5 jucatori de rezerva: lista_jucatori_rezerva
- Declara o lista goala cu jucatori scosi din teren: lista_jucatori_scosi
- Schimbari_efectuate = joaca-te cu valori diferite ca sa vezi cum trec datele prin cod
- SCHIMBARI_MAX va fi o constanta cu valoarea 3
Daca Jucatorul x e in teren si mai avem schimbari la dispozitie atunci:
- Efectuam schimbarea daca jucatorul e in lista de rezerve si nu exista in jucatorii de pe
teren
- Stergem jucatorul scos din lista de teren si il adaugam in lista de jucatori scosi
- Adaugam jucatorul intrat in lista de jucatori de pe teren si il scoatem din lista de jucatori
de rezerva
- Afisam pe ecran: a intrat x, a iesit y. Mai aveti z schimbari (inlocuiti x, y si z cu numele
variabilelor voastre)
Daca jucatorul pe care vrem sa il schimbam nu e in teren:
- Afisati ‘nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
Altfel, afisati ecran: ‘mai aveti z schimbari’
Google search hint: “how to check if item is in list python'
'''
lista_jucatori_teren = ['denis', 'mirel', 'catalin', 'david', 'ilie']
lista_jucatori_rezerva = ['ana', 'asa', 'miriam', 'ada', 'alina']
lista_jucatori_scosi = []
schimbari_efectuate = -3
SCHIMBARI_MAX = 3
if 'denis' in lista_jucatori_teren and SCHIMBARI_MAX:
    print('denis este in lista')
    schimbarea1 = lista_jucatori_teren.remove('denis')
    schimbarea1 = lista_jucatori_scosi.append('denis')
    lista_jucatori_rezerva.remove('ana')
    lista_jucatori_teren.append('ana')
    print(f'A iesit denis, a intrat ana, mai aveti 2 schimbari')
    schimbari_efectuate += 1
    if 'mirel' in lista_jucatori_teren and SCHIMBARI_MAX:
        print('mirel este in lista')
        schimbarea1 = lista_jucatori_teren.remove('mirel')
        schimbarea1 = lista_jucatori_scosi.append('mirel')
        lista_jucatori_rezerva.remove('miriam')
        lista_jucatori_teren.append('miriam')
        print(f'A iesit mirel, a intrat miriam, mai aveti o schimbare')
        print(f'lista teren: {lista_jucatori_teren}, lista rezerva: {lista_jucatori_rezerva}')
        schimbari_efectuate += 1
        if 'catalin' in lista_jucatori_teren and SCHIMBARI_MAX > 0:
            print('catalin este in lista')
            schimbarea1 = lista_jucatori_teren.remove('catalin')
            schimbarea1 = lista_jucatori_scosi.append('catalin')
            lista_jucatori_rezerva.remove('ada')
            lista_jucatori_teren.append('ada')
            print(f'A iesit catalin, a intrat ada')
            print(f'lista teren: {lista_jucatori_teren}, lista rezerva: {lista_jucatori_rezerva}')
            schimbari_efectuate += 0
            if schimbari_efectuate > 0:
                print('mai aveti o sansa sa schimbati jucatori')
            else:
                print('scrimbarile sau incheiat')