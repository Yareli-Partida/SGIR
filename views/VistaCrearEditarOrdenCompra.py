from PySide6 import QtCore
from PySide6.QtCore import QDateTime, QDate
from PySide6.QtWidgets import *
from PySide6.QtGui import Qt

from models.Insumo import Insumo
from models.OrdenCompra import OrdenCompra
from views.widgets.BotonPrincipalWidget import BotonPrincipalWidget
from views.widgets.EspacioHorizontalWidget import EspacioHorizontalWidget
from views.widgets.BotonSecundarioWidget import BotonSecundarioWidget
from views.widgets.TablaResponsivaRegular import TablaResponsivaRegular

class VistaCrearEditarOrdenCompra(QVBoxLayout):
    """
    Vista para crear y editar órdenes de compra.

    :param orden_compra: (None/OrdenCompra): Orden de compra a editar.

    :var titulo: (QLabel): Título principal de la vista.
    :var contenedor_botones: (QWidget): Contiene los botones guardar y volver.
    :var boton_guardar: (BotonPrincipalWidget): Botón para guardar la info actual en la forma en la orden actual o una nueva.
    :var boton_volver: (BotonPrincipalWidget): Botón para volver a la vista anterior.
    :var boton_agregar_insumo: (BotonSecundarioWidget): Botón para agregar una nueva fila a la tabla lista compras.
    :var tabla_lista_compras: (TablaResponsivaRegular): Muestra los insumos de la lista de compras de la orden.
    """

    def __init__(self, orden_compra=None):
        super().__init__()

        self.setSpacing(15)

        self.titulo = QLabel()
        self.titulo.setObjectName("titulo_principal_editar_crear")
        self.titulo.setProperty("cssClass", "titulo")

        self.contenedor_botones = QWidget()
        self.contenedor_botones.setLayout(QHBoxLayout())
        self.boton_volver = BotonPrincipalWidget("Volver")
        self.boton_volver.setFixedWidth(self.boton_volver.sizeHint().width() * 2)
        self.boton_guardar = BotonPrincipalWidget("Guardar")
        self.boton_guardar.setFixedWidth(self.boton_guardar.sizeHint().width() * 2)
        self.contenedor_botones.layout().addWidget(self.boton_volver)
        self.contenedor_botones.layout().addSpacerItem(EspacioHorizontalWidget())
        self.contenedor_botones.layout().addWidget(self.boton_guardar)

        self.boton_agregar_insumo = BotonSecundarioWidget("Agregar insumo", True)
        self.boton_agregar_insumo.clicked.connect(self.agregar_fila_tabla_compras)

        self.tabla_lista_compras = TablaResponsivaRegular()
        self.configurar_tabla_compras()

        if orden_compra:
            self.titulo.setText(f"Editar Orden #{orden_compra.num}")
        else:
            self.titulo.setText("Crear orden de compra")

        self.addWidget(self.contenedor_botones)
        self.addWidget(self.titulo)
        self.addWidget(self.boton_agregar_insumo)
        self.addWidget(self.tabla_lista_compras)

    def configurar_tabla_compras(self) -> None:
        """
        Configura columnas y encabezados de la tabla de lista de compras.
        :return:
        """

        self.tabla_lista_compras.setColumnCount(6)
        encabezados = ["Comprado", "Insumo", "Cantidad", "Unidad de medida",  "Fecha de compra", "Importe"]
        self.tabla_lista_compras.setHorizontalHeaderLabels(encabezados)

    def agregar_fila_tabla_compras(self, nom_insumo=None, cant=None, un_medida=None, fecha_compra=None, importe=None) -> None:
        """
        Agrega una fila a la tabla de lista de compras en blanco o llena. Los widgets mostrados dependen de si
        hay artículos comprados.

        :return:
        """

        lista_insumos_test = [
            Insumo(1, "Arroz", None, None, None, None, None, None),
            Insumo(2, "Papas", None, None, None, None, None, None),
            Insumo(3, "Pescado", None, None, None, None, None, None),
            Insumo(4, "Tomate", None, None, None, None, None, None)
        ]

        lista_unidades = ["kilos", "gramos"]
        lista_nombres = [insumo.nombre for insumo in lista_insumos_test]

        self.tabla_lista_compras.setRowCount(self.tabla_lista_compras.rowCount() + 1)
        fila_idx = self.tabla_lista_compras.rowCount() - 1

        contenedor_checkbox = QWidget()
        contenedor_checkbox.setLayout(QHBoxLayout())
        contenedor_checkbox.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        checkbox_comprado = QCheckBox()
        checkbox_comprado.setFixedWidth(int(checkbox_comprado.sizeHint().width() * 1.5))
        checkbox_comprado.setFixedHeight(int(checkbox_comprado.sizeHint().height() * 1.5))
        checkbox_comprado.setEnabled(True)
        checkbox_comprado.stateChanged.connect(lambda state, idx=fila_idx, cb=checkbox_comprado: self.toggle_selectores_opcionales(cb, idx))
        contenedor_checkbox.layout().addWidget(checkbox_comprado)

        if fecha_compra:
            checkbox_comprado.setChecked(True)
            checkbox_comprado.setEnabled(False)

            selector_fecha = self.tabla_lista_compras.cellWidget(fila_idx, 4)
            selector_fecha.setDate(QDate.fromString(fecha_compra))
            selector_fecha.setEnabled(False)
            selector_importe = self.tabla_lista_compras.cellWidget(fila_idx, 5)
            selector_importe.setValue(importe)
            selector_importe.setEnabled(False)

        elif not fecha_compra and not nom_insumo:
            checkbox_comprado.setChecked(False)
            checkbox_comprado.setEnabled(False)

        selector_insumo = QComboBox()
        selector_insumo.insertItems(len(lista_nombres), lista_nombres)
        selector_insumo.setCurrentIndex(-1)

        if nom_insumo:
            selector_insumo.setCurrentIndex(lista_nombres.index(nom_insumo))
            if fecha_compra:
                selector_insumo.setEnabled(False)

        selector_cantidad = QDoubleSpinBox()
        selector_cantidad.setMaximum(999999)

        if cant:
            selector_cantidad.setValue(cant)
            if fecha_compra:
                selector_cantidad.setEnabled(False)

        selector_unidad_medida = QComboBox()
        selector_unidad_medida.insertItems(len(lista_unidades), lista_unidades)
        selector_unidad_medida.setCurrentIndex(-1)

        if un_medida:
            selector_unidad_medida.setCurrentIndex(lista_unidades.index(un_medida))
            if fecha_compra:
                selector_unidad_medida.setEnabled(False)

        self.tabla_lista_compras.setCellWidget(fila_idx, 0, contenedor_checkbox)
        self.tabla_lista_compras.setCellWidget(fila_idx, 1, selector_insumo)
        self.tabla_lista_compras.setCellWidget(fila_idx, 2, selector_cantidad)
        self.tabla_lista_compras.setCellWidget(fila_idx, 3, selector_unidad_medida)

        celda_placeholder_1 = QTableWidgetItem()
        celda_placeholder_1.setFlags(QtCore.Qt.ItemFlag.ItemIsEditable)

        celda_placeholder_2 = QTableWidgetItem()
        celda_placeholder_2.setFlags(QtCore.Qt.ItemFlag.ItemIsEditable)

        self.tabla_lista_compras.setItem(fila_idx, 4, celda_placeholder_1)
        self.tabla_lista_compras.setItem(fila_idx, 5, celda_placeholder_2)

    def toggle_selectores_opcionales(self, checkbox:QCheckBox, fila_idx:int) -> None:
        """
        Agrega o quita los selectores opcionales de fecha de compra e importe cuando el producto
        en función de si el insumo se marca como comprado o no.
        Solo funciona con entradas nuevas (no guardadas en la BD).

        :param checkbox: (QCheckBox): La checkbox al que se conectará la función toggle.
        :param fila_idx: (int): El índice de la tabla lista de compras donde se modifican los selectores.
        :return:
        """

        if checkbox.isChecked():
            self.agregar_selectores_opcionales(fila_idx)
        else:
            celda_placeholder = QTableWidgetItem()
            celda_placeholder.setFlags(QtCore.Qt.ItemFlag.ItemIsEditable)

            self.tabla_lista_compras.removeCellWidget(fila_idx, 4)
            self.tabla_lista_compras.setItem(fila_idx, 4, celda_placeholder)

            self.tabla_lista_compras.removeCellWidget(fila_idx, 5)
            self.tabla_lista_compras.setItem(fila_idx, 5, celda_placeholder)

    def agregar_selectores_opcionales(self, fila_idx) -> None:
        """
        Lógica para agregar selectores opcionales de fecha de compra e importe.

        :param fila_idx: El índice de la tabla lista de compras donde se agregan los selectores.
        :return:
        """

        fecha = QDateTime.currentDateTime()
        selector_fecha_compra = QDateEdit()
        selector_fecha_compra.setDateTime(fecha)
        selector_fecha_compra.setCalendarPopup(True)
        selector_fecha_compra.setDisplayFormat("dd-MM-yyyy")

        self.tabla_lista_compras.setCellWidget(fila_idx, 4, selector_fecha_compra)

        selector_importe = QDoubleSpinBox()
        selector_importe.setMaximum(999999)
        selector_importe.setPrefix("$")

        self.tabla_lista_compras.setCellWidget(fila_idx, 5, selector_importe)
