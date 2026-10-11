from PySide6 import QtCore, QtWidgets, QtGui

from models.Menu import Menu
from models.Platillo import Platillo


class VistaMenuDetalles(QtWidgets.QWidget):
    def __init__(self, menu):
        super().__init__()
        self.layout = QtWidgets.QGridLayout()

        self.boton_volver = QtWidgets.QPushButton("Volver")
        self.boton_volver.setObjectName("boton_volver")
        self.boton_volver.setFixedWidth(int(self.boton_volver.sizeHint().width() * 1.25))
        self.boton_volver.setProperty("cssClass", "boton_principal")

        self.boton_editar_menu = QtWidgets.QPushButton("Editar")
        self.boton_editar_menu.setObjectName("boton_editar_menu")
        self.boton_editar_menu.setFixedWidth(int(self.boton_editar_menu.sizeHint().width() * 1.25))
        self.boton_editar_menu.setProperty("cssClass", "boton_principal")

        self.titulo_principal = QtWidgets.QLabel(menu.nombre)
        self.titulo_principal.setObjectName("titulo_principal")

        self.layout.addWidget(self.boton_volver, 0, 0)
        self.layout.addWidget(self.boton_editar_menu, 0, 3, alignment=QtGui.Qt.AlignmentFlag.AlignRight)
        self.layout.addWidget(self.titulo_principal, 1, 0, 1, 3)

        self.crear_lista_platillos_categoria("Platillo fuerte", [
        Platillo(1, "Pasta en salsa de tomate", 150),
        Platillo(2, "Puré de papas", 70),
        Platillo(3, "Filete de res", 250),
        Platillo(4, "Caldo de pollo", 180),
        Platillo(5, "Café", 50),
        ])

        self.setLayout(self.layout)

    def crear_tabla_platillos_categoria(self, categoria:str, lista_platillos):
        pass

    def toggle_lista_platillos(self, lista_widget):
        if not lista_widget.visibleRegion().isEmpty():
            pass
            # is visible True
        else:
            pass
            # is visible False
