


# Importo los modulos que se comunican directamente con el controlador
from tkinter import *
from Vista import *
from Modelo import *
from TopLevelTemas import *


# clase donde contengo los metodos a realizar con las distintas acciones de la app
class miControlador:


	#Llamada a la vista principal
	def vistaPrincipalC(self, ):
		try:
			registros.imagenPrincipal(self,)
		except:
			print("Error")
		finally:
			print("Controlador.py")
	
	# ventana emergente de temas
	def topLevel(self, varOpcion, varOpcion_txt, ):

		try:
			topLevel.aparecerBg(self, varOpcion, varOpcion_txt)
		except:
			print("Error")
		finally:
			print("Controlador.py")

	# opciones de var que vienen de TopLevelTemas.py y que se dirigen a modelo.py para despues en temas.py decidir que tematica aplicar 
	def temaOpcion(self, varOpcion,):

		try:
			miModelo.eleccionTema(self, varOpcion, self.tituloPrincipal, self.tituloReferencia, self.descripcionReferencia, 
				self.altaBase, self.borrar, self.modificarRegistro, self.temasPrograma, self.accionesMensajes,)
		except:
			print("Error")
		finally:
			print("Controlador.py")

	def temaOpcion_txt(self, varOpcion_txt,):
		try:
			miModelo.fuentes_txt(self, varOpcion_txt, self.tituloPrincipal, self.tituloReferencia, self.descripcionReferencia, 
	           	self.altaBase, self.borrar, self.modificarRegistro, self.temasPrograma, self.accionesMensajes,)
		except:
			print("Error")
		finally:
			print("Controlador.py")

	#boton salir app
	def salirAplicacion(self, root):
		try:
			miModelo.salir_app(self, root, )
		except:
			print("Error")
		finally:
			print("Controlador.py")

			
	def registroAltas(self, a_val, b_val, accionesMensajes, pantallaPrincipal ):

		try:
			miModelo.agregarRegistro(self, a_val, b_val, accionesMensajes,)
			miModelo.pedirRegistros(self, pantallaPrincipal)
		except:
			print("Error")
		finally:
			print("Controlador.py")
		
	def registroConsultas(self, pantallaPrincipal ):

		try:
			miModelo.pedirRegistros(self, pantallaPrincipal,)
		except:
			print("Error")
		finally:
			print("Controlador.py")

	def registroBorrar(self, pantallaPrincipal, accionesMensajes, ):

		try:
			miModelo.borrarRegistros(self, pantallaPrincipal, accionesMensajes,)
			miModelo.pedirRegistros(self, pantallaPrincipal,)
		except:
			print("Error")
		finally:
			print("Controlador.py")

	def registroActualizar(self, pantallaPrincipal, accionesMensajes, a_val, b_val,):

		try:
			miModelo.actualizarRegistro(self, pantallaPrincipal, accionesMensajes, a_val, b_val,)
			miModelo.pedirRegistros(self, pantallaPrincipal,)
		except:
			print("Error")
		finally:
			print("Controlador.py")


#Inicio de la vista apenas inicie el programa
if __name__ == '__main__':
	objetoIniciar = miControlador()
	objetoIniciar.vistaPrincipalC()

























	




