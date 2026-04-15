import numpy as np
import matplotlib.pyplot as plt

GM = 398600      # km^3/s^2
R = 6371         # km
h = 384400       # km

dt = 1           # paso de tiempo (s)

# distancia inicial: distancia Tierra-Luna
r0 = h

# velocidad inicial
v0 = 0

t = [0]
r = [r0]
v = [v0]

def dvdt(r):
    return -GM/(r**2)

def drdt(v):
    return v

i = 0

# el tiempo avanza hasta que r llegue al radio de la Tierra
while r[i] > R:

    k1v = dvdt(r[i])
    k1r = drdt(v[i])

    k2v = dvdt(r[i] + 0.5*dt*k1r)
    k2r = drdt(v[i] + 0.5*dt*k1v)

    k3v = dvdt(r[i] + 0.5*dt*k2r)
    k3r = drdt(v[i] + 0.5*dt*k2v)

    k4v = dvdt(r[i] + dt*k3r)
    k4r = drdt(v[i] + dt*k3v)

    v_new = v[i] + (dt/6)*(k1v + 2*k2v + 2*k3v + k4v)
    r_new = r[i] + (dt/6)*(k1r + 2*k2r + 2*k3r + k4r)

    v.append(v_new)
    r.append(r_new)
    t.append(t[i] + dt)

    i += 1

t = np.array(t)
r = np.array(r)
v = np.array(v)

plt.figure(figsize=(8,6))

plt.plot(t, r, label="distancia al centro de la Tierra (km)")
plt.plot(t, v, label="velocidad (km/s)")

plt.xlabel("Tiempo (s)")
plt.ylabel("Valor")
plt.legend()
plt.grid()

plt.show()
print("Velocidad final es :" , v[-1], "km/s")

