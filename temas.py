



# importo la libreria
from tkinter import *




# clase de colores
class tematicas:

	
	def tema1_red(self, tituloPrincipal, tituloReferencia, descripcionReferencia, altaBase, borrar, modificarRegistro, temasPrograma):

		try:

			tituloPrincipal.config(bg="red")
			borrar.config(bg="red")
			modificarRegistro.config(bg="red")
			temasPrograma.config(bg="red")
			altaBase.config(bg="red")

		except:
			print("Error")

		finally:
			print("Controlador.py/Modelo.py/temas.py")


	def tema2_blue(self, tituloPrincipal, tituloReferencia, descripcionReferencia, altaBase, borrar, modificarRegistro, temasPrograma):
	
		try:

			tituloPrincipal.config(bg="light blue")
			borrar.config(bg="light blue")
			modificarRegistro.config(bg="light blue")
			temasPrograma.config(bg="light blue")
			altaBase.config(bg="light blue")

		except:
			print("Error")

		finally:
			print("Controlador.py/Modelo.py/temas.py")

	def tema3_green(self, tituloPrincipal, tituloReferencia, descripcionReferencia, altaBase, borrar, modificarRegistro, temasPrograma):
		
		try:	
			tituloPrincipal.config(bg="light green")
			borrar.config(bg="light green")
			modificarRegistro.config(bg="light green")
			temasPrograma.config(bg="light green")
			altaBase.config(bg="light green")

		except:
			print("Error")

		finally:
			print("Controlador.py/Modelo.py/temas.py")
				
	def tema4_predeterminado(self, tituloPrincipal, tituloReferencia, descripcionReferencia, altaBase, borrar, modificarRegistro, temasPrograma):
		
		try:	
			tituloPrincipal.config(bg="#924e7d")
			borrar.config(bg="#924e7d")
			modificarRegistro.config(bg="#924e7d")
			temasPrograma.config(bg="#924e7d")
			altaBase.config(bg="#924e7d")

		except:
			print("Error")

		finally:
			print("Controlador.py/Modelo.py/temas.py")



# clase de tipo de letra
class fuentes:


	def perpetua_txt(self, tituloPrincipal, tituloReferencia, descripcionReferencia, altaBase, borrar, modificarRegistro, temasPrograma, accionesMensajes):

		try:
			tituloPrincipal.config(font=("Perpetua",10))
			tituloReferencia.config(font=("Perpetua",10))
			descripcionReferencia.config(font=("Perpetua",10))
			borrar.config(font=("Perpetua",10))
			modificarRegistro.config(font=("Perpetua",10))
			temasPrograma.config(font=("Perpetua",10))
			altaBase.config(font=("Perpetua",10))
			accionesMensajes.config(font=("Perpetua",10))

		except:
			print("Error")

		finally:
			print("Controlador.py/Modelo.py/temas.py")
		
	def simSun_txt(self, tituloPrincipal, tituloReferencia, descripcionReferencia, altaBase, borrar, modificarRegistro, temasPrograma, accionesMensajes):

		try:
			tituloPrincipal.config(font=("SimSun",10))
			tituloReferencia.config(font=("SimSun",10))
			descripcionReferencia.config(font=("SimSun",10))
			borrar.config(font=("SimSun",10))
			modificarRegistro.config(font=("SimSun",10))
			temasPrograma.config(font=("SimSun",10))
			altaBase.config(font=("SimSun",10))
			accionesMensajes.config(font=("SimSun",10))

		except:
			print("Error")

		finally:
			print("Controlador.py/Modelo.py/temas.py")

	def consolas_txt(self, tituloPrincipal, tituloReferencia, descripcionReferencia, altaBase, borrar, modificarRegistro, temasPrograma, accionesMensajes):

		try:
			tituloPrincipal.config(font=("Consolas",10))
			tituloReferencia.config(font=("Consolas",10))
			descripcionReferencia.config(font=("Consolas",10))
			borrar.config(font=("Consolas",10))
			modificarRegistro.config(font=("Consolas",10))
			temasPrograma.config(font=("Consolas",10))
			altaBase.config(font=("Consolas",10))
			accionesMensajes.config(font=("Consolas",10))

		except:
			print("Error")

		finally:
			print("Controlador.py/Modelo.py/temas.py")	

	def calibri_txt(self, tituloPrincipal, tituloReferencia, descripcionReferencia, altaBase, borrar, modificarRegistro, temasPrograma, accionesMensajes):

		try:
			tituloPrincipal.config(font=("Calibri",10))
			tituloReferencia.config(font=("Calibri",10))
			descripcionReferencia.config(font=("Calibri",10))
			borrar.config(font=("Calibri",10))
			modificarRegistro.config(font=("Calibri",10))
			temasPrograma.config(font=("Calibri",10))
			altaBase.config(font=("Calibri",10))
			accionesMensajes.config(font=("Calibri",10))

		except:
			print("Error")

		finally:
			print("Controlador.py/Modelo.py/temas.py")
		





















