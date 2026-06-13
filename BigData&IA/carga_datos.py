import psycopg2
import csv

# Conexión a PostgreSQL
conexion = psycopg2.connect(
    host="localhost",
    database="dataengineering",
    user="admin",
    password="admin123",
    port="5432"
)

cursor = conexion.cursor()

# Crear tabla ventas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS ventas (
        id SERIAL PRIMARY KEY,
        row_id INTEGER,
        order_id VARCHAR(50),
        order_date VARCHAR(20),
        ship_date VARCHAR(20),
        ship_mode VARCHAR(50),
        customer_name VARCHAR(100),
        segment VARCHAR(50),
        country VARCHAR(50),
        city VARCHAR(50),
        category VARCHAR(50),
        sub_category VARCHAR(50),
        product_name VARCHAR(200),
        sales FLOAT
    )
""")

# Cargar datos del CSV
with open('train.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
            INSERT INTO ventas (row_id, order_id, order_date, ship_date, ship_mode, 
            customer_name, segment, country, city, category, sub_category, product_name, sales)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row['Row ID'], row['Order ID'], row['Order Date'], row['Ship Date'],
            row['Ship Mode'], row['Customer Name'], row['Segment'], row['Country'],
            row['City'], row['Category'], row['Sub-Category'], row['Product Name'],
            row['Sales']
        ))

conexion.commit()
print("Datos cargados correctamente!")

# Contar registros
cursor.execute("SELECT COUNT(*) FROM ventas")
total = cursor.fetchone()
print(f"Total de registros cargados: {total[0]}")

conexion.close()