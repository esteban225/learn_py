# 28. Calcular el promedio de notas de un estudiante.
array = []

numNot = int(input("Ingrese el numero de notas que tiene el estudiante: \n"))
print("Ingrese las notas")

result = 0
for i in range(numNot):
    num = float(input())
    array.append(num)
    result += array[i]

prom = result // 2

print(f"El promedio del estudiante es de: {float(prom)}")

