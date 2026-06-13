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
    SELECT column_name, data_type 
    FROM information_schema.columns 
    WHERE table_name = 'ventas'
""")
columnas = cursor.fetchall()
for columna in columnas:
    print(f"Campo: {columna[0]} | Tipo: {columna[1]}")


conexion.close()
