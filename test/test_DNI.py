import pytest
from src.dni import Dni


def test_set_get_dni():
    dni = Dni("12345678Z")
    dni.set_dni("87654321X")
    assert dni.get_dni() == "87654321X"

def test_set_get_numero_sano():
    dni = Dni("12345678Z")
    dni.set_numero_sano(True)
    assert dni.get_numero_sano() is True

def test_set_get_letra_sana():
    dni = Dni("12345678Z")
    dni.set_letra_sana(True)
    assert dni.get_letra_sana() is True
