from PySide6 import QtCore
from PySide6.QtWidgets import *
from PySide6.QtGui import Qt

from models.Menu import Menu
from models.Platillo import Platillo
from views.widgets.BotonPrincipalWidget import BotonPrincipalWidget
from views.widgets.TablaResponsivaDesigual import TablaResponsivaDesigual
from views.widgets.EspacioHorizontalWidget import EspacioHorizontalWidget

class VistaMenuDetalles(QVBoxLayout):
    """
    Vista para ver detalles de un menú.

    :param menu: (Menu): Menú a mostrar.

    :var boton_volver: (BotonPrincipalWidget): Botón para volver a la vista anterior.
    :var boton_editar_menu: (BotonPrincipalWidget): Botón para ir a la vista de editar con el menú actual.
    :var contenedor_botones: (QWidget): Contiene los botones volver y editar.
    :var titulo_principal: (QLabel): Título principal de la vista.
    :var tabla_detalles_platillos: (QTableWidget): Tabla que muestra los platillos del menú.

    """
    def __init__(self, menu:Menu):
        super().__init__()

        self.boton_volver = BotonPrincipalWidget("Volver")
        self.boton_volver.setFixedWidth(self.boton_volver.sizeHint().width() * 2)

        self.boton_editar_menu = BotonPrincipalWidget("Editar")
        self.boton_editar_menu.setFixedWidth(self.boton_editar_menu.sizeHint().width() * 2)

        self.contenedor_botones = QWidget()
        self.contenedor_botones.setLayout(QHBoxLayout())
        self.contenedor_botones.layout().addWidget(self.boton_volver)
        self.contenedor_botones.layout().addSpacerItem(EspacioHorizontalWidget())
        self.contenedor_botones.layout().addWidget(self.boton_editar_menu)

        self.titulo_principal = QLabel(menu.nombre)
        self.titulo_principal.setObjectName("titulo_principal_detalles")
        self.titulo_principal.setProperty("cssClass", "titulo")

        self.tabla_detalles_platillos = TablaResponsivaDesigual()
        self.tabla_detalles_platillos.setShowGrid(False)
        self.tabla_detalles_platillos.setObjectName("tabla_detalles_platillos")
        self.tabla_detalles_platillos.setColumnCount(3)
        encabezados = ["Categoría", "Platillo", "Precio"]
        self.tabla_detalles_platillos.setHorizontalHeaderLabels(encabezados)

        self.addWidget(self.contenedor_botones)
        self.addWidget(self.titulo_principal)
        self.addWidget(self.tabla_detalles_platillos)

    def agregar_platillos_tabla(self, lista_platillos:list[Platillo]) -> None:
        """
        Llena la tabla detalles platillos.

        :param lista_platillos: (list[Platillo]): Lista de los platillos por agregar.
        :return:
        """

        self.tabla_detalles_platillos.setRowCount(len(lista_platillos))
        contador_fila = 0

        for platillo in lista_platillos:
            platillo_nombre = QTableWidgetItem(platillo.nombre)
            platillo_nombre.setFlags(QtCore.Qt.ItemFlag.ItemIsEditable)

            platillo_precio = QTableWidgetItem(f"${platillo.precio}")
            platillo_precio.setTextAlignment(Qt.AlignmentFlag.AlignVCenter)
            platillo_precio.setFlags(QtCore.Qt.ItemFlag.ItemIsEditable)

            # Categoria hard coded para testeo
            platillo_categoria = QTableWidgetItem("Platillo Fuerte")
            platillo_categoria.setFlags(QtCore.Qt.ItemFlag.ItemIsEditable)

            self.tabla_detalles_platillos.setItem(contador_fila, 0, platillo_categoria)
            self.tabla_detalles_platillos.setItem(contador_fila, 1, platillo_nombre)
            self.tabla_detalles_platillos.setItem(contador_fila, 2, platillo_precio)

            contador_fila += 1
