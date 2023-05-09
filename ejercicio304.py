import sqlite3

conexion=sqlite3.connect("bd1.db")
#Llamamos a execute y le pasamos como primer parámetro un comando SQL 'insert' con el caracter '?' 
# indicamos las posiciones donde se van a sustituir. El segundo parámetro es una tupla con los datos 
# que se utilizarán en la sustitució
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("naranjas", 23.50))
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("peras", 34))
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("bananas", 25))
#con el commit se actualizan los datos en la base de datos
conexion.commit()
conexion.close()