nombre = input ("Introduce tu nombre\n") 
edad = input ("Introduce tu edad\n")
telefono = input ("Introduce tu numero telefonico\n")
direccion = input ("Introduce tu domicilio\n")
nacion = input ("Intruce tu nacionalidad\n")
dia = input ("Introduce tu dia de nacimiento\n")
mes = input ("Introduce tu mes de nacimiento\n")
año = input ("Introduce tu año de nacimiento\n")
email = input ("Introduce tu correo electronico\n")

fecha = f"{dia}-{mes}-{año}"

edad = int(edad)
telefono = int(telefono)

print(f" Hola {nombre}\n Mencionaste que tienes {edad} años\n Que tu número telefonico es {telefono}\n Mencionas que vives en {direccion}\n Tu naciste en {nacion} el día {fecha}\n Podemos localizarte en el correo {email}")