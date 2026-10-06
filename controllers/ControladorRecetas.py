from PySide6 import QtWidgets
from pathlib import Path

from views.VistaRecetas import VistaRecetas
from views.VistaRecetaDetalles import VistaRecetaDetalles
from views.VistaCrearEditarReceta import VistaCrearEditarReceta
from models.Receta import Receta

class ControladorRecetas(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self._layout = QtWidgets.QVBoxLayout()

        self._vista_lista_recetas = VistaRecetas()
        self._vista_lista_recetas.setObjectName("vista_lista_recetas")

        self._vista_receta_detalles = None

        self._vista_crear_receta = VistaCrearEditarReceta()
        self._vista_crear_receta.setObjectName("vista_crear_receta")

        self._vista_editar_receta = None

        self._layout.addWidget(self._vista_lista_recetas)
        self.setLayout(self._layout)

        crear_receta_boton = self._vista_lista_recetas.findChild(QtWidgets.QPushButton, "boton_crear_receta")
        crear_receta_boton.clicked.connect(self.abrir_crear_receta)

        # esto es solo para testeo manual
        self.mostrar_lista_recetas([Receta(1, "Pasta en salsa de tomate", "", 10)])

        self.setStyleSheet((Path('views/styles/estilos_recetas.qss').read_text()))

    def abrir_vista_lista_recetas(self):
        self.remove_last_view()
        self._layout.addWidget(self._vista_lista_recetas)

    def mostrar_lista_recetas(self, lista_recetas:list):
        for receta in lista_recetas:
            boton_detalles = self._vista_lista_recetas.crear_boton_detalles()
            # aparentemente clicked.connect no toma funciones con argumentos, para hacerlo usa lambda
            boton_detalles.clicked.connect(lambda: self.abrir_vista_detalles_receta(receta))

            self._vista_lista_recetas.crear_elemento_lista(receta.nombre, boton_detalles)

    def abrir_vista_detalles_receta(self, receta):
        self._vista_receta_detalles = VistaRecetaDetalles(receta)
        self._vista_receta_detalles.setObjectName("vista_receta_detalles")

        self.remove_last_view()
        self._layout.addWidget(self._vista_receta_detalles)
        self.mostrar_detalles_receta()

    def mostrar_detalles_receta(self):
        pass

    def abrir_crear_receta(self):
        self.remove_last_view()
        self._vista_crear_receta.boton_volver.clicked.connect(self.abrir_vista_lista_recetas)
        self._layout.addWidget(self._vista_crear_receta)

    def remover_ultima_vista(self):
        last_view = self._layout.itemAt(0).widget()
        self._layout.removeWidget(last_view)
        last_view.setParent(None)