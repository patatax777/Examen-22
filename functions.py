name = ["Agua", "Alfajor", "Tostado"]
price = [700, 900, 2200]

def selection (a,c_money,s_money,quantity):
            print(f"""producto seleccionado: {name[a]}
    costo del producto: {price[a]}
    saldo actual: {c_money}""")
    
            if c_money >= price[a]:
                yes_no = int(input("""desea comprar este producto?
                sí = 1
                no = 0
                -"""))
                if yes_no == 1:
                    quantity[a] += 1
                    c_money = c_money - (price[a])
                    s_money = s_money + (price[a])
                    print("compra exitosa, regresando al menú principal...")
                elif yes_no == 0:
                    print("""compra cancelada, regresando al menú principal...""")
                else:
                    print("""opción no valida, compra cancelada. regresando al menú principal...""")
            else:
                print("no tienes suficiente dinero para comprar este producto")
                input("press enter")
            print ("")
            return c_money, s_money #agregado por copilot