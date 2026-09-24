# Examen práctico — Sistema de pedidos del kiosco

Van a desarrollar un programa en Python que simule el sistema de pedidos de un kiosco escolar.

El programa deberá comenzar pidiendo el nombre del cliente y cuánto dinero tiene disponible para realizar la compra.

Los productos disponibles serán:

```text
1. Agua       - $700
2. Alfajor    - $900
3. Tostado    - $2200
4. Consultar pedido
5. Finalizar compra
```

El programa se va a desarrollar por etapas. Cada vez que terminen una etapa y funcione correctamente, deberán realizar el **commit indicado y luego hacer push** antes de continuar.

## Importante

- El examen es individual.
- Pueden realizar consultas al profesor durante el examen.
- **Cada consulta realizada al profesor descuenta 1 punto del puntaje total.**
- Antes de preguntar, revisen el código, los mensajes de error y prueben distintas entradas.
- Se evaluará tanto el resultado final como el proceso de desarrollo y los commits realizados.

---

## Etapa 1 — Inicio

Crear las variables necesarias, e inicializarlas en algún valor para guardar:

- Nombre del cliente.
- Dinero disponible.
- Dinero gastado.
- Cantidad total de productos comprados.
- Cantidad de aguas compradas.
- Cantidad de alfajores comprados.
- Cantidad de tostados comprados.

También deberán crear dos listas:

- Una lista con los nombres de los productos.
- Una lista con el precio de cada producto.

Por ejemplo:

```text
Productos: Agua, Alfajor, Tostado
Precios: 700, 900, 2200
```

Pedir al usuario su nombre y cuánto dinero tiene disponible.

Luego mostrar un mensaje de bienvenida junto con el saldo inicial.

Por ejemplo:

```text
===== KIOSCO ESCOLAR =====

Nombre: Mateo
Dinero disponible: 5000

Hola Mateo.
Saldo disponible: $5000
```

Cuando esta etapa funcione correctamente:

**Commit:** `Etapa 1 - Inicio del sistema`

Luego realizar el **push**.

---

## Etapa 2 — Realizar compras

Mostrar el menú y pedir al usuario que seleccione una opción.

Según el producto elegido, deberán obtener el nombre del producto y su precio utilizando las listas creadas en la etapa anterior.

Antes de realizar la compra, comprobar si el usuario tiene dinero suficiente.

Si la compra puede realizarse:

- Restar el precio al dinero disponible.
- Sumar el precio al dinero gastado.
- Sumar uno a la cantidad total de productos comprados.
- Sumar uno al contador correspondiente al producto comprado.

Por ejemplo:

```text
Producto seleccionado: Tostado
Precio: $2200

Compra realizada correctamente.
Saldo restante: $2800
```

Si el usuario no tiene suficiente dinero:

```text
Saldo insuficiente para realizar esta compra.
```

El saldo **nunca puede quedar en negativo**.

También deberán contemplar qué pasa si el usuario ingresa una opción que no existe.

### Pista para probar esta etapa

No alcanza con probar solamente que una compra correcta funcione.

Para comprobar que la condición de saldo insuficiente funciona, pueden **cambiar momentáneamente el precio de un producto por un valor mucho mayor**, o directamente **ingresar menos dinero al comenzar el programa**.

Por ejemplo, si arrancan con $500, ningún producto debería poder comprarse.

Cuando terminen de probarlo, vuelvan a colocar los valores indicados en la consigna.

Cuando esta etapa funcione correctamente:

**Commit:** `Etapa 2 - Sistema de compras`

Luego realizar el **push**.

---

## Etapa 3 — Mantener el programa funcionando

Hasta este punto el programa realiza una sola operación.

Ahora deberán modificarlo para que el menú vuelva a aparecer después de cada acción.

El programa deberá continuar funcionando hasta que el usuario elija:

```text
5. Finalizar compra
```

El usuario puede comprar el mismo producto más de una vez.

Cada compra correcta deberá actualizar:

- El saldo disponible.
- El dinero gastado.
- La cantidad total de productos comprados.
- El contador correspondiente al producto comprado.

Las compras rechazadas por falta de saldo **no deben contarse**.

Cuando esta etapa funcione correctamente:

**Commit:** `Etapa 3 - Ciclo principal`

Luego realizar el **push**.

---

## Etapa 4 — Consultar el pedido

Cuando el usuario seleccione:

```text
4. Consultar pedido
```

El programa deberá mostrar:

- Nombre del cliente.
- Cantidad total de productos comprados.
- Dinero gastado.
- Saldo restante.
- Cantidad comprada de cada producto.

Por ejemplo:

```text
===== PEDIDO ACTUAL =====

Cliente: Mateo
Productos comprados: 5
Total gastado: $5400
Saldo restante: $1600

Agua: 2
Alfajores: 2
Tostados: 1
```

Si todavía no se realizó ninguna compra, el programa deberá indicar que el pedido está vacío.

Además, deberán mostrar nuevamente los productos disponibles y sus precios recorriendo las listas con un `for`.

Por ejemplo:

```text
Productos disponibles:

Agua - $700
Alfajor - $900
Tostado - $2200
```

Cuando el usuario seleccione la opción `5`, mostrar un resumen final de la compra y finalizar el programa.

Cuando todo el programa esté terminado:

**Commit:** `Etapa 4 - Programa finalizado`

Luego realizar el **push**.

---

## Condiciones

Para resolver el examen deberán utilizar únicamente los contenidos vistos en clase.

Entre otras cosas, van a necesitar:

- Variables.
- `input()` y `print()`.
- Conversión de datos.
- Operaciones matemáticas.
- `if`, `elif` y `else`.
- Comparaciones.
- `while`.
- Listas.
- Índices.
- `for`.
- `range()`.
- Formato de texto.

No hace falta utilizar funciones, clases ni librerías externas.

El programa final deberá poder ejecutarse de principio a fin sin errores.

También se va a evaluar el historial del repositorio, por lo que **los commits pedidos forman parte del examen**.
