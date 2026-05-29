import pyvista as pv
from pyvista.trame.ui import plotter_ui
from trame.app import get_server
from trame.ui.vuetify3 import SinglePageLayout
from trame.widgets import vuetify3

pv.OFF_SCREEN = True  # MUST. trame renders offscreen, streams to web

server = get_server()
state, ctrl = server.state, server.controller

pl = pv.Plotter()
actor = pl.add_mesh(pv.Sphere())

with SinglePageLayout(server) as layout:
    layout.title.set_text("My App")
    with layout.toolbar:
        # your tkinter controls -> become these
        vuetify3.VSlider(v_model=("radius", 1.0), min=0.1, max=5,
                         step=0.1, hide_details=True)
    with layout.content:
        view = plotter_ui(pl)        # <- PyVista plotter as web widget
        ctrl.view_update = view.update

# react to control changes
@state.change("radius")
def on_radius(radius, **_):
    pl.clear()
    pl.add_mesh(pv.Sphere(radius=radius))
    ctrl.view_update()              # push update to browser

server.start()  # opens browser at localhost:8080
