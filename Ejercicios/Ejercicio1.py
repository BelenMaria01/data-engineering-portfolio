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

# Ejercicio 1 - Ventas por categoría
cursor.execute("""
    SELECT category, COUNT(*) as total_ventas
    FROM ventas
    GROUP BY category
    ORDER BY total_ventas DESC
""")

resultados = cursor.fetchall()

print("Ventas por categoría:")
for fila in resultados:
    print(f"Categoría: {fila[0]} | Total ventas: {fila[1]}")

conexion.close()
