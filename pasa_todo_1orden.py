import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


fig, ((ax1), (ax2)) = plt.subplots(2, 1)

k = float(input())
w0 = float(input())

ceros = [1/w0, -1]
polos = [1/w0, 1]

sys = signal.TransferFunction(ceros, polos)

w, dB, phase = signal.bode(sys)
f = w/(2*np.pi)

ax1.semilogx(f, k*dB)
ax1.set_xlabel('Hz')
ax1.set_ylabel('dB')
ax1.set_title('Base 10')
ax1.grid(True)


ax2.semilogx(f, k*dB, basex = 2)
ax2.set_xlabel('Hz')
ax2.set_ylabel('dB')
ax2.set_title('Base 2')
ax2.grid(True)

fig.tight_layout()
plt.show()