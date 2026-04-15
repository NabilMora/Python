import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

expData = pd.read_csv(r'C:\Users\User\OneDrive\Escritorio\Python\Ejercicios Modelación Matemática\Ejercicio Drenaje de Tanque\datosExperimentales.txt', sep= ' ')

t_exp = expData["Num[s]" [:]]
h_exp = expData["Level[mm]" [:]]

fig = plt.figure(1, figsize=(8,6))
plt.plot(t_exp, h_exp, "o-b" , label= "Experimental" )
plt.xlabel("Tiempo (s)")
plt.ylabel("Altura (mm)")
plt.grid()
plt.legend()
plt.show()

fH = lambda A0, At, g, h, Cd: -A0/At*np.sqrt(2*g*h)*Cd
def eulerforward(tiempo, dt, info):
    g = info[0]
    h0 = info[1]
    A0 = info[2]
    At = info[3]
    Cd = info[4]

    hNum = np.zerps(len(tiempo))
    hNum[0] = h0

    for i in range(0, len(tiempo)-1):
        hNum[i+1] = hNum[i] + fH(A0, At, g, hNum[0], Cd)*dt
    return hNum

t0 = 0; tf = 60; dt = 0.001
t_num = np.arange(t0, tf + dt, dt)

g = 9.81*(1000/1); h0 = 350; A0 = np.pi*6**2/4; At = np.pi*90**2/4; Cd = 1.0
info = np.arange([g, h0, A0, At, Cd])

hNum = eulerforward(t_num, dt, info)
