import numpy as np
import matplotlib.pyplot as plt

M = 30000000
n = 0
tol= 0.001
err= 1
for i in range(1, M+1):
    if  i**2 < M:
        n = i
    else:
        break

while err>tol: 
    n_nuevo = 0.5*(n+M/n)
    err = abs(n_nuevo**2-M)
    n = n_nuevo

z = n**2


print("La raiz cuadrada de", M, "es", n, "y el valor numerico de M es:", z)



  