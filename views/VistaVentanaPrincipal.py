from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QStatusBar, QMainWindow

from views.widgets.BarraHerramientasWidget import BarraHerramientasWidget


class VistaVentanaPrincipal(QMainWindow):

    abrir_vista_home_signal = Signal()
    abrir_recetas_signal = Signal()
    abrir_menus_signal = Signal()
    abrir_ordenes_compra = Signal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema de gestión de inventario")
        self.barra_herramientas = BarraHerramientasWidget()

        self.barra_herramientas.boton_recetas.triggered.connect(self.emitir_mostrar_recetas)
        self.barra_herramientas.boton_menus.triggered.connect(self.emitir_mostrar_menus)
        self.barra_herramientas.boton_ordenes_compra.triggered.connect(self.emitir_mostrar_ordenes_compra)
        self.barra_herramientas.boton_inventario.triggered.connect(self.emitir_mostrar_inventario)
        self.barra_herramientas.boton_merma.triggered.connect(self.emitir_mostrar_merma)
        self.barra_herramientas.boton_ventas.triggered.connect(self.emitir_mostrar_venta)

        self.addToolBar(Qt.LeftToolBarArea, self.barra_herramientas)
        self.setStatusBar(QStatusBar(self))

    def emitir_mostrar_recetas(self):
        self.abrir_recetas_signal.emit()

    def emitir_mostrar_menus(self):
        self.abrir_menus_signal.emit()

    def emitir_mostrar_ordenes_compra(self):
        self.abrir_ordenes_compra.emit()

    def emitir_mostrar_inventario(self):
        pass

    def emitir_mostrar_merma(self):
        pass

    def emitir_mostrar_venta(self):
        pass