from pathlib import Path

from PySide6.QtWidgets import *
from PySide6.QtCore import Signal
from PySide6.QtGui import *

from views.widgets.TablaResponsivaRegular import TablaResponsivaRegular


class VistaTablaInventario(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.layout.setSpacing(75)

        self.titulo = QLabel("Inventario")
        self.titulo.setProperty("cssClass", "titulo")

        self.tabla_insumos = TablaResponsivaRegular()
        self.configurar_tabla_insumos()

        self.layout.addWidget(self.titulo)
        self.layout.addWidget(self.tabla_insumos)

        self.setLayout(self.layout)

        self.setStyleSheet((Path('views/styles/estilos_inventario.qss').read_text()))

    def configurar_tabla_insumos(self):
        encabezados = ["Nombre", "Fecha compra", "Fecha caducidad", "Precio unitario\nde compra", "Umbral", "Stock", "Unidad de medida", "Tipo", "Marca"]

        self.tabla_insumos.setColumnCount(9)
        self.tabla_insumos.setHorizontalHeaderLabels(encabezados)
        self.tabla_insumos.verticalHeader().show()
        self.tabla_insumos.showGrid()

