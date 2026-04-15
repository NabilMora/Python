import numpy as np
import matplotlib.pyplot as plt

# Sacado de Internet, METODO DE SOLUCION MAS SENCILLO DEL PROBLEMA EN ESTADO ESTACIONARIO#

N = 20  # Nodos en x
M = 20  # Nodos en y
T_borde = 100.0
T_inicial = 0.0

# Inicializar matriz de temperatura
T = np.full((N, M), T_inicial)

# Condiciones de frontera (ej. borde superior caliente)
T[0, :] = T_borde

# Iteración (Método de Jacobi)
for _ in range(500):
    T_old = T.copy()
    T[1:-1, 1:-1] = 0.25 * (T_old[2:, 1:-1] + T_old[:-2, 1:-1] + 
                             T_old[1:-1, 2:] + T_old[1:-1, :-2])

plt.figure(figsize=(8, 6))
plt.imshow(T, cmap='hot', interpolation='bilinear') 
plt.colorbar(label='Temperatura (°C)')
plt.title('Distribución de Calor en la Placa')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.show()

# 1. Configuración de la placa y física
L = 1.0        # Dimensión (m)
alpha = 0.01   # Difusividad térmica
n = 30         # Nodos (30x30)
dx = L / (n - 1)

# 2. Estabilidad (Criterio de Courant para 2D)
dt = (dx**2) / (4 * alpha) * 0.9  # Paso de tiempo seguro
pasos = 200    # Cuántos pasos temporales simular

# 3. Inicialización
T = np.zeros((n, n))
T[0, :] = 100.0  # Borde superior caliente

# 4. Simulación temporal
for t in range(pasos):
    T_old = T.copy()
    # Ecuación de conducción de calor 2D
    T[1:-1, 1:-1] = T_old[1:-1, 1:-1] + alpha * dt * (
        (T_old[2:, 1:-1] - 2*T_old[1:-1, 1:-1] + T_old[:-2, 1:-1])/dx**2 +
        (T_old[1:-1, 2:] - 2*T_old[1:-1, 1:-1] + T_old[1:-1, :-2])/dx**2
    )

# 5. Gráfica final
plt.figure(figsize=(7, 5))
img = plt.imshow(T, cmap='magma', extent=[0, L, 0, L])
plt.colorbar(img, label='Temperatura (°C)')
plt.title(f'Estado de la placa tras {pasos} pasos de tiempo')
plt.show()

print("Temperatura en el centro:", T[N//2, M//2])