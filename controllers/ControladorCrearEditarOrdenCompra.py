from PySide6.QtCore import QObject, Slot

from models.Insumo import Insumo
from models.OrdenCompra import OrdenCompra
from views.VistaCrearEditarOrdenCompra import VistaCrearEditarOrdenCompra

class ControladorCrearEditarOrdenCompra(QObject):
    """
    Controlador para la vista de crear editar una orden de compra.

    :param vista: (VistaCrearEditarOrdenCompra): Vista del formulario para crear o editar una orden de compra.
    :param servicio: (Servicio): Clase servicio para la VistaCrearEditarOrdenCompra.
    """

    def __init__(self, vista:VistaCrearEditarOrdenCompra, servicio=None):
        super().__init__()
        self.vista = vista
        self.servicio = servicio

        self.vista.obtener_insumos_signal.connect(self.pasar_todos_insumos_combobox)
        self.vista.llenar_forma_signal.connect(self.llenar_tabla_editar)
        self.vista.llenar_forma_signal.connect(lambda: self.llenar_tabla_editar)
        # self.vista.guardar_orden_compra_signal.connect()

    def pasar_todos_insumos_combobox(self) -> None:
        """
        Conecta con la capa servicios para obtener todos los insumos de la BD y los pasa a la vista para mostrarlos
        como opciones del combobox para cada fila de la tabla.
        """

        lista_insumos_test = [
            Insumo(1, "Arroz", None, None, None, None, None, None),
            Insumo(2, "Papas", None, None, None, None, None, None),
            Insumo(3, "Pescado", None, None, None, None, None, None),
            Insumo(4, "Tomate", None, None, None, None, None, None)
        ]

        self.vista.asignar_insumos_combobox(lista_insumos_test)

    @Slot(OrdenCompra)
    def llenar_tabla_editar(self, orden_compra:OrdenCompra) -> None:
        """
        Conecta con la capa servicios para obtener los insumos de una lista de compras asociada a una orden de compra
        y agrega una fila a la tabla por cada uno.

        :param orden_compra: (OrdenCompra): Orden de compra de la que obtiene la lista de compras.

        """

        lista_insumos_test = [
            Insumo(1, "Arroz", None, None, None, None, None, None),
            Insumo(2, "Papas", None, None, None, None, None, None),
            Insumo(3, "Pescado", None, None, None, None, None, None),
            Insumo(4, "Tomate", None, None, None, None, None, None)
        ]

        for entrada in lista_insumos_test:
            if entrada.num == 4:
                self.vista.agregar_fila_tabla_compras(entrada.nombre, 5, "kilos", "21-10-2026", 586)
                continue

            self.vista.agregar_fila_tabla_compras(entrada.nombre, 5, "kilos")

