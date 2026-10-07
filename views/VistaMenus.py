from PySide6 import QtCore, QtWidgets, QtGui

from models.Platillo import Platillo


class VistaMenus(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QGridLayout()
        self.lista_tajetas_menu = []

        self.titulo_principal = QtWidgets.QLabel("Menús")
        self.titulo_principal.setObjectName("titulo_principal")

        efecto_sombra = QtWidgets.QGraphicsDropShadowEffect(self)
        efecto_sombra.setOffset(1, 1)
        efecto_sombra.setBlurRadius(4)
        efecto_sombra.setColor(QtGui.QColor(122, 122, 133, 100))

        self.boton_crear_menu = QtWidgets.QPushButton("Crear menú")
        self.boton_crear_menu.setObjectName("boton_crear_menu")
        self.boton_crear_menu.setFixedWidth(int(self.boton_crear_menu.sizeHint().width() * 1.25))
        self.boton_crear_menu.setGraphicsEffect(efecto_sombra)

        self.layout.addWidget(self.titulo_principal, 0, 0)
        self.layout.addWidget(self.boton_crear_menu, 0, 3)

        self.setLayout(self.layout)

    def crear_tarjeta_menu(self, menu, platillos=None):
        tarjeta = QtWidgets.QWidget()
        tarjeta.setObjectName("tarjeta_menu")
        tarjeta_layout = QtWidgets.QVBoxLayout()

        efecto_sombra = QtWidgets.QGraphicsDropShadowEffect(self)
        efecto_sombra.setOffset(1, 1)
        efecto_sombra.setBlurRadius(4)
        efecto_sombra.setColor(QtGui.QColor(122, 122, 133, 100))

        tarjeta.setGraphicsEffect(efecto_sombra)

        contenedor_titulo_menu = QtWidgets.QWidget()
        contenedor_titulo_menu.setObjectName("contenedor_titulo_menu")
        contenedor_titulo_menu_layout = QtWidgets.QHBoxLayout()

        etiqueta_nombre_menu = QtWidgets.QLabel(menu.nombre)
        etiqueta_nombre_menu.setObjectName("etiqueta_nombre_menu")
        etiqueta_nombre_menu.setWordWrap(True)
        boton_ver_mas = QtWidgets.QPushButton("Ver más")
        boton_ver_mas.setObjectName(f"{menu.nombre}")
        boton_ver_mas.setProperty("cssClass", "boton_secundario")
        boton_ver_mas.setFixedWidth(int(boton_ver_mas.sizeHint().width() * 1.25))
        contenedor_titulo_menu_layout.addWidget(etiqueta_nombre_menu)
        contenedor_titulo_menu_layout.addSpacerItem(QtWidgets.QSpacerItem(40, 20,
                                                                  QtWidgets.QSizePolicy.Policy.Expanding,
                                                                  QtWidgets.QSizePolicy.Policy.Minimum))
        contenedor_titulo_menu_layout.addWidget(boton_ver_mas)
        contenedor_titulo_menu.setLayout(contenedor_titulo_menu_layout)
        tarjeta_layout.addWidget(contenedor_titulo_menu)

        for platillo in platillos:
            contenedor = QtWidgets.QWidget()
            contenedor.setObjectName("elemento_platillos")
            contenedor_layout = QtWidgets.QHBoxLayout()
            contenedor_layout.setAlignment(QtGui.Qt.AlignmentFlag.AlignLeft)
            etiqueta_platillo = QtWidgets.QLabel(platillo.nombre)
            etiqueta_platillo.setWordWrap(True)
            etiqueta_precio = QtWidgets.QLabel(f"${platillo.precio}")
            etiqueta_precio.setFixedWidth(etiqueta_precio.sizeHint().width())

            contenedor_layout.addWidget(etiqueta_platillo)
            contenedor_layout.addSpacerItem(QtWidgets.QSpacerItem(40, 20,
                                                                  QtWidgets.QSizePolicy.Policy.Expanding,
                                                                  QtWidgets.QSizePolicy.Policy.Minimum))
            contenedor_layout.addWidget(etiqueta_precio)
            contenedor.setLayout(contenedor_layout)

            tarjeta_layout.addWidget(contenedor)

        tarjeta.setLayout(tarjeta_layout)
        self.lista_tajetas_menu.append(tarjeta)

        return tarjeta

    def resizeEvent(self, event):
        super().resizeEvent(event)

        for tarjeta in self.lista_tajetas_menu:
            tarjeta.setFixedWidth(self.width() // 3)