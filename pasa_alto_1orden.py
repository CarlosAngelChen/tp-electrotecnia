import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


#   PRUEBA  #
#Defino mi sistema de funcion de transferencia
#   1 argumento: ceros
#   2 argumento: polos
#   dentro del corchete son polinomios de s: ejem s^2 + s + 1 <=> [1,1,1]

#sys = signal.TransferFunction([1], [0, 1, 1])

#cuando grafico en bode, me devuelve 3 argumentos
#   1 argumento: w, un array en frecuencia
#   2 argumento: mag, magnitud (dB)
#   3 argumento: phase, fase

#w, dB, fase = signal.bode(sys)

#   PRUEBA  #

fig, ((ax1), (ax2)) = plt.subplots(2, 1)

k =  float(input())
w0 = float(input())
ceros = [1, 0]
polos = [0, w0*1, 1]
sys = signal.TransferFunction(ceros, polos)

w, dB, phase = signal.bode(sys)

ax1.semilogx(w, dB)
ax1.set_xlabel('Hz')
ax1.set_ylabel('dB')
ax1.set_title('Base 10')
ax1.grid(True)


ax2.semilogx(w, dB, basex = 2)
ax2.set_xlabel('Hz')
ax2.set_ylabel('dB')
ax2.set_title('Base 2')
ax2.grid(True)

fig.tight_layout()
plt.show()
