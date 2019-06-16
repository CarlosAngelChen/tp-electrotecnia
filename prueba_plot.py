import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

ceros = [1, 1]
polos = [1/10, 7/10, 1]
k = 1
w, h = signal.freqs_zpk(ceros, polos, k, worN=np.logspace(-1, 2, 1000))
plt.semilogx(w, 20 * np.log10(abs(h)))
plt.xlabel('Frequency')
plt.ylabel('Amplitude response [dB]')
plt.grid()
plt.show()