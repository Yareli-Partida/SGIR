from pathlib import Path

from PySide6 import QtCore
from PySide6.QtGui import Qt, QColor
from PySide6.QtWidgets import *
from PySide6.QtCore import Signal

from models.OrdenCompra import OrdenCompra
from views.widgets.BotonPrincipalWidget import BotonPrincipalWidget
from views.widgets.BotonSecundarioWidget import BotonSecundarioWidget
from views.widgets.TablaResponsivaDesigual import TablaResponsivaDesigual

class VistaListaOrdenesCompra(QWidget):
    """
    Vista de la lista de todas las órdenes de compra.

    :var mostrar_ordenes_signal: (Signal): Señal para enlistar todas las órdenes de compra.
    :var abrir_crear_orden_signal: (Signal): Señal para ir a la vista de crear.
    :var abrir_detalles_orden_signal: (Signal(Menu)): Señal para ir a la vista de detalles.
    :var titulo: (QLabel): Título principal de la vista.
    :var boton_crear_orden_compra: (BotonPrincipalWidget): Botón para ir a la vista para crear una orden de compra.
    :var contenedor_titulo: (QWidget): Contiene el título de la vista y el botón para crear una orden de compra.
    :var tabla_ordenes_compra: (QTableWidget): Tabla que muestra todas las órdenes de compras.

    """

    mostrar_ordenes_signal = Signal()
    abrir_crear_orden_signal = Signal()
    abrir_detalles_orden_signal = Signal(OrdenCompra)

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.layout.setSpacing(45)

        self.titulo = QLabel("Ordenes de Compra")
        self.titulo.setProperty("cssClass", "titulo")
        self.titulo.setObjectName("titulo_principal_lista_ordenes")

        self.boton_crear_orden_compra = BotonPrincipalWidget("Crear orden")
        self.boton_crear_orden_compra.clicked.connect(self.emitir_evento_abrir_crear_orden)

        self.contenedor_titulo = QWidget()
        self.contenedor_titulo.setObjectName("contenedor_titulo")
        self.contenedor_titulo.setLayout(QHBoxLayout())
        self.contenedor_titulo.layout().addWidget(self.titulo)
        self.contenedor_titulo.layout().addWidget(self.boton_crear_orden_compra)

        self.tabla_ordenes_compra = TablaResponsivaDesigual()
        self.tabla_ordenes_compra.setObjectName("tabla_ordenes_compra")
        encabezados = ["Número de orden", "Fecha de creación", "Estado", ""]
        self.tabla_ordenes_compra.setObjectName("tabla_ordenes_compra")
        self.tabla_ordenes_compra.setColumnCount(4)
        self.tabla_ordenes_compra.verticalHeader().hide()
        self.tabla_ordenes_compra.setHorizontalHeaderLabels(encabezados)
        self.tabla_ordenes_compra.setShowGrid(False)

        self.layout.addWidget(self.contenedor_titulo)
        self.layout.addWidget(self.tabla_ordenes_compra)
        self.setLayout(self.layout)

        self.setStyleSheet((Path('views/styles/estilos_ordenes_compra.qss').read_text()))

    def crear_fila_tabla_ordenes_compra(self, orden_compra:OrdenCompra) -> None:
        """
        Crea una fila llena en la tabla de órdenes de compra

        :param orden_compra: (OrdenCompra): La orden de compra que se mostrará.
        :return:
        """
        self.tabla_ordenes_compra.setRowCount(self.tabla_ordenes_compra.rowCount() + 1)
        current_row = self.tabla_ordenes_compra.rowCount() - 1

        orden_compra_num = QTableWidgetItem(str(orden_compra.num))
        orden_compra_num.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        orden_compra_num.setFlags(QtCore.Qt.ItemFlag.ItemIsEditable)

        orden_compra_fecha_creacion = QTableWidgetItem(orden_compra.fecha_creacion)
        orden_compra_fecha_creacion.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        orden_compra_fecha_creacion.setFlags(QtCore.Qt.ItemFlag.ItemIsEditable)
        # hardcoded para testeo
        orden_estado = QTableWidgetItem("En Progreso")
        orden_estado.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        orden_estado.setFlags(QtCore.Qt.ItemFlag.ItemIsEditable)

        if orden_estado.text() == "En Progreso":
            orden_estado.setBackground(QColor.fromRgb(255, 178, 0))
        elif orden_estado.text() == "Terminada":
            orden_estado.setBackground(QColor.fromRgb(57, 255, 0))
        elif orden_estado.text() == "Cancelada":
            orden_estado.setBackground(QColor.fromRgb(255, 44, 0))

        boton_detalles = BotonSecundarioWidget("Ver orden")
        boton_detalles.clicked.connect(lambda: self.emitir_evento_abrir_detalles_orden(orden_compra))

        self.tabla_ordenes_compra.setItem(current_row, 0, orden_compra_num)
        self.tabla_ordenes_compra.setItem(current_row, 1, orden_compra_fecha_creacion)
        self.tabla_ordenes_compra.setItem(current_row, 2, orden_estado)
        self.tabla_ordenes_compra.setCellWidget(current_row, 3, boton_detalles)

    def emitir_evento_abrir_crear_orden(self) -> None:
        """
        Emite la señal para abrir la vista de crear orden de compra.
        """

        self.abrir_crear_orden_signal.emit()

    def emitir_evento_abrir_detalles_orden(self, orden:OrdenCompra) -> None:
        """
        Emite la señal para abrir la vista de detalles.
        """

        self.abrir_detalles_orden_signal.emit(orden)
