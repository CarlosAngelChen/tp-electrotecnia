import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def validation(w0, wz):
    if wz < w0:
        return 1
    else:
        print("Error, wz < w0")
        print("Ingrese los datos de nuevo")
        #pa_notch()
        return 0

def pa_notch():
    k = float(input())
    #f1 = float(input()) #input frec usuario
    #fz = float(input()) #input frec Z
    ethaZ = float(input())
    etha = float(input())

    wz = float(input())
    w0 = float(input())

    if validation(w0, wz):
        ceros = [k/(wz**2), k*ethaZ/wz, k]
        polos = [1/(w0**2), 2*etha/w0, 1]

        sys = signal.TransferFunction(ceros, polos)

        w, dB, phase = signal.bode(sys)

        f = w/np.pi

        return w, f, dB, phase, sys, w0

    else:
        print("Error, wz < w0")
        return 0

def pa_notch_plot(w, f, dB, phase):
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

    return 0

#w, f, dB, phase, sys, w0 = pa_notch()
#pa_notch_plot(w, f, dB, phase)