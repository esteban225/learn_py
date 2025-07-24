# 13. Intercambiar el valor de dos variables.
print("Ingresa los numeros: \n")

name = []
i = 0
vc = ""

while i < 2:
    word = input("Ingrese el nombre y el apellido:")
    name.append(word)
    i += 1
    
a = name[0]
b = name[1]

print (f"valores antes del intercambio a = {a}, b = {b}.")
vc = a 
a = b
b = vc
print (f"valores despues del intercambio a = {a}, b = {b}.")
