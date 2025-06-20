"""Módulo que define las clases para calcular áreas de figuras geométricas."""
# pylint: disable=too-few-public-methods

import math


class Circulo:
    """Clase que representa un círculo."""

    def __init__(self, radio: float):
        if radio <= 0:
            raise ValueError("El radio debe ser un número positivo.")
        self.radio = radio

    def calcular_area(self) -> float:
        """Calcula el área del círculo."""
        return math.pi * self.radio ** 2


class Triangulo:
    """Clase que representa un triángulo."""

    def __init__(self, base: float, altura: float):
        if base <= 0 or altura <= 0:
            raise ValueError("Base y altura deben ser números positivos.")
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        """Calcula el área del triángulo."""
        return (self.base * self.altura) / 2


class Rectangulo:
    """Clase que representa un rectángulo."""

    def __init__(self, base: float, altura: float):
        if base <= 0 or altura <= 0:
            raise ValueError("Base y altura deben ser números positivos.")
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        """Calcula el área del rectángulo."""
        return self.base * self.altura


class Cuadrado:
    """Clase que representa un cuadrado."""

    def __init__(self, lado: float):
        if lado <= 0:
            raise ValueError("El lado debe ser un número positivo.")
        self.lado = lado

    def calcular_area(self) -> float:
        """Calcula el área del cuadrado."""
        return self.lado ** 2
