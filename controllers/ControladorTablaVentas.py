from PySide6.QtCore import QObject, Slot

from views.VistaTablaVentas import VistaTablaVentas


class ControladorTablaVentas(QObject):
    def __init__(self, vista:VistaTablaVentas, servicio=None):
        super().__init__()

        self.vista = vista
        self.servicio = servicio