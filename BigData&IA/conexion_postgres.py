import psycopg2

conexion = psycopg2.connect(
    host="localhost",
    database="dataengineering",
    user="admin",
    password="admin123",
    port="5432"
)

print("Conexión exitosa a PostgreSQL!")

cursor = conexion.cursor()
cursor.execute("SELECT version();")
version = cursor.fetchone()
print(f"Versión de PostgreSQL: {version[0]}")

conexion.close()
print("Conexión cerrada.")