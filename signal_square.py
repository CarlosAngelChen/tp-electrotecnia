import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

import pasa_alto_1orden
import pasa_alto_2orden
import pasa_alto_notch
import pasa_bajo_1orden
import pasa_bajo_2orden
import pasa_bajo_notch
import pasa_banda_2orden
import pasa_todo_1orden
import pasa_todo_2orden
import notch

def switcher(filt):
    if "pa1" == filt:
        sqr_pa1()

    elif "pa2" == filt:
        sqr_pa2()

    elif "paN" == filt:
        sqr_paNotch()

    elif "pb1" == filt:
        sqr_pb1()

    elif "pb2" == filt:
        sqr_pb2()

    elif "pbN" == filt:
        sqr_pbNotch()

    elif "pbd" == filt:
        sqr_pbd()

    elif "pt1" == filt:
        sqr_pt1()

    elif "pt2" == filt:
        sqr_pt2()

    elif "Notch" == filt:
        sqr_notch()

def sqr_pa1():

    w, f, dB, phase, sys, w0 = pasa_alto_1orden.pa_1()

    duty = float(input())#input del duty
    f1 = float(input())#input de frec de la cuadrada
    w1 = f1 * 2 * np.pi
    t = np.linspace(0, 2, 500)  # , endpoint=False
    A = float(input()) #input de amplitud de la cuadrada
    u = A*signal.square(2 * np.pi * w1 * t, duty)

    tout, y, x = signal.lsim(sys, u, t)

    fig, ((ax1), (ax2)) = plt.subplots(2, 1)

    ax1.plot(tout, y)
    ax1.set_xlabel('seg')
    ax1.set_ylabel('A (amplitud)')
    ax1.set_title('Señal de output')
    ax1.grid(True)

    ax2.plot(t, u)
    ax2.set_xlabel('seg')
    ax2.set_ylabel('A (amplitud)')
    ax2.set_title('Señal de input')
    ax2.grid()

    fig.tight_layout()
    plt.show()

def sqr_pa2():
    w, f, dB, phase, sys, w0 = pasa_alto_2orden.pa_2()

    duty = float(input())#input del duty
    f1 = float(input())#input de frec de la cuadrada
    w1 = f1 * 2 * np.pi
    t = np.linspace(0, 2, 500)  # , endpoint=False
    A = float(input())
    u = A * signal.square(2 * np.pi * w1 * t, duty)

    tout, y, x = signal.lsim(sys, u, t)

    fig, ((ax1), (ax2)) = plt.subplots(2, 1)

    ax1.plot(tout, y)
    ax1.set_xlabel('seg')
    ax1.set_ylabel('A (amplitud)')
    ax1.set_title('Señal de output')
    ax1.grid(True)

    ax2.plot(t, u)
    ax2.set_xlabel('seg')
    ax2.set_ylabel('A (amplitud)')
    ax2.set_title('Señal de input')
    ax2.grid()

    fig.tight_layout()
    plt.show()

def sqr_paNotch():
    w, f, dB, phase, sys, w0 = pasa_alto_notch.pa_notch()
    duty = float(input())#input del duty
    f1 = float(input())#input de frec de la cuadrada
    w1 = f1 * 2 * np.pi
    t = np.linspace(0, 2, 500)  # , endpoint=False
    A = float(input())
    u = A * signal.square(2 * np.pi * w1 * t, duty)
    tout, y, x = signal.lsim(sys, u, t)

    fig, ((ax1), (ax2)) = plt.subplots(2, 1)

    ax1.plot(tout, y)
    ax1.set_xlabel('seg')
    ax1.set_ylabel('A (amplitud)')
    ax1.set_title('Señal de output')
    ax1.grid(True)

    ax2.plot(t, u)
    ax2.set_xlabel('seg')
    ax2.set_ylabel('A (amplitud)')
    ax2.set_title('Señal de input')
    ax2.grid()

    fig.tight_layout()
    plt.show()

def sqr_pb1():
    w, f, dB, phase, sys, w0 = pasa_bajo_1orden.pb_1()
    duty = float(input())#input del duty
    f1 = float(input())#input de frec de la cuadrada
    w1 = f1 * 2 * np.pi
    t = np.linspace(0, 2, 500)  # , endpoint=False
    A = float(input())
    u = A * signal.square(2 * np.pi * w1 * t, duty)
    tout, y, x = signal.lsim(sys, u, t)

    fig, ((ax1), (ax2)) = plt.subplots(2, 1)

    ax1.plot(tout, y)
    ax1.set_xlabel('seg')
    ax1.set_ylabel('A (amplitud)')
    ax1.set_title('Señal de output')
    ax1.grid(True)

    ax2.plot(t, u)
    ax2.set_xlabel('seg')
    ax2.set_ylabel('A (amplitud)')
    ax2.set_title('Señal de input')
    ax2.grid()

    fig.tight_layout()
    plt.show()

