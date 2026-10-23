"""Funciones de ejemplo para la demostración de GitHub Actions."""
import math


def suma_dos_numeros(a, b):
    """Devuelve la suma de dos números."""
    return a + b


def potencia(base, exponente):
    """Devuelve base elevada al exponente."""
    return base ** exponente


def area_circulo(radio):
    """Devuelve el área de un círculo; el radio no puede ser negativo."""
    if radio < 0:
        raise ValueError("El radio no puede ser negativo")
    return math.pi * radio ** 2
