import pandas as pd

# Leer el CSV completo en un DataFrame
df = pd.read_csv('CSV/train.csv')

# Ver las primeras 5 filas
print(df.head())

# Cuántas filas y columnas tiene
print("Dimensiones (filas, columnas):")
print(df.shape)

# Nombres de todas las columnas
print("\nColumnas:")
print(df.columns.tolist())

# Resumen de tipos de datos y nulos
print("\nInformación general:")
print(df.info())