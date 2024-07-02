import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,6,100)
y = np.sin(t)

plt.figure(1)
plt.plot(t,y,'r')

for i in range(len(t)):
    tmp, = plt.plot(t[i],y[i],'g-o') # Bead
    plt.pause(0.02)
    tmp.remove()

plt.pause(1)
plt.close()