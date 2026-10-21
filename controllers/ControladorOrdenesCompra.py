from PySide6.QtWidgets import QWidget
from pathlib import Path

from views.VistaListaOrdenesCompra import VistaListaOrdenesCompra
from views.VistaOrdenesCompraDetalles import VistaOrdenesCompraDetalles
from views.widgets.BotonSecundarioWidget import BotonSecundarioWidget
from models.OrdenCompra import OrdenCompra
from models.Insumo import Insumo

class ControladorOrdenesCompra(QWidget):
    def __init__(self):
        super().__init__()
        self.vista_lista_ordenes_compra = None
        self.vista_orden_compra_detalles = None

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
            boton_ver_orden.clicked.connect(lambda state, orden_obj=orden: self.abrir_vista_detalles(orden_obj))
            self.vista_lista_ordenes_compra.crear_fila_tabla_ordenes_compra(orden, boton_ver_orden)

    def abrir_vista_crear_orden(self):
        pass

    def abrir_vista_detalles(self, orden_compra:OrdenCompra) -> None:
        """
        Crea un obj de VistaOrdenesCompraDetalles, conecta los botones de la vista a sus respectivas funciones
        y cambia el layout actual.
        :param orden_compra: (OrdenCompra): Orden de compra a mostrar.
        :return:
        """

        self.remover_ultima_vista()
        self.vista_orden_compra_detalles = VistaOrdenesCompraDetalles(orden_compra)
        self.vista_orden_compra_detalles.setObjectName("vista_orden_compra_detalles")
        self.vista_orden_compra_detalles.boton_volver.clicked.connect(self.abrir_vista_lista_ordenes_compra)
        self.vista_orden_compra_detalles.boton_editar.clicked.connect(lambda state, orden_obj=orden_compra: self.abrir_vista_editar_orden_compra(orden_obj))

        self.setLayout(self.vista_orden_compra_detalles)
        self.llenar_tabla_detalles(orden_compra)

    def llenar_tabla_detalles(self, orden_compra: OrdenCompra) -> None:
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
            self.vista_orden_compra_detalles.crear_fila_tabla(entrada.nombre, 5, "kilos", "")

    def abrir_vista_editar_orden_compra(self, orden_compra:OrdenCompra) -> None :
        pass

    def remover_ultima_vista(self) -> None:
        """
        Borra la referencia el layout anterior al asignarlo a un widget que no será guardado.
        """

        QWidget().setLayout(self.layout())

    def resizeEvent(self, event):
        pass