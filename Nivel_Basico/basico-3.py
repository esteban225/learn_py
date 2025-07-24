# 3. Calcular la suma de los primeros N números naturales.
num = int(input("Ingrese la cantidad de numeros naturales que quieres sumar: "))
result = 0
for i in range(num + 1 ):
    result = i + result
    print(result)

print("Resultado: ", result)

# Se utulizo siclo for iterando el rango del numero tomado 
# se incio la variable result en cero 
# y se genero el ciclo sumando uno tras otro hasta llegar al rango dado 