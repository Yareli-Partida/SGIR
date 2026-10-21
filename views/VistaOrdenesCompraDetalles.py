from PySide6.QtWidgets import *
from PySide6.QtGui import Qt

from models.OrdenCompra import OrdenCompra
from views.widgets.EspacioHorizontalWidget import EspacioHorizontalWidget
from views.widgets.BotonPrincipalWidget import BotonPrincipalWidget
from views.widgets.TablaResponsivaDesigual import TablaResponsivaDesigual

class VistaOrdenesCompraDetalles(QVBoxLayout):
    """
    Vista para ver detalles de una orden de compra.

    :param orden_compra: (OrdenCompra): Orden de compra a mostrar.

    :var contenedor_botones: (QWidget): Contiene los botones volver y editar.
    :var boton_volver: (BotonPrincipalWidget): Botón para ir a la vista anterior.
    :var boton_editar: (BotonPrincipalWidget): Botón para ir a la vista editar con la orden de compra actual.
    :var titulo: (QLabel): Título principal de la orden de compra.
    :var etiqueta_fecha_creacion: (QLabel): Muestra la fecha de creación de la orden de compra.
    :var etiqueta_fecha_cierre: (QLabel): Muestra la fecha de cierre de la orden de compra.
    :var etiqueta_edo_orden: (QLabel): Muestra el estado actual de la orden de compra.
    :var tabla_lista_compras: (TablaResponsivaDesigual): Muestra los insumos de la orden de compra.

    """

    def __init__(self, orden_compra:OrdenCompra):
        super().__init__()

        self.setSpacing(15)

        self.contenedor_botones = QWidget()
        self.contenedor_botones.setLayout(QHBoxLayout())
        self.boton_volver = BotonPrincipalWidget("Volver")
        self.boton_volver.setFixedWidth(self.boton_volver.sizeHint().width() * 2)
        self.boton_editar = BotonPrincipalWidget("Editar")
        self.boton_editar.setFixedWidth(self.boton_editar.sizeHint().width() * 2)
        self.contenedor_botones.layout().addWidget(self.boton_volver)
        self.contenedor_botones.layout().addSpacerItem(EspacioHorizontalWidget())
        self.contenedor_botones.layout().addWidget(self.boton_editar)

        self.titulo = QLabel(f"Orden #{orden_compra.num}")
        self.titulo.setProperty("cssClass", "titulo")

        self.etiqueta_fecha_creacion = QLabel(f"Fecha de creación: {orden_compra.fecha_creacion}",
                                              alignment=Qt.AlignmentFlag.AlignLeft)

        if orden_compra.fecha_cierre is not None:
            orden_fecha_cierre = orden_compra.fecha_cierre
        else:
            orden_fecha_cierre = "N/A"

        self.etiqueta_fecha_cierre = QLabel(f"Fecha de cierre: {orden_fecha_cierre}",
                                            alignment=Qt.AlignmentFlag.AlignLeft)

        # self.etiqueta_edo_orden = QLabel(orden_compra.estado_orden)
        # Aún no hay propiedad estado_orden en la clase
        self.etiqueta_edo_orden = QLabel("En Progreso", alignment=Qt.AlignmentFlag.AlignCenter)
        self.etiqueta_edo_orden.setFixedWidth(int(self.etiqueta_edo_orden.sizeHint().width() * 1.25))
        self.etiqueta_edo_orden.setFixedHeight(int(self.etiqueta_edo_orden.sizeHint().height() * 1.25))
        self.etiqueta_edo_orden.setObjectName("etiqueta_edo_orden")

        if self.etiqueta_edo_orden.text() == "En Progreso":
            self.etiqueta_edo_orden.setProperty("cssClass", "en_progreso")
        elif self.etiqueta_edo_orden.text() == "Terminada":
            self.etiqueta_edo_orden.setProperty("cssClass", "terminada")
        elif self.etiqueta_edo_orden.text() == "Cancelada":
            self.etiqueta_edo_orden.setProperty("cssClass", "cancelada")

        self.tabla_lista_compras = TablaResponsivaDesigual()
        self.tabla_lista_compras.setObjectName("tabla_lista_compras")
        self.configurar_tabla_lista_compras()

        self.addWidget(self.contenedor_botones)
        self.addWidget(self.titulo)
        self.addWidget(self.etiqueta_fecha_creacion)
        self.addWidget(self.etiqueta_fecha_cierre)
        self.addWidget(self.etiqueta_edo_orden)
        self.addWidget(self.tabla_lista_compras)

    def configurar_tabla_lista_compras(self) -> None:
        """
        Configura encabezados y columnas de la tabla lista de compras.

        :return:
        """

        encabezados = ["", "Nombre insumo", "Cantidad", "Unidad de medida",  "Fecha de compra", "Importe"]

        self.tabla_lista_compras.setColumnCount(6)
        self.tabla_lista_compras.setHorizontalHeaderLabels(encabezados)
        self.tabla_lista_compras.setShowGrid(False)

    def crear_fila_tabla(self, nombre_insumo:str, cant:float, unidad_med:str, importe=None, fecha_compra=None) -> None:
        """
        Crea una fila en la tabla con los datos de un insumo a comprar.

        :param nombre_insumo: (str): Nombre del insumo que se mostrará.
        :param cant: (float): Cantidad que se comprará del insumo.
        :param unidad_med: (str): Unidad de medida de la compra.
        :param importe: (None/float): Precio de la compra, solo aplica si ya se compró
        :param fecha_compra: (None/str): Fecha de compra del producto si ya se compró, opcional.
        :return:
        """

        self.tabla_lista_compras.setRowCount(self.tabla_lista_compras.rowCount() + 1)
        fila_idx = self.tabla_lista_compras.rowCount() - 1

        # checkbox marcado en función de si ya se compró o no
        contenedor_checkbox = QWidget()
        contenedor_checkbox.setLayout(QHBoxLayout())
        contenedor_checkbox.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        checkbox = QCheckBox()
        checkbox.setChecked(True)
        checkbox.setEnabled(False)
        contenedor_checkbox.layout().addWidget(checkbox)

        celda_nombre_insumo = QTableWidgetItem(nombre_insumo)
        celda_nombre_insumo.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        celda_cantidad = QTableWidgetItem(str(cant))
        celda_cantidad.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        celda_unidad_medida = QTableWidgetItem(str(unidad_med))
        celda_unidad_medida.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        if fecha_compra:
            celda_fecha_compra = QTableWidgetItem(str(fecha_compra))
        else:
            celda_fecha_compra = QTableWidgetItem("N/A")

        celda_fecha_compra.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        if importe:
            celda_importe = QTableWidgetItem(str(importe))
        else:
            celda_importe = QTableWidgetItem("N/A")

        celda_importe.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tabla_lista_compras.setCellWidget(fila_idx, 0, contenedor_checkbox)
        self.tabla_lista_compras.setItem(fila_idx, 1, celda_nombre_insumo)
        self.tabla_lista_compras.setItem(fila_idx, 2, celda_cantidad)
        self.tabla_lista_compras.setItem(fila_idx, 3, celda_unidad_medida)
        self.tabla_lista_compras.setItem(fila_idx, 4, celda_fecha_compra)
        self.tabla_lista_compras.setItem(fila_idx, 5, celda_importe)
