# 24. Sumar los elementos de una lista ingresada por el usuario.

def sumArray(array):
    result = 0
    for num in array:
        result += num
    return result

array = []

cantNum = int(input("Ingrese la cantidad de números de la lista: \n"))

print("Ingrese los números de la lista:")

for _ in range(cantNum):
    numero = int(input()) 
    array.append(numero)

print(f"La suma de la lista de números es: {sumArray(array)}")
