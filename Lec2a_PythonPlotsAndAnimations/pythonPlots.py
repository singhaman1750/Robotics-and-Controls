import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,6,50)
y1 = np.sin(t)
y2 = np.cos(t)
y3 = np.tan(t)

plt.figure(1)
plt.plot(t,y1,'r')
plt.plot(t,y2,'b-.')
plt.legend(['sin','cos'])
plt.xlabel('t')
plt.ylabel('y')
plt.title('Graph of sine and cosine functions')
plt.pause(10)
plt.close()

plt.figure(2)
plt.plot(t,y3,'g-.')
plt.legend(['tan'])
plt.pause(10)
plt.close()