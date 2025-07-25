# 22. Calcular el perímetro de un círculo.

import math
def perimeter(diameter):
    result = math.pi * diameter
    return result

diameter = int(input("ingrese el diametro del circulo: \n"))
print(f"El perimetro del triangulo es de: {perimeter(diameter)}")

