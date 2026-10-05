from PySide6 import QtWidgets

from views.VistaRecetas import VistaRecetas
from views.VistaRecetaDetalles import VistaRecetaDetalles
from models.Receta import Receta

class ControladorRecetas(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self._layout = QtWidgets.QVBoxLayout()
        self._vista_lista_recetas = VistaRecetas()
        self._vista_lista_recetas.setObjectName("vista_lista_recetas")
        self._vista_receta_detalles = None

        self._layout.addWidget(self._vista_lista_recetas)
        self.setLayout(self._layout)
        # esto es solo para testeo manual
        self.mostrar_lista_recetas([Receta(1, "Pasta en salsa de tomate", "", 10)])

    def abrir_vista_lista_recetas(self):
        self._layout.removeWidget(self._vista_receta_detalles)
        self._layout.addWidget(self._vista_lista_recetas)
        # también esto es para testeo manual
        self.mostrar_lista_recetas([Receta(1, "Pasta en salsa de tomate", "", 10)])

    def mostrar_lista_recetas(self, lista_recetas:list):
        for receta in lista_recetas:
            boton_detalles = self._vista_lista_recetas.crear_boton_detalles()
            # aparentemente clicked.connect no toma funciones con argumentos, para hacerlo usa lambda
            boton_detalles.clicked.connect(lambda: self.abrir_vista_detalles_receta(receta))

            self._vista_lista_recetas.crear_elemento_lista(receta.nombre, boton_detalles)

    def abrir_vista_detalles_receta(self, receta):
        self._vista_receta_detalles = VistaRecetaDetalles(receta)
        self._vista_receta_detalles.setObjectName("vista_receta_detalles")

        self._layout.removeWidget(self._vista_lista_recetas)
        self._layout.addWidget(self._vista_receta_detalles)
        self.mostrar_detalles_receta()

    def mostrar_detalles_receta(self):
        pass