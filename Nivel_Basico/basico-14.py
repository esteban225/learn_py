# 14. Convertir una cantidad de días en años, meses y días.
import math
days = int(input("Ingrese la cantidad de dias."))

numYears = days / 365
numMounts = days / 30
numDay = days

print(f"años: {math.ceil(numYears)}, meses:{math.ceil(numMounts)}, dias:{numDay}")