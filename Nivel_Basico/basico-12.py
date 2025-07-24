# 12. Calcular el promedio de 3 números ingresados.

print("Ingresa los tres numeros:")

num = []

for count in range(3):
    value = int(input(f"{count + 1} :"))
    num.append(value)

addNum = 0 
for i in range(len(num)):
    addNum += num[i]

cant = len(num)

result  = addNum / cant 

print(f"EL promedro de los numero eingresados es: {result}" )