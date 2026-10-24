from PySide6.QtCore import QObject, Slot

from models.Menu import Menu
from models.Platillo import Platillo
from views.VistaMenuDetalles import VistaMenuDetalles

class ControladorDetallesMenu(QObject):
    """
    Controlador para la vista que muestra los detalles de un menú en particular.

    :param vista: (VistaMenuDetalles): Vista que muestra los platillos de un menú.
    :param servicio: (Servicio): Clase servicio para la VistaMenuDetalles.

    """

    def __init__(self, vista:VistaMenuDetalles, servicio=None):
        super().__init__()

        self.vista = vista
        self.servicio = servicio

        self.vista.mostrar_detalles_signal.connect(self.mostrar_platillos_detalles)
        self.vista.mostrar_detalles_signal.connect(lambda: self.mostrar_platillos_detalles)


    @Slot(Menu)
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

        self.vista.agregar_platillos_tabla(lista_test)
