import numpy as np
import matplotlib.pyplot as plt

# Parameters
mass = 1.0
k = 10.0
amplitude = 1.0

omega = np.sqrt(k/mass)
phi = 0 
time_period = 2*np.pi/omega

# Independent and dependent variables
t_max = 2 * time_period
t = np.linspace(0,t_max,100)

dt = t[1]-t[0]

x = amplitude * np.cos(omega*t + phi)

for i in range(len(t)):
    mass_plt, =  plt.plot(x[i],0,'ro')
    spring_plt, = plt.plot([0, x[i]], [0,0], 'b-')
    plt.xlim(-1.5*amplitude, 1.5*amplitude)
    plt.ylim(-1.5,1.5)
    plt.pause(dt)
    mass_plt.remove()
    spring_plt.remove()

# plt.pause(1)
plt.close()