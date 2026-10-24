from PySide6 import QtWidgets, QtCore, QtGui


class BarraHerramientasWidget(QtWidgets.QToolBar):
    """
    Barra de herramientas lateral con acceso a todas las herramientas.

    """

    def __init__(self):
        super().__init__()
        self.setMovable(False)

        self.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        # Crea etiquetas de cada sección
        etiqueta_nombre_proyecto = QtWidgets.QLabel("SGIR")
        etiqueta_nombre_proyecto.setObjectName("proyecto_titulo")
        etiqueta_seccion_herramientas = QtWidgets.QLabel("Herramientas")
        etiqueta_seccion_gestion_consulta = QtWidgets.QLabel("Gestión y consultas")

        # Agrega etiquetas y botones a la barra_herramientas
        self.addWidget(etiqueta_nombre_proyecto)
        self.addSeparator()

        self.addWidget(etiqueta_seccion_herramientas)

        self.boton_recetas = self.crear_boton_recetas()
        self.addAction(self.boton_recetas)

        # self.addAction(self.crear_boton_platillos())
        self.boton_menus = self.crear_boton_menus()
        self.addAction(self.boton_menus)

        self.boton_ordenes_compra = self.crear_boton_ordenes_compra()
        self.addAction(self.boton_ordenes_compra)

        self.addSeparator()

        self.addWidget(etiqueta_seccion_gestion_consulta)

        self.boton_inventario = self.crear_boton_inventario()
        self.addAction(self.boton_inventario)

        self.boton_merma = self.crear_boton_merma()
        self.addAction(self.boton_merma)

        self.boton_ventas = self.crear_boton_ventas()
        self.addAction(self.boton_ventas)

    def crear_boton_recetas(self):
        recetas_action_button = QtGui.QAction(QtGui.QIcon("views/resources/icons/icono_receta.svg"), "&Recetas", self)
        recetas_action_button.setStatusTip("Crea, modifica y consulta recetas")
        return recetas_action_button

    def crear_boton_menus(self):
        menus_action_button = QtGui.QAction(QtGui.QIcon("views/resources/icons/icono_menu.svg"), "&Menús", self)
        menus_action_button.setStatusTip("Crea, modifica y consulta menús")
        return menus_action_button

    def crear_boton_ordenes_compra(self):
        list_compras_action_button = QtGui.QAction(QtGui.QIcon("views/resources/icons/icono_orden_compra.svg"),
                                                   "&Ordenes de Compra", self)
        list_compras_action_button.setStatusTip("Genera, actualiza y consulta ordenes de compra")
        return list_compras_action_button

    def crear_boton_inventario(self):
        inventario_action_button = QtGui.QAction(QtGui.QIcon("views/resources/icons/icono_inventario.svg"),
                                                 "&Inventario", self)
        inventario_action_button.setStatusTip("Consulta y actualiza el inventario")
        return inventario_action_button

    def crear_boton_merma(self):
        merma_action_button = QtGui.QAction(QtGui.QIcon("views/resources/icons/icono_merma.svg"), "&Merma", self)
        merma_action_button.setStatusTip("Consulta y actualiza la merma")
        return merma_action_button

    def crear_boton_ventas(self):
        ventas_action_button = QtGui.QAction(QtGui.QIcon("views/resources/icons/icono_venta.svg"), "&Ventas", self)
        ventas_action_button.setStatusTip("Consulta y registra ventas")
        return ventas_action_button