# 4. Contar cuántas vocales tiene una palabra.
word = input("Ingrese la palabra: ")
count_vocals = 0 
vocal = "aeiouAEIOU"

for caracter in word:
    if caracter in vocal:
        count_vocals += 1
        
print(f"La palabra {word} tiene {count_vocals} vocales.")