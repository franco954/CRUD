



"""
AUTOR: Franco Alejandro Nuñez
Ultima modificacion: 06/09


Modulo: Modelo.py


Modulo que recibe las ordenes directamente del controlador y que dependiendo el pedido va a realizar la conexion con los distintos
modulos que tiene a su mando (temas.py, validarAlfa.py, conexion.py)

"""


# importo la libreria usada y sus caracteristicas
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#importo los modulos al servicio de Modelo.py
from conexion import *
from validarAlfa import *
from temas import *



class miModelo:


    # metodos que se comunican con el modulo temas.py, llevando los datos de las vistas a modificar
    def fuentes_txt(self, varOpcion_txt, tituloPrincipal, tituloReferencia, descripcionReferencia, 
            altaBase, borrar, modificarRegistro, temasPrograma, accionesMensajes, ):

        try:
        
            if self.varOpcion_txt.get() == 1:
                fuentes.perpetua_txt(self, self.tituloPrincipal, self.tituloReferencia, self.descripcionReferencia, 
                self.altaBase, self.borrar, self.modificarRegistro, self.temasPrograma, self.accionesMensajes, )

            elif self.varOpcion_txt.get() == 2:
                fuentes.simSun_txt(self, self.tituloPrincipal, self.tituloReferencia, self.descripcionReferencia, 
                self.altaBase, self.borrar, self.modificarRegistro, self.temasPrograma, self.accionesMensajes, )

            elif self.varOpcion_txt.get() == 3:
                fuentes.consolas_txt(self, self.tituloPrincipal, self.tituloReferencia, self.descripcionReferencia, 
                self.altaBase, self.borrar, self.modificarRegistro, self.temasPrograma, self.accionesMensajes, )

            elif self.varOpcion_txt.get() == 4:
                fuentes.calibri_txt(self, self.tituloPrincipal, self.tituloReferencia, self.descripcionReferencia, 
                self.altaBase, self.borrar, self.modificarRegistro, self.temasPrograma, self.accionesMensajes, )
            else:
                pass

        except:
            print("Error")

        finally:
            print("Controlador.py/Modelo.py")


    def eleccionTema(self, varOpcion, tituloPrincipal, tituloReferencia, descripcionReferencia, 
            altaBase, borrar, modificarRegistro, temasPrograma, accionesMensajes,):

        try:

            if self.varOpcion.get() == 1:
                tematicas.tema1_red(self, self.tituloPrincipal, self.tituloReferencia, self.descripcionReferencia, 
                self.altaBase, self.borrar, self.modificarRegistro, self.temasPrograma, )

            elif self.varOpcion.get() == 2:
                tematicas.tema2_blue(self, self.tituloPrincipal, self.tituloReferencia, self.descripcionReferencia, 
                self.altaBase, self.borrar, self.modificarRegistro, self.temasPrograma, )

            elif self.varOpcion.get() == 3:
                tematicas.tema3_green(self, self.tituloPrincipal, self.tituloReferencia, self.descripcionReferencia, 
                self.altaBase, self.borrar, self.modificarRegistro, self.temasPrograma, )

            elif self.varOpcion.get() == 4:
                tematicas.tema4_predeterminado(self, self.tituloPrincipal, self.tituloReferencia, self.descripcionReferencia, 
                self.altaBase, self.borrar, self.modificarRegistro, self.temasPrograma, )

            else:
                pass
        
        except:
            print("Error")

        finally:
            print("Controlador.py/Modelo.py")


"""
     Metodos de consulta con las bases de datos, reciben la orden del controlador y realizan la accion correspondiente al boton presionado
     se comunican con el modulo conexion.py para poder obtener la info de la bbdd y asi poder trabajar
"""
    def salir_app(self, root, ):

        try:
            var_salir = messagebox.askquestion("Programa","¿Estas seguro que deseas salir?")
            if var_salir=="yes":
                root.destroy()  
        except:
            print("Error")

        finally:
            print("Controlador.py/Modelo.py")


    def agregarRegistro(self, a_val, b_val, accionesMensajes ):
        #objeto = conexion.objeto
        con = objeto.conectar()

        try:

            if validacion.validar(self, self.a_val.get()) == True and validacion.validar(self, self.b_val.get()) == True:
                objeto.insertarregistro(con, self.a_val.get(), self.b_val.get())
                self.accionesMensajes.config(text="Registro guardado con exito", fg="green")
            else:
                self.accionesMensajes.config(text="Carga de registro invalida", fg="red")
        except:
            print("Error")

        finally:
            print("Controlador.py/Modelo.py")


    def pedirRegistros(self, pantallaPrincipal):
    	#objeto = conexion.objeto
        try:           
            con = objeto.conectar()
            datosGuardados = self.pantallaPrincipal.get_children()
            for datos in datosGuardados:
                self.pantallaPrincipal.delete(datos)
            objeto.consultar_Base(con,)
            listado = conexiones.consultar_Base(self, con,)
            for filas in listado:
                self.pantallaPrincipal.insert("", 0, text= filas[0], values= (filas[1], filas[2]))
        except:
            print("Error")
        finally:
            print("Controlador.py/Modelo.py")

    def borrarRegistros(self, pantallaPrincipal, accionesMensajes):

        #objeto = conexion.objeto
        try:
            con = objeto.conectar()
            pase = False
            for elementos_pantalla in self.pantallaPrincipal.selection():
                pase = True
                if pase == True:
                    miItem = (self.pantallaPrincipal.item(elementos_pantalla)["text"])
                    print(miItem)
                    objeto.borrarDat(con, miItem)
                    self.accionesMensajes.config(text="Registro borrado con exito", fg="green")
            if pase == False:

                self.accionesMensajes.config(text="Debes seleccionar un registro", fg="red")
        except:
            print("Error")

        finally:
            print("Controlador.py/Modelo.py")	

    def actualizarRegistro(self, a_val, b_val, pantallaPrincipal, accionesMensajes,):

        #objeto = conexion.objeto
        con = objeto.conectar()
        pase = False
        try:
            if validacion.validar(self, self.a_val.get()) == True and validacion.validar(self, self.b_val.get()) == True:
                for elementos_pantalla in self.pantallaPrincipal.selection(): 
                    miItem = (self.pantallaPrincipal.item(elementos_pantalla)["text"])
                    print(miItem)
                    objeto.actualizarDat(con, self.a_val.get(), self.b_val.get(), miItem)
                    self.accionesMensajes.config(text="Actualizacion de registro exitosa", fg="green")
                    pase = True
                if pase == False:
                    self.accionesMensajes.config(text="Debes seleccionar un registro", fg="red")
                else: 
                    pass
            else:
                self.accionesMensajes.config(text="Error al actualizar el registro", fg= "red")
        except UnboundLocalError:
            self.accionesMensajes.config(text="Error al actualizar el registro", fg= "red")
        finally:
            print("Controlador.py/Modelo.py")

