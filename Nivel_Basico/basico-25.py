# 25. Leer una edad y mostrar si es mayor de edad.

def edad(num):
    if num > 18:
        return("Es mayor de edad.")
    else: 
        return("Es menor de edad.")

num = int(input("Ingrese la edad: "))

print(f"{edad(num)}")