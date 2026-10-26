from PySide6.QtCore import QObject, Slot

from views.VistaTablaInventario import VistaTablaInventario

class ControladorTablaInventario(QObject):
    def __init__(self, vista:VistaTablaInventario, servicio=None):
        super().__init__()

        self.vista = vista
        self.servicio = servicio

