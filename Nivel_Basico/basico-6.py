# 6. Sumar todos los números pares entre 1 y N.
num = int(input("Ingrese el numero: "))
result = 0
for i in range(1, num + 1 ):
    if i % 2 == 0:
        result += i
        
print(f"La suma de los numeros pares es de: {result}")

