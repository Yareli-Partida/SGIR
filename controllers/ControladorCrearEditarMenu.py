from PySide6.QtCore import QObject, Slot

from models.Menu import Menu
from models.Platillo import Platillo
from views.VistaCrearEditarMenu import VistaCrearEditarMenu


class ControladorCrearEditarMenu(QObject):
    """
    Controlador para la vista de crear editar un menú.

    :param vista: (VistaCrearEditarMenu): Vista del formulario para crear o editar un menú.
    :param servicio: (Servicio): Clase servicio para la VistaCrearEditarMenu.

    """

    def __init__(self, vista:VistaCrearEditarMenu, servicio=None):
        super().__init__()

        self.vista = vista
        self.servicio = servicio

        self.vista.obtener_platillos_signal.connect(self.pasar_todos_los_platillos_combobox)
        self.vista.llenar_forma_signal.connect(self.llenar_forma_menu)
        self.vista.llenar_forma_signal.connect(lambda: self.llenar_forma_menu)
        # self.vista.guardar_menu_signal.connect()

    def pasar_todos_los_platillos_combobox(self) -> None:
        """
        Conecta con la capa servicios para obtener todos los platillos de la BD y los pasa a la vista para mostrarlos
        como opciones del combobox para cada fila de la tabla.
        """

        # testeo
        # lista_platillos = [Platillo(1, "Pasta en salsa de tomate", 150),
        #     Platillo(2, "Puré de papas", 70),
        #     Platillo(3, "Filete de res", 250),
        #     Platillo(4, "Caldo de pollo", 180),
        #     Platillo(5, "Café", 50),
        # ]

        lista_platillos_test = [
            {"num": 1, "nombre": "Pasta en salsa de tomate", "precio": 150},
            {"num": 2, "nombre": "Puré de papas", "precio": 70},
            {"num": 3, "nombre": "Filete de res", "precio": 250},
            {"num": 4, "nombre": "Caldo de pollo", "precio": 180},
            {"num": 5, "nombre": "Café", "precio": 50}
        ]

        self.vista.asignar_platillos_combobox(lista_platillos_test)

    @Slot(Menu)
    def llenar_forma_menu(self, menu:Menu) -> None:
        """
        Conecta con la capa servicios para obtener los platillos de un menú y agrega una fila a la tabla de
        VistaEditarCrearMenu por cada uno.

        :param menu: (Menu): El menú del que se llenará la forma.
        """

        # menu_platillos = [
        #     Platillo(1, "Pasta en salsa de tomate", 150),
        #     Platillo(2, "Puré de papas", 70),
        #     Platillo(3, "Filete de res", 250),
        #     Platillo(4, "Caldo de pollo", 180),
        #     Platillo(5, "Café", 50),
        # ]

        lista_platillos_test = [
            {"num": 1, "nombre": "Pasta en salsa de tomate", "precio": 150},
            {"num": 2, "nombre": "Puré de papas", "precio": 70},
            {"num": 3, "nombre": "Filete de res", "precio": 250},
            {"num": 4, "nombre": "Caldo de pollo", "precio": 180},
            {"num": 5, "nombre": "Café", "precio": 50}
        ]

        # for platillo in lista_platillos_test:
        #     categoria = "Platillo Fuerte"
        #     self.vista.agregar_fila_tabla_platillo(platillo.nombre, int(platillo.precio), categoria)

        for platillo in lista_platillos_test:
            categoria = "Platillo Fuerte"
            self.vista.agregar_fila_tabla_platillo(platillo["nombre"], int(platillo["precio"]), categoria)
