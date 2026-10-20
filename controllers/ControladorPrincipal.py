from PySide6.QtCore import Qt
from PySide6.QtWidgets import QStatusBar, QMainWindow

from views.VistaPrincipal import VistaPrincipal
from controllers.ControladorRecetas import ControladorRecetas
from controllers.ControladorMenus import ControladorMenus
from controllers.ControladorOrdenesCompra import ControladorOrdenesCompra
from controllers.ControladorInventario import VistaInventario
from controllers.ControladorMerma import ControladorMerma
from controllers.ControladorVentas import VistaVentas
from views.widgets.BarraHerramientasWidget import BarraHerramientasWidget

class ControladorPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema de gestión de inventario")
        self.vista_principal = VistaPrincipal()
        self.barra_herramientas = BarraHerramientasWidget()

        self.barra_herramientas.boton_recetas.triggered.connect(self.mostrar_recetas)
        self.barra_herramientas.boton_menus.triggered.connect(self.mostrar_menus)
        self.barra_herramientas.boton_ordenes_compra.triggered.connect(self.mostrar_ordenes_compra)
        self.barra_herramientas.boton_inventario.triggered.connect(self.mostrar_inventario)
        self.barra_herramientas.boton_merma.triggered.connect(self.mostrar_merma)
        self.barra_herramientas.boton_ventas.triggered.connect(self.mostrar_venta)

        self.setCentralWidget(self.vista_principal)
        self.addToolBar(Qt.LeftToolBarArea, self.barra_herramientas)
        self.setStatusBar(QStatusBar(self))

    def mostrar_recetas(self):
        self.setCentralWidget(ControladorRecetas())

    # def mostrar_platillos(self):
    #     self.setCentralWidget(ControladorPlatillos())

    def mostrar_menus(self):
        self.setCentralWidget(ControladorMenus())

    def mostrar_ordenes_compra(self):
        self.setCentralWidget(ControladorOrdenesCompra())

    def mostrar_inventario(self):
        self.setCentralWidget(VistaInventario())

    def mostrar_merma(self):
        self.setCentralWidget(ControladorMerma())

    def mostrar_venta(self):
        self.setCentralWidget(VistaVentas())