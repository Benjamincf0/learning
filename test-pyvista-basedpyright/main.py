import pyvista as pv

pl = pv.Plotter()
sphere = pv.Sphere()
actor = pl.add_mesh(sphere)
pl.remove_actor(actor)
pl.add_actor(actor)

pl.show()
