# tema
# clasa Angajat
# nume, prenume, salariu, vechima, functie
# constructor: nume, prenume, salariu, vechima, functie
# metode
# descriere
# marime salariu in functie de vechime
# actualizare vechime (ia parametrul = noua vechime)
        # self.vechime = noua_vechime
# daca are vechime sub 5 ani, marim cu 300, peste 5 ani, 500
#descriere

class Angajat:
    # constructor
    def __init__(self, nume, prenume, functie, salariu, vechime):
        self.nume = nume
        self.prenume = prenume
        self.functie = functie
        self.salariu = salariu
        self.vechime = vechime

    # metode
    def descrierea(self):
        print(f'Nume {self.nume}')
        print(f'Prenume {self.prenume}')
        print(f'Functia {self.functie}')
        print(f'Salariu {self.salariu} euro')
        print(f'Vechime {self.vechime}')
        print('--------------------------------------')

    def marireSalariu(self, vechime):
        # marire de salariu in functie de vechime
        if vechime <= 5:
            print(vechime + 300)
        elif vechime >= 5:
            print(vechime + 500)
        else:
            print('Vechime incorecta')

    def actualizare_vechime(self, noua_vechime):
        if self.vechime:
            return noua_vechime



