import numpy as np
import matplotlib.pyplot as plt

x, y = np.meshgrid(np.linspace(-5, 5, 20), np.linspace(-5,5 , 20))
x_fine, y_fine = np.meshgrid(np.linspace(-5, 5, 200), np.linspace(-5, 5, 200))

z_fine = np.sin(x_fine)*np.cos(y_fine)-np.cos(y_fine**2)
dfdx = np.cos(x)*np.cos(y)
dfdy = 2*y*np.sin(y**2)-np.sin(x)*np.sin(y)

magnitude = np.sqrt(dfdx**2+dfdy**2)
magnitude[magnitude == 0] = 1

fig, ax = plt.subplots(figsize = (8,6))

contf = ax.contourf(x_fine, y_fine, z_fine, levels=30, cmap='coolwarm', alpha=0.6)
cont  = ax.contour (x_fine, y_fine, z_fine, levels=30, colors='k', linewidths=0.4, alpha=0.4)
fig.colorbar(contf, ax=ax, label="f(x,y) = $sin(x)cos(x)-cos(y^2)$ ")

q = ax.quiver(x, y, dfdx / magnitude, dfdy / magnitude,
              magnitude, cmap='plasma', scale=40, width=0.004)
fig.colorbar(q, ax=ax, label='Magnitud |∇f|')

ax.set_title('Campo vectorial $\\nabla f = (cos(x)cos(y),\\ 2ysin(y^2)-sin(x)sin(y) )$ sobre el plano x-y')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True, linestyle='--', alpha=0.3)
ax.set_aspect('equal')

plt.tight_layout()
plt.show()
