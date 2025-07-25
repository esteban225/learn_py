# 23. Leer un número decimal y mostrar solo la parte entera.
import math

def whole(decimal):
    result = math.trunc(decimal)
    return result

decimal = float(input("ingrese un número decimal: \n"))

print(f"La parte entera del numero decimal {decimal} es: {whole(decimal)}")