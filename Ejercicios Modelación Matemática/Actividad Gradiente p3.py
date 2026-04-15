import numpy as np
import matplotlib.pyplot as plt

x = np.outer(np.linspace(-10,10,32), np.ones(32))
y = x.copy().T     
z = (x*y)**2-np.sin(x*y)

fig = plt.figure(figsize=(14,8))
ax = plt.axes(projection  = "3d")

z_min, z_max = np.percentile(z, 5), np.percentile(z, 95)
z_clipped = np.clip(z, z_min, z_max)  

surf = ax.plot_surface(x, y, z_clipped,
                       cmap='plasma', 
                       vmin=z_min,
                       vmax=z_max,
                       linewidth=0,
                       antialiased=True)

ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
ax.set_title("Superficie P3")   

fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label='Valor de Z')

plt.show()