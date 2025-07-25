# 30. Mostrar los primeros N números naturales al revés.

n = int(input("Ingrese la cantidad de números naturales: "))

numeros = list(range(1, n + 1))  
numeros.reverse()               

print("Los primeros", n, "números naturales al revés son:")
for numero in numeros:
    print(numero)