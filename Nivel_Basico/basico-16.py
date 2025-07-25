# 16. Mostrar el doble de un número si es menor que 10.

num = int(input("Ingrese el numero: \n"))

if num < 10:
    result = num * 2
    print(f"El doble es: {result}")
else:
    print("El numero tiene que ser menor a 10")
