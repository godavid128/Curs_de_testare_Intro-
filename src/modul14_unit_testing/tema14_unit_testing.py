import pytest as pytest

class Dreptunghi:
    @staticmethod
    def aria_dreptunghi(lungime, latime):
        return lungime * latime

    @staticmethod
    def perimetru_dreptunghi(lungime, latime):
        return 2 * (lungime + latime)

    @staticmethod
    def schimbarea_culorii(culoarea):
        return culoarea == 'verde'


@pytest.fixture
def dreptunghi():
    return Dreptunghi()


def test_aria_dreptunghi():
    assert Dreptunghi.aria_dreptunghi(3, 5) == 15


def test_perimetru_dreptunghi():
    assert Dreptunghi.perimetru_dreptunghi(3, 5) == 16


def test_culoarea():
    assert Dreptunghi.schimbarea_culorii('verde')
