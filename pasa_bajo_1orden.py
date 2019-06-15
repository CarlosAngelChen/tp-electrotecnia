import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

k =  float(input())
w0 = float(input())
ceros = [k]
polos = [0, 1/w0, 1]
sys = signal.TransferFunction(ceros, polos)

w, dB, phase = signal.bode(sys)
f = w/(2*np.pi)

ax1.semilogx(f, k*dB)
ax1.set_xlabel('Hz')
ax1.set_ylabel('dB')
ax1.set_title('Base 10')
ax1.grid(True)

ax2.semilogx(w, k*dB)
ax2.set_xlabel('rad/s')
ax2.set_ylabel('dB')
ax2.set_title('Base 10')
ax2.grid(True)

ax3.semilogx(f, k*dB, basex = 2)
ax3.set_xlabel('Hz')
ax3.set_ylabel('dB')
ax3.set_title('Base 2')
ax3.grid(True)

ax4.semilogx(w, k*dB, basex = 2)
ax4.set_xlabel('rad/s')
ax4.set_ylabel('dB')
ax4.set_title('Base 2')
ax4.grid(True)

fig.tight_layout()
plt.show()
