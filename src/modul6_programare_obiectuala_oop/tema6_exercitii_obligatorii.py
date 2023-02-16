from math import pi

print('CLASS CERC')


# 1.Clasa Cerc. Atribute: raza, culoare. Constructor pentru ambele atribute
# Metode: ● descrie_cerc() - va PRINTA culoarea și raza. ● aria() - va RETURNA aria
# ● diametru(). ● circumferinta()
class Cerc:
    # atribute/ fields
    def __init__(self, raza, culoare):
        self._raza = raza
        self._culoare = culoare

    def descriere_cerc(self):
        print(f'Raza cercului este: {self._raza}')
        print(f'Culoarea cercului este: {self._culoare}')

    def aria_cerc(self):
        return pi * self._raza ** 2

    def diametru_cerc(self):
        return 2 * self._raza

    def circumferinta_cerc(self):
        return 2 * self._raza * pi


# Creeam obiectul
calcul_cercului = Cerc(10, 'Verde')
calcul_cercului1 = Cerc(20, 'Mov')

# zona de apelare a metodelor
calcul_cercului.descriere_cerc()
print(calcul_cercului.aria_cerc())
print(calcul_cercului.diametru_cerc())
print(calcul_cercului.circumferinta_cerc())
calcul_cercului1.descriere_cerc()
print(calcul_cercului1.aria_cerc())
print(calcul_cercului1.diametru_cerc())
print(calcul_cercului1.circumferinta_cerc())


# 2. Clasa Dreptunghi. Atribute: lungime, latime, culoare. Constructor pentru toate atributele
#   Metode: ● descrie() ● aria() ● perimetrul() ● schimbă_culoarea(noua_culoare)
#   - această metodă nu return nimic. Ea va lua ca și parametr o nouă culoare și va suprascrie
#   atributul 'self.culoare.' Puteti verifica schimb culor prin apel metodei descrie().
print(end='\n')
print('CLASS DREPTUNGHI')


class Dreptunghi:

    def __init__(self, lungime, latime, culoare):
        self._lungime = lungime
        self._latime = latime
        self._culoare = culoare

    def descriere_dreptunghi(self):
        print(f'Lungimea dreptunghiului este: {self._lungime}')
        print(f'Latime dreptunghiului este: {self._latime}')
        print(f'Culoare dreptunghiului este: {self._culoare}')

    def aria_dreptunghi(self):
        return self._lungime * self._latime

    def perimetrul_dreptunghi(self):
        return 2 * (self._lungime + self._latime)

    def schimba_culoarea(self, noua_culoare):
        print(f'Dreptunghiul si-a schimbat din culoarea {self._culoare} in {noua_culoare}')


# creem obiectul
calcul_dreptunghi = Dreptunghi(10, 4, 'Galben')
calcul_dreptunghi1 = Dreptunghi(20, 6, 'Albastru')
# zona de apelare a metodei
calcul_dreptunghi.descriere_dreptunghi()
print(calcul_dreptunghi.aria_dreptunghi())
print(calcul_dreptunghi.perimetrul_dreptunghi())
calcul_dreptunghi.schimba_culoarea('Alb')
calcul_dreptunghi1.descriere_dreptunghi()
print(calcul_dreptunghi1.aria_dreptunghi())
print(calcul_dreptunghi1.perimetrul_dreptunghi())
calcul_dreptunghi1.schimba_culoarea('Argintiu')

# 3. Clasa Angajat. Atribute: nume, prenume, salariu. Constructor pt toate atributele
#   Metode: ● descrie(). ● nume_complet(). ● salariu_lunar(). ● salariu_anual(). ● marire_salariu(procent)
print(end='\n')
print('CLASS ANGAJAT')


class Angajat:
    def __init__(self, nume, prenume, salariu):
        self._nume = nume
        self._prenume = prenume
        self._salariu = salariu

    def descriere_angajat(self, ):
        print(f'Nume: {self._nume}, Prenume: {self._prenume}, Salariu {self._salariu} RON')
        print(f'Numele complet este {self._nume} {self._prenume}')

    def salariu_anual(self):
        salariu_anual = self._salariu * 12
        print('Salariul anual este:', end=' ')
        return salariu_anual

    def marire_salariu(self):  # marime salariu in functie de ani lucrati
        procent_1_an = (self._salariu * 5 / 50) + self._salariu
        print('Salariul creste in fiecare an cu 5 % si este = ', end=' ')
        return procent_1_an


date_angajat = Angajat('Cretu', 'Liviu', 5000)
date_angajat1 = Angajat('Cretu', 'Silvea', 1000)

date_angajat.descriere_angajat()
print(date_angajat.salariu_anual())
print(date_angajat.marire_salariu())

date_angajat1.descriere_angajat()
print(date_angajat1.salariu_anual())
print(date_angajat1.marire_salariu())

# 4. Clasa Cont. Atribute: iban, titular_cont, sold. Constructor pentru toate atributele
#   Metode: ● afisare_sold() - Titularul x are în contul y suma de n lei
#   ● debitare_cont(suma). ● creditare_cont(suma)
print(end='\n')
print('CLASS CONT')


class Cont:
    def __init__(self, titular_cont, iban):
        self._titular_cont = titular_cont
        self._iban = iban
        self._sold = 0

    def afisare_sold(self):
        print(f'Titularul {self._titular_cont} are in contul {self._iban} '
              f'are suma de {self._sold} RON')

    def creditare_cont(self, suma_depusa):
        self._sold += suma_depusa
        print(f'Ati alimentat {suma_depusa}, Aveti in cont {self._sold}')
        return self._sold

    def debitare_cont(self, suma_extrasa):
        if suma_extrasa <= self._sold:
            self._sold -= suma_extrasa
            print(f'Ati extras suma de: {suma_extrasa}, Aveti in cont {self._sold}')
            return self._sold
        else:
            return 'Fonduri insuficiente'


cont_client = Cont('Grecu Adi', 'RO2345')
cont_client1 = Cont('Grecu Adriana', 'RO001')


print(cont_client.creditare_cont(3000))
print(cont_client.debitare_cont(4000))
print(cont_client.debitare_cont(3000))
cont_client.afisare_sold()
print('----------------')
print(cont_client1.creditare_cont(1000))
print(cont_client1.debitare_cont(800))
cont_client1.afisare_sold()
