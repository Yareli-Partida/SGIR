from PySide6.QtCore import QObject, Slot

from controllers.ControladorCrearEditarMenu import ControladorCrearEditarMenu
from controllers.ControladorCrearEditarOrdenCompra import ControladorCrearEditarOrdenCompra
from controllers.ControladorCrearEditarReceta import ControladorCrearEditarReceta
from controllers.ControladorDetallesMenu import ControladorDetallesMenu
from controllers.ControladorDetallesOrdenCompra import ControladorDetallesOrdenCompra
from controllers.ControladorListaMenus import ControladorListaMenus
from controllers.ControladorListaOrdenesCompra import ControladorListaOrdenesCompra
from models.Menu import Menu
from models.OrdenCompra import OrdenCompra
from models.Receta import Receta
from views.VistaHome import VistaHome

from views.VistaListaRecetas import VistaListaRecetas
from views.VistaCrearEditarReceta import VistaCrearEditarReceta
from views.VistaRecetaDetalles import VistaRecetaDetalles

from views.VistaListaMenus import VistaListaMenus
from views.VistaCrearEditarMenu import VistaCrearEditarMenu
from views.VistaMenuDetalles import VistaMenuDetalles

from views.VistaListaOrdenesCompra import VistaListaOrdenesCompra
from views.VistaCrearEditarOrdenCompra import VistaCrearEditarOrdenCompra
from views.VistaOrdenesCompraDetalles import VistaOrdenesCompraDetalles

from views.VistaVentanaPrincipal import VistaVentanaPrincipal

from controllers.ControladorListaRecetas import ControladorListaRecetas
from controllers.ControladorDetallesReceta import ControladorDetallesReceta


