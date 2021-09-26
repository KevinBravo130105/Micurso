#Pedir un valor en °C y devolveros en °F
#(°C × 9/5) + 32

grados_C = input ("Favor de ingresar los datos a convertir\n")
grados_C = float (grados_C)
grados_F = (grados_C * 9/5) + 32

print(f"La conversion de {grados_C}°C a °F es: {grados_F}°F")