#NO SE TOMAN EN CUENTA LAS CONDICIONES PUESTAS PARA EL EXAMEN
"""
product = {"Agua" : 700,
           "Alfajor" : 900,
           "Tostado" : 2200}
"""
name = ["Agua", "Alfajor", "Tostado"]
price = [700, 900, 2200]
quantity = [0, 0, 0]
products = sum(quantity)

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
print ("---KIOSKO PATATAX777---")
client = input("ingrese su nombre: ")
c_money = input("ingrese su dinero: ")
print ()
input(f"""¡hola {client}!, estás ingresando al "KIOSKO PATATAX777".
su saldo disponible es de: {c_money}
        
        presione "enter" para continuar--""")
option = 1
while option != 5:
    print ("""
    ---KIOSKO PATATAX777---
    1. Agua       - $700
    2. Alfajor    - $900
    3. Tostado    - $2200
    4. Consultar pedido
    5. Finalizar compra
    """)
    option = int(input("por favor, seleccione una opción en NÚMEROS: "))
    if option == 1:
        print ("seleccionó 1")#postergado
    elif option == 4:
        print()
    elif option == 5:
        print("COMPRA FINALIZADA")
    else:
        print("el número ingresado es inválido. por favor, seleccione un número que aparezca enn la tabla.")
        input("press enter")