class ControladorPrincipal(QObject):
    def __init__(self, vista:VistaVentanaPrincipal, servicio=None):
        """
        Controlador para la ventana principal que se encarga de cambiar el widget principal.

        """

        super().__init__()

        self.vista = vista
        self.servicio = servicio

        self.vista.abrir_vista_home_signal.connect(self.mostrar_vista_home)
        self.vista.abrir_recetas_signal.connect(self.mostrar_vista_recetas)
        self.vista.abrir_menus_signal.connect(self.mostrar_vista_menus)
        self.vista.abrir_ordenes_compra.connect(self.mostrar_vista_ordenes_compra)

    def mostrar_vista_home(self):
        self.vista.setCentralWidget(VistaHome())

    def mostrar_vista_recetas(self):
        vista_lista_recetas = VistaListaRecetas()
        ControladorListaRecetas(vista_lista_recetas, self.vista)

        vista_lista_recetas.abrir_crear_receta_signal.connect(self.mostrar_vista_crear_receta)
        vista_lista_recetas.abrir_detalles_receta_signal.connect(self.mostrar_vista_detalles_receta)

        self.vista.setCentralWidget(vista_lista_recetas)
        vista_lista_recetas.mostrar_recetas_signal.emit()

    def mostrar_vista_crear_receta(self):
        vista_crear_receta = VistaCrearEditarReceta()
        vista_crear_receta.volver_vista_anterior_signal.connect(self.mostrar_vista_recetas)

        self.vista.setCentralWidget(vista_crear_receta)

    @Slot(Receta)
    def mostrar_vista_detalles_receta(self, receta:Receta):
        vista_detalles_recetas = VistaRecetaDetalles(receta)
        vista_detalles_recetas.abrir_vista_editar_signal.connect(lambda receta_obj=receta: self.mostrar_vista_editar_receta(receta_obj))
        vista_detalles_recetas.volver_vista_anterior_signal.connect(self.mostrar_vista_recetas)

        ControladorDetallesReceta(vista_detalles_recetas)

        self.vista.setCentralWidget(vista_detalles_recetas)
        vista_detalles_recetas.mostrar_detalles_signal.emit(receta)

    @Slot(Receta)
    def mostrar_vista_editar_receta(self, receta:Receta):
        vista_editar_receta = VistaCrearEditarReceta(receta)
        vista_editar_receta.volver_vista_anterior_signal.connect(lambda receta_obj=receta: self.mostrar_vista_detalles_receta(receta_obj))

        ControladorCrearEditarReceta(vista_editar_receta)

        self.vista.setCentralWidget(vista_editar_receta)
        vista_editar_receta.llenar_forma_signal.emit(receta)

    def mostrar_vista_menus(self):
        vista_menus = VistaListaMenus()
        vista_menus.abrir_crear_menu_signal.connect(self.mostrar_vista_crear_menu)
        vista_menus.abrir_detalles_signal.connect(self.mostrar_vista_detalles_menu)

        ControladorListaMenus(vista_menus)

        self.vista.setCentralWidget(vista_menus)
        vista_menus.mostrar_menus_signal.emit()

    def mostrar_vista_crear_menu(self):
        vista_crear_menu = VistaCrearEditarMenu()
        vista_crear_menu.volver_vista_anterior_signal.connect(self.mostrar_vista_menus)

        ControladorCrearEditarMenu(vista_crear_menu)

        self.vista.setCentralWidget(vista_crear_menu)
        vista_crear_menu.obtener_platillos_signal.emit()

    @Slot(Menu)
    def mostrar_vista_detalles_menu(self, menu:Menu):
        vista_detalles_menu = VistaMenuDetalles(menu)
        vista_detalles_menu.volver_vista_anterior_signal.connect(self.mostrar_vista_menus)
        vista_detalles_menu.abrir_editar_menu_signal.connect(lambda menu_obj=menu: self.mostrar_vista_editar_menu(menu_obj))

        ControladorDetallesMenu(vista_detalles_menu)

        self.vista.setCentralWidget(vista_detalles_menu)
        vista_detalles_menu.mostrar_detalles_signal.emit(menu)

    @Slot(Menu)
    def mostrar_vista_editar_menu(self, menu:Menu):
        vista_editar_menu = VistaCrearEditarMenu(menu)
        vista_editar_menu.volver_vista_anterior_signal.connect(lambda menu_obj=menu: self.mostrar_vista_detalles_menu(menu_obj))

        ControladorCrearEditarMenu(vista_editar_menu)

        self.vista.setCentralWidget(vista_editar_menu)
        vista_editar_menu.obtener_platillos_signal.emit()
        vista_editar_menu.llenar_forma_signal.emit(menu)

    def mostrar_vista_ordenes_compra(self):
        vista_ordenes_compra = VistaListaOrdenesCompra()
        # vista_ordenes_compra.abrir_crear_orden_signal.connect()
        vista_ordenes_compra.abrir_detalles_orden_signal.connect(self.mostrar_vista_detalles_orden_compra)

        ControladorListaOrdenesCompra(vista_ordenes_compra)

        self.vista.setCentralWidget(vista_ordenes_compra)
        vista_ordenes_compra.mostrar_ordenes_signal.emit()

    def mostrar_vista_crear_orden_compra(self):
        vista_crear_orden_compra = VistaCrearEditarOrdenCompra()
        vista_crear_orden_compra.volver_vista_anterior_signal.connect(self.mostrar_vista_ordenes_compra)

        ControladorCrearEditarOrdenCompra(vista_crear_orden_compra)

        self.vista.setCentralWidget(vista_crear_orden_compra)
        vista_crear_orden_compra.obtener_insumos_signal.emit()

    @Slot(OrdenCompra)
    def mostrar_vista_detalles_orden_compra(self, orden:OrdenCompra):
        vista_detalles_orden_compra = VistaOrdenesCompraDetalles(orden)
        vista_detalles_orden_compra.volver_vista_anterior_signal.connect(self.mostrar_vista_ordenes_compra)
        vista_detalles_orden_compra.abrir_vista_editar_orden_signal.connect(lambda orden_obj=orden: self.mostrar_vista_editar_orden_compra(orden_obj))

        ControladorDetallesOrdenCompra(vista_detalles_orden_compra)

        self.vista.setCentralWidget(vista_detalles_orden_compra)
        vista_detalles_orden_compra.mostrar_detalles_signal.emit(orden)

    @Slot(OrdenCompra)
    def mostrar_vista_editar_orden_compra(self, orden: OrdenCompra):
        vista_editar_orden_compra = VistaCrearEditarOrdenCompra(orden)
        vista_editar_orden_compra.volver_vista_anterior_signal.connect(lambda orden_obj=orden: self.mostrar_vista_detalles_orden_compra(orden_obj))

        ControladorCrearEditarOrdenCompra(vista_editar_orden_compra)

        self.vista.setCentralWidget(vista_editar_orden_compra)
        vista_editar_orden_compra.obtener_insumos_signal.emit()
        vista_editar_orden_compra.llenar_forma_signal.emit(orden)