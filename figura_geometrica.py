"""Módulo para el cálculo de áreas de figuras geométricas.

Contiene clases abstractas e implementaciones concretas para rectángulos,
triángulos y círculos, siguiendo el principio de polimorfismo.
"""

from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    """Clase abstracta que define la interfaz para calcular áreas de figuras."""

    @abstractmethod
    def calcular_area(self):
        """Calcula el área de la figura geométrica.

        Returns:
            float: El área calculada de la figura.
        """

    @abstractmethod
    def tipo_figura(self):
        """Devuelve el tipo de figura geométrica.

        Returns:
            str: Tipo de figura.
        """


class Rectangulo(FiguraGeometrica):
    """Clase que representa un rectángulo y calcula su área."""

    def __init__(self, base, altura):
        """Inicializa el rectángulo con base y altura.

        Args:
            base (float): Base del rectángulo.
            altura (float): Altura del rectángulo.
        """
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del rectángulo.

        Returns:
            float: Área del rectángulo (base * altura).
        """
        return self.base * self.altura

    def tipo_figura(self):
        """Devuelve el tipo de figura geométrica.

        Returns:
            str: Tipo de figura.
        """
        return "Rectángulo"


class Triangulo(FiguraGeometrica):
    """Clase que representa un triángulo y calcula su área."""

    def __init__(self, base, altura):
        """Inicializa el triángulo con base y altura.

        Args:
            base (float): Base del triángulo.
            altura (float): Altura del triángulo.
        """
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del triángulo.

        Returns:
            float: Área del triángulo (base * altura / 2).
        """
        return (self.base * self.altura) / 2

    def tipo_figura(self):
        """Devuelve el tipo de figura geométrica.

        Returns:
            str: Tipo de figura.
        """
        return "Triángulo"


class Circulo(FiguraGeometrica):
    """Clase que representa un círculo y calcula su área."""

    def __init__(self, radio):
        """Inicializa el círculo con radio.

        Args:
            radio (float): Radio del círculo.
        """
        self.pi = 3.14159
        self.radio = radio

    def calcular_area(self):
        """Calcula el área del círculo.

        Returns:
            float: Área del círculo (π * radio²).
        """
        return self.pi * (self.radio ** 2)

    def tipo_figura(self):
        """Devuelve el tipo de figura geométrica.

        Returns:
            str: Tipo de figura.
        """
        return "Círculo"


# Constantes globales
BASE_RECTANGULO = 10
ALTURA_RECTANGULO = 5
BASE_TRIANGULO = 7
ALTURA_TRIANGULO = 4
RADIO_CIRCULO = 3


def main():
    """Función principal que ejecuta el cálculo de áreas."""
    rectangulo = Rectangulo(BASE_RECTANGULO, ALTURA_RECTANGULO)
    triangulo = Triangulo(BASE_TRIANGULO, ALTURA_TRIANGULO)
    circulo = Circulo(RADIO_CIRCULO)

    print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
    print(f"El área del triángulo es: {triangulo.calcular_area()}")
    print(f"El área del círculo es: {circulo.calcular_area()}")


if __name__ == "__main__":
    main()
