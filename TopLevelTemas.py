

"""
AUTOR: Franco Alejandro Nuñez
Ultima modificacion: 06/09


Modulo: TopLevelTemas


Modulo que despues del clickeo en su boton correspondiente, es llamado por el controlador para largar la vista emergente relacionado a la modificacion
de tematicas de la app
"""


# importo la libreria
from tkinter import *



# clase de la ventana
class topLevel:

	try:

		# metodo que lanza la vista y que dependiendo el valor de los parametros va a lanzar una invocacion
		def aparecerBg(self, varOpcion, varOpcion_txt, ):

			self.ventanaTematicas = Toplevel()
			self.ventanaTematicas.title("Temas")

			self.mensajePer = Label(self.ventanaTematicas, text="Personaliza la aplicacion")
			self.mensajePer.grid(row=0, column=0, columnspan=2)

			self.mensajeTema = Label(self.ventanaTematicas, text="Color")
			self.mensajeTema.grid(row=1, column=0)

			self.tema1Radio = Radiobutton(self.ventanaTematicas, bg="red", width=10, variable=self.varOpcion, value=1, command= lambda: self.temaOpcion(self.varOpcion))
			self.tema1Radio.grid(row=2, column=0)

			self.tema2Radio = Radiobutton(self.ventanaTematicas, bg="light blue", width=10, variable=self.varOpcion, value=2, command= lambda: self.temaOpcion(self.varOpcion))
			self.tema2Radio.grid(row=3, column=0)

			self.tema3Radio = Radiobutton(self.ventanaTematicas, bg="light green", width=10, variable=self.varOpcion, value=3, command=lambda: self.temaOpcion(self.varOpcion))
			self.tema3Radio.grid(row=4, column=0)

			self.tema4Radio = Radiobutton(self.ventanaTematicas, bg="#924e7d", width=10, variable=self.varOpcion, value=4, command=lambda: self.temaOpcion(self.varOpcion))
			self.tema4Radio.grid(row=5, column=0)

			self.mensajeTema = Label(self.ventanaTematicas, text="Fuente")
			self.mensajeTema.grid(row=1, column=1)

			self.tema1Radio = Radiobutton(self.ventanaTematicas, text="Perpetua", font=("Perpetua",10), width=10, variable=self.varOpcion_txt, value=1, command=lambda: self.temaOpcion_txt(self.varOpcion_txt))
			self.tema1Radio.grid(row=2, column=1)

			self.tema2Radio = Radiobutton(self.ventanaTematicas, text="SimSun", font=("SimSun",10), width=10, variable=self.varOpcion_txt, value=2, command=lambda: self.temaOpcion_txt(self.varOpcion_txt))
			self.tema2Radio.grid(row=3, column=1)

			self.tema3Radio = Radiobutton(self.ventanaTematicas, text="Consolas", font=("Consolas",10), width=10, variable=self.varOpcion_txt, value=3, command=lambda: self.temaOpcion_txt(self.varOpcion_txt))
			self.tema3Radio.grid(row=4, column=1)

			self.tema4Radio = Radiobutton(self.ventanaTematicas, text="Calibri", font=("Calibri",10), width=10, variable=self.varOpcion_txt, value=4, command=lambda: self.temaOpcion_txt(self.varOpcion_txt))
			self.tema4Radio.grid(row=5, column=1)

			self.ventanaTematicas.grab_set()
			self.ventanaTematicas.focus_set()
			self.ventanaTematicas.wait_window()
			self.ventanaTematicas.mainloop()

	except:
		print("Error al cargar el topLevel")

	finally:
		print("Controlador.py/ToplevelTemas")


