import tkinter as tk
from vtkmodules.tk.vtkTkRenderWindowInteractor import (
    vtkTkRenderWindowInteractor,
)
import pyvista as pv

root = tk.Tk()

# pyvista plotter, but don't let it make its own window
pl = pv.Plotter(off_screen=False)
pl.add_mesh(pv.Sphere())

ren_win = pl.ren_win  # pyvista's vtkRenderWindow

widget = vtkTkRenderWindowInteractor(root, rw=ren_win, width=600, height=600)
widget.pack(fill="both", expand=True)
widget.Initialize()
widget.Start()

root.mainloop()
