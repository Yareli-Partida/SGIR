from PySide6.QtCore import QObject, Slot

from models.Insumo import Insumo
from models.OrdenCompra import OrdenCompra
from views.VistaOrdenesCompraDetalles import VistaOrdenesCompraDetalles


class ControladorDetallesOrdenCompra(QObject):
    """
    Controlador para la vista que muestra los detalles de una orden de compra en particular y su lista de compras.

    :param vista: (VistaOrdenesCompraDetalles): Vista que muestra los detalles de una orden de compra.
    :param servicio: (Servicio): Clase servicio para la VistaOrdenesCompraDetalles.

    """

    def __init__(self, vista:VistaOrdenesCompraDetalles, servicio=None):
        super().__init__()
        self.vista = vista
        self.servicio = servicio

        self.vista.mostrar_detalles_signal.connect(self.llenar_tabla_detalles)
        self.vista.mostrar_detalles_signal.connect(lambda: self.llenar_tabla_detalles)

    @Slot(OrdenCompra)
    def llenar_tabla_detalles(self, orden_compra:OrdenCompra) -> None:
        """
        Conecta con la capa de servicios para obtener la lista de insumos de la orden de compra
        y crea una fila en tabla de la VistaOrdenesCompraDetalles por cada orden.

        :param orden_compra: (OrdenCompra): Orden de compra a mostrar.
        :return:
        """

        lista_insumos_test = [
            Insumo(1, "Arroz", None, None, None, None, None, None),
            Insumo(2, "Papas", None, None, None, None, None, None),
            Insumo(3, "Pescado", None, None, None, None, None, None),
            Insumo(4, "Tomate", None, None, None, None, None, None)
        ]

        for entrada in lista_insumos_test:
            # para test
            if entrada.num == 4:
                self.vista.crear_fila_tabla(entrada.nombre, 5, "kilos", "21-10-2026", 586)
                continue

            self.vista.crear_fila_tabla(entrada.nombre, 5, "kilos")