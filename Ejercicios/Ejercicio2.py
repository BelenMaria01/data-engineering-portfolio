# Ejercicio 2 — ¿Cuál es el top 5 de ciudades con más ventas?
# Escribe tú la query — es un SELECT con GROUP BY, ORDER BY y LIMIT 5. Igual que en Oracle.
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

# Ejercicio 2
cursor.execute("""
    SELECT CITY, COUNT(*) AS TOTAL_VENTAS
    FROM VENTAS
    GROUP BY CITY
    ORDER BY TOTAL_VENTAS DESC
    LIMIT 5
""")

resultados = cursor.fetchall() # cursor.fetchall() recoge todo los registros y lo mete en la variable resultado
for fila in resultados:
    print(f"Ciudad: {fila[0]} | Total ventas: {fila[1]}")
    # {fila[0]} recoge el primer valor que es la cuidad
    # {fila[1]} recoge el segundo valor que es el count

conexion.close()
