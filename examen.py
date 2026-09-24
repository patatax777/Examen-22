#NO SE TOMAN EN CUENTA LAS CONDICIONES PUESTAS PARA EL EXAMEN
"""
product = {"Agua" : 700,
           "Alfajor" : 900,
           "Tostado" : 2200}
"""
#creación de variavlea
name = ["Agua", "Alfajor", "Tostado"]
price = [700, 900, 2200]
quantity = [0, 0, 0]
products = sum(quantity)
s_money = 0  
option = 1

"""
product ={
        "product_1": {
            "name": "Agua",
            "price": 700,
            "bought": 0}

        "product_2": {
            "name": "Alfajor",
            "price": 900,
            "bought": 0}

        "product_3": {
            "name": "Tostado",
            "price": 2200,
            "bought": 0}
}

print (product)
"""

#pedido de datos y bienvenida
print ("---KIOSKO PATATAX777---")
client = input("ingrese su nombre: ")
c_money = int(input("ingrese su dinero: "))
print ()
input(f"""¡hola {client}!, estás ingresando al "KIOSKO PATATAX777".
su saldo disponible es de: {c_money}
        
        presione "enter" para continuar--""")
print()

#empezando bucle kiosko patatax777 
while option != 5:
    print ("""---KIOSKO PATATAX777---
    1. Agua       - $700
    2. Alfajor    - $900
    3. Tostado    - $2200
    4. Consultar pedido
    5. Finalizar compra
    """)
    option = int(input("por favor, seleccione una opción en NÚMEROS: "))
    print()

    if option == 1:
        print(f"""producto seleccionado: {name[0]}
costo del producto: {price[0]}
saldo actual: {c_money}""")

        if c_money >= price[0]:
            yes_no = int(input("""desea comprar este producto?
            sí = 1
            no = 0
            -"""))
            if yes_no == 1:
                quantity[0] += 1
                c_money -= price[0]
                s_money += price[0]
                print("compra exitosa, regresando al menú principal...")
            elif yes_no == 0:
                print("""compra cancelada, regresando al menú principal...""")
            else:
                print("""opción no valida, compra cancelada. regresando al menú principal...""")
        else:
            print("no tienes suficiente dinero para comprar este producto")
            input("press enter")
        print ("")
    elif option == 4:
        print()
    elif option == 5:
        print("COMPRA FINALIZADA")
    else:
        print("el número ingresado es inválido. por favor, seleccione un número que aparezca enn la tabla.")
        input("press enter")
        #ya m canse wn quiero dibujar :w
