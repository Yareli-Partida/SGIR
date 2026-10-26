from pathlib import Path

from PySide6.QtWidgets import *
from PySide6.QtCore import Signal
from PySide6.QtGui import *

from models.Categoria import Categoria
from models.Platillo import Platillo
from models.Receta import Receta
from views.widgets.BotonPrincipalWidget import BotonPrincipalWidget
from views.widgets.EspacioHorizontalWidget import EspacioHorizontalWidget

class VistaCrearEditarPlatillo(QWidget):

    llenar_forma_signal = Signal(Platillo)
    guardar_platillo_signal = Signal()
    volver_vista_anterior_signal = Signal()
    obtener_lista_recetas_signal = Signal()
    obtener_lista_categorias_signal = Signal()

    def __init__(self, platillo=None):
        super().__init__()

        self.layout = QGridLayout()
        self.layout.setVerticalSpacing(50)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.lista_nombre_recetas = []
        self.lista_nombre_categorias = []

        self.titulo = QLabel()
        self.titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titulo.setProperty("cssClass", "titulo")

        self.contenedor_botones = QWidget()
        self.contenedor_botones.setLayout(QHBoxLayout())
        self.boton_guardar = BotonPrincipalWidget("Guardar")
        self.boton_guardar.setFixedWidth(self.boton_guardar.sizeHint().width() * 2)
        self.boton_guardar.clicked.connect(self.emitir_evento_guardar_platillo)

        self.boton_volver = BotonPrincipalWidget("Volver")
        self.boton_volver.setFixedWidth(self.boton_volver.sizeHint().width() * 2)
        self.boton_volver.clicked.connect(self.emitir_evento_volver)

        self.contenedor_botones.layout().addWidget(self.boton_volver)
        self.contenedor_botones.layout().addSpacerItem(EspacioHorizontalWidget())
        self.contenedor_botones.layout().addWidget(self.boton_guardar)

        self.contenedor_nombre_platillo = None
        self.contenedor_selector_categoria = None
        self.contenedor_nueva_categoria = None
        self.contenedor_receta = None

        if platillo:
            self.titulo.setText(f"Editar: {platillo.nombre}")
        else:
            self.titulo.setText("Crear platillo")

        self.layout.addWidget(self.contenedor_botones, 0, 0)
        self.layout.addWidget(self.titulo, 1, 0)

        self.setLayout(self.layout)

        self.setStyleSheet((Path('views/styles/estilos_platillos.qss').read_text()))

    def crear_formulario(self):
        self.crear_campo_nombre_platillo()
        self.crear_selector_categoria()
        self.crear_campo_nueva_categoria()
        self.crear_selector_receta()

        self.layout.addWidget(self.contenedor_nombre_platillo, 2, 0)
        self.layout.addWidget(self.contenedor_selector_categoria, 3, 0)
        self.layout.addWidget(self.contenedor_receta, 4, 0)

    def crear_campo_nombre_platillo(self):
        self.contenedor_nombre_platillo = QWidget()
        self.contenedor_nombre_platillo_layout = QHBoxLayout()
        self.contenedor_nombre_platillo.setLayout(self.contenedor_nombre_platillo_layout)
        self.contenedor_nombre_platillo_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.campo_nombre = QLineEdit()
        self.campo_nombre.setFixedHeight(30)
        self.campo_nombre.setFixedWidth(250)

        self.etiqueta_campo_nombre = QLabel("Nombre: ")
        self.etiqueta_campo_nombre.setProperty("cssClass", "etiqueta_formulario")
        self.etiqueta_campo_nombre.setMaximumWidth(int(self.etiqueta_campo_nombre.sizeHint().width() * 1.25))

        self.contenedor_nombre_platillo.layout().addWidget(self.etiqueta_campo_nombre)
        self.contenedor_nombre_platillo.layout().addWidget(self.campo_nombre)

    def crear_selector_categoria(self):
        self.contenedor_selector_categoria = QWidget()
        self.contenedor_selector_categoria_layout = QHBoxLayout()
        self.contenedor_selector_categoria.setLayout(self.contenedor_selector_categoria_layout)
        self.contenedor_selector_categoria_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.selector_categoria = QComboBox()
        self.selector_categoria.insertItems(len(self.lista_nombre_categorias), self.lista_nombre_categorias)
        self.selector_categoria.setCurrentIndex(-1)
        self.selector_categoria.setFixedHeight(30)
        self.selector_categoria.setFixedWidth(250)
        self.selector_categoria.currentIndexChanged.connect(lambda: self.mostrar_crear_nueva_categoria())

        self.etiqueta_selector_categoria = QLabel("Categoría: ")
        self.etiqueta_selector_categoria.setProperty("cssClass", "etiqueta_formulario")

        self.contenedor_selector_categoria.layout().addWidget(self.etiqueta_selector_categoria)
        self.contenedor_selector_categoria.layout().addWidget(self.selector_categoria)

    def crear_campo_nueva_categoria(self):
        self.contenedor_nueva_categoria = QWidget()
        self.contenedor_nueva_categoria_layout = QHBoxLayout()
        self.contenedor_nueva_categoria.setLayout(self.contenedor_nueva_categoria_layout)
        self.contenedor_nueva_categoria_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.campo_nueva_categoria = QLineEdit()
        self.campo_nueva_categoria.setFixedHeight(30)
        self.campo_nueva_categoria.setFixedWidth(250)

        self.etiqueta_nueva_categoria = QLabel("Ingresa el nombre de la categoría: ")
        self.etiqueta_nueva_categoria.setFixedWidth(int(self.etiqueta_nueva_categoria.sizeHint().width() * 1.5))
        self.etiqueta_nueva_categoria.setProperty("cssClass", "etiqueta_formulario")

        self.contenedor_nueva_categoria.layout().addWidget(self.etiqueta_nueva_categoria)
        self.contenedor_nueva_categoria.layout().addWidget(self.campo_nueva_categoria)

    def crear_selector_receta(self):
        self.contenedor_receta = QWidget()
        self.contenedor_receta_layout = QHBoxLayout()
        self.contenedor_receta.setLayout(self.contenedor_receta_layout)
        self.contenedor_receta_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.selector_receta_base = QComboBox()
        self.selector_receta_base.setFixedHeight(30)
        self.selector_receta_base.setFixedWidth(250)
        self.selector_receta_base.insertItems(len(self.lista_nombre_recetas), self.lista_nombre_recetas)
        self.selector_receta_base.setCurrentIndex(-1)

        self.etiqueta_receta_base = QLabel("Receta base: ")
        self.etiqueta_receta_base.setProperty("cssClass", "etiqueta_formulario")

        self.contenedor_receta.layout().addWidget(self.etiqueta_receta_base)
        self.contenedor_receta.layout().addWidget(self.selector_receta_base)

    def llenar_formulario(self, platillo_nombre:str, categoria:str, receta_base:str):
        self.campo_nombre.setText(platillo_nombre)

        categoria_idx = self.lista_nombre_categorias.index(categoria)
        receta_idx = self.lista_nombre_recetas.index(receta_base)

        self.selector_categoria.setCurrentIndex(categoria_idx)
        self.selector_receta_base.setCurrentIndex(receta_idx)

    def mostrar_crear_nueva_categoria(self):
        mostrando_nueva_cat_campo = not self.campo_nueva_categoria.visibleRegion().isEmpty()

        if self.selector_categoria.currentIndex() is not (len(self.lista_nombre_categorias) - 1) and mostrando_nueva_cat_campo is False:
            return

        self.toggle_campo_nueva_receta()

    def toggle_campo_nueva_receta(self):

        if self.campo_nueva_categoria.visibleRegion().isEmpty():
            self.contenedor_receta.setParent(None)
            self.layout.addWidget(self.contenedor_nueva_categoria, 4, 0)
            self.layout.addWidget(self.contenedor_receta, 5, 0)
        else:
            self.contenedor_nueva_categoria.setParent(None)
            self.layout.addWidget(self.contenedor_receta, 4, 0)

    def asignar_lista_recetas(self, lista:list[Receta]):
        self.lista_nombre_recetas = [receta.nombre for receta in lista]

        if len(self.lista_nombre_categorias):
            self.crear_formulario()

    def asignar_lista_categorias(self, lista:list[Categoria]):
        self.lista_nombre_categorias = [cat.nombre for cat in lista]
        self.lista_nombre_categorias.append("Crear nueva categoría")

        if len(self.lista_nombre_recetas):
            self.crear_formulario()

    def emitir_evento_guardar_platillo(self):
        self.guardar_platillo_signal.emit()

    def emitir_evento_volver(self):
        self.volver_vista_anterior_signal.emit()