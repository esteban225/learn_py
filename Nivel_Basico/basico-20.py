# 20. Verificar si un número tiene tres dígitos. 

def cantidad(num):
    count = 0
    while num > 0:
        count += 1
        num = num // 10
    return count

n = int(input("ingrese el numero: \n "))


if cantidad(n) == 3:
    print(f"El número {n} tiene {cantidad(n)} digitos requeridos.")
else:
    print(f"El número {n} tiene {cantidad(n)} digitos")
