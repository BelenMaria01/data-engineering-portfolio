# 👋 Hola, soy Belen

Soy **Packaged App Development Associate en Accenture** con 3 años de experiencia 
en entornos Oracle (SQL, PL/SQL). Actualmente en transición hacia **Data Engineering**, 
especializándome en Python, Big Data e Inteligencia Artificial.

---

## 🚀 Data Engineering — Python + PostgreSQL + Docker

Pipeline de datos con Python conectado a PostgreSQL corriendo en Docker, 
simulando un entorno de datos empresarial real.

### ¿Qué hace?
- Conecta Python con PostgreSQL mediante psycopg2
- Crea una tabla de empleados con SQL desde Python
- Inserta y consulta registros desde código Python

### 🛠️ Tecnologías
- Python 3.13
- PostgreSQL 18.4
- Docker Desktop
- psycopg2

### 📁 Ficheros
- `conexion_postgres.py` — Conexión básica y verificación de versión
- `creacion_tablas.py` — Creación de tabla, inserción y consulta de datos

### ▶️ Cómo ejecutarlo

1. Levantar PostgreSQL con Docker:
```bash
docker run --name postgres-data -e POSTGRES_PASSWORD=admin123 -e POSTGRES_USER=admin -e POSTGRES_DB=dataengineering -p 5432:5432 -d postgres
```

2. Instalar dependencias:
```bash
python -m pip install psycopg2-binary
```

3. Ejecutar los scripts en orden:
```bash
python conexion_postgres.py
python creacion_tablas.py
```

---

## 📚 Sobre mí
- 💼 Actualmente: Packaged App Development Associate en Accenture
- 🎯 Objetivo: Data Engineer
- 🧠 Aprendiendo: Python, Docker, PostgreSQL, Apache Spark, Airflow
- 📍 Bilbao, País Vasco

---

## 📬 Contacto
- LinkedIn: https://www.linkedin.com/in/belenmariacamachoruiz/
- GitHub: https://github.com/BelenMaria01