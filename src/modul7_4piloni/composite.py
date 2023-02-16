
print('COMPOZITIE') # todo Agreg si Comp sunt auxiliarii celor 4 piloni, pt a crea un cod mai obiectual
# - todo Compozitie - prin compoz construim un obiect,
#    care in componenta lui are un alt obiect obligatoriu
#    - o folosim cand suntem convisi ca un element e construit pe baza altui element,
#       si acela n-o sa se modifice niciodata. Ex: class Masina si class Roti, stim
#       ca intodeauna masina are nevoie de roti, altfel nu-i masina
#    - Cand vrei sa lasi libertat din exteri si sa controlez m multe optiuni pt un
#      angajat - folosesti AGREGARE,
#     - Cand e ceva fix pt un angajat - folos COMPOZITIA
class Salary:
    def __init__(self, payment):
        self._payment = payment

    def get_total(self):
        return 12 * self._payment // 5

    def get_meal_tikets(self):
        return 300


# s = Salary(1000)
# print(s.get_total())

class Employee:
    def __init__(self, payment, bonus):
        self._payment = Salary(payment)
        self._bonus = bonus

    def get_annual_revenue(self):
        return self._bonus + self._payment.get_total() + \
            self._payment.get_meal_tikets()


income_ion = Employee(50000, 5000)     #income - sursa de venit
print(f'{income_ion.get_annual_revenue()} Euro')
