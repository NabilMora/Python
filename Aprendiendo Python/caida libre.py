import numpy as np
import matplotlib.pyplot as plt
def f(t):
    return -g*t+v0
g = 9.81
v0 = 0
t0 = 0
dt = 0.001
tf = 4.5
t = np.arange(t0, tf+dt, dt)
y = np.zeros(len(t))
t[0] = t0
y[0] = 100
for i in range(len(t)-1):
    y[i+1] = y[i]+dt*f(t[i])


t_r =np.arange(0,4.5, 0.001)

h = -0.5*g*t_r**2+v0*t_r+100

plt.figure( 1, figsize=(8,6))
plt.plot(t_r,h, label = "Altura real ", color="green" )
plt.plot(t, y, label="Función de caida libre ")
plt.xlabel("Tiempo(s)")
plt.ylabel("Altura (m)")
plt.grid()
plt.legend()
plt.show()