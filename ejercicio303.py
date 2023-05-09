#para trabajar con sql se importa el modulo sqlite3
import sqlite3
#Para establecer una conexion se llama a la funcion connect
conexion=sqlite3.connect("bd1.db")
#el try se añade ya que cuando se ejecuta por segunda vez el codigo te dice
# que ya existe 
try:
    conexion.execute("""create table articulos (
                              codigo integer primary key autoincrement,
                              descripcion text,
                              precio real
                        )""")
    print("se creo la tabla articulos")                        
except sqlite3.OperationalError:
    print("La tabla articulos ya existe")                    
conexion.close()

##si no se desea que aparezca la excepcion se modifica el comando SQL 
#de la creacion de la tabla con la sintaxis
import sqlite3
conexion=sqlite3.connect("bd1.db")
conexion.execute("""create table if not exists articulos (
                          codigo integer primary key AUTOINCREMENT,
                          descripcion text,
                          precio real
                    )""")
conexion.close()