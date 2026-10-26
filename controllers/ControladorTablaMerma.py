from PySide6.QtCore import QObject, Slot

from views.VistaTablaMerma import VistaTablaMerma


class ControladorTablaMerma(QObject):
    def __init__(self, vista:VistaTablaMerma, servicio=None):
        super().__init__()

        self.vista = vista
        self.servicio = servicio
