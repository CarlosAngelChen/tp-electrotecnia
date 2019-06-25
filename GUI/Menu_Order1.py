import tkinter as tk

import Config
from UserInput import userinput, filtro, modo, ejex, ejey, senhal, senhalparams, orden


class Orden1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#c0c0c0')

        self.controller = controller
        self.parent = parent

        self.titulo = tk.Label(
            self,
            text="Configure su circuito:",
            font=Config.VERY_LARGE_FONT,
            bg='#87cefa'

        )
        self.titulo.grid(row=0, column=0, sticky='nswe', columnspan=8)

        self.vacio = tk.Label(
            self,
            bg='#c0c0c0'
        )
        self.vacio.grid(row=1)

        self.vacio2 = tk.Label(
            self,
            bg='#c0c0c0'
        )
        self.vacio2.grid(column=7, padx=50)




        self.etiquetas = [tk.Label(self, text='Orden del Filtro', font=Config.SMALL_FONT, bg='#c0c0c0'),
                          tk.Label(self, text='Tipo de Filtro', font=Config.SMALL_FONT, bg='#c0c0c0'),
                          tk.Label(self, text='Tipo de Grafico', font=Config.SMALL_FONT, bg='#c0c0c0'),
                          tk.Label(self, text='Ejes Bode', font=Config.SMALL_FONT, bg='#c0c0c0'),
                          tk.Label(self, text='Tipo de senal', font=Config.SMALL_FONT, bg='#c0c0c0')]

        self.show_etiquetas()

        self.orden = tk.IntVar(value=99)

        self.circuloorden1 = tk.Radiobutton(
            self,
            height=5,
            text='Filtro de primer Orden',
            value=0,
            variable=self.orden,
            command=self.assign_var_orden,
            bg='#c0c0c0'
        )
        self.circuloorden1.grid(row=3, column=0)

        self.circuloorden2 = tk.Radiobutton(
            self,
            height=5,
            text='Filtro de segundo Orden',
            value=1,
            variable=self.orden,
            command=self.assign_var_orden,
            bg='#c0c0c0'
        )
        self.circuloorden2.grid(row=4, column=0)

        self.modofiltro = tk.IntVar(value=99)

        self.circuloalto = tk.Radiobutton(
            self,
            height=5,
            text='Pasa Alto',
            value=0,
            variable=self.modofiltro,
            command=self.asign_var_filtro,
            background='#c0c0c0',
            state=tk.DISABLED
        )
        self.circuloalto.grid(row=3, column=1)

        self.circulobajo = tk.Radiobutton(
            self,
            height=5,
            text='Pasa Bajo',
            value=1,
            variable=self.modofiltro,
            command=self.asign_var_filtro,
            background='#c0c0c0',
            state=tk.DISABLED
        )
        self.circulobajo.grid(row=4, column=1)

        self.circulotodo = tk.Radiobutton(
            self,
            height=5,
            text='Pasa Todo',
            value=2,
            variable=self.modofiltro,
            command=self.asign_var_filtro,
            background='#c0c0c0',
            state=tk.DISABLED
        )
        self.circulotodo.grid(row=5, column=1)

        self.circulobanda = tk.Radiobutton(
            self,
            height=5,
            text='Pasa banda',
            value=3,
            variable=self.modofiltro,
            command=self.asign_var_filtro,
            background='#c0c0c0',
            state=tk.DISABLED
        )
        self.circulobanda.grid(row=6, column=1)

        self.circulonotch = tk.Radiobutton(
            self,
            height=5,
            text='Pasa Notch',
            value=4,
            variable=self.modofiltro,
            command=self.asign_var_filtro,
            background='#c0c0c0',
            state=tk.DISABLED
        )
        self.circulonotch.grid(row=7, column=1)

        self.modografico = tk.IntVar(value=99)

        self.circuloBode = tk.Radiobutton(
            self,
            height=5,
            text='Gráfico Bode',
            value=0,
            variable=self.modografico,
            command=self.asign_var_grafico,
            background='#c0c0c0',
            state=tk.DISABLED
        )
        self.circuloBode.grid(row=3, column=2)

        self.circuloSenhal = tk.Radiobutton(
            self,
            height=5,
            text='Gráfico Salida',
            value=1,
            variable=self.modografico,
            command=self.asign_var_grafico,
            background='#c0c0c0',
            state=tk.DISABLED
        )
        self.circuloSenhal.grid(row=4, column=2)

        self.modoejex = tk.IntVar(value=99)
        self.modoejey = tk.IntVar(value=99)

        self.circuloHertz = tk.Radiobutton(
            self,
            height=5,
            text='Bode en Hertz',
            value=0,
            variable=self.modoejex,
            command=self.asign_var_ejex,
            background='#c0c0c0',
            state=tk.DISABLED
        )
        self.circuloHertz.grid(row=3, column=3)

        self.circuloRadianes = tk.Radiobutton(
            self,
            height=5,
            text='Bode en Radianes',
            value=1,
            variable=self.modoejex,
            command=self.asign_var_ejex,
            background='#c0c0c0',
            state=tk.DISABLED
        )
        self.circuloRadianes.grid(row=4, column=3)

        self.circuloDB = tk.Radiobutton(
            self,
            height=5,
            text='Bode en DB',
            value=0,
            variable=self.modoejey,
            command=self.asign_var_ejey,
            background='#c0c0c0',
            state=tk.DISABLED
        )
        self.circuloDB.grid(row=5, column=3)

        self.circuloB = tk.Radiobutton(
            self,
            height=5,
            text='Bode en B',
            value=1,
            variable=self.modoejey,
            command=self.asign_var_ejey,
            background='#c0c0c0',
            state=tk.DISABLED
        )
        self.circuloB.grid(row=6, column=3)

        self.tipodesenhal = tk.IntVar(value=99)

        self.circulosenoide = tk.Radiobutton(
            self,
            height=5,
            text='Senoide',
            value=0,
            variable=self.tipodesenhal,
            command=self.asign_var_senhal,
            state=tk.DISABLED,
            background='#c0c0c0'
        )
        self.circulosenoide.grid(row=3, column=4)

        self.circulopulso = tk.Radiobutton(
            self,
            height=5,
            text='Pulso',
            value=1,
            variable=self.tipodesenhal,
            command=self.asign_var_senhal,
            state=tk.DISABLED,
            background='#c0c0c0'
        )
        self.circulopulso.grid(row=4, column=4)

        self.circulopulsoper = tk.Radiobutton(
            self,
            height=5,
            text='Pulso Periodico',
            value=2,
            variable=self.tipodesenhal,
            command=self.asign_var_senhal,
            state=tk.DISABLED,
            background='#c0c0c0'
        )
        self.circulopulsoper.grid(row=5, column=4)

        self.labelpolo = tk.Label(
            self,
            text='Ingrese el polo del filtro:',
            bg='#c0c0c0',
            state=tk.DISABLED

        )
        self.labelpolo.grid(row=3, column=5)

        self.labelganancia = tk.Label(
            self,
            text='Ingrese la ganancia del filtro:',
            bg='#c0c0c0',
            state=tk.DISABLED
        )
        self.labelganancia.grid(row=4, column=5)

        self.inputpolo = tk.StringVar()
        self.inputcero = tk.StringVar()

        self.entrypolo = tk.Entry(
            self,
            textvariable=self.inputpolo,
            background='#c0c0c0',
            state=tk.DISABLED
        )
        self.entrypolo.grid(row=3, column=6)

        self.entryganancia = tk.Entry(
            self,
            textvariable=self.inputcero,
            background='#c0c0c0',
            state=tk.DISABLED
        )
        self.entryganancia.grid(row=4, column=6)

        self.labelamp = tk.Label(
            self,
            text='Ingrese amplitud de la señal',
            bg='#c0c0c0',
            state=tk.DISABLED
        )
        self.labelamp.grid(row=7, column=5)

        self.inputsenoide = tk.StringVar()

        self.entryamp = tk.Entry(
            self,
            textvariable=self.inputsenoide,
            background='#c0c0c0',
            state=tk.DISABLED
        )
        self.entryamp.grid(row=7, column=6, pady=25)

        self.labelfrecuencia = tk.Label(
            self,
            text='Ingrese la frecuencia de la señal:',
            bg='#c0c0c0',
            state=tk.DISABLED
        )
        self.labelfrecuencia.grid(row=8, column=5, pady=25)

        self.inputfrecuencia = tk.StringVar()

        self.entryfrecuencia = tk.Entry(
            self,
            textvariable=self.inputfrecuencia,
            background='#c0c0c0',
            state=tk.DISABLED
        )

        self.entryfrecuencia.grid(row=8, column=6)

        self.labeldc = tk.Label(
            self,
            text='Ingrese el valor del Dutycycle del pulso:',
            bg='#c0c0c0',
            state=tk.DISABLED
        )
        self.labeldc.grid(row=9, column=5, pady=25)

        self.inputdc = tk.StringVar()

        self.entrydc = tk.Entry(
            self,
            textvariable=self.inputdc,
            bg='#c0c0c0',
            state=tk.DISABLED
        )
        self.entrydc.grid(row=9, column=6, pady=25)

        self.labelw0 = tk.Label(
            self,
            text='Ingrese el valor de w0:',
            bg='#c0c0c0',
            state=tk.DISABLED
        )

        self.labelw0.grid(row=5, column=5)

        self.inputw0 = tk.StringVar()

        self.entryw0 = tk.Entry(
            self,
            textvariable=self.inputw0,
            bg='#c0c0c0',
            state=tk.DISABLED
        )
        self.entryw0.grid(row=5, column=6)

        self.labelE = tk.Label(
            self,
            text='Ingrese el valor de e:',
            bg='#c0c0c0',
            state=tk.DISABLED

        )
        self.labelE.grid(row=6, column=5)

        self.inputE = tk.StringVar()

        self.entryE = tk.Entry(
            self,
            textvariable=self.inputE,
            bg='#c0c0c0',
            state=tk.DISABLED
        )
        self.entryE.grid(row=6, column=6)

        self.continuar = tk.Button(
            self,
            text="Continuar",
            font=Config.SMALL_FONT,
            background="#c0c0c0",
            command=self.continuar
        )
        self.continuar.grid(row=10, column=6, pady=25)

    def assign_var_orden(self):
        orden['orden1'] = 0
        orden['oprden2'] = 0

        if not self.orden.get():
            self.TurnOnEntry([self.entrypolo, self.entryganancia], [self.labelpolo, self.labelganancia])
            self.TurnOnButton([self.circuloalto, self.circulobajo, self.circulotodo])

            self.TurnOffButton([self.circulobanda, self.circulonotch])
            self.TurnOffEntry([self.entryw0, self.entryE], [self.labelw0, self.labelE])

            orden['orden1'] = 1
        else:
            self.TurnOnEntry([self.entryganancia, self.entryw0, self.entryE], [self.labelganancia, self.labelw0, self.labelE])
            self.TurnOffEntry([self.entrypolo], [self.labelpolo])

            self.TurnOnButton([self.circuloalto,self.circulobajo, self.circulotodo, self.circulobanda, self.circulonotch])

            orden['orden2'] = 1



    #este método escribe en userinput que tipo de filtro se pide
    def asign_var_filtro(self):
        self.TurnOnButton([self.circuloBode, self.circuloSenhal])

        filtro['alto'] = 0
        filtro['bajo'] = 0
        filtro['todo'] = 0

        if not self.modofiltro.get():
            filtro['alto'] = 1
        elif self.modofiltro.get() == 1:
            filtro['bajo'] = 1
        elif self.modofiltro.get() == 2:
            filtro['todo'] = 1
        elif self.modofiltro.get() == 3:
            filtro["banda"] = 1
        else:
            filtro["notch"] = 1

    def asign_var_grafico(self):
        modo['Bode'] = 0
        modo['Salida'] = 0

        if not self.modografico.get():

            modo['Bode'] = 1
            #Activa los botones
            self.TurnOnButton([self.circuloHertz, self.circuloRadianes, self.circuloDB, self.circuloB])

            #desactiva botones que no se usan
            self.TurnOffButton([self.circulosenoide, self.circulopulso, self.circulosenoide, self.circulopulso, self.circulopulsoper])

        else:
            modo['Salida'] = 1
            #Desactiva los botones
            self.TurnOnButton([self.circulosenoide, self.circulopulso, self.circulopulsoper])

            self.TurnOffButton([self.circuloHertz, self.circuloRadianes, self.circuloDB, self.circuloB])

    def asign_var_ejex(self):

        ejex['Hertz'] = 0
        ejex['Radianes'] = 0

        if not self.modoejex.get():
            ejex['Hertz'] = 1
        else:
            ejex['Radianes'] = 1

    def asign_var_ejey(self):

        ejey['Decibeles'] = 0
        ejey['Beles'] = 0

        if not self.modoejey.get():
            ejey['Decibeles'] = 1
        else:
            ejey['Beles'] = 1

    def asign_var_senhal(self):
        senhal['senoide'] = 0
        senhal['pulso'] = 0
        senhal['pulsoper'] = 0

        self.labelamp.configure(state=tk.NORMAL)
        self.entryamp.configure(state=tk.NORMAL)
        self.labelfrecuencia.configure(state=tk.NORMAL)
        self.entryfrecuencia.configure(state=tk.NORMAL)

        if not self.tipodesenhal.get():
            self.TurnOnEntry([self.entryamp, self.entryfrecuencia], [self.labelamp, self.labelfrecuencia])

            self.TurnOffEntry([self.entrydc], [self.labeldc])
            senhal['senoide'] = 1
        elif self.tipodesenhal.get() == 1:
            self.TurnOnEntry([self.entryamp], [self.labelamp])
            self.TurnOffEntry([self.entryfrecuencia, self.entrydc], [self.labelfrecuencia, self.labeldc])

            senhal['pulso'] = 1
        else:
            self.TurnOnEntry([self.entryamp, self.entryfrecuencia, self.entrydc], [self.labelamp, self.labelfrecuencia, self.labeldc])
            senhal['pulsoper'] = 1

    #muestro siguiente pantalla y asigno el valor de la frecuencia del polo y/o cero, falta agregar que apsa si me mete algo que no sea un numero o vacio
    def continuar(self):
        if self.entrypolo.get():
            userinput['f0'] = float(self.entrypolo.get())

        if self.entryganancia.get():
            userinput['c'] = float(self.entryganancia.get())

        if self.entryfrecuencia.get():
            senhalparams['frecuencia'] = float(self.entryfrecuencia.get())

        if self.entryamp.get():
            senhalparams['Amplitud'] = float(self.entryamp.get())

        if self.entrydc.get():
            senhalparams['DutyCicle'] = float(self.entrydc.get())

        if self.entryw0.get():
            userinput['wo'] = float(self.entryw0.get())

        if self.entryE.get():
            userinput['e'] = float(self.entryE.get())

        from Menu_Grafico import Grafico

        self.controller.showFrame(Grafico)

    def show_etiquetas(self):
        contador = 0
        for L in self.etiquetas:
            L.grid(row=2, column=contador)
            contador += 1

    def TurnOffAllEntries(self):
        self.labelpolo.configure(state=tk.DISABLED)
        self.labelganancia.configure(state=tk.DISABLED)
        self.entrypolo.configure(state=tk.DISABLED)
        self.entryganancia.configure(state=tk.DISABLED)
        self.labelamp.configure(state=tk.DISABLED)
        self.entryamp.configure(state=tk.DISABLED)
        self.labeldc.configure(state=tk.DISABLED)
        self.entrydc.configure(state=tk.DISABLED)
        self.labelE.configure(state=tk.DISABLED)
        self.entryE.configure(state=tk.DISABLED)
        self.labelfrecuencia.configure(state=tk.DISABLED)
        self.entryfrecuencia.configure(state=tk.DISABLED)
        self.labelw0.configure(state=tk.DISABLED)
        self.entryw0.configure(state=tk.DISABLED)

    def TurnOffEntry(self, entry_lst, label_lst):
        for entry in entry_lst:
            entry.configure(state=tk.DISABLED)

        for label in label_lst:
            label.configure(state=tk.DISABLED)


    def TurnOnAllEntries(self):
        self.labelpolo.configure(state=tk.NORMAL)
        self.labelganancia.configure(state=tk.NORMAL)
        self.entrypolo.configure(state=tk.NORMAL)
        self.entryganancia.configure(state=tk.NORMAL)
        self.labelamp.configure(state=tk.NORMAL)
        self.entryamp.configure(state=tk.NORMAL)
        self.labeldc.configure(state=tk.NORMAL)
        self.entrydc.configure(state=tk.NORMAL)
        self.labelE.configure(state=tk.NORMAL)
        self.entryE.configure(state=tk.NORMAL)
        self.labelfrecuencia.configure(state=tk.NORMAL)
        self.entryfrecuencia.configure(state=tk.NORMAL)
        self.labelw0.configure(state=tk.NORMAL)
        self.entryw0.configure(state=tk.NORMAL)

    def TurnOnEntry(self, entry_lst, label_lst):
        for entry in entry_lst:
            entry.configure(state=tk.NORMAL)

        for label in label_lst:
            label.configure(state=tk.NORMAL)

    def TurnOnButton(self, lst):
        for button in lst:
            button.configure(state=tk.NORMAL)

    def TurnOffButton(self, lst):
        for button in lst:
            button.configure(state=tk.DISABLED)

    def focus(self):
        pass
