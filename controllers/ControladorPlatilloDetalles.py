from PySide6.QtCore import QObject, Slot

from models.Categoria import Categoria
from models.Platillo import Platillo
from models.Receta import Receta
from views.VistaPlatilloDetalles import VistaPlatilloDetalles


class ControladorPlatilloDetalles(QObject):
    def __init__(self, vista:VistaPlatilloDetalles, servicio=None):
        super().__init__()

        self.vista = vista
        self.servicio = servicio

        self.vista.mostrar_detalles_signal.connect(self.llenar_tabla_detalles)
        self.vista.mostrar_detalles_signal.connect(lambda: self.llenar_tabla_detalles)

    @Slot(Platillo)
    def llenar_tabla_detalles(self, platillo:Platillo):
        categoria_test = "Platillo Fuerte"
        receta_test = "Pasta en salsa de tomate"
        precio_actual_test = "200"

        self.vista.llenar_tabla_detalles(platillo, categoria_test, receta_test, precio_actual_test)