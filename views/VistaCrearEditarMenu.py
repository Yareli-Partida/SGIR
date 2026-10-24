from pathlib import Path

from PySide6.QtWidgets import *
from PySide6.QtCore import Signal

from models.Menu import Menu
from models.Platillo import Platillo
from views.widgets.BotonPrincipalWidget import BotonPrincipalWidget
from views.widgets.BotonSecundarioWidget import BotonSecundarioWidget
from views.widgets.TablaResponsivaDesigual import TablaResponsivaDesigual
from views.widgets.EspacioHorizontalWidget import EspacioHorizontalWidget

class VistaCrearEditarMenu(QWidget):
    """
    Vista para crear y editar un menú.

        :param menu: (None/Menu): Es el menú que se quiere mostrar si es que se va a usar la vista para editar uno.

        :var obtener_platillos_signal: (Signal): Señal para pedir al controlador todos los platillos.
        :var llenar_forma_signal: (Signal(Menu)): Señal para llenar la tabla de platillos si se va a editar.
        :var volver_vista_anterior_signal: (Signal(Menu)): Señal para ir a la vista anterior.
        :var guardar_menu_signal: (Signal): Señal para guardar el formulario actual.
        :var lista_opciones_platillos: (list[Platillo]): Los platillos que mostrarán los combobox.
        :var boton_volver: (QPushBotton): Botón para volver a la vista anterior.
        :var boton_guardar: (QPushBotton): Botón para guardar la info actual en la forma en el menú actual o uno nuevo.
        :var contenedor_botones: (QWidget): Contiene los botones volver y guardar.
        :var titulo: (QLabel): Título principal de la vista. Cambia en función de si se va a editar o crear.
        :var boton_agregar_platillo: (QPushBotton): Botón para agregar una fila en blanco a la tabla de platillos.
        :var tabla_platillos: (TablaResponsivaDesigual): Tabla donde se muestran los detalles de cada platillo.
    """

    obtener_platillos_signal = Signal()
    llenar_forma_signal = Signal(Menu)
    volver_vista_anterior_signal = Signal()
    guardar_menu_signal = Signal()

    def __init__(self, menu=None):
        super().__init__()

        self.layout = QVBoxLayout()
        self.lista_opciones_platillos = []

        self.boton_volver = BotonPrincipalWidget("Volver")
        self.boton_volver.setFixedWidth(self.boton_volver.sizeHint().width() * 2)
        self.boton_volver.clicked.connect(self.emitir_evento_volver)
        self.boton_guardar = BotonPrincipalWidget("Guardar")
        self.boton_guardar.setFixedWidth(self.boton_guardar.sizeHint().width() * 2)
        self.boton_guardar.clicked.connect(self.emitir_evento_guardar)

        self.contenedor_botones = QWidget()
        self.contenedor_botones.setLayout(QHBoxLayout())
        self.contenedor_botones.layout().addWidget(self.boton_volver)
        self.contenedor_botones.layout().addSpacerItem(EspacioHorizontalWidget())
        self.contenedor_botones.layout().addWidget(self.boton_guardar)

        self.titulo = QLabel()
        self.titulo.setObjectName("titulo_crear_editar")
        self.titulo.setProperty("cssClass", "titulo")

        self.boton_agregar_platillo = BotonSecundarioWidget("Agregar platillo")
        self.boton_agregar_platillo.clicked.connect(self.agregar_fila_tabla_platillo)

        self.tabla_platillos = TablaResponsivaDesigual()
        encabezados = ["Categoría", "Platillo", "Precio"]
        self.tabla_platillos.verticalHeader().hide()
        self.tabla_platillos.setColumnCount(3)
        self.tabla_platillos.setRowCount(0)
        self.tabla_platillos.setHorizontalHeaderLabels(encabezados)

        if menu:
            self.titulo.setText("Editar Menú")
        else:
            self.titulo.setText("Crear Menú")

        self.layout.addWidget(self.contenedor_botones)
        self.layout.addWidget(self.titulo)
        self.layout.addWidget(self.boton_agregar_platillo)
        self.layout.addWidget(self.tabla_platillos)

        self.setLayout(self.layout)

        self.setStyleSheet((Path('views/styles/estilos_menus.qss').read_text()))

    def agregar_fila_tabla_platillo(self, nombre_platillo=None, precio_platillo=None, categoria=None) -> None:
        """
        Agrega una fila en blanco o llena a la tabla Platillos dependiendo los args.

            :param nombre_platillo: (String/None): El nombre del platillo que se va a agregar a la fila.
            :param precio_platillo: (int/None): El precio del platillo que se va a agregar a la fila.
            :param categoria: (String/None): El nombre de la categoría a la que pertenece el platillo.

        """

        self.tabla_platillos.setRowCount(self.tabla_platillos.rowCount() + 1)
        num_fila = self.tabla_platillos.rowCount() - 1
        selector_platillo_nombre = QComboBox()
        # lista_nombres_platillos = [platillo.nombre for platillo in self.lista_opciones_platillos]
        lista_nombres_platillos = [platillo["nombre"] for platillo in self.lista_opciones_platillos]
        selector_platillo_nombre.insertItems(len(self.lista_opciones_platillos), lista_nombres_platillos)

        if nombre_platillo:
            selector_platillo_nombre.setCurrentIndex(lista_nombres_platillos.index(nombre_platillo))
        else:
            selector_platillo_nombre.setCurrentIndex(-1)

        selector_platillo_precio = QDoubleSpinBox()
        selector_platillo_precio.setMaximum(999999)
        selector_platillo_precio.setPrefix("$")

        if precio_platillo:
            selector_platillo_precio.setValue(precio_platillo)

        # Categoria hard coded para testeo
        etiqueta_platillo_categoria = QTableWidgetItem("")

        if categoria:
            etiqueta_platillo_categoria.setText(categoria)

        selector_platillo_nombre.currentIndexChanged.connect(lambda: self.cambiar_texto_etiqueta_categoria(etiqueta_platillo_categoria))

        self.tabla_platillos.setItem(num_fila, 0, etiqueta_platillo_categoria)
        self.tabla_platillos.setCellWidget(num_fila, 1, selector_platillo_nombre)
        self.tabla_platillos.setCellWidget(num_fila, 2, selector_platillo_precio)

        num_fila += 1

    def cambiar_texto_etiqueta_categoria(self, etiqueta:QTableWidgetItem) -> None:
        """
        Borraré esto al final
        :param etiqueta: (QTableWidgetItem)
        :return:
        """

        etiqueta.setText("Platillo Fuerte")

    def asignar_platillos_combobox(self, lista:list[Platillo]) -> None:
        """
        Asigna la lista de platillos que pasa el controlador al atributo lista_opciones_platillos. Esto se usará para
        asignar como opciones a los combobox.

        :param lista: (list[Platillo]): Lista de todos los platillos en la BD.
        """

        self.lista_opciones_platillos = lista

    def emitir_evento_volver(self) -> None:
        """
        Emite la señal para volver a la vista anterior.
        """

        self.volver_vista_anterior_signal.emit()

    def emitir_evento_guardar(self) -> None:
        """
        Emite la señal para guardar los datos en el formulario actual.
        """

        self.guardar_menu_signal.emit()
