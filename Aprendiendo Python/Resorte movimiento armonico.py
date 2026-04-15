import numpy as np
import matplotlib.pyplot as plt

k = 1
m = 1
t0 = 0
tf = 20
dt = 0.001

t = np.arange(t0, tf+dt, dt)
v = np.zeros(len(t))
x = np.zeros(len(t))

v[0] = 0
x[0] = 1

def dvdt(x):
    return -(k/m)*x
def dxdt(v):
    return v

for i in range(0, len(t)-1):
    v[i+1] = v[i]+dt*dvdt(x[i])
    x[i+1] = x[i]+dt*dxdt(v[i])

plt.figure(figsize=(8,6))
plt.plot(t,v, label = "Función velocidad", color= "blue")
plt.plot(t,x, label= "Función posición ", color  = "green")
plt.xlabel("Tiempo")
plt.ylabel("Valor")
plt.legend()
plt.grid()
plt.show()


