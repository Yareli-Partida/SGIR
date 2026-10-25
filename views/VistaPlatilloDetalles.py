from pathlib import Path
from typing import cast

from PySide6 import QtCore
from PySide6.QtWidgets import *
from PySide6.QtCore import Signal
from PySide6.QtGui import *

from models.Categoria import Categoria
from models.Platillo import Platillo
from models.Receta import Receta
from views.widgets.BotonPrincipalWidget import BotonPrincipalWidget
from views.widgets.EspacioHorizontalWidget import EspacioHorizontalWidget
from views.widgets.TablaResponsivaRegular import TablaResponsivaRegular


class VistaPlatilloDetalles(QWidget):

    mostrar_detalles_signal = Signal(Platillo)
    volver_vista_anterior_signal = Signal()
    abrir_vista_editar_signal = Signal(Platillo)

    def __init__(self, platillo:Platillo):
        super().__init__()

        self.layout = QGridLayout()
        self.layout.setVerticalSpacing(50)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.boton_volver = BotonPrincipalWidget("Volver")
        self.boton_volver.setFixedWidth(self.boton_volver.sizeHint().width() * 2)
        self.boton_volver.clicked.connect(self.emitir_evento_volver)
        self.boton_editar_menu = BotonPrincipalWidget("Editar")
        self.boton_editar_menu.setFixedWidth(self.boton_editar_menu.sizeHint().width() * 2)
        self.boton_editar_menu.clicked.connect(lambda: self.emitir_evento_editar(platillo))

        self.contenedor_botones = QWidget()
        self.contenedor_botones.setLayout(QHBoxLayout())
        self.contenedor_botones.layout().addWidget(self.boton_volver)
        self.contenedor_botones.layout().addSpacerItem(EspacioHorizontalWidget())
        self.contenedor_botones.layout().addWidget(self.boton_editar_menu)
        self.contenedor_botones.setFixedHeight(self.contenedor_botones.sizeHint().height())

        self.titulo = QLabel(platillo.nombre)
        self.titulo.setProperty("cssClass", "titulo")

        self.tabla_detalles = TablaResponsivaRegular()
        self.configurar_tabla()

        self.layout.addWidget(self.contenedor_botones, 0, 0)
        self.layout.addWidget(self.titulo, 1, 0)
        self.layout.addWidget(self.tabla_detalles, 2, 0)

        self.setLayout(self.layout)

        self.setStyleSheet((Path('views/styles/estilos_platillos.qss').read_text()))

    def configurar_tabla(self):
        encabezados_blanco = ["", ""]
        self.tabla_detalles.setColumnCount(2)
        self.tabla_detalles.setRowCount(4)
        self.tabla_detalles.setHorizontalHeaderLabels(encabezados_blanco)

    def llenar_tabla_detalles(self, platillo:Platillo, categoria_nom:str, receta_nom:str, precio_actual:str):

        nombre_indicador = QTableWidgetItem("Nombre")
        nombre_indicador.setFlags(QtCore.Qt.ItemFlag.ItemIsEditable)
        nombre_platillo_cell = QTableWidgetItem(platillo.nombre)
        nombre_platillo_cell.setFlags(QtCore.Qt.ItemFlag.ItemIsEditable)

        categoria_indicador = QTableWidgetItem("Categoría")
        categoria_indicador.setFlags(QtCore.Qt.ItemFlag.ItemIsEditable)
        nombre_categoria_cell = QTableWidgetItem(categoria_nom)
        nombre_categoria_cell.setFlags(QtCore.Qt.ItemFlag.ItemIsEditable)

        receta_indicador = QTableWidgetItem("Receta base")
        receta_indicador.setFlags(QtCore.Qt.ItemFlag.ItemIsEditable)
        nombre_receta_cell = QTableWidgetItem(receta_nom)
        nombre_receta_cell.setFlags(QtCore.Qt.ItemFlag.ItemIsEditable)

        precio_actual_indicador = QTableWidgetItem("Precio actual")
        precio_actual_indicador.setFlags(QtCore.Qt.ItemFlag.ItemIsEditable)
        precio_actual_cell = QTableWidgetItem(f"${precio_actual}")
        precio_actual_cell.setFlags(QtCore.Qt.ItemFlag.ItemIsEditable)

        self.tabla_detalles.setItem(0, 0, nombre_indicador)
        self.tabla_detalles.setItem(0, 1, nombre_platillo_cell)
        self.tabla_detalles.setItem(1, 0, categoria_indicador)
        self.tabla_detalles.setItem(1, 1, nombre_categoria_cell)
        self.tabla_detalles.setItem(2, 0, receta_indicador)
        self.tabla_detalles.setItem(2, 1, nombre_receta_cell)
        self.tabla_detalles.setItem(3, 0, precio_actual_indicador)
        self.tabla_detalles.setItem(3, 1, precio_actual_cell)

    def emitir_evento_volver(self):
        self.volver_vista_anterior_signal.emit()

    def emitir_evento_editar(self, platillo:Platillo):
        self.abrir_vista_editar_signal.emit(platillo)