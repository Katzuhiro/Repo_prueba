print("Bienvenido a nuestra pizzeria")
print("Menú")
print("1. Hawaiana $10000")
print("2. Pepperoni $20000")
print("3. Napolitana $13500")
print("4. Champiñones $14600")

hawaiana = 10000
pepperoni = 20000
napolitana = 13500
champiñones = 14600

accion = int(input("Por favor elija una accion del menú: "))

if accion ==1:
    cantidad = int(input("ingrese la cantidad de pizzas que desea ordenar: "))
    resultado = cantidad * hawaiana
    print("el costo de su orden es:", resultado)

elif accion ==2:
    cantidad = int(input("ingrese la cantidad de pizzas que desea ordenar: "))
    resultado2 = cantidad * pepperoni
    print("el costo de su orden es:", resultado2)

elif accion ==3:
    cantidad = int(input("ingrese la cantidad de pizzas que desea ordenar: "))
    resultado3 = cantidad * napolitana
    print("el costo de su orden es:", resultado3)

elif accion ==4:
    cantidad = int(input("ingrese la cantidad de pizzas que desea ordenar: "))
    resultado4 = cantidad * champiñones
    print("el costo de su orden es:", resultado4)
else:
    print("Opcion invalida, por favor seleccione una opcion del menú valida.")