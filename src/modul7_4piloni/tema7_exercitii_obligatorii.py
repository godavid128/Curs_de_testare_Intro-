print('EXERCITII OBLIGATORII')
'''
ABSTRACTION
- Clasa abstractă FormaGeometrica.  - Conține un field PI=3.14
- Conține o metodă abstractă aria (opțional)
- Conține o metodă a clasei descrie() 
- aceasta print ‘Cel mai probabil am colturi’
INHERITANCE
- Clasa Pătrat - moștenește FormaGeometrica.
- constructor pentru latură
ENCAPSULATION
- latura este propriet privată. 
- Implementeaza getter, setter, deleter pentru latură
- Impleme metoda cerută de interfață (opțional, doar dacă ai ales să impleme metod abst aria)
Clasa Cerc - moștenește FormaGeometrica
- constructor pentru rază
- raza este proprietate privată
- Implementează getter, setter, deleter pentru rază
- Implementează metoda cerută de interfață: în calcul folosește field PI
mostenit din clasa părinte (opțional, doar dacă ai ales să implemen metoda abst aria)
POLYMORPHISM
- Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
- Creează un obiect de tip Patrat și joacă-te cu metodele lui
- Creează un obiect de tip Cerc și joacă-te cu metodele lui

'''

from abc import ABC, abstractmethod, abstractproperty
from math import pi


# Abstraction - se folos prin apelarea 'ABC'
class FormaGeometrica(ABC):
    # atribute, field
    pi = 'pi'

    @abstractmethod
    def aria(self):
        raise NotImplemented

    def descriere_form_geometrica(self):
        print('Patratul, cel mai probabil are colturi')


# INHERITANCE - copil mosteneste de la parinte ce are el
class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    # Encapsulation - avem 3 metode: privat, protected, public
    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Getter: Latura este {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura):
        print(f'Setter: Noua latura este {latura}')
        self.__latura = latura

    @latura.deleter
    def latura(self):
        print(f'Deleter: Am sters latura')
        self.__latura = None

    def aria(self):
        print(f'Aria patratului este:', self.__latura * 2)


class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Getter: Raza cercului este: {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza):
        print(f'Setter: Raza cercului este: {raza}')
        self.__raza = raza

    @raza.deleter
    def raza(self):
        print(f'Deleter: Am sters raza')
        self.__raza = pi * 10 ** 2

    def aria(self):
        print(f'Aria cercului este:', pi * self.__raza ** 2)

    # Polymorphism - cand exista 2 functii cu acelasi nume, dar au comport diferit
    def descriere_form_geometrica(self):
        print('Eu, cercul, n-am colturi')


# creem obiecte si ne jucam cu ele:
print('----------------------------------PATRAT')
patrat = Patrat(10)
patrat.descriere_form_geometrica()
patrat.aria()
patrat.latura = '20'
patrat.latura
del patrat.latura
patrat.latura

print('------------------------------------CERC')
cerc = Cerc(12)
cerc.descriere_form_geometrica()
cerc.aria()
cerc.raza = '20'
cerc.raza
del cerc.raza
cerc.raza