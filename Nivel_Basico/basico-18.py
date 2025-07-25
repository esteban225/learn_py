# 18. Determinar si una letra es vocal o consonante.

vocales = ["A","E","I","O","U","Á", "É", "Í", "Ó", "Ú"]
consonantes = ["B", "C", "D", "F", "G", "H" , "J", "K", "L", "M", "N", "Ñ", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]

letra = input("Ingresa una letra: ").upper()

if len(letra) != 1 or not letra.isalpha():
    print("Por favor, ingrese solo una letra del alfabeto.")
elif letra in vocales:
    print("La letra es una vocal.")
elif letra in consonantes:
    print("La letra es una consonante.")
else:
    print("Letra no reconocida.")