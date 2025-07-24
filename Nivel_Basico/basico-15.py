# 15. Imprimir todos los números impares entre 1 y 100.

num = 100
result = 0 
for i in range(num + 1):
    if i % 2 != 0:
        print(i)