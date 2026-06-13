import pandas as pd

# ============================================
# CHULETA DE PANDAS - Referencia rápida
# Ejemplos con la columna 'Category' para que sirvan
# de guía sin resolverte los ejercicios de Segment/Region/Ship Mode
# ============================================

df = pd.read_csv('train.csv')


# --- VER Y EXPLORAR DATOS ---

df.head()              # primeras 5 filas
df.head(10)            # primeras 10 filas
df.shape               # (nº filas, nº columnas)
df.columns.tolist()    # lista de nombres de columnas
df.info()              # tipos de dato y nulos por columna
df.describe()          # estadísticas (media, min, max...) de columnas numéricas


# --- SELECCIONAR COLUMNAS ---

df['Sales']                      # una sola columna
df[['Category', 'Sales']]        # varias columnas (van entre doble corchete)


# --- AGRUPAR Y CALCULAR (GROUP BY) ---
# Patrón: df.groupby('columna_agrupar')['columna_calcular'].operación()

df.groupby('Category')['Sales'].sum()     # SUMA de ventas por categoría
df.groupby('Category')['Sales'].mean()    # MEDIA de ventas por categoría
df.groupby('Category')['Sales'].max()     # MÁXIMO por categoría
df.groupby('Category')['Sales'].min()     # MÍNIMO por categoría
df.groupby('Category').size()             # CONTAR filas por categoría (como COUNT(*))


# --- ORDENAR ---

df.groupby('Category')['Sales'].sum().sort_values()                  # ascendente
df.groupby('Category')['Sales'].sum().sort_values(ascending=False)   # descendente


# --- LIMITAR RESULTADOS ---

df.groupby('Category')['Sales'].sum().head(5)   # los primeros 5 (como LIMIT 5)


# --- REDONDEAR DECIMALES AL MOSTRAR ---
# Dentro de una f-string: {valor:.2f} muestra 2 decimales
# Ejemplo:
total = df['Sales'].sum()
print(f"Total de ventas: {total:.2f}€")