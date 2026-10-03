from PySide6 import QtCore, QtWidgets, QtGui

from views.VistaPrincipal import VistaPrincipal
from controllers.ControladorRecetas import ControladorRecetas

class ControladorPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self._vista_principal = VistaPrincipal()
        self._barra_herramientas = None

        self.setCentralWidget(self._vista_principal)
        self.crear_barra_herramientas()
        self.setStatusBar(QtWidgets.QStatusBar(self))

    def crear_barra_herramientas(self):
        self._barra_herramientas = QtWidgets.QToolBar("Barra de herramientas")
        self._barra_herramientas.setMovable(False)

        self._barra_herramientas.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.addToolBar(QtCore.Qt.LeftToolBarArea, self._barra_herramientas)

        # Crea etiquetas de cada sección
        etiqueta_nombre_proyecto = QtWidgets.QLabel("SGIR")
        etiqueta_nombre_proyecto.setObjectName("proyecto_titulo")
        etiqueta_seccion_herramientas = QtWidgets.QLabel("Herramientas")
        etiqueta_seccion_gestion_consulta = QtWidgets.QLabel("Gestión y consultas")

        # Agrega etiquetas y botones a la _barra_herramientas
        self._barra_herramientas.addWidget(etiqueta_nombre_proyecto)
        self._barra_herramientas.addSeparator()

        self._barra_herramientas.addWidget(etiqueta_seccion_herramientas)
        self._barra_herramientas.addAction(self.crear_boton_recetas())
        self._barra_herramientas.addAction(self.crear_boton_platillos())
        self._barra_herramientas.addAction(self.crear_boton_menus())
        self._barra_herramientas.addAction(self.crear_boton_ordenes_compra())
        self._barra_herramientas.addSeparator()

        self._barra_herramientas.addWidget(etiqueta_seccion_gestion_consulta)
        self._barra_herramientas.addAction(self.crear_boton_inventario())
        self._barra_herramientas.addAction(self.crear_boton_merma())
        self._barra_herramientas.addAction(self.crear_boton_ventas())

    def crear_boton_recetas(self):
        recetas_action_button = QtGui.QAction(QtGui.QIcon("views/resources/icons/icono_receta.svg"), "&Recetas", self)
        recetas_action_button.setStatusTip("Crea, modifica y consulta recetas")
        recetas_action_button.triggered.connect(self.mostrar_recetas)
        return recetas_action_button

    def crear_boton_platillos(self):
        platillos_action_button = QtGui.QAction(QtGui.QIcon("views/resources/icons/icono_platillo.svg"), "&Platillos",
                                                self)
        platillos_action_button.setStatusTip("Crea, modifica y consulta platillos")
        # recetas_action_button.triggered.connect(self.show_recetas_widget)
        return platillos_action_button

    def crear_boton_menus(self):
        menus_action_button = QtGui.QAction(QtGui.QIcon("views/resources/icons/icono_menu.svg"), "&Menús", self)
        menus_action_button.setStatusTip("Crea, modifica y consulta menús")
        # recetas_action_button.triggered.connect(self.show_recetas_widget)
        return menus_action_button

    def crear_boton_ordenes_compra(self):
        list_compras_action_button = QtGui.QAction(QtGui.QIcon("views/resources/icons/icono_orden_compra.svg"),
                                                   "&Lista de Compras", self)
        list_compras_action_button.setStatusTip("Genera, actualiza y consulta ordenes de compras")
        # list_compras_action_button.triggered.connect(self.toolbar_button_clicked)
        return list_compras_action_button

    def crear_boton_inventario(self):
        inventario_action_button = QtGui.QAction(QtGui.QIcon("views/resources/icons/icono_inventario.svg"),
                                                 "&Inventario", self)
        inventario_action_button.setStatusTip("Consulta y actualiza el inventario")
        # inventario_action_button.triggered.connect(self.toolbar_button_clicked)
        return inventario_action_button

    def crear_boton_merma(self):
        merma_action_button = QtGui.QAction(QtGui.QIcon("views/resources/icons/icono_merma.svg"), "&Merma", self)
        merma_action_button.setStatusTip("Consulta y actualiza la merma")
        # merma_action_button.triggered.connect(self.toolbar_button_clicked)
        return merma_action_button

    def crear_boton_ventas(self):
        ventas_action_button = QtGui.QAction(QtGui.QIcon("views/resources/icons/icono_venta.svg"), "&Ventas", self)
        ventas_action_button.setStatusTip("Consulta y registra ventas")
        # ventas_action_button.triggered.connect(self.toolbar_button_clicked)
        return ventas_action_button

    def mostrar_recetas(self):
        self.setCentralWidget(ControladorRecetas())

    def mostrar_platillos(self):
        self.setCentralWidget(ControladorRecetas())