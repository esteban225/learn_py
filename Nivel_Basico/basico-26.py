# 26. Mostrar los múltiplos de 3 entre 1 y 100.

def mult(num):
    array = []
    for i in range(100 + 1):
        if i % num == 0:
            array.append(i)
    return array
num = 3
print(f"Los multiplos son: {mult(num)}")