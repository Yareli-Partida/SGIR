from pathlib import Path

from PySide6.QtGui import Qt, QColor, QResizeEvent
from PySide6.QtWidgets import *
from PySide6.QtCore import Signal

from models.Menu import Menu
from models.Platillo import Platillo
from views.widgets.BotonPrincipalWidget import BotonPrincipalWidget
from views.widgets.BotonSecundarioWidget import BotonSecundarioWidget
from views.widgets.EspacioHorizontalWidget import EspacioHorizontalWidget

class VistaListaMenus(QWidget):
    """
    Vista de la lista de todos los menús.

    :var mostrar_menus_signal: (Signal): Señal para enlistar todos los menús.
    :var abrir_crear_menu_signal: (Signal): Señal para ir a la vista de crear.
    :var abrir_detalles_signal: (Signal(Menu)): Señal para ir a la vista de detalles.
    :var lista_tarjetas_menu: (list[QWidget]): Guarda la referencia a todas las tarjetas.
    :var titulo_principal: (QLabel): Título principal de la vista.
    :var boton_crear_menu: (BotonPrincipalWidget): Botón para ir a la vista para crear menú.

    """

    mostrar_menus_signal = Signal()
    abrir_crear_menu_signal = Signal()
    abrir_detalles_signal = Signal(Menu)

    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout.setVerticalSpacing(50)
        self.lista_tarjetas_menu = []

        self.titulo_principal = QLabel("Menús")
        self.titulo_principal.setObjectName("titulo")
        self.titulo_principal.setProperty("cssClass", "titulo")

        self.boton_crear_menu = BotonPrincipalWidget("Crear menú")
        self.boton_crear_menu.clicked.connect(self.emitir_evento_abrir_crear_menu)

        self.layout.addWidget(self.titulo_principal, 0, 0)
        self.layout.addWidget(self.boton_crear_menu, 0, 2, alignment=Qt.AlignmentFlag.AlignRight)
        self.setLayout(self.layout)

        self.setStyleSheet((Path('views/styles/estilos_menus.qss').read_text()))

    def crear_tarjeta_menu(self, menu:Menu, platillos:list) -> QWidget:
        """
        Crea un widget "tarjeta" para mostrar una vista previa al menú.

        :param menu: (Menu): El menú del que se mostrarán los detalles.
        :param platillos: (list[Platillo])La lista de los platillos asociados al menú.
        :return:
        """

        tarjeta = QWidget()
        tarjeta.setObjectName("tarjeta_menu")
        tarjeta_layout = QVBoxLayout()

        efecto_sombra = QGraphicsDropShadowEffect(self)
        efecto_sombra.setOffset(1, 1)
        efecto_sombra.setBlurRadius(4)
        efecto_sombra.setColor(QColor(122, 122, 133, 100))

        tarjeta.setGraphicsEffect(efecto_sombra)

        contenedor_titulo_menu = QWidget()
        contenedor_titulo_menu.setObjectName("contenedor_titulo_menu")
        contenedor_titulo_menu_layout = QHBoxLayout()

        etiqueta_nombre_menu = QLabel(menu.nombre)
        etiqueta_nombre_menu.setObjectName("etiqueta_nombre_menu")
        etiqueta_nombre_menu.setWordWrap(True)
        boton_ver_mas = BotonSecundarioWidget("Ver más")
        boton_ver_mas.setObjectName(f"{menu.nombre}")
        boton_ver_mas.clicked.connect(lambda: self.emitir_evento_abrir_detalles_menu(menu))

        contenedor_titulo_menu_layout.addWidget(etiqueta_nombre_menu)
        contenedor_titulo_menu_layout.addSpacerItem(EspacioHorizontalWidget())
        contenedor_titulo_menu_layout.addWidget(boton_ver_mas)
        contenedor_titulo_menu.setLayout(contenedor_titulo_menu_layout)
        tarjeta_layout.addWidget(contenedor_titulo_menu)

        for platillo in platillos:
            contenedor = QWidget()
            contenedor.setObjectName("elemento_platillos")
            contenedor_layout = QHBoxLayout()
            contenedor_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
            # etiqueta_platillo = QLabel(platillo.nombre)
            etiqueta_platillo = QLabel(platillo["nombre"])
            etiqueta_platillo.setWordWrap(True)
            # etiqueta_precio = QLabel(f"${platillo.precio}")
            etiqueta_precio = QLabel(f"${platillo["precio"]}")
            etiqueta_precio.setFixedWidth(etiqueta_precio.sizeHint().width())

            contenedor_layout.addWidget(etiqueta_platillo)
            contenedor_layout.addSpacerItem(EspacioHorizontalWidget())
            contenedor_layout.addWidget(etiqueta_precio)
            contenedor.setLayout(contenedor_layout)

            tarjeta_layout.addWidget(contenedor)

        tarjeta.setLayout(tarjeta_layout)
        tarjeta.setFixedHeight(tarjeta.sizeHint().height())
        self.lista_tarjetas_menu.append(tarjeta)

        return tarjeta

    def emitir_evento_abrir_crear_menu(self) -> None:
        """
        Emite la señal para abrir la vista de crear menú.
        """

        self.abrir_crear_menu_signal.emit()

    def emitir_evento_abrir_detalles_menu(self, menu:Menu) -> None:
        """
        Emite la señal para abrir la vista de detalles.
        """

        self.abrir_detalles_signal.emit(menu)

    def resizeEvent(self, event:QResizeEvent) -> None:
        """
        Hace override a la función resizeEvent para ajustar el tamaño de cada tarjeta al ancho actual del widget.

        :param event: (QResizeEvent)
        """
        margenes = self.layout.contentsMargins().left() * 4
        medida = (self.width() - margenes) // 3

        for tarjeta in self.lista_tarjetas_menu:
            tarjeta.setFixedWidth(medida)

        self.maximumSize().setHeight(self.sizeHint().height())