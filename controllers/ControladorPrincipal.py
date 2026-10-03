from PySide6 import QtCore, QtWidgets, QtGui

from views.VistaPrincipal import VistaPrincipal
from views.VistaBarraHerramientas import VistaBarraHerramientas

class ControladorPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self._vista_principal = VistaPrincipal()
        self.setCentralWidget(self._vista_principal)

        # Agrega barra de herramientas
        self.barra_herramientas = VistaBarraHerramientas()
        self.addToolBar(QtCore.Qt.LeftToolBarArea, self.barra_herramientas.obten_barra_herramientas())
        self.setStatusBar(QtWidgets.QStatusBar(self))
