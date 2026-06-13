# Ejercicio 3 — ¿Cuál es la venta media por segmento?
# Escribe tú la query usando AVG(sales) agrupado por segmento.
import psycopg2

conexion = psycopg2.connect(
    host = "localhost",
    database = "dataengineering",
    user = "admin",
    password = "admin123",
    port = "5432"
)

cursor = conexion.cursor()

cursor.execute("""
    SELECT segment, AVG(sales) AS media_ventas
    FROM ventas
    GROUP BY segment
    ORDER BY media_ventas DESC
""")

resultados = cursor.fetchall()

for fila in resultados:
    print("--------------") 
    print(f"Segmento: {fila[0]} | Media ventas: {fila[1]}")
    print(f"Segmento: {fila[0]} | Media ventas: {fila[1]:.2f}") 
    print("--------------") 
conexion.close()