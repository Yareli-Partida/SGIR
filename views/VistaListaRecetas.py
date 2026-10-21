from PySide6.QtWidgets import *
from PySide6.QtGui import QColor

from views.widgets.BotonPrincipalWidget import BotonPrincipalWidget

class VistaListaRecetas(QGridLayout):
    """
    Vista de la lista de todas las recetas.

    :var titulo: (QLabel): Título principal de la vista.
    :var boton_crear_receta: (BotonPrincipalWidget): Botón para ir a la vista para crear recetas.
    :var lista_recetas: (QListWidget): Lista de todas las recetas.

    """
    def __init__(self):
        super().__init__()

        self.titulo = QLabel("Recetas")
        self.titulo.setObjectName("titulo")
        self.titulo.setProperty("cssClass", "titulo")

        self.boton_crear_receta = BotonPrincipalWidget("Crear receta")

        self.lista_recetas = QListWidget()
        self.lista_recetas.setObjectName("lista_recetas")
        self.lista_recetas.setSpacing(10)

        self.addWidget(self.titulo, 0, 0)
        self.addWidget(self.boton_crear_receta, 0, 1)
        self.addWidget(self.lista_recetas, 1, 0, 1, 2)

    def crear_elemento_lista(self, nombre:str, boton) -> None:
        """
        Crea un elemento con el nombre de la receta y botón de detalles en la lista.

        :param nombre: (str): Nombre de la receta.
        :param boton: (BotonSecundarioWidget): Botón de detalles.
        :return:
        """

        elemento = QListWidgetItem()
        widget = QWidget()
        widget.setObjectName("elemento_lista")

        layout_elemento = QHBoxLayout()
        etiqueta_nombre = QLabel(nombre)
        etiqueta_nombre.setObjectName("etiqueta")

        layout_elemento.addWidget(etiqueta_nombre)
        layout_elemento.addWidget(boton)

        widget.setLayout(layout_elemento)
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setOffset(1, 1)
        sombra.setBlurRadius(4)
        sombra.setColor(QColor(122, 122, 133, 100))
        widget.setGraphicsEffect(sombra)
        elemento.setSizeHint(widget.sizeHint())

        self.lista_recetas.addItem(elemento)
        self.lista_recetas.setItemWidget(elemento, widget)
