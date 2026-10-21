from PySide6.QtGui import Qt, QColor
from PySide6.QtWidgets import *

from models.Menu import Menu
from models.Platillo import Platillo
from views.widgets.BotonPrincipalWidget import BotonPrincipalWidget
from views.widgets.BotonSecundarioWidget import BotonSecundarioWidget
from views.widgets.EspacioHorizontalWidget import EspacioHorizontalWidget

class VistaListaMenus(QGridLayout):
    """
    Vista de la lista de todos los menús.

    :var lista_tarjetas_menu: (list[QWidget]): Guarda la referencia a todas las tarjetas.
    :var titulo_principal: (QLabel): Título principal de la vista.
    :var boton_crear_menu: (BotonPrincipalWidget): Botón para ir a la vista para crear menú.

    """

    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setVerticalSpacing(50)
        self.lista_tarjetas_menu = []

        self.titulo_principal = QLabel("Menús")
        self.titulo_principal.setObjectName("titulo")
        self.titulo_principal.setProperty("cssClass", "titulo")

        self.boton_crear_menu = BotonPrincipalWidget("Crear menú")

        self.addWidget(self.titulo_principal, 0, 0)
        self.addWidget(self.boton_crear_menu, 0, 3, alignment=Qt.AlignmentFlag.AlignRight)

    def crear_tarjeta_menu(self, menu:Menu, platillos:list[Platillo]) -> QWidget:
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
            etiqueta_platillo = QLabel(platillo.nombre)
            etiqueta_platillo.setWordWrap(True)
            etiqueta_precio = QLabel(f"${platillo.precio}")
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

    def ajustar_tarjetas(self) -> None:
        """
        Ajusta el tamaño de cada tarjeta al ancho actual del Parent Widget
        :return:
        """

        for tarjeta in self.lista_tarjetas_menu:
            tarjeta.setFixedWidth(self.parentWidget().width() // 3)

        self.maximumSize().setHeight(self.parentWidget().sizeHint().height())