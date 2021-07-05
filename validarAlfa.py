


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