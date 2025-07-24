# 10. Calcular el área de un triángulo.

num = []
print("ingrese los numeros:")
for i in range (2):
    valor = float(input(f"{i+1}: "))
    num.append(valor)
base = num[0]
altura = num[1]

result = (base * altura ) / 2
print(f"Resultado del area del triangulo: {result}")

# utilizamos .append para añadirle el valor numerico al array