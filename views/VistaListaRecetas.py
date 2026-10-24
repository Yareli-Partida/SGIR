from pathlib import Path

from PySide6.QtWidgets import *
from PySide6.QtGui import QColor
from PySide6.QtCore import Signal

from models.Receta import Receta
from views.widgets.BotonPrincipalWidget import BotonPrincipalWidget
from views.widgets.BotonSecundarioWidget import BotonSecundarioWidget

class VistaListaRecetas(QWidget):
    """
    Vista de la lista de todas las recetas.

    :var mostrar_recetas_signal: (Signal): Señal para enlistar todas las recetas.
    :var abrir_crear_receta_signal: (Signal): Señal para ir a la vista de crear.
    :var abrir_detalles_receta_signal: (Signal(Receta)): Señal para ir a la vista de detalles.
    :var titulo: (QLabel): Título principal de la vista.
    :var boton_crear_receta: (BotonPrincipalWidget): Botón para ir a la vista para crear recetas.
    :var lista_recetas: (QListWidget): Lista de todas las recetas.

    """

    mostrar_recetas_signal = Signal()
    abrir_crear_receta_signal = Signal()
    abrir_detalles_receta_signal = Signal(Receta)

    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()

        self.titulo = QLabel("Recetas")
        self.titulo.setObjectName("titulo")
        self.titulo.setProperty("cssClass", "titulo")

        self.boton_crear_receta = BotonPrincipalWidget("Crear receta")
        self.boton_crear_receta.clicked.connect(self.emitir_evento_abrir_crear_receta)

        self.lista_recetas = QListWidget()
        self.lista_recetas.setObjectName("lista_recetas")
        self.lista_recetas.setSpacing(10)

        self.layout.addWidget(self.titulo, 0, 0)
        self.layout.addWidget(self.boton_crear_receta, 0, 1)
        self.layout.addWidget(self.lista_recetas, 1, 0, 1, 2)
        self.setLayout(self.layout)

        self.setStyleSheet((Path('views/styles/estilos_recetas.qss').read_text()))

    def crear_elemento_lista(self, receta:Receta) -> None:
        """
        Crea un elemento con el nombre de la receta y botón de detalles en la lista.

        :param receta: (Receta): Receta que se va a enlistar.
        :return:
        """

        elemento = QListWidgetItem()
        widget = QWidget()
        widget.setObjectName("elemento_lista")

        layout_elemento = QHBoxLayout()
        etiqueta_nombre = QLabel(receta.nombre)
        etiqueta_nombre.setObjectName("etiqueta")
        boton_detalles = BotonSecundarioWidget("Detalles")
        boton_detalles.clicked.connect(lambda: self.emitir_evento_abrir_detalles_receta(receta))

        layout_elemento.addWidget(etiqueta_nombre)
        layout_elemento.addWidget(boton_detalles)

        widget.setLayout(layout_elemento)
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setOffset(1, 1)
        sombra.setBlurRadius(4)
        sombra.setColor(QColor(122, 122, 133, 100))
        widget.setGraphicsEffect(sombra)
        elemento.setSizeHint(widget.sizeHint())

        self.lista_recetas.addItem(elemento)
        self.lista_recetas.setItemWidget(elemento, widget)

    def emitir_evento_abrir_crear_receta(self) -> None:
        """
        Emite la señal para abrir la vista de crear receta.
        """

        self.abrir_crear_receta_signal.emit()

    def emitir_evento_abrir_detalles_receta(self, receta:Receta) -> None:
        """
        Emite la señal para abrir la vista de detalles.
        """

        self.abrir_detalles_receta_signal.emit(receta)