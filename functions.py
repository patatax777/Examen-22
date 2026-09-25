name = ["Agua", "Alfajor", "Tostado"]
price = [700, 900, 2200]

def selection (a,c_money,s_money,quantity):
            if c_money >= price[a]:
                quant_2 = int(input("cuantas unidades desea comprar? "))
                print(f"""producto seleccionado: {name[a]}
                    costo del/los producto/s: {price[a]*quant_2}
                    saldo actual: {c_money}""")
                yes_no = int(input("""desea comprar este producto?
                sí = 1
                no = 0
                -"""))
                if yes_no == 1:
                    quantity[a] += quant_2
                    c_money = c_money - (price[a] * quant_2)
                    s_money = s_money + (price[a] * quant_2)
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