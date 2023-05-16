import sqlite3
import os
 
def check_db(filename):
    return os.path.exists(filename)
 
db_file = 'database.db'
schema_file = 'e:/M3/schema.sql'
 
if check_db(db_file):
    print('La base de datos existe...')
    exit(0)
 
with open(schema_file, 'r') as rf:
    # crea el esquema para el archivo
    schema = rf.read()
 
with sqlite3.connect(db_file) as conn:
    print('Conexion creada!')
    # Ejecuta la consulta SQL para crear la tabla
    conn.executescript(schema)
    print('Tabla creada! Ahora insertando')
    conn.executescript("""
                    insert into  imagenes (nombre, tamaño, fecha)
                       values
                       ('sample.png', 100, '2019-10-10'),
                       ('ask_python.png', 450, '2019-05-02'),
                       ('class_room.jpeg', 1200, '2018-04-07');
                       """)
    print('Valores insertados en la tabla')
print('!cerrando la conexion!')