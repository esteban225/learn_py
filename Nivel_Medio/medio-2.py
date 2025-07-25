# 32. Crear una calculadora con operaciones básicas.

# + - * / 

def calculadora(operador, num1, num2 ):
    if operador == "+": 
        result = num1 + num2 
    elif operador == "-":
        result = num1 - num2
    elif operador == "x":
        result = num1 * num2
    elif operador == "/":
        result = num1 / num2
    return result

operador = input(" Ingresa el operador ( + , - , x , / ):\n")
num1 = int(input("Ingresa el primer número:\n "))
num2 = int(input("Ingresa el segundo número:\n "))

resultado = calculadora(operador, num1, num2)

print(f"La operación: {num1} {operador} {num2} = {resultado} ")