from datetime import date


# TODO EXERCITII OPTIONALE
# 1. Clasa Factura. Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile
#   vor avea aceeași serie), număr, nume_produs, cantitate, pret_buc
#   Constructor: toate atributele, fara serie
#   Metode: ● schimbă_cantitatea(cantitate) ● schimbă_prețul(pret). ● schimbă_nume_produs(nume)
#   ● generează_factura() - va printa tabelar dacă reușiți.
#           Factura seria x numar y
#           Data: generați automat data de azi
#           Produs | cantitate | preț bucată | Total
#           Telefon | 7 | 700 | 49000
#           Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/
class Factura:
    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self._numar = numar
        self._nume_produs = nume_produs
        self._cantitate = cantitate
        self._pret_buc = pret_buc
        self._seria = 20341
        self._total = 0

    def schimba_produs(self, nume):
        self._numar = numar
        self._nume_produs = nume

    def schimba_cantitatea(self, cantitate):
        self._cantitate += cantitate
        return self._cantitate

    def schimba_pretul(self, pret):
        self._pret_buc = pret
        return self._pret_buc

    def genereaza_factura(self):
        print(f'Factura cu seria {self._seria}, numar {self._numar}', end='\n')
        print(f'data {date.today()}', end='\n')
        print(f'Produs  | Cantita | Pret_buc | Total')
        print(f'{self._nume_produs}, | {self._cantitate},     | {self._pret_buc},       | '
              f'{self._pret_buc * self._cantitate} ')


# Pentru a afla pret total, am incercat sa fac o metoda in care sa apelez: 2 metode - n-am reusit
# Apoi am reusit sa fac aceasta operatie direct in printer => a functionat :)

client1 = Factura(23, 'Caiet ', 20, 3)
client1.genereaza_factura()
print('-----------------------------------------')
client2 = Factura(30, 'Stilou', 210, 10)
client2.genereaza_factura()

# 2.Clasa Masina. Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
#   culori_dispo (set), inmatri (bool)
# Culoare = gri - toate mașinile cand ies din fabrica sunt gri
# Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
# Culori disponibile = alegeți voi 5-7 culori
# Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
# Inmatriculata = False
# Constructor: model, viteza_maxima
# Metode:
# ● descrie() - se vor printa toate atributele, în afară de culori_disponibile
# ● înmatriculare() - va schimba atributul înmatriculată în True
# ● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
# culoare e în opțiunea de culori disponibile, altfel afișați o eroare
# ● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e negativă-eroare,
# daca viteza e mai mare decat viteza_max - masina va accelera până la viteza maximă
# ● franeaza() - mașina se va opri și va avea viteza 0
print(end='\n')
print('CLASS MASINA')


class Masina:
    # TODO Cand putem pune atributele in afara metodelor, chiar sub class Masina?
    def __init__(self, model, viteza_maxima):
        self._marca = 'Scoda'
        self._model = model
        self._viteza_maxima = viteza_maxima
        self._viteza_actu = 0
        self._culoarea = 'Gri'
        self._culori_disponibile = {'verde', 'galben', 'rosu', 'negru', 'alba', 'mov'}
        self._inmatriculata = False

    def metode(self, ):
        print(f'Marca si modelul este {self._marca} {self._model}, are viteza actu = {self._viteza_actu}'
              f' si viteza max = {self._viteza_maxima}.', end='\n'
                                                              f'Are culoarea {self._culoarea} si imatricularea este = {self._inmatriculata}')
        print(end='\n')

    def inmatriculare(self, ):
        return 'Masina este imatriculata', True

    def vopsirea(self, culoarea_cu_lowercase):
        #                                       TODO cum setam 'lower case' pentru culori?
        if culoarea_cu_lowercase in self._culori_disponibile:
            return f'Culoare vopsita e:', culoarea_cu_lowercase
        else:
            return 'Culoare aleasa nu exista'

    def accelerare(self, viteza):
        if viteza > self._viteza_maxima:
            return self._viteza_maxima
        elif viteza <= 200 and viteza >= 0:
            return viteza
        else:
            return f'Eroare, viteza {viteza} e prea mica'

    def franare(self):
        return f'Masina s-a oprit la viteza:', self._viteza_actu


voiture1 = Masina('Fabia', 200)
voiture1.metode()
print(voiture1.inmatriculare())
print(voiture1.vopsirea('albastra'))
print(voiture1.vopsirea('mov'))
print(voiture1.accelerare(-20))
print(voiture1.accelerare(300))
print(voiture1.accelerare(130))
print(voiture1.franare())
print('-----------------------')
voiture2 = Masina('Superb', 430)
voiture2.metode()
print(voiture2.inmatriculare())
print(voiture2.vopsirea('neagra'))
print(voiture2.vopsirea('alba'))
print(voiture2.accelerare(-2))
print(voiture2.accelerare(500))
print(voiture2.accelerare(90))
print(voiture2.franare())

# 3. Clasa TodoList. Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
# Metode:    ● adauga_task(nume, descriere) - se va adauga in dict
#            ● finalizează_task(nume) - se va sterge din dict.
#            ● afișează_todo_list() - doar cheile
#   ● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
# print detal suplim. ○ Dacă taskul nu e în todo list, întreb utiliz dacă vrea să-l adauge.
# ○ Dacă acesta răspunde nu - la revedere
# ○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în dict
print(end='\n')
print('CLASS TODOLIST')
# todo in curs.........................................

class TodoList:
    dict = {}

    def adauga_task(self, nume, descriere):
        self.dict[nume] = descriere
        return self.dict
    def finalizeaza_task(self, nume): # stergem un dict
        if nume in self.dict:
            del self.dict[nume]
        else:
            print('Task-ul nu exista')
    def afiseaza_todo_list(self):       # afisam doar cheile
        return self.dict.keys()
    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task in self.dict.keys():
            return f'taskul {nume_task} deja exista'
        if nume_task not in self.dict.keys():
            raspunde = input(f'Taskul {nume_task}, nu exista in lista.Vrei sa-l adaug? da /nu: ')
            if raspunde == 'da':
                detalii = input(f'spunem detalii despre {nume_task}: ')
                self.dict[nume_task] = detalii
                return self.dict
            else:
                return 'La revedere'

lista1 = TodoList()
print(lista1.adauga_task('ion', '10 ani'))
print(lista1.adauga_task('maria', '12 ani'))
lista1.finalizeaza_task('vasile')
lista1.finalizeaza_task('ion')
print(lista1.adauga_task('casa', 34))
print(lista1.afiseaza_todo_list())
print(lista1.afiseaza_detalii_suplimentare('maria'))
print(lista1.afiseaza_detalii_suplimentare('ion'))
print(lista1.afiseaza_detalii_suplimentare('gradina'))