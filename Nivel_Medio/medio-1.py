# 31. Verificar si una palabra es palíndroma.
import re

def palindromo(palabra):
    pal_clear = palabra.lower()
    pal_clear = re.sub(r'[^a-z0-9]', '', pal_clear)
    
    longitud = len(pal_clear)
    for i in range(longitud // 2):
        if pal_clear[i] != pal_clear[longitud -1 -i]:
            return False
    return True

print(f"Bucle -'reconocer' es palíndormo: {palindromo('reconocer')}")
print(f"Bucle -'Python' es palíndormo: {palindromo('Python')}")