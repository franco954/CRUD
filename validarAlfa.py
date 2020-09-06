

"""
AUTOR: Franco Alejandro Nuñez
Ultima modificacion: 06/09


Modulo: validarAlfa.py


Modulo que es llamado cada vez que se realicen acciones de insertar o actualizar registros. Realiza la validacion alfanumerica de los mismos.

"""


# importo expresiones regulares
import re



class validacion:

	# metodo validar
	def validar(self, filas):

		try:
			verificar = re.compile("^[A-Za-z]+(?:[ _-][A-Za-z]+)*$")
			if re.match(verificar, filas):
				return True
			else:
				return False
		except:
			print("Validacion erronea")
		finally:
			print("Controlador.py/Modelo.py/validarAlfa.py")