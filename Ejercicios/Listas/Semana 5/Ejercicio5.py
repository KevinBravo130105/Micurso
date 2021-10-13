# Ejercicio 5.1
lugares_Por_Visitar = ["Cancun", "Taj Mahal", "Machu Picchu", "Isla de Pascua", "Chichén Itzá"]

print("LUGARES EN LISTA ORIGNAL")
for lugares in lugares_Por_Visitar:
    print(lugares)

# Ejercicio 5.2
print("\n")
lugares_Inverso = sorted(lugares_Por_Visitar, reverse=True)

print("LUGARES EN LISTA ORIGNAL")
for lugares in lugares_Por_Visitar:
    print(lugares)
print("\n") 
print("LUGARES EN ORDEN INVERSO")   
for lugares in lugares_Inverso:
    print(lugares)

# EJercicio 5.3
print("\n")
lugares_Inverso = sorted(lugares_Por_Visitar)

print("LUGARES EN LISTA ORIGNAL")
for lugares in lugares_Por_Visitar:
    print(lugares)
print("\n")
print("LUGARES EN ORDEN")
for lugares in lugares_Inverso:
    print(lugares)

# Ejercicio 5.5
print("\n")
lugares_Por_Visitar.sort()
print("LUGARES EN ORDEN POR METODO SORT")
for lugares in lugares_Por_Visitar:
    print(lugares)

# Ejercicio 5.6
print("\n")
lugares_Por_Visitar.sort(reverse=True)
print("LUGARES EN ORDEN INVERSO POR METODO SORT")
for lugares in lugares_Por_Visitar:
    print(lugares)