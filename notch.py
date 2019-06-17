import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def notch():
    k = float(input())
    w0 = float(input())
    etha = float(input())

    ceros = [k/(w0**2), 0, k]
    polos = [1/(w0**2), 2*etha/w0, 1]

    sys = signal.TransferFunction(ceros, polos)

    w, dB, phase = signal.bode(sys)

    f = w/np.pi

    return w, f, dB, phase

def notch_plot(w, f, dB, phase):
    fig, ((ax1, ax3), (ax2, ax4)) = plt.subplots(2, 2)

    ax1.semilogx(f, dB)
    ax1.set_xlabel('Hz')
    ax1.set_ylabel('dB')
    ax1.set_title('Base 10')
    ax1.grid(True)

    ax2.semilogx(w, dB)
    ax2.set_xlabel('rad/s')
    ax2.set_ylabel('dB')
    ax2.set_title('Base 2')
    ax2.grid(True)

    ax3.semilogx(f, dB, basex=2)
    ax3.set_xlabel('Hz')
    ax3.set_ylabel('dB')
    ax3.set_title('Base 2')
    ax3.grid(True)

    ax4.semilogx(w, dB, basex=2)
    ax4.set_xlabel('rad/s')
    ax4.set_ylabel('dB')
    ax4.set_title('Base 2')
    ax4.grid(True)

    fig.tight_layout()
    plt.show()

    return 0

#w, f, dB, phase = notch()
#notch_plot(w, f, dB, phase)