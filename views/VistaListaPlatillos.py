from pathlib import Path

from PySide6.QtWidgets import *
from PySide6.QtCore import Signal
from PySide6.QtGui import *

from models.Platillo import Platillo
from views.widgets.BotonPrincipalWidget import BotonPrincipalWidget
from views.widgets.BotonSecundarioWidget import BotonSecundarioWidget

class VistaListaPlatillos(QWidget):

    mostrar_platillos_signal = Signal()
    abrir_crear_signal = Signal()
    abrir_detalles_signal = Signal(Platillo)

    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()
        self.layout.setVerticalSpacing(50)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.lista_tarjetas_platillos = []

        self.titulo = QLabel("Platillos")
        self.titulo.setProperty("cssClass", "titulo")
        self.titulo.setObjectName("titulo_principal")

        self.boton_crear_platillo = BotonPrincipalWidget("Crear platillo")
        self.boton_crear_platillo.clicked.connect(self.emitir_evento_abrir_crear)

        self.layout.addWidget(self.titulo, 0, 0)
        self.layout.addWidget(self.boton_crear_platillo, 0, 2, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(self.layout)

        self.setStyleSheet((Path('views/styles/estilos_platillos.qss').read_text()))

    def crear_tarjeta(self, platillo:Platillo, categoria:str):
        tarjeta = QWidget()
        tarjeta.setProperty("cssClass", "tarjeta_platillo")
        tarjeta_layout = QVBoxLayout()

        sombra = QGraphicsDropShadowEffect(self)
        sombra.setOffset(1, 1)
        sombra.setBlurRadius(4)
        sombra.setColor(QColor(122, 122, 133, 100))

        tarjeta.setGraphicsEffect(sombra)

        etiqueta_nombre_platillo = QLabel(platillo.nombre)
        etiqueta_nombre_platillo.setWordWrap(True)
        etiqueta_nombre_platillo.setProperty("cssClass", "etiqueta_nombre_platillos")

        etiqueta_categoria = QLabel(categoria, alignment=Qt.AlignmentFlag.AlignCenter)
        etiqueta_categoria.setFixedWidth(int(etiqueta_categoria.sizeHint().width() * 1.25))
        etiqueta_categoria.setFixedHeight(int(etiqueta_categoria.sizeHint().height() * 1.25))
        etiqueta_categoria.setProperty("cssClass", categoria.lower().replace(" ", "_"))

        boton_detalles = BotonSecundarioWidget("Detalles")
        boton_detalles.clicked.connect(lambda: self.emitir_evento_abrir_detalles(platillo))

        tarjeta_layout.addWidget(etiqueta_nombre_platillo)
        tarjeta_layout.addWidget(etiqueta_categoria)
        tarjeta_layout.addWidget(boton_detalles)

        tarjeta.setLayout(tarjeta_layout)
        tarjeta.setFixedHeight(int(tarjeta.sizeHint().height() * 1.5))

        self.lista_tarjetas_platillos.append(tarjeta)

        return tarjeta

    def emitir_evento_abrir_crear(self):
        self.abrir_crear_signal.emit()

    def emitir_evento_abrir_detalles(self, platillo:Platillo):
        self.abrir_detalles_signal.emit(platillo)

    def resizeEvent(self, event:QResizeEvent) -> None:
        """
        Hace override a la función resizeEvent para ajustar el tamaño de cada tarjeta al ancho actual del widget.

        :param event: (QResizeEvent)
        """

        margenes = self.layout.contentsMargins().left() * 4
        medida = (self.width() - margenes) // 3

        for tarjeta in self.lista_tarjetas_platillos:
            tarjeta.setFixedWidth(medida)

        self.maximumSize().setHeight(self.sizeHint().height())
