# 11. Determinar si un número es múltiplo de otro.
print("ingrese los numeros:")

num = []
for count in range(2):
    value = int(input(f"{count + 1}:"))
    num.append(value)

a = num[0]
b = num[1]

if a == 0 and b == 0:
    print("numeros no validos")
else:
    if b == 0: 
        print("No se puede dividor ente cero")
    elif a % b == 0:
        print(f"{a} es multiplo de: {b} ")
    else:
        print(f"{a} no es multiplo de: {b} ")
    