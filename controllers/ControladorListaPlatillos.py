from PySide6.QtCore import QObject, Slot

from models.Platillo import Platillo
from views.VistaListaPlatillos import VistaListaPlatillos


class ControladorListaPlatillos(QObject):
    def __init__(self, vista:VistaListaPlatillos, servicio=None):
        super().__init__()

        self.vista = vista
        self.servicio = servicio

        self.vista.mostrar_platillos_signal.connect(lambda: self.mostrar_platillos())

    def mostrar_platillos(self):

        # testeo
        platillos_prueba = [Platillo(1, "Pizza de peperoni"),
        Platillo(1, "Pasta en salsa de tomate"),
        Platillo(2, "Limonada mineral"),
        Platillo(3, "Naranjada mineral")]

        categorias_prueba = ["Platillo Fuerte", "Platillo Fuerte", "Bebida", "Bebida"]

        fila = 1
        col = 0
        contador = 0

        for platillo in platillos_prueba:
            tarjeta = self.vista.crear_tarjeta(platillo, categorias_prueba[contador])
            tarjeta.setFixedWidth(self.vista.width() // 3)
            self.vista.layout.addWidget(tarjeta, fila, col)
            col += 1
            contador += 1

            if col >= 3:
                fila += 1
                col = 0