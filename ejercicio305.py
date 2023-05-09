import sqlite3

conexion=sqlite3.connect("bd1.db")
#Se implementa un script que ejecuta un select en la tabla
#articulos y nos devuelve todas sus filas.
#El método execute retorna un objeto de la clase Cursor
cursor=conexion.execute("select codigo,descripcion,precio from articulos")
for fila in cursor:
    print(fila)
conexion.close()