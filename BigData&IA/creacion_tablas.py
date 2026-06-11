import psycopg2

conexion = psycopg2.connect(
    host="localhost",
    database="dataengineering",
    user="admin",
    password="admin123",
    port="5432"
)

cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS empleados (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100),
        rol VARCHAR(100),
        salario FLOAT,
        años_experiencia INT
    )
""")

# Insertar datos
cursor.execute("""
    INSERT INTO empleados (nombre, rol, salario, años_experiencia)
    VALUES 
        ('Belen', 'Packaged App Developer', 1500.0, 3),
        ('Juan', 'Data Engineer', 3000.0, 5),
        ('Maria', 'Data Scientist', 3500.0, 4)
""")

conexion.commit()
print("Tabla creada e insertados 3 empleados!")

# Consultar datos
cursor.execute("SELECT * FROM empleados")
empleados = cursor.fetchall()

print("\nEmpleados en la base de datos:")
for empleado in empleados:
    print(f"ID: {empleado[0]} | Nombre: {empleado[1]} | Rol: {empleado[2]} | Salario: {empleado[3]}€ | Experiencia: {empleado[4]} años")

conexion.close()