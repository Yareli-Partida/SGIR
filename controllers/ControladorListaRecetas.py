from PySide6.QtCore import QObject, Slot

from views.VistaListaRecetas import VistaListaRecetas
from models.Receta import Receta


class ControladorListaRecetas(QObject):
    """
    Controlador para la vista que muestra todas las recetas en la BD.

    :param vista: (VistaListaRecetas): Vista que muestra las recetas.
    :param servicio: (Servicio): Clase servicio para la VistaListaRecetas.

    """

    def __init__(self, vista: VistaListaRecetas, servicio=None):
        super().__init__()
        self.vista = vista
        self.servicio = servicio

        self.vista.mostrar_recetas_signal.connect(lambda: self.mostrar_lista_recetas())

    def mostrar_lista_recetas(self) -> None:
        """
        Conecta con la capa de servicios para obtener la lista de recetas y crea un elemento de lista para cada una.
        """
        # esto es solo para testeo manual
        lista_recetas = [Receta(1, "Pasta en salsa de tomate", 10, )]

        for receta in lista_recetas:
            self.vista.crear_elemento_lista(receta)
