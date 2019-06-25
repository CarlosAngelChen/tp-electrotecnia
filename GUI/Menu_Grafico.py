import tkinter as tk
import Config
from tkinter import *

from UserInput import *

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from numpy import pi

#parece qeu pulso periodico no anda
#Este menu es el correspondiente al grafico de Bode
class Grafico(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#42f498')

        self.controller = controller
        self.parent = parent

        self.graph = tk.Canvas(self)

        self.fig, self.ax1 = plt.subplots()

        self.dataPlot = FigureCanvasTkAgg(self.fig, master=self.graph)
        self.nav = NavigationToolbar2Tk(self.dataPlot, self.graph)
        self.dataPlot.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.dataPlot._tkcanvas.pack(side=tk.BOTTOM, fill=tk.X, expand=1)

        self.graph.pack(side=tk.TOP, expand=1, fill=tk.BOTH)

        self.backButton = tk.Button(
            self,
            height=2,
            width=50,
            text="Volver",
            font=Config.SMALL_FONT,
            background="#cfffd5",
            command=self.goback

        )
        self.backButton.pack(side=tk.TOP, fill=tk.BOTH)

    def focus(self):
        self.ax1.clear()

        self.ax1.minorticks_on()
        self.ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
        self.ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')


        #Aca decide qeu dibujar, puede dibujar orden 1 o 2, luego alto, bajo, tod, banda o notch, y luego en rads, hertz dbs o bs
        if orden['orden1']:
            if filtro['alto']:
                self.plotPasaAlto1Orden()
            elif filtro['bajo']:
                self.plotPasaBajo1Orden()
            else:
                self.plotPasaTodo1Orden()
        elif orden['orden2']:
            if filtro['alto']:
                self.plotPasaAlto2Orden()
            elif filtro['bajo']:
                self.plotPasaBajo2Orden()
            elif filtro['todo']:
                self.plotPasaTodo2Orden()
            elif filtro['banda']:
                self.plotPasaBanda2Orden()
            else:
                pass

        self.dataPlot.draw()


    def goback(self):
        from Menu_Order1 import Orden1
        self.controller.showFrame(Orden1)



    #en esta función esta lo qeu dibujo ya sea el bode o el grafico de la respuesta
    #decide de que tipo de garfico se tratasegun lo qeu dice userinput y luego lo grafica
    def plotPasaAlto1Orden(self):
        ganancia = userinput['c']
        f0 = userinput['f0']
        w0 = 2 * pi * f0

        k = ganancia/w0
        ceros = [k, 0]
        polos = [0, 1/w0, 1]

        sys2 = signal.TransferFunction(ceros, polos)

        w, dB, phase = signal.bode(sys2)
        f = w/(2 * pi)

        if modo['Bode']:
            self.grafBode(f, dB, w)
        else:
            self.grafSignal(sys2, w0)


    def plotPasaBajo1Orden(self):
        ganancia = userinput['c']
        f0 = userinput['f0']
        w0 = 2 * pi * f0

        k = ganancia
        ceros = [k]
        polos = [0, 1/w0, 1]

        sys2 = signal.TransferFunction(ceros, polos)

        w, dB, phase = signal.bode(sys2)
        f = w / (2 * pi)

        if modo['Bode']:
            self.grafBode(f, dB, w)
        else:
            self.grafSignal(sys2, w0)


    def plotPasaTodo1Orden(self):
        ganancia = userinput['c']
        f0 = userinput['f0']
        k = ganancia

        w0 = f0 * 2 * pi
        ceros = [k / w0, -k]
        polos = [0, 1 / w0, 1]

        sys2 = signal.TransferFunction(ceros, polos)

        w, dB, phase = signal.bode(sys2)
        f = w / (2 * pi)

        if modo['Bode']:
            self.grafBode(f, dB, w)
        else:
            self.grafSignal(sys2, w0)

    def plotPasaAlto2Orden(self):
        ganancia = userinput['c']
        e = userinput['e']
        w0 = userinput['wo']

        k = ganancia/(w0*w0)

        ceros = [k, 0, 0]
        polos = [1/(w0*w0), (2*e)/w0, 1]

        sys2 = signal.TransferFunction(ceros, polos)

        w, dB, phase = signal.bode(sys2, n=500)
        f = w/np.pi

        print(userinput["c"])
        print(userinput["e"])
        print(userinput["wo"])
        if modo['Bode']:
            self.grafBode(f, dB, w)
        else:
            self.grafSignal(sys2, w0)



    def plotPasaBajo2Orden(self):
        ganancia = userinput['c']
        w0 = userinput['wo']
        e = userinput['e']

        k = ganancia

        ceros = [k]
        polos = [1/(w0*w0), 2*e/w0, 1]

        sys2 = signal.lti(ceros, polos)

        w, dB, phase = signal.bode(sys2, n=500)

        f = w/np.pi

        if modo['Bode']:
            self.grafBode(f, dB, w)
        else:
            self.grafSignal(sys2, w0)


    def plotPasaTodo2Orden(self):
        ganancia = userinput['c']
        w0 = userinput['wo']
        e = userinput['e']

        k = ganancia

        ceros = [k/(w0**2), -2*k*e/w0, k]
        polos = [1 / (w0 * w0), 2 * e / w0, 1]

        sys2 = signal.TransferFunction(ceros, polos)

        w, dB, phase = signal.bode(sys2)

        f = w / np.pi

        if modo['Bode']:
            self.grafBode(f, dB, w)
        else:
            self.grafSignal(sys2, w0)


    def plotPasaBanda2Orden(self):
        ganancia = userinput['c']
        w0 = userinput['wo']
        e = userinput['e']

        k = ganancia*2*e/w0
        ceros = [k, 0]
        polos = [1/(w0**2), 2*e/w0, 1]

        sys2 = signal.TransferFunction(ceros, polos)

        w, dB, phase = signal.bode(sys2, w=None, n=500)

        f = w/(2*np.pi)

        if modo['Bode']:
            self.grafBode(f, dB, w)
        else:
            self.grafSignal(sys2, w0)

    def plotPasaNotch2Orden(self):
        ganancia = userinput['c']
        w0 = userinput['wo']
        e = userinput['e']

        k = ganancia
        ceros = [k / (w0 ** 2), 0, k]
        polos = [1 / (w0 ** 2), 2 * e / w0, 1]

        sys2 = signal.lti(ceros, polos)

        w, dB, phase = signal.bode(sys2, n=500)

        f = w/(2*np.pi)

        if modo['Notch']:
            self.grafBode(f, dB, w)
        else:
            self.grafSignal(sys2, w0)

    def grafBode(self, f, dB, w):
        if modo['Bode']:
            if ejex['Hertz'] and ejey['Decibeles']:
                self.ax1.semilogx(f, dB)
                self.ax1.set_xlabel('Hz')
                self.ax1.set_ylabel('dB')
                self.ax1.set_title('Base 10')
                self.ax1.grid(True)

            elif ejex['Radianes'] and ejey['Decibeles']:
                self.ax1.semilogx(w, dB)
                self.ax1.set_xlabel('rad/s')
                self.ax1.set_ylabel('B')
                self.ax1.set_title('Base 10')
                self.ax1.grid(True)

            elif ejex['Hertz'] and ejey['Beles']:
                self.ax1.semilogx(f, dB, basex=2)
                self.ax1.set_xlabel('Hz')
                self.ax1.set_ylabel('dB')
                self.ax1.set_title('Base 2')
                self.ax1.grid(True)

            elif ejex['Radianes'] and ejey['Beles']:
                self.ax1.semilogx(w, dB, basex=2)
                self.ax1.set_xlabel('rad/s')
                self.ax1.set_ylabel('B')
                self.ax1.set_title('Base 2')
                self.ax1.grid(True)

    def grafSignal(self, sys2, w0):
        if senhal['senoide']:
            amp = senhalparams['Amplitud']
            w1 = senhalparams['frecuencia']
            t = np.linspace(0, 5, 500)
            u = amp * np.sin(w1 * t)

            tout, y, x = signal.lsim(sys2, u, t)

            self.ax1.plot(tout, y)
            self.ax1.set_xlabel('seg')
            self.ax1.set_ylabel('A (ammplitud)')
            self.ax1.grid(True)

        elif senhal['pulso']:
            amp = senhalparams['Amplitud']
            t = np.linspace(0, 5 * (1 / w0), 5000)
            u = amp * (np.sign(t) + 1)

            tout, y, x = signal.lsim(sys2, u, t)

            self.ax1.plot(tout, y)
            self.ax1.set_xlabel('seg')
            self.ax1.set_ylabel('A (ammplitud)')
            self.ax1.grid(True)

        else:
            amp = senhalparams['Amplitud']
            duty = senhalparams['DutyCicle']
            f1 = senhalparams['frecuencia']
            w1 = f1 * 2 * np.pi
            t = np.linspace(0, 2, 500)
            u = amp * signal.square(2 * np.pi * w1 * t, duty)

            tout, y, x = signal.lsim(sys2, u, t)

            self.ax1.plot(tout, y)
            self.ax1.set_xlabel('seg')
            self.ax1.set_ylabel('A (ammplitud)')
            self.ax1.grid(True)