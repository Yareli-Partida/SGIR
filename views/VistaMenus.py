from PySide6 import QtCore, QtWidgets, QtGui
from pathlib import Path

from views.VistaListaMenus import VistaListaMenus
from views.VistaMenuDetalles import VistaMenuDetalles
from models.Menu import Menu
from models.Platillo import Platillo

class VistaMenus(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self._layout = QtWidgets.QVBoxLayout()
        self._vista_menus = VistaListaMenus()
        self._vista_menu_detalles = None

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

        for menu in lista_menu:
            tarjeta = self._vista_menus.crear_tarjeta_menu(menu, lista_platillos)
            tarjeta.setFixedWidth(self.width() // 3)
            boton = tarjeta.findChild(QtWidgets.QWidget, "contenedor_titulo_menu").findChild(QtWidgets.QPushButton, menu.nombre)
            boton.clicked.connect(lambda state, menu_obj=menu: self.abrir_vista_menu_detalles(menu_obj))
            self._vista_menus.layout.addWidget(tarjeta, fila, col)
            col += 1

            if col > 3:
                fila += 1
                col = 0

    def abrir_vista_menu_detalles(self, menu):
        self._vista_menu_detalles = VistaMenuDetalles(menu)
        self.remover_ultima_vista()
        self._layout.addWidget(self._vista_menu_detalles)

    def abrir_vista_editar_menu(self, menu):
        self.remover_ultima_vista()

    def abrir_vista_crear_menu(self):
        pass

    def remover_ultima_vista(self):
        last_view = self._layout.itemAt(0).widget()
        self._layout.removeWidget(last_view)
        last_view.setParent(None)