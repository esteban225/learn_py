# 21. Contar cuántos números positivos hay en una lista.

def cant(list):
    count = 0
    while list[count] > 0:
        count += 1
    return count

list = [1, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , -1 , -2 , -3 , -4 , -5 ]

print(cant(list))