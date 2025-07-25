# 29. Convertir metros a centímetros.

def cent(metros):
    result = metros * 100
    return result

metros = float(input("Ingrese los metros: \n"))

print(f"Son {cent(metros)}cm")