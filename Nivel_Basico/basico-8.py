# 8. Imprimir la tabla de multiplicar de un número.

num = int(input("Ingrese el numero: "))

for i in range(1, 11):
    print(f"{i} x {num} = { i * num}")
