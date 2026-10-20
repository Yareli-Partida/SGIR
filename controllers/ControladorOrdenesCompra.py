from PySide6.QtWidgets import QWidget
from pathlib import Path

from views.VistaListaOrdenesCompra import VistaListaOrdenesCompra
from views.widgets.BotonSecundarioWidget import BotonSecundarioWidget
from models.OrdenCompra import OrdenCompra

class ControladorOrdenesCompra(QWidget):
    def __init__(self):
        super().__init__()
        self.vista_lista_ordenes_compra = None

        self.abrir_vista_lista_ordenes_compra()

        self.setStyleSheet((Path('views/styles/estilos_ordenes_compra.qss').read_text()))

    def abrir_vista_lista_ordenes_compra(self) -> None:
        """
        Crea un obj de VistaListaOrdenesCompra, conecta los botones de la vista a sus respectivas funciones
        y cambia el layout actual.
        """

        self.vista_lista_ordenes_compra = VistaListaOrdenesCompra()
        self.vista_lista_ordenes_compra.boton_crear_orden_compra.clicked.connect(self.abrir_vista_crear_orden)
        self.mostrar_tabla_ordenes_compra()

        if self.layout():
            self.remover_ultima_vista()

        self.setLayout(self.vista_lista_ordenes_compra)

    def mostrar_tabla_ordenes_compra(self) -> None:
        """
        Conecta con la capa de servicios para obtener la lista de órdenes de compra
        y crea una fila en tabla de la vistaListaOrdenesCompra por cada orden.
        """

        # Hardcoded para testeo
        lista_orden_compra = [OrdenCompra(1, "25/09/2026", "15/10/2026", 5789),
                              OrdenCompra(2, "16/10/2026", None, 7500)
                              ]

        for orden in lista_orden_compra:
            boton_ver_orden = BotonSecundarioWidget("Ver orden", ancho_fijo=False)
            boton_ver_orden.clicked.connect(lambda orden_obj=orden: self.abrir_vista_detalles(orden_obj))
            self.vista_lista_ordenes_compra.crear_fila_tabla_ordenes_compra(orden, boton_ver_orden)

    def abrir_vista_crear_orden(self):
        pass

    def abrir_vista_detalles(self, orden_compra):
        pass

    def remover_ultima_vista(self) -> None:
        """
        Borra la referencia el layout anterior al asignarlo a un widget que no será guardado.
        """

        QWidget().setLayout(self.layout())

    def resizeEvent(self, event):
        pass