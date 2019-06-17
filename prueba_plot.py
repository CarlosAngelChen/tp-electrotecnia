import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
#from UserInput import userInput


#ceros = [1, 1]
#polos = [1/10, 7/10, 1]
#k = 1
#w, h = signal.freqs_zpk(ceros, polos, k, worN=np.logspace(-1, 2, 1000))
#plt.semilogx(w, 20 * np.log10(abs(h)))
#plt.xlabel('Frequency')
#plt.ylabel('Amplitude response [dB]')
#plt.grid()
#plt.show()

w0 = 10
etha = 0.1
k = 1
ceros = [k]
polos = [1/(w0**2), 2*etha/w0, 1]

#sys = signal.TransferFunction(ceros, polos)

#w, dB, phase = signal.bode(sys)
#t, y = signal.impulse2(sys)


#plt.plot(t, y)
#plt.figure()
#plt.semilogx(w, dB)
#plt.show()

sys = signal.lti(ceros, polos)
t = np.linspace(0, 5, 500)
u = np.ones_like(t)
tout, y, x = signal.lsim(sys, u, t)
plt.plot(t, y)
plt.show()