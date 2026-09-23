#def producto ():

products = {"name_p" : ["Agua", "Alfajor", "Tostado"],
             "price_p" : [700, 900, 2200]}

#producto = ("Agua", "Alfajor", "Tostado")
#precio = (700, 900, 2200)
#for x, y in productos.items():
#  print(x, y)

name = input("ingrese su nombre: ")
money = int(input("ingrese su dinero disponible: "))


print(f"""
      ♥♦♣♠KIOSKKO PATATAX777♠♣♦♥
      Hola {name}!
      Dinero disponible: ${money}

        ---PRODUCTOS---
        1. Agua       - $700
        2. Alfajor    - $900
        3. Tostado    - $2200
        4. Consultar pedido
        5. Finalizar compra

        por favor, seleccione una opción con los números:""")
opcion = int(input("-"))


if opcion<1 or opcion>5:
    print("La opción seleccionada no se encuentra dentro de las opciónes. Por favor, vuelva a iniciar el programa.")

elif opcion == 1:
    for values in products.values():
        print(values[0])
    
    if 700 > (money):
        print("Saldo insuficiente para realizar esta compra.")
    else:
        money = money - 700
        water = water + 1
        products = products + 1
        money_w = money_w + (price[0])
        
elif opcion == 2:
    print()
elif opcion == 3:
   print()
elif opcion == 4:
    print()
elif opcion == 5:
    print (f"""{name}
            {money}
            {money_w}
            {products}
            {water}
            {alfajor}
            {tostados}
""")
