from PySide6 import QtCore, QtWidgets, QtGui
from pathlib import Path

from views.VistaMenus import VistaMenus
from models.Menu import Menu
from models.Platillo import Platillo

class ControladorMenus(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self._layout = QtWidgets.QVBoxLayout()
        self._vista_menus = VistaMenus()

        self._layout.addWidget(self._vista_menus)
        self.mostrar_menu()

        self.setLayout(self._layout)
        self.setStyleSheet((Path('views/styles/estilos_menus.qss').read_text()))

    def mostrar_menu(self):
        # para testeo manual
        lista_menu = [
            Menu(1, "Menú de entre semana", 5),
            Menu(2, "Menú de fin de semana", 7)
        ]

        lista_platillos = [
            Platillo(1, "Pasta en salsa de tomate", 150),
            Platillo(2, "Puré de papas", 70),
            Platillo(3, "Filete de res", 250),
            Platillo(4, "Caldo de pollo", 180),
            Platillo(5, "Café", 50),
        ]

        fila = 1
        col = 0

        for i in range(len(lista_menu)):
            tarjeta = self._vista_menus.crear_tarjeta_menu(lista_menu[i], lista_platillos)
            tarjeta.setFixedWidth(self.width() // 3)
            boton = tarjeta.findChild(QtWidgets.QWidget, "contenedor_titulo_menu").findChild(QtWidgets.QPushButton, lista_menu[i].nombre)
            boton.clicked.connect(lambda: self.abrir_vista_editar_menu(lista_menu[i]))
            print(f"connected menu {lista_menu[i].nombre} to {boton.objectName()}")
            self._vista_menus.layout.addWidget(tarjeta, fila, col)
            col += 1

            if col > 3:
                fila += 1
                col = 0

    def abrir_vista_editar_menu(self, menu):
        print(menu.nombre)

    def abrir_vista_crear_menu(self):
        pass