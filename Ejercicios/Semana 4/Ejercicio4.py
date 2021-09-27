entero = input ("Ingresa un numero del 1-1024\n")
entero = int(entero)

if (entero >= 1  and entero <= 1024):
    print(bin (entero))
else: 
    print("Este numero rebasa los limites")