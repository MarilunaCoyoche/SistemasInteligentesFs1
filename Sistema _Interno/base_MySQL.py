import sqlite3

conexion = sqlite3.connect('mi_base_de_datos.db')

cursor = conexion.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS desayunos (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    calorias INTEGER,
                    ingredientes TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS almuerzos (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    calorias INTEGER,
                    ingredientes TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS refrigerios (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    calorias INTEGER,
                    ingredientes TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS cenas (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    calorias INTEGER,
                    ingredientes TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS aperitivos (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    calorias INTEGER,
                    grasas_saturadas TEXT,
                    sodio TEXT,
                    otros TEXT
                )''')

conexion.commit()
conexion.close()

print("La base de datos SQLite ha sido creada exitosamente.")

