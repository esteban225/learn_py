a = int(input("Intengresa un numero: "))
b = int(input("Intengresa un numero: "))
c = int(input("Intengresa un numero: "))

if a != b and a != c and b != c:
    if a > b: 
        if a > c:
            print( "El numero mayor es: ", a)
        else:
            print("El numero mayor es: ", c)
    else:
        if b > c: 
            print("El numero mayor es:" , b) 
        else: 
            print("Error al comparar los numeros.")
else:
    print("Ingresa 3 numeros diferentes.") 