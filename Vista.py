


#importo libreria
from tkinter import * 
from tkinter import ttk

 

class registros:

    try:

        #vista principal de la app
        def imagenPrincipal(self, ):

            root = Tk()
            root.title("RegistrosTP")
            root.config(relief=RIDGE, border=5)
            self.tituloPrincipal = Label(root, text=" Ingrese sus datos ", width=114, bg="light blue", font=("Calibri",10))
            self.tituloPrincipal.grid(row=0, column=0)

            self.tituloReferencia = Label(root, text="Titulo: ", font=("Calibri",10))
            self.tituloReferencia.grid(row=2, column=0, sticky="w")

            self.accionesMensajes = Label(root, text="", fg="red", font=("Calibri",10))
            self.accionesMensajes.grid(row=4, column=0, sticky="NSEW")

            self.descripcionReferencia = Label(root, text="Descripcion: ", font=("Calibri",10))
            self.descripcionReferencia.grid(row=3, column=0, sticky="w")

            self.varOpcion = IntVar()

            self.varOpcion_txt = IntVar()
                        
            self.a_val = StringVar()

            self.b_val = StringVar() 
                        
            self.tituloIngreso = Entry(root, textvariable = self.a_val )
            self.tituloIngreso.grid(row=2, column=0)
            self.descripcionIngreso = Entry(root, textvariable = self.b_val)
            self.descripcionIngreso.grid(row=3, column=0)

            self.pantallaPrincipal = ttk.Treeview(root, height=5, columns=("#0","#1","#2"))
            self.pantallaPrincipal.grid(row=5, column=0)
            self.pantallaPrincipal.heading("#0", text="ID", anchor=CENTER)
            self.pantallaPrincipal.heading("#1", text="Titulos", anchor=CENTER)
            self.pantallaPrincipal.heading("#2", text="Descripcion", anchor=CENTER)

            self.barraDesplazamiento = Scrollbar(root, command=self.pantallaPrincipal.yview)
            self.barraDesplazamiento.grid(row=5, column=1, sticky=NSEW)

            #botones que llaman a distintos metodos del controlador una vez pulsados

            self.altaBase = Button(root, text="Alta", border=5, command= lambda: self.registroAltas(self.a_val, self.b_val, self.accionesMensajes, self.pantallaPrincipal), bg="light blue", font=("Calibri",10))
            self.altaBase.grid(row=7, column=0, sticky=S + E)
            self.registroConsultas(self.pantallaPrincipal,)

            self.salirBase = Button(root, text="X", border=2, bg="black", fg="white", command= lambda: self.salirAplicacion(root))
            self.salirBase.grid(row=0, column=0, sticky=N + E)

            self.borrar = Button(root, text="Borrar", border=5, bg="light blue",command= lambda: self.registroBorrar(self.pantallaPrincipal, self.accionesMensajes), font=("Calibri",10))
            self.borrar.grid(row=7, column=0, sticky= S + W)

            self.modificarRegistro = Button(root, text="Actualizar", border=5,command= lambda: self.registroActualizar(self.pantallaPrincipal, self.accionesMensajes, self.a_val, self.b_val), bg="light blue", font=("Calibri",10))
            self.modificarRegistro.grid(row=7, column=0, sticky=S)

            self.temasPrograma = Button(root, text="Cambiar tematica",border=5, relief="ridge", command= lambda: self.topLevel(self.varOpcion, self.varOpcion_txt), width=114, bg="light blue", font=("Calibri",10))
            self.temasPrograma.grid(row=8, column=0)

            self.pantallaPrincipal.config(yscrollcommand=self.barraDesplazamiento.set)

            root.mainloop()
    except:
        print("Error al cargar la vista")
    finally:
        print("Controlador.py/Vista.py")







