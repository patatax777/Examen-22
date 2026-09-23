# Examen práctico - Sistema de pedidos del kiosco
# Nombre y apellido:kiyomi melillan
# Curso:2 2
#
# IMPORTANTE:
# Resolver el programa siguiendo las etapas indicadas en el README.md.
# Realizar los commits y push cuando se indique.



# =========================
# ETAPA 1 - INICIO
# =========================

# Crear las variables necesarias.
# Crear las listas de productos y precios.
# Pedir los datos del cliente.

nombre_c = 0
dinero = 0
dinero_g = 0
productos_c = 0
aguas_c = 0
alfajor_c = 0
tostados_c = 0

nombres_p = ("Agua", "Alfajor", "Tostado")
precio_p = (700, 900, 2200)

nombre_c = input("ingrese su nombre: ")
dinero = input("ingrese su dinero disponible: ")

print(f"""
      ♥♦♣♠KIOSKKO PATATAX777♠♣♦♥
      
      Hola {nombre_c}
      Dinero disponible: ${dinero}
      """)

# =========================
# ETAPA 2 - COMPRAS
# =========================

# Mostrar el menú y procesar la opción seleccionada.
# Utilizar las listas para obtener producto y precio.

print("""
---PRODUCTOS---
1. Agua       - $700
2. Alfajor    - $900
3. Tostado    - $2200
4. Consultar pedido
5. Finalizar compra

por favor, seleccione una opción con los números.
""")
opcion = int(input(": "))

if opcion<1 or opcion>5:
    print("La opción seleccionada no se encuentra dentro de las opciónes. Por favor, vuelva a iniciar el programa.")
elif opcion == 1:
    print(f"{producto[0]}: ${precio[0]}")
    
    if dinero < (precio[0]):
        print("Saldo insuficiente para realizar esta compra.")
    else:
        dinero = dinero - (precio[0])
        aguas_c = aguas_c + 1
        productos_c = productos_c + 1
        dinero_g = dinero_g + (precio[0])
        
elif opcion == 2:
    print(f"{producto[1]}: ${precio[1]}")
elif opcion == 3:
    print(f"{producto[2]}: ${precio[2]}")
elif opcion == 4:
    print(f"{producto[3]}: ${precio[3]}")
elif opcion == 5:
    print(f"{producto[4]}: ${precio[4]}")
    
    print (f"""{nombre_c}
{dinero}
{dinero_g}
{productos_c}
{aguas_c}
{alfajor_c}
{tostados_c}""")
    
# =========================
# ETAPA 3 - CICLO PRINCIPAL
# =========================

# Modificar el programa para que continúe funcionando
# hasta que el usuario decida finalizar la compra.


# =========================
# ETAPA 4 - PEDIDO Y RESUMEN
# =========================

# Mostrar el estado actual del pedido.
# Recorrer las listas con un for para mostrar productos y precios.
