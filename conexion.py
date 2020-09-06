
"""
AUTOR: Franco Alejandro Nuñez
Ultima modificacion: 06/09


Modulo: conexion.py

Este modulo consiste en una clase con diversos metodos que se encargan de hacer distintas consultas con la base de datos
y devolver los valores obtenidos al Modelo

"""


# importo la base de datos sqlite3 usada en este caso
import sqlite3



#clase con los distintos metodos de consulta a la bbdd
class conexiones:


    # conexion con la bbdd
    def conectar(self,):
        try:
            con = sqlite3.connect('BaseDeDatos1.db')
            return con
        except:
            print("Error")
        finally:
            print("Controlador.py/Modelo.py/conexion.py")
    
    # creacion de la tablas en la bbdd (si no es la primera vez que se inicia la app, saltara la excepcion)
    def creartabla(self, con):

        try:
            cursorObj = con.cursor()
            cursorObj.execute("CREATE TABLE REGISTROS (id integer PRIMARY KEY, titulo varchar, descripcion varchar)")
            con.commit()
        except:
            print("Base de datos ya existente")
        finally:
            print("Controlador.py/Modelo.py/conexion.py")
        

    # insentar registros
    def insertarregistro(self, con, a, b):

        try:
            cursorObj = con.cursor()
            sql = "INSERT INTO REGISTROS (titulo, descripcion) VALUES (?, ?)"
            datos = (a, b)
            cursorObj.execute(sql, datos)
            con.commit()
        except:
            print("error")
        finally:
            print("Controlador.py/Modelo.py/conexion.py")

    # consultas registros
    def consultar_Base(self, con,):

        try:
            cursorObj = con.cursor()
            sql = "SELECT * FROM REGISTROS ORDER BY id ASC" 
            cursorObj.execute(sql)
            return cursorObj.fetchall()
            con.commit()
        except:
            print("error")
        finally:
            print("Controlador.py/Modelo.py/conexion.py")

    # eliminar algun registro
    def borrarDat(self, con, miItem, ):
        print(miItem)
        try:
            cursorObj = con.cursor()
            sql = ("DELETE FROM REGISTROS WHERE id = ?")
            cursorObj.execute(sql, [str(miItem)], )
            con.commit()
        except:
            print("error")
        finally:
            print("Controlador.py/Modelo.py/conexion.py")
            
    # actualizar registro
    def actualizarDat(self, con, a_val, b_val, miItem):

        try:
            cursorObj = con.cursor()
            sql = ("UPDATE REGISTROS SET titulo = ?, descripcion = ? WHERE id = ?")
            parametros = (a_val, b_val, miItem)
            cursorObj.execute(sql, parametros)
            con.commit()
        except:
            print("error")
        finally:
            print("Controlador.py/Modelo.py/conexion.py")





objeto = conexiones()
objeto.conectar()
objeto.creartabla(objeto.conectar())
objeto.consultar_Base(objeto.conectar())

