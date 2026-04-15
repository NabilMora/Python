import numpy as np
import matplotlib.pyplot as plt

g=9.81
h0=100.
v0=0.00
t0=0.00
dt=0.01
tf=4.6
t=np.arange(t0,tf,dt)

h = lambda t:  -0.5*g*t**2+v0*t+h0

Altura= h(t)
  
fig= plt.figure(figsize=(8,10))
plt.plot(t,Altura)
plt.xlabel("Tiempo")
plt.ylabel("Altura")
plt.grid()
plt.show()