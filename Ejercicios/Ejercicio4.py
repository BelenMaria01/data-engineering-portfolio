# Ejercicio 4 — ¿Cuánto se ha vendido en total por categoría?
# Escribe tú la query usando SUM(sales) agrupado por categoría.
import psycopg2

# Conexión a PostgreSQL
conexion = psycopg2.connect(
    host="localhost",
    database="dataengineering",
    user="admin",
    password="admin123",
    port="5432"
)

cursor = conexion.cursor()

cursor.execute("""
    SELECT CATEGORY, SUM(SALES) TOTAL_VENTAS
    FROM VENTAS
    GROUP BY CATEGORY
    ORDER BY TOTAL_VENTAS DESC
""")

resultados = cursor.fetchall()

for fila in resultados:
    print(f"Categoria: {fila[0]} | total venta: {fila[1]:.2f}")


conexion.close()