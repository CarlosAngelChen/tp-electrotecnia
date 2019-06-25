import tkinter as tk
import Config


class MenuPrincipal(tk.Frame):
    def __init__(self, parent, controller):
        # parent representa el Frame principal del programa, tenemos que indicarle cuando Menu principal será dibujado

        # controller lo utilizamos cuando necesitamos que el controlador principal del programa haga algo

        # llamamos al constructor, hay herencia de la clase Frame, es decir Menu principal es un Frame al que le
        # agregamos widgets como atributos y luego la clase UI lo utiliza para dibujar en pantalla
        tk.Frame.__init__(self, parent,  bg='#42f498')

        self.controller = controller
        self.parent = parent

        self.titulo = tk.Label(
            self,
            text="Interfaz gráfica configurable: filtros de primer y segundo orden",
            font=Config.SMALL_FONT,
            bg='#42f498'


        )

        self.titulo.pack(pady = 5)

        self.botoncomenzar = tk.Button(
            self,
            height=3,
            width=40,
            text="Comenzar",
            font=Config.SMALL_FONT,
            command=self.comenzar,
        )

        self.botoncomenzar.pack(pady=200)

    def comenzar(self):
        from Menu_Order1 import Orden1
        self.controller.showFrame(Orden1)

    def focus(self):
        pass

