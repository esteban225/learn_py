print("Calculadora básica (+, -, *, /)")
a = float(input("Número 1: "))
b = float(input("Número 2: "))
op = input("Operación (+ - * /): ")

if op == "+":
    print("Resultado: ", a + b)
elif op == "-":
    print("Resultado: ", a - b)
elif op == "*":
    print("Resultado: ", a * b)
elif op == "/":
    if b != 0:
        print("Resultado: ", a / b)
    else:
        print("No se puede dividor entre 0")
else:
    print("Operación no valida")