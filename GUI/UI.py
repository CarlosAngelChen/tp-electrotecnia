import tkinter as tk
from tkinter import *

from Main_Menu import MenuPrincipal
from Menu_Order1 import Orden1
from Menu_Grafico import Grafico

menus = [MenuPrincipal,
         Orden1,
         Grafico]

startFrame = MenuPrincipal


class UI(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.protocol('WM_DELETE_WINDOW', self.exitFunction)
        self.title("Ejemplo gui 01")

        #self.resizable(width=False, height=False)
        #self.minsize(width=700, height=500)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand = True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in menus:
            # cargamos a la memoria la información de todos los frames
            self.frames[F] = F(self.container, self)
            self.frames[F].grid_propagate(True)
            self.frames[F].grid(row=0, column=0, sticky=E + W + N + S)

            # comenzamos la aplicación en startFrame que es la variable que nos indica en que menu empezar
        self.showFrame(startFrame)

    def showFrame(self, frame):
        # este método controla que menues se estan mostrando
        self.frames[frame].focus()
        frame = self.frames[frame]
        frame.tkraise()
        self.frame = frame

    def getCurrentFrame(self):
        # obtener el frame actual
        return self.frame

    def run(self):
        # comenzar el programa
        # el loop lo controla tkinter, llamando "mainloop" se lo entregamos
        self.mainloop()

    def exitFunction(self):
        # funciones de tkinter que administran que debe suceder cuando salimos del programa
        self.quit()
        self.destroy()


if __name__ == "__main__":
    UI().run()