def sqr_pb2():
    w, f, dB, phase, sys, w0 = pasa_bajo_2orden.pb_2()
    duty = float(input())#input del duty
    f1 = float(input())#input de frec de la cuadrada
    w1 = f1 * 2 * np.pi
    t = np.linspace(0, 2, 500)  # , endpoint=False
    A = float(input())
    u = A * signal.square(2 * np.pi * w1 * t, duty)
    tout, y, x = signal.lsim(sys, u, t)

    fig, ((ax1), (ax2)) = plt.subplots(2, 1)

    ax1.plot(tout, y)
    ax1.set_xlabel('seg')
    ax1.set_ylabel('A (amplitud)')
    ax1.set_title('Señal de output')
    ax1.grid(True)

    ax2.plot(t, u)
    ax2.set_xlabel('seg')
    ax2.set_ylabel('A (amplitud)')
    ax2.set_title('Señal de input')
    ax2.grid()

    fig.tight_layout()
    plt.show()

def sqr_pbNotch():
    w, f, dB, phase, sys, w0 = pasa_bajo_notch.pb_notch()
    duty = float(input())#input del duty
    f1 = float(input())#input de frec de la cuadrada
    w1 = f1 * 2 * np.pi
    t = np.linspace(0, 2, 500)  # , endpoint=False
    A = float(input())
    u = A * signal.square(2 * np.pi * w1 * t, duty)
    tout, y, x = signal.lsim(sys, u, t)

    fig, ((ax1), (ax2)) = plt.subplots(2, 1)

    ax1.plot(tout, y)
    ax1.set_xlabel('seg')
    ax1.set_ylabel('A (amplitud)')
    ax1.set_title('Señal de output')
    ax1.grid(True)

    ax2.plot(t, u)
    ax2.set_xlabel('seg')
    ax2.set_ylabel('A (amplitud)')
    ax2.set_title('Señal de input')
    ax2.grid()

    fig.tight_layout()
    plt.show()

def sqr_pbd():
    w, f, dB, phase, sys, w0 = pasa_banda_2orden.pbanda()
    duty = float(input())#input del duty
    f1 = float(input())#input de frec de la cuadrada
    w1 = f1 * 2 * np.pi
    t = np.linspace(0, 2, 500)  # , endpoint=False
    A = float(input())
    u = A * signal.square(2 * np.pi * w1 * t, duty)
    tout, y, x = signal.lsim(sys, u, t)

    fig, ((ax1), (ax2)) = plt.subplots(2, 1)

    ax1.plot(tout, y)
    ax1.set_xlabel('seg')
    ax1.set_ylabel('A (amplitud)')
    ax1.set_title('Señal de output')
    ax1.grid(True)

    ax2.plot(t, u)
    ax2.set_xlabel('seg')
    ax2.set_ylabel('A (amplitud)')
    ax2.set_title('Señal de input')
    ax2.grid()

    fig.tight_layout()
    plt.show()

def sqr_pt1():
    w, f, dB, phase, sys, w0 = pasa_todo_1orden.pt_1()
    duty = float(input())#input del duty
    f1 = float(input())#input de frec de la cuadrada
    w1 = f1 * 2 * np.pi
    t = np.linspace(0, 2, 500)  # , endpoint=False
    A = float(input())
    u = A * signal.square(2 * np.pi * w1 * t, duty)
    tout, y, x = signal.lsim(sys, u, t)

    fig, ((ax1), (ax2)) = plt.subplots(2, 1)

    ax1.plot(tout, y)
    ax1.set_xlabel('seg')
    ax1.set_ylabel('A (amplitud)')
    ax1.set_title('Señal de output')
    ax1.grid(True)

    ax2.plot(t, u)
    ax2.set_xlabel('seg')
    ax2.set_ylabel('A (amplitud)')
    ax2.set_title('Señal de input')
    ax2.grid()

    fig.tight_layout()
    plt.show()

def sqr_pt2():
    w, f, dB, phase, sys, w0 = pasa_todo_2orden.pt_2()
    duty = float(input())#input del duty
    f1 = float(input())#input de frec de la cuadrada
    w1 = f1 * 2 * np.pi
    t = np.linspace(0, 2, 500)  # , endpoint=False
    A = float(input())
    u = A * signal.square(2 * np.pi * w1 * t, duty)
    tout, y, x = signal.lsim(sys, u, t)

    fig, ((ax1), (ax2)) = plt.subplots(2, 1)

    ax1.plot(tout, y)
    ax1.set_xlabel('seg')
    ax1.set_ylabel('A (amplitud)')
    ax1.set_title('Señal de output')
    ax1.grid(True)

    ax2.plot(t, u)
    ax2.set_xlabel('seg')
    ax2.set_ylabel('A (amplitud)')
    ax2.set_title('Señal de input')
    ax2.grid()

    fig.tight_layout()
    plt.show()

def sqr_notch():
    w, f, dB, phase, sys, w0 = notch.notch()
    duty = float(input())#input del duty
    f1 = float(input())#input de frec de la cuadrada
    w1 = f1 * 2 * np.pi
    t = np.linspace(0, 2, 500)  # , endpoint=False
    A = float(input())
    u = A * signal.square(2 * np.pi * w1 * t, duty)
    tout, y, x = signal.lsim(sys, u, t)

    fig, ((ax1), (ax2)) = plt.subplots(2, 1)

    ax1.plot(tout, y)
    ax1.set_xlabel('seg')
    ax1.set_ylabel('A (amplitud)')
    ax1.set_title('Señal de output')
    ax1.grid(True)

    ax2.plot(t, u)
    ax2.set_xlabel('seg')
    ax2.set_ylabel('A (amplitud)')
    ax2.set_title('Señal de input')
    ax2.grid()

    fig.tight_layout()
    plt.show()

filt = input()
switcher(filt)