from PySide6.QtWidgets import QWidget, QPushButton
from pathlib import Path

from PySide6.QtGui import QResizeEvent

from views.VistaListaMenus import VistaListaMenus
from views.VistaMenuDetalles import VistaMenuDetalles
from views.VistaCrearEditarMenu import VistaCrearEditarMenu
from models.Menu import Menu
from models.Platillo import Platillo

class ControladorMenus(QWidget):
    def __init__(self):
        super().__init__()
        self.vista_menus = None
        self.vista_menu_detalles = None
        self.vista_editar_menu = None
        self.vista_crear_menu = None

        self.abrir_vista_lista_menus()
        self.setStyleSheet((Path('views/styles/estilos_menus.qss').read_text()))

    def abrir_vista_lista_menus(self) -> None:
        """
        Crea un obj de VistaListaMenus, conecta los botones a sus respectivas funciones y cambia el layout actual.
        """

        self.vista_menus = VistaListaMenus()
        self.vista_menus.setObjectName("vista_menus")
        self.vista_menus.boton_crear_menu.clicked.connect(self.abrir_vista_crear_menu)
        self.mostrar_menu()

        if self.layout():
            self.remover_ultima_vista()

        self.setLayout(self.vista_menus)

    def mostrar_menu(self) -> None:
        """
        Conecta al repositorio para obtener la lista de menús y de sus platillos
        y crea una tarjeta en la VistaListaMenus para cada menú.
        """

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
            tarjeta = self.vista_menus.crear_tarjeta_menu(menu, lista_platillos)
            tarjeta.setFixedWidth(self.width() // 3)
            boton = tarjeta.findChild(QWidget, "contenedor_titulo_menu").findChild(QPushButton, menu.nombre)
            boton.clicked.connect(lambda state, menu_obj=menu: self.abrir_vista_menu_detalles(menu_obj))
            self.vista_menus.addWidget(tarjeta, fila, col)
            col += 1

            if col > 3:
                fila += 1
                col = 0

    def abrir_vista_menu_detalles(self, menu:Menu) -> None:
        """
        Abre un obj VistaMenuDetalles, conecta los botones a sus respectivas funciones y cambia la vista actual.

        :param menu: (Menu): Menú del que se muestran los detalles.
        """

        self.vista_menu_detalles = VistaMenuDetalles(menu=menu)
        self.vista_menu_detalles.setObjectName("vista_menu_detalles")
        self.vista_menu_detalles.boton_volver.clicked.connect(self.abrir_vista_lista_menus)
        self.vista_menu_detalles.boton_editar_menu.clicked.connect(lambda: self.abrir_vista_editar_menu(menu))
        self.mostrar_platillos_detalles(menu)

        self.remover_ultima_vista()
        self.setLayout(self.vista_menu_detalles)

    def mostrar_platillos_detalles(self, menu: Menu) -> None:
        """
        Conecta con la capa de servicios para obtener la lista de platillos
        del menú y los agrega a la tabla de platillos de VistaMenuDetalles.

        :param menu: (Menu): Menú del que se consultarán los platillos.
        """

        lista_test = [
            Platillo(1, "Pasta en salsa de tomate", 150),
            Platillo(2, "Puré de papas", 70),
            Platillo(3, "Filete de res", 250),
            Platillo(4, "Caldo de pollo", 180),
            Platillo(5, "Café", 50),
        ]

        self.vista_menu_detalles.agregar_platillos_tabla(lista_test)

    def abrir_vista_editar_menu(self, menu:Menu) -> None:
        """
        Crea un obj VistaCrearEditarMenu con arg menu,
        conecta con la capa de servicios para obtener todos los platillos,
        conecta los botones a sus respectivas funciones
        y cambia el layout actual.

        :param menu: (Menu): Menú que se va a editar.
        """

        self.vista_editar_menu = VistaCrearEditarMenu(menu=menu, lista_platillos=[
            Platillo(1, "Pasta en salsa de tomate", 150),
            Platillo(2, "Puré de papas", 70),
            Platillo(3, "Filete de res", 250),
            Platillo(4, "Caldo de pollo", 180),
            Platillo(5, "Café", 50),
        ])
        self.vista_editar_menu.boton_volver.clicked.connect(lambda: self.abrir_vista_menu_detalles(menu))
        self.vista_editar_menu.boton_agregar_platillo.clicked.connect(self.vista_editar_menu.agregar_fila_tabla_platillo)
        self.vista_editar_menu.setObjectName("vista_editar_menu")
        self.llenar_forma_menu(menu)

        self.remover_ultima_vista()
        self.setLayout(self.vista_editar_menu)

    def llenar_forma_menu(self, menu:Menu) -> None:
        """
        Conecta con la capa servicios para obtener los platillos de un menú
        y agrega una fila a la tabla de VistaEditarCrearMenu por cada uno.

        :param menu: (Menu): El menú del que se llenará la forma.
        """

        menu_platillos = [
            Platillo(1, "Pasta en salsa de tomate", 150),
            Platillo(2, "Puré de papas", 70),
            Platillo(3, "Filete de res", 250),
            Platillo(4, "Caldo de pollo", 180),
            Platillo(5, "Café", 50),
        ]

        for platillo in menu_platillos:
            categoria = "Platillo Fuerte"
            self.vista_editar_menu.agregar_fila_tabla_platillo(platillo.nombre, int(platillo.precio), categoria)

    def abrir_vista_crear_menu(self) -> None:
        """
        Crea un obj VistaCrearEditarMenu, conecta con la capa de servicios para obtener todos los platillos,
        conecta los botones a sus respectivas funciones y cambia el layout actual.
        """

        self.vista_crear_menu = VistaCrearEditarMenu(lista_platillos=[
            Platillo(1, "Pasta en salsa de tomate", 150),
            Platillo(2, "Puré de papas", 70),
            Platillo(3, "Filete de res", 250),
            Platillo(4, "Caldo de pollo", 180),
            Platillo(5, "Café", 50),
        ])
        self.vista_crear_menu.boton_volver.clicked.connect(self.abrir_vista_lista_menus)
        self.vista_crear_menu.boton_agregar_platillo.clicked.connect(self.vista_crear_menu.agregar_fila_tabla_platillo)
        self.vista_crear_menu.agregar_fila_tabla_platillo()

        self.remover_ultima_vista()
        self.setLayout(self.vista_crear_menu)

    def remover_ultima_vista(self) -> None :
        """
        Borra la referencia el layout anterior al asignarlo a un widget que no será guardado.
        """

        QWidget().setLayout(self.layout())

    def resizeEvent(self, event:QResizeEvent) -> None:
        """
        Hace override a la función resizeEvent para llamar una función de vistaListaMenus en un ResizeEvent.

        :param event: (QResizeEvent)
        """

        if self.layout().objectName() == "vista_menus":
            self.vista_menus.ajustar_tarjetas()