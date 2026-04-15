import numpy as np
import matplotlib.pyplot as plt
def dvdt(g):
    return -g
t0 = 0
tf = 4.5
g = 9.81
dt = 0.001
t = np.arange(t0, tf+dt,dt )
v = np.zeros(len(t))
t[0] = 0
v[0] = 0
for i in range(0, len(t)-1 ):
    v[i+1] = v[i]+dt*dvdt(g)

def dxdt(v):
    return v

x = np.zeros(len(v))
x[0]= 100

for i in range(0, len(v)-1):
    x[i+1] = x[i]+dt*dxdt(v[i])



plt.figure(figsize=(8,6))
plt.plot(t,v, label="Funcion de velocidad")
plt.plot(t,x, label = "Función de posición")
plt.xlabel("tiempo")
plt.ylabel("Velocidad")
plt.legend()
plt.grid()
plt.show()
