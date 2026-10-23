import math

import pytest

from calculos import area_circulo, potencia, suma_dos_numeros


def test_suma_dos_numeros():
    assert suma_dos_numeros(2, 3) == 5


def test_potencia():
    assert potencia(2, 10) == 1024


def test_area_circulo():
    assert area_circulo(1) == pytest.approx(math.pi)


def test_area_circulo_radio_negativo():
    with pytest.raises(ValueError):
        area_circulo(-1)
