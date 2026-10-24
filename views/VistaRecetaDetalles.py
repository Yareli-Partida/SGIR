from pathlib import Path

from PySide6.QtWidgets import *
from PySide6.QtGui import Qt
from PySide6.QtCore import Signal

from models.Receta import Receta
from views.widgets.BotonPrincipalWidget import BotonPrincipalWidget

class VistaRecetaDetalles(QWidget):
    """
    Vista para ver los detalles de una receta.

    :var mostrar_detalles_signal: (Signal(Receta)): Señal para ir a la vista de detalles.
    :var volver_vista_anterior_signal: (Signal): Señal para ir a la vista anterior.
    :var abrir_vista_editar_signal: (Signal(Receta)): Señal para ir a la vista de editar.
    :var boton_editar: (BotonPrincipalWidget): Botón para ir a la vista de editar con la receta actual.
    :var titulo: (QLabel): Título principal de la vista.
    :var etiqueta_num_porciones: (QLabel): Indica el número de porciones de la receta.
    :var lista_ingredientes: (QListWidget): Lista de todos los ingredientes de la receta.
    :var lista_instrucciones: (QListWidget): Lista de todas las instrucciones de la receta.

    """

    mostrar_detalles_signal = Signal(Receta)
    volver_vista_anterior_signal = Signal()
    abrir_vista_editar_signal = Signal(Receta)

    def __init__(self, receta:Receta):
        super().__init__()

        self.layout = QGridLayout()

        self.boton_editar = BotonPrincipalWidget("Editar")
        self.boton_editar.setFixedWidth(self.boton_editar.sizeHint().width() * 2)
        self.boton_editar.clicked.connect(lambda: self.emitir_evento_abrir_vista_editar(receta))
        self.boton_volver = BotonPrincipalWidget("Volver")
        self.boton_volver.setFixedWidth(self.boton_volver.sizeHint().width() * 2)
        self.boton_volver.clicked.connect(self.emitir_evento_volver)

        self.titulo = QLabel(receta.nombre)
        self.titulo.setObjectName("titulo")
        self.titulo.setProperty("cssClass", "titulo")

        self.etiqueta_num_porciones = QLabel(f"Porciones: {receta.num_porciones}")
        self.etiqueta_num_porciones.setObjectName("etiqueta_num_porciones")

        self.lista_ingredientes = QListWidget()
        self.lista_ingredientes.setObjectName("lista_ingredientes")

        self.lista_instrucciones = QListWidget()
        self.lista_instrucciones.setObjectName("lista_instrucciones")

        self.layout.addWidget(self.boton_volver, 0, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.boton_editar, 0, 1, alignment=Qt.AlignmentFlag.AlignRight)
        self.layout.addWidget(self.titulo, 1, 0)
        self.layout.addWidget(self.etiqueta_num_porciones, 2, 0)
        self.layout.addWidget(self.lista_ingredientes, 3, 0, 3, 2)
        self.layout.addWidget(self.lista_instrucciones, 4, 0, 4, 2)

        self.setLayout(self.layout)

        self.setStyleSheet((Path('views/styles/estilos_recetas.qss').read_text()))

    def emitir_evento_volver(self) -> None:
        """
        Emite la señal para volver a la vista anterior.
        """

        self.volver_vista_anterior_signal.emit()

    def emitir_evento_abrir_vista_editar(self, receta:Receta) -> None:
        """
        Emite la señal para ir a la vista de editar.
        """

        self.abrir_vista_editar_signal.emit(receta)