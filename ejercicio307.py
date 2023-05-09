#Se crea un script en el cual se solicita el ingreso de un precio y nos muestra
#la descripcion de los articulos con un precio mas bajo que el ingresado

import sqlite3

conexion=sqlite3.connect("bd1.db")
precio=float(input("Ingrese un precio:"))
cursor=conexion.execute("select descripcion from articulos where precio<?", (precio, ))
# Con fetchall de la clase Cursor y nos retorna una lista con todas las filas de la tabla 
#que cumplen la condición de tener un precio inferior al ingresado
filas=cursor.fetchall()
#Si no esta vacia se procede a imprimir
if len(filas)>0:
    for fila in filas:
        print(fila)
else:
    print("No existen artículos con un precio menor al ingresado.")
conexion.close()