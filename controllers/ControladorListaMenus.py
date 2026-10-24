from PySide6.QtCore import QObject, Slot

from models.Menu import Menu
from models.Platillo import Platillo
from views.VistaListaMenus import VistaListaMenus


class ControladorListaMenus(QObject):
    """
    Controlador para la vista que muestra todos los menús en la BD.

    :param vista: (VistaListaMenus): Vista que muestra los menús.
    :param servicio: (Servicio): Clase servicio para la VistaListaMenus.

    """

    def __init__(self, vista:VistaListaMenus, servicio=None):
        super().__init__()

        self.vista = vista
        self.servicio = servicio

        self.vista.mostrar_menus_signal.connect(lambda: self.mostrar_menus())

    def mostrar_menus(self) -> None:
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
            tarjeta = self.vista.crear_tarjeta_menu(menu, lista_platillos)
            tarjeta.setFixedWidth(self.vista.width() // 3)
            self.vista.layout.addWidget(tarjeta, fila, col)
            col += 1

            if col > 3:
                fila += 1
                col = 0