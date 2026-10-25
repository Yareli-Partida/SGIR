from PySide6.QtCore import QObject, Slot

from models.Categoria import Categoria
from models.Platillo import Platillo
from models.Receta import Receta
from views.VistaCrearEditarPlatillo import VistaCrearEditarPlatillo

class ControladorCrearEditarPlatillo(QObject):
    def __init__(self, vista:VistaCrearEditarPlatillo, servicio=None):
        super().__init__()

        self.vista = vista
        self.servicio = servicio

        self.vista.obtener_lista_recetas_signal.connect(lambda: self.pasar_lista_recetas())
        self.vista.obtener_lista_categorias_signal.connect(lambda: self.pasar_lista_categorias())
        self.vista.llenar_forma_signal.connect(self.llenar_forma)
        self.vista.llenar_forma_signal.connect(lambda: self.llenar_forma)

    def pasar_lista_recetas(self):
        lista_test = [
            Receta(1, "Pasta en salsa de tomate", 10),
            Receta(2, "Puré de papas", 15),
            Receta(3, "Filete de res", 2),
            Receta(4, "Caldo de pollo", 20),
            Receta(5, "Café", 40),
        ]

        self.vista.asignar_lista_recetas(lista_test)

    def pasar_lista_categorias(self):
        lista_test = [
            Categoria("pfue", "Platillo Fuerte"),
            Categoria("bebi", "Bebida")
        ]

        self.vista.asignar_lista_categorias(lista_test)

    @Slot(Platillo)
    def llenar_forma(self, platillo: Platillo):
        categoria_test = "Platillo Fuerte"
        receta_test = "Pasta en salsa de tomate"

        self.vista.llenar_formulario(platillo.nombre, categoria_test, receta_test)