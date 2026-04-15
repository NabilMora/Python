import numpy as np
import matplotlib.pyplot as plt

x, y = np.meshgrid(np.linspace(-5, 5, 20), np.linspace(-5,5 , 20))
x_fine, y_fine = np.meshgrid(np.linspace(-5, 5, 200), np.linspace(-5, 5, 200))

z_fine = x_fine**3+4*x_fine**2*y_fine-5*x_fine*y_fine**2-y_fine**3
dfdx = 3*x**2+8*x*y+5*y**2
dfdy = 4*x**2-10*x*y-3*y**2

magnitude = np.sqrt(dfdx**2+dfdy**2)
magnitude[magnitude == 0] = 1

fig, ax = plt.subplots(figsize = (8,6))

contf = ax.contourf(x_fine, y_fine, z_fine, levels=30, cmap='coolwarm', alpha=0.6)
cont  = ax.contour (x_fine, y_fine, z_fine, levels=30, colors='k', linewidths=0.4, alpha=0.4)
fig.colorbar(contf, ax=ax, label="f(x,y) = $x^3+4x^2y+5xy^2-y^3$ ")

q = ax.quiver(x, y, dfdx / magnitude, dfdy / magnitude,
              magnitude, cmap='plasma', scale=18, width=0.004)
fig.colorbar(q, ax=ax, label='Magnitud |∇f|')

ax.set_title('Campo vectorial $\\nabla f = (3x^2+8xy-5y^2,\\ 4x^2-10xy-3y^2)$ sobre el plano x-y')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True, linestyle='--', alpha=0.3)
ax.set_aspect('equal')

plt.tight_layout()
plt.show()