nombres = ["Karen", "Leslie", "Jessica"]

for nombre in nombres:
    print(f"Hola {nombre} ¿Cómo te encuentas el dia de hoy? Quería invitarte a mi fiesta de cumpleaños, este jueves a las 3 de la tarde")

print(f"\nGracias por confirmar que no podrás asistir {nombres [2]}\n")
nombres.pop(2)

nombres.insert(2, "Ximena")
print(f"Hola {nombres [2]} ¿Cómo te encuentas el dia de hoy? Quería invitarte a mi fiesta de cumpleaños, este jueves a las 3 de la tarde\n")

nombres.insert(0, "Raymundo")
nombres.insert(2, "Luis")
nombres.append("Mayavi")

for nombre in nombres:
    print(f"Hola {nombre} ¿Cómo te encuentas el dia de hoy? Quería invitarte a mi fiesta de cumpleaños, este jueves a las 3 de la tarde")

print("\n")
while len(nombres) > 2:
    nombre = nombres.pop()
    print(f"Lo siento {nombre}, no estas invitado por falta de asientos")

print("\n")
for nombre in nombres:
    print(f"Hola {nombre}\nGracias por asistir a mi fiesta, ¿cómo te parecio la cena?")