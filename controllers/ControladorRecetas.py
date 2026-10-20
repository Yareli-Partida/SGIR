from PySide6.QtWidgets import QWidget
from pathlib import Path

from views.VistaListaRecetas import VistaListaRecetas
from views.VistaRecetaDetalles import VistaRecetaDetalles
from views.VistaCrearEditarReceta import VistaCrearEditarReceta
from views.widgets.BotonSecundarioWidget import BotonSecundarioWidget
from models.Receta import Receta

class ControladorRecetas(QWidget):
    def __init__(self):
        super().__init__()
        self.vista_lista_recetas = None
        self.vista_receta_detalles = None
        self.vista_crear_receta = None
        self.vista_editar_receta = None

        self.abrir_vista_lista_recetas()

        self.setStyleSheet((Path('views/styles/estilos_recetas.qss').read_text()))

    def abrir_vista_lista_recetas(self) -> None:
        """
        Crea un obj VistaListaRecetas, conecta los botones a sus respectivas funciones y cambia el layout actual.
        """

        self.vista_lista_recetas = VistaListaRecetas()
        self.vista_lista_recetas.setObjectName("vista_lista_recetas")
        self.vista_lista_recetas.boton_crear_receta.clicked.connect(self.abrir_crear_receta)
        self.mostrar_lista_recetas()

        if self.layout():
            self.remover_ultima_vista()

        self.setLayout(self.vista_lista_recetas)

    def mostrar_lista_recetas(self) -> None:
        """
        Conecta con la capa de servicios para obtener la lista de recetas y crea un elemento de lista para cada una.
        """

        # esto es solo para testeo manual
        lista_recetas = [Receta(1, "Pasta en salsa de tomate", "", 10)]

        for receta in lista_recetas:
            boton_detalles = BotonSecundarioWidget("Detalles")
            # aparentemente, clicked.connect no toma funciones con argumentos, para hacerlo usa lambda
            boton_detalles.clicked.connect(lambda state, receta_obj=receta: self.abrir_vista_detalles_receta(receta_obj))

            self.vista_lista_recetas.crear_elemento_lista(receta.nombre, boton_detalles)

    def abrir_vista_detalles_receta(self, receta:Receta) -> None:
        """
        Crea un obj VistaRecetaDetalles con arg receta, conecta los botones a sus respectivas funciones
        y cambia el layout actual.

        :param receta: (Receta): Receta de la que mostrará los detalles.
        """

        self.vista_receta_detalles = VistaRecetaDetalles(receta=receta)
        self.vista_receta_detalles.setObjectName("vista_receta_detalles")

        self.remover_ultima_vista()
        self.setLayout(self.vista_receta_detalles)
        self.vista_receta_detalles.boton_editar.clicked.connect(lambda state, receta_obj=receta: self.abrir_editar_receta(receta_obj))
        self.vista_receta_detalles.boton_volver.clicked.connect(self.abrir_vista_lista_recetas)
        self.mostrar_detalles_receta()

    def mostrar_detalles_receta(self):
        pass

    def abrir_crear_receta(self) -> None:
        """
        Crea un obj VistaCrearEditarReceta, conecta los botones a sus respectivas funciones y cambia el layout actual.
        """

        self.vista_crear_receta = VistaCrearEditarReceta()
        self.vista_crear_receta.setObjectName("vista_crear_receta")
        self.vista_crear_receta.boton_volver.clicked.connect(self.abrir_vista_lista_recetas)

        self.remover_ultima_vista()
        self.setLayout(self.vista_crear_receta)

    def abrir_editar_receta(self, receta:Receta) -> None:
        """
        Crea un obj VistaCrearEditarReceta con arg receta, conecta los botones a sus respectivas funciones
        y cambia el layout actual.

        :param receta: (Receta): Receta que se editará.
        """

        self.vista_editar_receta = VistaCrearEditarReceta(receta_editar=receta)
        self.vista_editar_receta.boton_volver.clicked.connect(lambda state, receta_obj=receta: self.abrir_vista_detalles_receta(receta_obj))
        self.llenar_forma_receta(receta)

        self.remover_ultima_vista()
        self.setLayout(self.vista_editar_receta)

    def llenar_forma_receta(self, receta:Receta) -> None:
        """
        Configura la información básica de la receta,
        conecta a la capa de servicios para obtener los ingredientes de una receta
        y agrega una fila a la tabla de VistaCrearEditarReceta por cada uno.

        :param receta: (Receta): Receta con la que se llenará la forma.
        """

        self.vista_editar_receta.selector_num_porciones.setValue(receta.num_porciones)
        self.vista_editar_receta.campo_nombre_receta.setText(receta.nombre)

    def remover_ultima_vista(self) -> None:
        """
        Borra la referencia el layout anterior al asignarlo a un widget que no será guardado.
        """

        QWidget().setLayout(self.layout())
