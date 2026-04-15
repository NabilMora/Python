import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.widgets import Button
from mpl_toolkits.mplot3d import Axes3D
import os

matplotlib.use('tkAgg')

carpeta = os.path.dirname(os.path.abspath(__file__))

x = -2
y = -3


divF1 = 3*x**2-3*y**2
divF2 = -3*x**2+3*y**2
divF3 = 2*x*y**2-np.cos(x*y)*x
divF4 = np.cos(x)*np.cos(y)+2*y*np.sin(y**2)
divF5 = 3*x**2+8*x*y-10*x*y-3*y**2
divF6 = -np.sin(x**3)*3*x**2+8*x*np.cos(x**2)*np.cos(y)-15*y**2*x**2+4*x**3*y

rotF1 = np.array([0,0,0])
rotF2 = np.array([0,0,0])
rotF3 = np.array([0,0,-y*np.cos(x*y) -2*y*x**2])
rotF4 = np.array([0,0,np.sin(y)*np.sin(x)])
rotF5 = np.array([0,0,-5*y**2-4*x**2])
rotF6 = np.array([0,0,-10*x*y**3+6*x**2*y**2+4*np.sin(x**2)*np.sin(y)])

x_vals = np.linspace(-2, 2, 300)
y_vals = np.linspace(-2, 2, 300)
X, Y = np.meshgrid(x_vals, y_vals)
 
xq = np.linspace(-2, 2, 15)
yq = np.linspace(-2, 2, 15)
Xq, Yq = np.meshgrid(xq, yq)
 
campos = [
    {
        "nombre": r"Campo 1:  $\mathbf{f} = x^3\,\mathbf{i} - y^3\,\mathbf{j}$",
        "div":    lambda x, y: 3*x**2 - 3*y**2,
        "rot":    lambda x, y: np.zeros_like(x),
    },
    {
        "nombre": r"Campo 2:  $\mathbf{f} = -x^3\,\mathbf{i} + y^3\,\mathbf{j}$",
        "div":    lambda x, y: -3*x**2 + 3*y**2,
        "rot":    lambda x, y: np.zeros_like(x),
    },
    {
        "nombre": r"Campo 3:  $\mathbf{f} = x^2y^2\,\mathbf{i} - \sin(xy)\,\mathbf{j}$",
        "div":    lambda x, y: 2*x*y**2 - x*np.cos(x*y),
        "rot":    lambda x, y: -y*np.cos(x*y) - 2*x**2*y,
    },
    {
        "nombre": r"Campo 4:  $\mathbf{f} = \sin x\cos y\,\mathbf{i} - \cos(y^2)\,\mathbf{j}$",
        "div":    lambda x, y: np.cos(x)*np.cos(y) + 2*y*np.sin(y**2),
        "rot":    lambda x, y: -np.sin(x)*np.sin(y),
    },
    {
        "nombre": r"Campo 5:  $\mathbf{f} = (x^3+4x^2y)\,\mathbf{i} - (5xy^2+y^3)\,\mathbf{j}$",
        "div":    lambda x, y: 3*x**2 + 8*x*y - 5*y**2 - 3*y**2,
        "rot":    lambda x, y: -5*y**2 - 4*x**2,
    },
    {
        "nombre": r"Campo 6:  $\mathbf{f} = (\cos(x^3)+4\sin(x^2)\cos y)\,\mathbf{i} - (5x^2y^3-2x^3y^2)\,\mathbf{j}$",
        "div":    lambda x, y: (-3*x**2*np.sin(x**3) + 8*x*np.cos(x**2)*np.cos(y)
                                - (15*x**2*y**2 - 4*x**3*y)),
        "rot":    lambda x, y: (-(10*x*y**3 - 6*x**2*y**2)
                                - (-4*np.sin(x**2)*np.sin(y))),
    },
]
 
def dibujar_campo(fig, idx):
    fig.clear()
    campo = campos[idx]
 
    
    fig.suptitle(campo["nombre"], fontsize=12, fontweight='bold', y=0.97)
 
    
    ax1 = fig.add_subplot(1, 2, 1, projection='3d')
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
 
    
    Z_div = np.clip(campo["div"](X, Y), -50, 50)
    surf = ax1.plot_surface(X, Y, Z_div, cmap='RdBu_r', alpha=0.9, linewidth=0)
    ax1.set_title(r"Divergencia $\nabla \cdot \mathbf{f}$", fontsize=10)
    ax1.set_xlabel("x"); ax1.set_ylabel("y"); ax1.set_zlabel("div f")
    fig.colorbar(surf, ax=ax1, shrink=0.45, pad=0.1)
 
    
    Zq = campo["rot"](Xq, Yq)
    ax2.plot_surface(Xq, Yq, np.zeros_like(Xq), alpha=0.06, color='gray')
    norm = np.max(np.abs(Zq)) if np.max(np.abs(Zq)) > 0 else 1
    colors = ['royalblue' if v >= 0 else 'tomato' for v in Zq.ravel()]
    ax2.quiver(Xq, Yq, np.zeros_like(Xq),
               np.zeros_like(Xq), np.zeros_like(Yq), Zq * (1.2 / norm),
               length=0.25, normalize=False, color=colors, linewidth=1.2)
    ax2.set_title(r"Rotacional $\nabla \times \mathbf{f}$ — comp. $\hat{k}$", fontsize=10)
    ax2.set_xlabel("x"); ax2.set_ylabel("y"); ax2.set_zlabel(r"$(\nabla\times f)_z$")
    ax2.set_zlim(-2, 2)
 
   
    fig.text(0.5, 0.01, f"  {idx+1} / {len(campos)}  ", ha='center',
             fontsize=10, color='gray')
 
    
    ax_prev = fig.add_axes([0.35, 0.04, 0.12, 0.04])
    ax_next = fig.add_axes([0.53, 0.04, 0.12, 0.04])
    ax_save = fig.add_axes([0.44, 0.09, 0.12, 0.04])
 
    btn_prev = Button(ax_prev, '◀  Anterior', color='#e8e8e8', hovercolor='#c8c8ff')
    btn_next = Button(ax_next, 'Siguiente  ▶', color='#e8e8e8', hovercolor='#c8c8ff')
    btn_save = Button(ax_save, ' Guardar', color='#d0f0d0', hovercolor='#90e090')
 
    def ir_anterior(event):
        state['idx'] = (state['idx'] - 1) % len(campos)
        dibujar_campo(fig, state['idx'])
        fig.canvas.draw()
 
    def ir_siguiente(event):
        state['idx'] = (state['idx'] + 1) % len(campos)
        dibujar_campo(fig, state['idx'])
        fig.canvas.draw()
 
    def guardar(event):
        fname = os.path.join(carpeta, f"campo_{state['idx']+1}.png")
        fig.savefig(fname, dpi=150, bbox_inches='tight')
        print(f"✓ Guardado: {fname}")
 
    btn_prev.on_clicked(ir_anterior)
    btn_next.on_clicked(ir_siguiente)
    btn_save.on_clicked(guardar)

    fig._btns = (btn_prev, btn_next, btn_save)

state = {'idx': 0}
 
fig = plt.figure(figsize=(16, 7))
fig.subplots_adjust(bottom=0.15)
dibujar_campo(fig, state['idx'])
 
plt.show()
 
 





