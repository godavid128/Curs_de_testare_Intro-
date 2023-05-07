# facem o functie pt unit testing
import pytest as pytest


class MiniCalculator:
    # metod statica e o metoda din interi class care nu are nevoie de self - nu ai nevoi de nimic din constructor
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def dif(a, b):
        return a - b

    @staticmethod
    def multiplication(a, b):
        return a * b

    @staticmethod
    def impartire(a, b):
        return a / b


# facem o functie pt mini calculator
@pytest.fixture
def mini_calc():
    return MiniCalculator()  # Ex: return webdriver.chrome. Si atunci in celelalte functii de test o sa ai un parametru
    # numit 'mydriver'. si efectiv: mydriver.get => va deschide site; mydriver.find_element...


def test_add():
    assert MiniCalculator.add(3, 5) == 8


def test_dif():
    assert MiniCalculator.dif(3, 5) == -2


def test_multiplication():
    assert MiniCalculator.multiplication(3, 5) == 15


def test_impartire():
    assert MiniCalculator.impartire(15, 5) == 3


def test_add_negative_input(mini_calc):
    assert mini_calc.add(-3, -5) != 8


@pytest.mark.parametrize('a, b, expected_result', [
    (1, 2, 3),
    (3, 5, 8),
    (5, 7, 12)
])
def test_add_with_multiple_inputs(mini_calc, a, b, expected_result):
    assert mini_calc.add(a, b) == expected_result
# fixture - este o functie care e fol pt a initial o alta functie = un decorator. Ex.:Putem avea o functie care
# creeaza un mini calculator

# pt a rula 2 teste in paralel: instal o librarie - EX: una din librarii e =>
# 'pip install pytest-xdist' si ii trasm cu '-n' cate teste dorim

# De ce are sens sa testam prin 'API', daca putem oricum prin client?
# - ca sa testezi mai rapid.
# - prindem bug-uri mai rapid prin back-und.
# - oferi o calitate mai buna la produs
# + insa nu-i suficient, tb si o validara la nivel de client

# todo pt selenium - faceti o functie de tip fixture = care face instant la chrome driver si aia o trasmit la orice alta functie
#  sa aplicam ideea de fixture cu pytest pt un ex din selenium
