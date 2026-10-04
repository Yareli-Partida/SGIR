from PySide6 import QtWidgets


class VistaRecetaDetalles(QtWidgets.QWidget):
    def __init__(self, receta):
        super().__init__()

        self.layout = QtWidgets.QGridLayout(self)
        self.titulo = QtWidgets.QLabel(receta.nombre)
        self.titulo.setObjectName("titulo")
        self.layout.addWidget(self.titulo)
        self.tabla_ingredientes = QtWidgets.QTableWidget()

        self.setLayout(self.layout)
