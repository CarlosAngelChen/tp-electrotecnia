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
        imp_pa1()

    elif "pa2" == filt:
        imp_pa2()

    elif "paN" == filt:
        imp_paNotch()

    elif "pb1" == filt:
        imp_pb1()

    elif "pb2" == filt:
        imp_pb2()

    elif "pbN" == filt:
        imp_pbNotch()

    elif "pbd" == filt:
        imp_pbd()

    elif "pt1" == filt:
        imp_pt1()

    elif "pt2" == filt:
        imp_pt2()

    elif "Notch" == filt:
        imp_notch()

def imp_pa1():
    w, f, dB, phase, sys, w0 = pasa_alto_1orden.pa_1()

    t, y = sys.impulse(N = 500)
    plt.plot(t, y)
    plt.xlabel('seg')
    plt.ylabel('A (amplitud)')
    plt.grid()
    plt.show()

def imp_pa2():
    w, f, dB, phase, sys, w0 = pasa_alto_2orden.pa_2()
    t, y = sys.impulse(N=500)

    plt.plot(t, y)
    plt.xlabel('seg')
    plt.ylabel('A (amplitud)')
    plt.grid()
    plt.show()

def imp_paNotch():
    w, f, dB, phase, sys, w0 = pasa_alto_notch.pa_notch()
    t, y = sys.impulse(N=500)

    plt.plot(t, y)
    plt.xlabel('seg')
    plt.ylabel('A (amplitud)')
    plt.grid()
    plt.show()

def imp_pb1():
    w, f, dB, phase, sys, w0 = pasa_bajo_1orden.pb_1()
    t, y = sys.impulse(N = 500)

    plt.plot(t, y)
    plt.xlabel('seg')
    plt.ylabel('A (amplitud)')
    plt.grid()
    plt.show()

def imp_pb2():
    w, f, dB, phase, sys, w0 = pasa_bajo_2orden.pb_2()
    t, y = sys.impulse(N = 500)

    plt.plot(t, y)
    plt.xlabel('seg')
    plt.ylabel('A (amplitud)')
    plt.grid()
    plt.show()

def imp_pbNotch():
    w, f, dB, phase, sys, w0 = pasa_bajo_notch.pb_notch()
    t, y = sys.impulse(N=500)

    plt.plot(t, y)
    plt.xlabel('seg')
    plt.ylabel('A (amplitud)')
    plt.grid()
    plt.show()

def imp_pbd():
    w, f, dB, phase, sys, w0 = pasa_banda_2orden.pbanda()
    t, y = sys.impulse(N = 500)

    plt.plot(t, y)
    plt.xlabel('seg')
    plt.ylabel('A (amplitud)')
    plt.grid()
    plt.show()

def imp_pt1():
    w, f, dB, phase, sys, w0 = pasa_todo_1orden.pt_1()
    t, y = sys.impulse(N = 500)

    plt.plot(t, y)
    plt.xlabel('seg')
    plt.ylabel('A (amplitud)')
    plt.grid()
    plt.show()

def imp_pt2():
    w, f, dB, phase, sys, w0 = pasa_todo_2orden.pt_2()
    t, y = sys.impulse(N = 500)

    plt.plot(t, y)
    plt.xlabel('seg')
    plt.ylabel('A (amplitud)')
    plt.grid()
    plt.show()

def imp_notch():
    w, f, dB, phase, sys, w0 = notch.notch()
    t, y = sys.impulse(N = 500)

    plt.plot(t, y)
    plt.xlabel('seg')
    plt.ylabel('A (amplitud)')
    plt.grid()
    plt.show()

filt = input()
switcher(filt)