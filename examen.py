#NO SE TOMAN EN CUENTA LAS CONDICIONES PUESTAS PARA EL EXAMEN
"""
product = {"Agua" : 700,
           "Alfajor" : 900,
           "Tostado" : 2200}
"""
#import funciones
from functions import selection
#creación de variables
name = ["Agua", "Alfajor", "Tostado"]
price = [700, 900, 2200]
quantity = [0, 0, 0]
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
        c_money, s_money = selection(0, c_money, s_money, quantity) #modificación de copilot
    elif option == 2:
        c_money, s_money = selection(1, c_money, s_money, quantity) #antes: (1, c_money, s_money, quantity) 
    elif option == 3:
        c_money, s_money = selection(2, c_money, s_money, quantity) # ahora + c_money, s_money = selection(...)
    elif option == 4:
        print(f""" pedido y datos actuales:
        nombre: {client}
        saldo actual: {c_money}
        dinero gastado: {s_money}

    cantidad de productos: {sum(quantity)}
        {name[0]}: {quantity[0]}
        {name[1]}: {quantity[1]}
        {name[2]}: {quantity[2]}
        """)
        input("presione enter para volver al menúmprincipál...")
    elif option == 5:
        print("COMPRA FINALIZADA")
        print(f"""datos finales:
        nombre: {client}
        saldo final: {c_money}
        dinero gastado: {s_money}

        cantidad de productos: {sum(quantity)}
        {name[0]}: {quantity[0]}
        {name[1]}: {quantity[1]}
        {name[2]}: {quantity[2]}
        """)
        #si copilot se acredita estas ultimas lineas de codigo es xq no quería escribir xddddd
    else:
        print("el número ingresado es inválido. por favor, seleccione un número que aparezca enn la tabla.")
        input("press enter")
        #ya m canse wn quiero dibujar :w -NOOOOOOLLLLL w (xd)

