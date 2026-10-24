from PySide6.QtCore import QObject, Slot

from views.VistaRecetaDetalles import VistaRecetaDetalles

class ControladorDetallesReceta(QObject):
    """
    Controlador para la vista que muestra los detalles de una receta en particular.

    :param vista: (VistaRecetaDetalles): Vista que muestra los ingredientes de una receta.
    :param servicio: (Servicio): Clase servicio para la VistaRecetaDetalles.

    """

    def __init__(self, vista: VistaRecetaDetalles, servicio=None):
        super().__init__()
        self.vista = vista
        self.servicio = servicio

        self.vista.mostrar_detalles_signal.connect(self.llenar_detalles_receta)
        self.vista.mostrar_detalles_signal.connect(lambda: self.llenar_detalles_receta)

    def llenar_detalles_receta(self):
        pass