from pathlib import Path

from PySide6.QtWidgets import *
from PySide6.QtCore import Signal
from PySide6.QtGui import *

from views.widgets.TablaResponsivaRegular import TablaResponsivaRegular

class VistaTablaVentas(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.layout.setSpacing(75)

        self.titulo = QLabel("Ventas")
        self.titulo.setProperty("cssClass", "titulo")

        self.tabla_merma = TablaResponsivaRegular()
        self.configurar_tabla_ventas()

        self.layout.addWidget(self.titulo)
        self.layout.addWidget(self.tabla_merma)

        self.setLayout(self.layout)

        self.setStyleSheet((Path('views/styles/estilos_ventas.qss').read_text()))

    def configurar_tabla_ventas(self):
        encabezados = ["Fecha", "Comensales", "Monto total", "Platillos"]

        self.tabla_merma.setColumnCount(4)
        self.tabla_merma.setHorizontalHeaderLabels(encabezados)
        self.tabla_merma.verticalHeader().show()
        self.tabla_merma.showGrid()