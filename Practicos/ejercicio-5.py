secreto = 7
intento = int(input("Adivina el número (entre 1 y 10): "))
while intento != secreto:
    print("¡Incorrecto! Intenta de nuevo. ")
    intento = int(input("Adivina el número:"))
print("¡Correcto! 🤓")