import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import scipy as sci

x = np.linspace(0, 1000, 100)
w0 = 50
k = 1
def pa_alto (x, w0, k):
    y = k * x/np.sqrt((x/w0)**2+1)
    return 20*np.log(y)

fig, ax = plt.subplots()
plt.subplots_adjust(left = 0.1, bottom=0.25)
#p, = plt.plot(x, pa_alto(x, w0, k), 'r')
f, = plt.plot(x, pa_alto(x, w0, k), 'r')
plt.ylim(1, 100)
plt.grid()

#area del slider
#   1 arguemnto: con respecto de la izq, que tan lejos lo queres
#   2 argumento: con respecto de abajo, que tan alto lo queres
#   3 arguemnto: ancho total
#   4 argumento: altura
axSlider1 = plt.axes([0.1, 0.1, 0.8, 0.04])
axSlider2 = plt.axes([0.1, 0.05, 0.8, 0.04])

#argumentos del slider
#   1 arguemnto: recibe el eje al cual slidea
#   2 argumento: le das un nombre
#   3 arguemnto: el valor minimo
#   4 argumento: el valor maximo
sld1 = Slider(axSlider1, 'slider 1', valmin=0, valmax=w0)

sld2 = Slider(  ax = axSlider2,
                label = 'slider 2',
                valmin= 1,
                valmax= 2*w0,
                valinit= w0, #valor inicial
                valfmt= '%1.2f',  #los decimales que tiene que tomar
                color = 'green')

def val_update (val):
    w0 = sld2.val
    g = pa_alto(x, w0, k)
    f.set_ydata(g)
    #plt.draw()
    fig.canvas.draw_idle()


sld2.on_changed(val_update)

plt.show()

