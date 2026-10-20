from PySide6.QtWidgets import *
from PySide6.QtGui import Qt

from models.Receta import Receta
from views.widgets.BotonPrincipalWidget import BotonPrincipalWidget

class VistaRecetaDetalles(QGridLayout):
    """
    Vista para ver los detalles de una receta.

    :var boton_editar: (BotonPrincipalWidget): Botón para ir a la vista de editar con la receta actual.
    :var titulo: (QLabel): Título principal de la vista.
    :var etiqueta_num_porciones: (QLabel): Indica el número de porciones de la receta.
    :var lista_ingredientes: (QListWidget): Lista de todos los ingredientes de la receta.
    :var lista_instrucciones: (QListWidget): Lista de todas las instrucciones de la receta.

    """

    def __init__(self, receta:Receta):
        super().__init__()

        self.boton_editar = BotonPrincipalWidget("Editar")
        self.boton_editar.setFixedWidth(self.boton_editar.sizeHint().width() * 2)
        self.boton_volver = BotonPrincipalWidget("Volver")
        self.boton_volver.setFixedWidth(self.boton_volver.sizeHint().width() * 2)

        self.titulo = QLabel(receta.nombre)
        self.titulo.setObjectName("titulo_principal")
        self.titulo.setProperty("cssClass", "titulo_principal")

        self.etiqueta_num_porciones = QLabel(f"Porciones: {receta.num_porciones}")
        self.etiqueta_num_porciones.setObjectName("etiqueta_num_porciones")

        self.lista_ingredientes = QListWidget()
        self.lista_ingredientes.setObjectName("lista_ingredientes")

        self.lista_instrucciones = QListWidget()
        self.lista_instrucciones.setObjectName("lista_instrucciones")

        self.addWidget(self.boton_volver, 0, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        self.addWidget(self.boton_editar, 0, 1, alignment=Qt.AlignmentFlag.AlignRight)
        self.addWidget(self.titulo, 1, 0)
        self.addWidget(self.etiqueta_num_porciones, 2, 0)
        self.addWidget(self.lista_ingredientes, 3, 0, 3, 2)
        self.addWidget(self.lista_instrucciones, 4, 0, 4, 2)
