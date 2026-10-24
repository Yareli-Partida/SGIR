from PySide6.QtCore import QObject, Slot

from views.VistaCrearEditarReceta import VistaCrearEditarReceta
from models.Receta import Receta

class ControladorCrearEditarReceta(QObject):
    """
    Controlador para la visa de crear y editar una receta.

    :param vista: (VistaCrearEditarReceta): Vista del formulario para crear o editar una receta.
    :param servicio: (Servicio): Clase servicio para la VistaCrearEditarReceta.

    """

    def __init__(self, vista:VistaCrearEditarReceta, servicio=None):
        super().__init__()
        self.vista = vista
        self.servicio = servicio

        # Por alguna razón tiene que conectar con las sig. 2 líneas juntas, usar una o la otra sola no funciona
        self.vista.llenar_forma_signal.connect(self.llenar_forma_receta)
        self.vista.llenar_forma_signal.connect(lambda: self.llenar_forma_receta)
        # self.vista.guardar_receta_signal.connect()

    @Slot(Receta)
    def llenar_forma_receta(self, receta:Receta) -> None:
        """
        Configura la información básica de la receta,
        conecta a la capa de servicios para obtener los ingredientes de una receta
        y agrega una fila a la tabla de VistaCrearEditarReceta por cada uno.

        :param receta: (Receta): Receta con la que se llenará la forma.
        """

        self.vista.selector_num_porciones.setValue(receta.num_porciones)
        self.vista.campo_nombre_receta.setText(receta.nombre)

