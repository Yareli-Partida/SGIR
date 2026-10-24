from PySide6.QtCore import QObject, Slot

from models.OrdenCompra import OrdenCompra
from views.VistaListaOrdenesCompra import VistaListaOrdenesCompra


class ControladorListaOrdenesCompra(QObject):
    """
    Controlador para la vista que muestra todas las órdenes de compra en la BD.

    :param vista: (VistaListaOrdenesCompra): Vista que muestra las órdenes de compra.
    :param servicio: (Servicio): Clase servicio para la VistaListaOrdenesCompra.

    """

    def __init__(self, vista:VistaListaOrdenesCompra, servicio=None):
        super().__init__()
        self.vista = vista
        self.servicio = servicio

        self.vista.mostrar_ordenes_signal.connect(lambda: self.mostrar_tabla_ordenes_compra())

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
            self.vista.crear_fila_tabla_ordenes_compra(orden)
