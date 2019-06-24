import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def pb_2():
    k = float(input())
    #f1 = float(input())
    etha = float(input())

    w0 = float(input())

    ceros = [k]
    polos = [1/(w0*w0), 2*etha/w0, 1]

    sys = signal.lti(ceros, polos)

    w, dB, phase = signal.bode(sys, n=500)

    f = w/np.pi

    return w, f, dB, phase, sys, w0, etha

def pb_2_plot(w, f, dB, phase):
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

w, f, dB, phase, sys, w0, etha = pb_2()
pb_2_plot(w, f, dB, phase)