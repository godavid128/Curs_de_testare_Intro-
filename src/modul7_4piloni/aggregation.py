
print('AGREGARE') #   TODO class Salary pt agregare ramane la fel ca la compozitie
# - todo Agregarea, e similar, insa nu e obliga sa ai un anumit obiect, poti sa-l creezi
#    din exterior, e similar polimorfism
#    - agregare - ex: masina ca sa functioneze, are nevoie de combustibil,
#       dar tu poti sa trasm din exterior ce tip de combusti:
#       si dupa ai class Motorin, Electric, Gaz, etc.

class Salary:
    def __init__(self, payment):
        self._payment = payment

    def get_total(self):
        return 12 * self._payment // 5

    def get_meal_tikets(self):
        return 300


class Employee:
    def __init__(self, payment, bonus):
        self._payment = payment
        self._bonus = bonus

    def get_annual_revenue(self):
        return self._bonus + self._payment.get_total() + \
            self._payment.get_meal_tikets()


s = Salary(1000)
income_ion = Employee(s, 5000)
print(f'{income_ion.get_annual_revenue()} Euro')

# TODO -cititi despre SOLID
