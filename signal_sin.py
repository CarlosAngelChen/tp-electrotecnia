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
        sin_pa1()

    elif "pa2" == filt:
        sin_pa2()

    elif "paN" == filt:
        sin_paNotch()

    elif "pb1" == filt:
        sin_pb1()

    elif "pb2" == filt:
        sin_pb2()

    elif "pbN" == filt:
        sin_pbNotch()

    elif "pbd" == filt:
        sin_pbd()

    elif "pt1" == filt:
        sin_pt1()

    elif "pt2" == filt:
        sin_pt2()

    elif "Notch" == filt:
        sin_notch()

def sin_pa1():
    w, f, dB, phase, sys, w0 = pasa_alto_1orden.pa_1()

    A = float(input()) #amplitud del seno de mi señal
    w1 = float(input()) #frecuencia de mi señal
    t = np.linspace(0, 2, 500)  # , endpoint=False
    u = A *np.sin(w1 * t)

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
    plt.show()

def sin_pa2():
    w, f, dB, phase, sys, w0 = pasa_alto_2orden.pa_2()
    A = float(input())  # amplitud del seno de mi señal
    w1 = float(input())  # frecuencia de mi señal
    t = np.linspace(0, 5, 500)
    u = A * np.sin(w1 * t)
    tout, y, x = signal.lsim(sys, u, t)
    plt.plot(t, y)
    plt.xlabel('seg')
    plt.ylabel('A (amplitud)')
    plt.grid()
    plt.show()

def sin_paNotch():
    w, f, dB, phase, sys, w0 = pasa_alto_notch.pa_notch()
    A = float(input())  # amplitud del seno de mi señal
    w1 = float(input())  # frecuencia de mi señal
    t = np.linspace(0, 5, 500)
    u = A * np.sin(w1 * t)
    tout, y, x = signal.lsim(sys, u, t)
    plt.plot(t, y)
    plt.xlabel('seg')
    plt.ylabel('A (amplitud)')
    plt.grid()
    plt.show()

def sin_pb1():
    w, f, dB, phase, sys, w0 = pasa_bajo_1orden.pb_1()
    A = float(input())  # amplitud del seno de mi señal
    w1 = float(input())  # frecuencia de mi señal
    t = np.linspace(0, 5, 500)
    u = A * np.sin(w1 * t)
    tout, y, x = signal.lsim(sys, u, t)
    plt.plot(t, y)
    plt.xlabel('seg')
    plt.ylabel('A (amplitud)')
    plt.grid()
    plt.show()

def sin_pb2():
    w, f, dB, phase, sys, w0 = pasa_bajo_2orden.pb_2()
    A = float(input())  # amplitud del seno de mi señal
    w1 = float(input())  # frecuencia de mi señal
    t = np.linspace(0, 5, 500)
    u = A * np.sin(w1 * t)
    tout, y, x = signal.lsim(sys, u, t)
    plt.plot(t, y)
    plt.xlabel('seg')
    plt.ylabel('A (amplitud)')
    plt.grid()
    plt.show()

def sin_pbNotch():
    w, f, dB, phase, sys, w0 = pasa_bajo_notch.pb_notch()
    A = float(input())  # amplitud del seno de mi señal
    w1 = float(input())  # frecuencia de mi señal
    t = np.linspace(0, 5, 500)
    u = A * np.sin(w1 * t)
    tout, y, x = signal.lsim(sys, u, t)
    plt.plot(t, y)
    plt.xlabel('seg')
    plt.ylabel('A (amplitud)')
    plt.grid()
    plt.show()

def sin_pbd():
    w, f, dB, phase, sys, w0 = pasa_banda_2orden.pbanda()
    A = float(input())  # amplitud del seno de mi señal
    w1 = float(input())  # frecuencia de mi señal
    t = np.linspace(0, 5, 500)
    u = A * np.sin(w1 * t)
    tout, y, x = signal.lsim(sys, u, t)
    plt.plot(t, y)
    plt.xlabel('seg')
    plt.ylabel('A (amplitud)')
    plt.grid()
    plt.show()

def sin_pt1():
    w, f, dB, phase, sys, w0 = pasa_todo_1orden.pt_1()
    A = float(input())  # amplitud del seno de mi señal
    w1 = float(input())  # frecuencia de mi señal
    t = np.linspace(0, 5, 500)
    u = A * np.sin(w1 * t)
    tout, y, x = signal.lsim(sys, u, t)
    plt.plot(t, y)
    plt.xlabel('seg')
    plt.ylabel('A (amplitud)')
    plt.grid()
    plt.show()

def sin_pt2():
    w, f, dB, phase, sys, w0 = pasa_todo_2orden.pt_2()
    A = float(input())  # amplitud del seno de mi señal
    w1 = float(input())  # frecuencia de mi señal
    t = np.linspace(0, 5, 500)
    u = A * np.sin(w1 * t)
    tout, y, x = signal.lsim(sys, u, t)
    plt.plot(t, y)
    plt.xlabel('seg')
    plt.ylabel('A (amplitud)')
    plt.grid()
    plt.show()

def sin_notch():
    w, f, dB, phase, sys, w0 = notch.notch()
    A = float(input())  # amplitud del seno de mi señal
    w1 = float(input())  # frecuencia de mi señal
    t = np.linspace(0, 5, 500)
    u = A * np.sin(w1 * t)
    tout, y, x = signal.lsim(sys, u, t)
    plt.plot(t, y)
    plt.xlabel('seg')
    plt.ylabel('A (amplitud)')
    plt.grid()
    plt.show()

filt = input()
switcher(filt)