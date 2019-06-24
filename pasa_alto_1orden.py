import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from scipy import signal
#%matplotlib qt

#   PRUEBA  #
#Defino mi sistema de funcion de transferencia
#   1 argumento: ceros
#   2 argumento: polos
#   dentro del corchete son polinomios de s: ejem s^2 + s + 1 <=> [1,1,1]

#sys = signal.TransferFunction([1], [0, 1, 1])

#cuando grafico en bode, me devuelve 3 argumentos
#   1 argumento: w, un array en frecuencia
#   2 argumento: mag, magnitud (dB)
#   3 argumento: phase, fase

#w, dB, fase = signal.bode(sys)

#   PRUEBA  #


def pa_1():

    k =  float(input())
    f1 = float(input()) #input de frecuencia del usuario
    w0 = 2 * np.pi * f1

    ceros = [k, 0]
    polos = [0, 1/w0, 1]
    sys = signal.TransferFunction(ceros, polos)

    w, dB, phase = signal.bode(sys)

    f = w/(2*np.pi)

#duda: el K que ingresan, lo tengo que multiplicar por w0?

    return w, f, dB, phase, sys, w0

def pa_1_plot(w, f, dB, phase):
    fig, ((ax1), (ax2), ax3) = plt.subplots(3, 1)

    ax1.semilogx(f, dB)
    ax1.set_xlabel('Hz')
    ax1.set_ylabel('dB')
    ax1.set_title('Base 10')
    ax1.grid(True)

    ax2.semilogx(w, dB)
    ax2.set_xlabel('rad/s')
    ax2.set_ylabel('dB')
    ax2.set_title('Base 10')
    ax2.grid(True)

    ax3.semilogx(w, phase)
    ax3.set_xlabel('rad/s')
    ax3.set_ylabel('Grados')
    ax3.grid(True)

    fig.tight_layout()
    plt.show()

#w, f, dB, phase, sys, w0 = pa_1()
#pa_1_plot(w, f, dB, phase)