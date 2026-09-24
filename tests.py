""" no entendí cómo funciona xddd (y no termina de cargar w)
from dash import Dash, html, dash_table
import pandas as pd

# 1. Crear un DataFrame de ejemplo con Pandas
df = pd.DataFrame({
    'Fruta': ['Manzana', 'Naranja', 'Banana', 'Pera'],
    'Cantidad': [4, 15, 8, 12],
    'Precio': [1.20, 2.50, 0.80, 1.50]
})

# 2. Inicializar la aplicación Dash
app = Dash(__name__)

# 3. Definir el diseño (layout) incluyendo la DataTable
app.layout = html.Div([
    html.H1('Mi primer tablero con tabla en Dash'),
    dash_table.DataTable(
        id='tabla-productos',
        # Definir las columnas de forma dinámica o manual
        columns=[{'name': col, 'id': col} for col in df.columns],
        # Convertir el DataFrame a formato de registros (diccionarios)
        data=df.to_dict('records'),
        # Habilitar características interactivas básicas
        page_size=10,  # Paginación
        sort_action='native',  # Ordenar al hacer clic en los encabezados
        filter_action='native'  # Filtrado básico por columna
    )
])

# 4. Ejecutar el servidor local
if __name__ == '__main__':
    app.run(debug=True)
"""

