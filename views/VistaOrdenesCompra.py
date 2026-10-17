from PySide6 import QtWidgets
from pathlib import Path
from views.VistaListaOrdenesCompra import VistaListaOrdenesCompra

from models.OrdenCompra import OrdenCompra

class VistaOrdenesCompra(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QHBoxLayout()

        self.vista_lista_ordenes_compra = VistaListaOrdenesCompra()
        self.vista_lista_ordenes_compra.boton_crear_orden_compra.clicked.connect(self.abrir_vista_crear_orden)

        self.layout.addWidget(self.vista_lista_ordenes_compra)

        # testeo
        self.mostrar_tabla_ordenes_compra([OrdenCompra(1, "25/09/2026", "15/10/2026", 5789),
                                           OrdenCompra(2, "16/10/2026", None, 7500)
                                           ])

        self.setLayout(self.layout)
        self.setStyleSheet((Path('views/styles/estilos_ordenes_compra.qss').read_text()))

    def abrir_vista_lista_ordenes_compra(self):
        self.remover_ultima_vista()
        self.layout.addWidget(self.vista_lista_ordenes_compra)

    def mostrar_tabla_ordenes_compra(self, lista_orden_compra):
        for orden in lista_orden_compra:
            boton_ver_orden = self.vista_lista_ordenes_compra.crear_boton_ver_orden()
            boton_ver_orden.clicked.connect(lambda orden_obj=orden: self.abrir_vista_detalles(orden_obj))
            self.vista_lista_ordenes_compra.crear_fila_tabla_ordenes_compra(orden, boton_ver_orden)

    def abrir_vista_crear_orden(self):
        pass

    def abrir_vista_detalles(self, orden_compra):
        pass

    def remover_ultima_vista(self):
        last_view = self.layout.itemAt(0).widget()
        self.layout.removeWidget(last_view)
        last_view.setParent(None)
