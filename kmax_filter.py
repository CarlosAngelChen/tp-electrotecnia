import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def switcher(filt):
    if "pa1" == filt:
        kmax_pa1()

    elif "pa2" == filt:
        kmax_pa2()

    elif "paN" == filt:
        kmax_paNotch()

    elif "pb1" == filt:
        kmax_pb1()

    elif "pb2" == filt:
        kmax_pb2()

    elif "pbN" == filt:
        kmax_pbNotch()

    elif "pbd" == filt:
        kmax_pbd()

    elif "pt1" == filt:
        kmax_pt1()

    elif "pt2" == filt:
        kmax_pt2()

    elif "Notch" == filt:
        kmax_notch()

def kmax_pa2():
    g = float(input())
    f1 = float(input())
    etha = float(input())

    w0 = 2 * np.pi * f1

    k = g / (w0 *w0)

    w_max = w0 / np.sqrt(1 - 2*etha*etha)

    ceros = [k, 0, 0]
    polos = [1 / (w_max * w_max), 2 * etha / w0, 1]

    sys = signal.lti(ceros, polos)

    w, dB, phase = signal.bode(sys, n=500)

    f = w/np.pi

    fig, ((ax1), (ax2)) = plt.subplots(2)

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

    fig.tight_layout()
    plt.show()

    return 0

def kmax_pb2():
    k = float(input())
    f1 = float(input())
    etha = float(input())

    w0 = f1 *2*np.pi
    w_max = w0 * np.sqrt(1 - 2*etha*etha)

    ceros = [k]
    polos = [1/(w_max*w_max), 2*etha/w_max, 1]

    sys = signal.lti(ceros, polos)

    w, dB, phase = signal.bode(sys)

    f = w/np.pi

    fig, ((ax1), (ax2)) = plt.subplots(2)

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

    fig.tight_layout()
    plt.show()

    return 0

def kmax_pbd():
    g = float(input())
    f1 = float(input())
    etha = float(input())

    w0 = f1 * 2 * np.pi
    #de las ecuaciones, decia que w_max = w0
    k = 2 * etha *g/w0

    ceros = [k, 0]
    polos = [1/(w0**2), 2*etha/w0, 1]

    sys = signal.TransferFunction(ceros, polos)

    w, dB, phase = signal.bode(sys, w = None, n = 500)

    f = w/np.pi

    fig, ((ax1), (ax2)) = plt.subplots(2)

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

    fig.tight_layout()
    plt.show()

    return 0

def kmax_paNotch():

    def validation(w0, wz):
        if wz < w0:
            return 1
        else:
            print("Error, wz < w0")
            print("Ingrese los datos de nuevo")
            # pa_notch()
            return 0

    k = float(input())
    f1 = float(input()) #input frec usuario
    fz = float(input()) #input frec Z
    ethaZ = float(input())
    etha = float(input())

    wz = fz *2*np.pi
    w0 = f1*2*np.pi

    if validation(w0, wz):

        w_max = w0* np.sqrt( ( (wz/w0)**2 * (1 - 2*etha*etha) - 1) / ( (wz/w0)**2 + 2*etha*etha - 1 ) )

        ceros = [k/(wz**2), k*ethaZ/wz, k]
        polos = [1/(w_max**2), 2*etha/w_max, 1]

        sys = signal.lti(ceros, polos)

        w, dB, phase = signal.bode(sys, n =500)

        f = w/np.pi

        fig, ((ax1), (ax2)) = plt.subplots(2)

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

        fig.tight_layout()
        plt.show()

    else:
        print("Error, wz < w0")
        return 0

def kmax_pbNotch():

    def validation(w0, wz):
        if wz > w0:
            return 1
        else:
            print("Error, wz < w0")
            print("Ingrese los datos de nuevo")
            # pb_notch()
            return 0

    k = float(input())
    f1 = float(input())
    fz = float(input())
    ethaZ = float(input())
    etha = float(input())

    w0 = f1 *2*np.pi
    wz = fz *2*np.pi

    if validation(w0, wz):

        w_max = w0* np.sqrt( ( (wz/w0)**2 * (1 - 2*etha*etha) - 1) / ( (wz/w0)**2 + 2*etha*etha - 1 ) )

        ceros = [k/(wz**2), k*ethaZ/wz, k]
        polos = [1/(w_max**2), 2*etha/w_max, 1]

        sys = signal.lti(ceros, polos)

        w, dB, phase = signal.bode(sys, n=500)

        f = w/np.pi

        fig, ((ax1), (ax2)) = plt.subplots(2)

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

        fig.tight_layout()
        plt.show()

    else:
        print("Error, wz < w0")
        return 0

def kmax_pa1():
    #duda
    g =  float(input())
    f1 = float(input()) #input de frecuencia del usuario
    w0 = 2 * np.pi * f1
    k = g/w0
    ceros = [k, 0]
    polos = [0, 1/w0, 1]
    sys = signal.lti(ceros, polos)

    w, dB, phase = signal.bode(sys)


    fig, ((ax1), (ax2)) = plt.subplots(2)

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

    fig.tight_layout()
    plt.show()

    return 0

def kmax_pb1():
    k =  float(input())
    f1 = float(input())
    w0 = f1 *2*np.pi
    ceros = [k]
    polos = [0, 1/w0, 1]
    sys = signal.TransferFunction(ceros, polos)

    w, dB, phase = signal.bode(sys)
    f = w/(2*np.pi)

    fig, ((ax1), (ax2)) = plt.subplots(2)

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

    fig.tight_layout()
    plt.show()

    return 0

def kmax_pt1():
    k = float(input())
    f1 = float(input())

    w0 = f1*2*np.pi
    ceros = [k/w0, -k]
    polos = [0, 1/w0, 1]

    sys = signal.TransferFunction(ceros, polos)

    w, dB, phase = signal.bode(sys)
    f = w/(2*np.pi)

    fig, ((ax1), (ax2)) = plt.subplots(2)

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

    fig.tight_layout()
    plt.show()

    return 0

def kmax_pt2():
    k = float(input())
    f1 = float(input())
    etha = float(input())

    w0 = f1*2*np.pi
    ceros = [k/(w0**2), -2*k*etha/w0, k]
    polos = [1/(w0**2), 2*etha/w0, 1]

    sys = signal.TransferFunction(ceros, polos)

    w, dB, phase = signal.bode(sys)

    f = w/np.pi

    fig, ((ax1), (ax2)) = plt.subplots(2)

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

    fig.tight_layout()
    plt.show()

    return 0

#def kmax_Notch():


#filt = input()
#switcher(filt)