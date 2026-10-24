from pathlib import Path

from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from PySide6.QtCore import Signal

from models.Receta import Receta
from views.widgets.BotonPrincipalWidget import BotonPrincipalWidget
from views.widgets.BotonSecundarioWidget import BotonSecundarioWidget
from views.widgets.EspacioHorizontalWidget import EspacioHorizontalWidget
from views.widgets.TablaResponsivaRegular import TablaResponsivaRegular

class VistaCrearEditarReceta(QWidget):
    """
    Vista para crear y editar recetas.

        :param receta_editar: (None/Receta): Es la receta que se quiere mostrar si es que se va a usar la vista para editar una.

        :var llenar_forma_signal: (Signal(OrdenCompra)): Señal para llenar la tabla de ingredientes si se va a editar.
        :var volver_vista_anterior_signal: (Signal): Señal para ir a la vista anterior.
        :var guardar_receta_signal: (Signal): Señal para guardar el formulario actual.
        :var titulo: (QLabel): Título principal de la vista.
        :var botones_contenedor: (QWidget): Contiene los botones guardar y volver.
        :var boton_guardar_receta: (BotonPrincipalWidget): Botón para guardar la info actual en la forma en la receta actual o una nueva.
        :var boton_volver: (BotonPrincipalWidget): Botón para volver a la vista anterior.
        :var nombre_receta_contenedor: (QWidget): Contiene la etiqueta de nombre de receta y su campo de texto.
        :var etiqueta_nombre_receta: (QLabel): Indica el campo del nombre de la receta.
        :var campo_nombre_receta: (QLineEdit): Campo editable del nombre de la receta.
        :var num_porciones_contenedor: (QWidget): Contiene la etiqueta de num porciones y su selector.
        :var etiqueta_num_porciones: (QLabel): Indica el selector del num de porciones.
        :var selector_num_porciones: (QSpinBox): Selector de número de porciones.
        :var tabla_ingredientes_titulo_contenedor: (QWidget): Contiene la etiqueta de tabla ingredientes y su botón para agregar fila.
        :var etiqueta_tabla_ingredientes: (QLabel): Título de la tabla ingredientes.
        :var boton_agregar_ingrediente: (QPushButton): Botón para agregar una fila en blanco a la tabla ingredientes.
        :var tabla_ingredientes: (TablaResponsivaRegular): Tabla donde se muestran los detalles de los ingredientes.
        :var tabla_instrucciones_titulo_contenedor: (QWidget): Contiene la etiqueta de la tabla instrucciones y su botón para agregar fila.
        :var etiqueta_tabla_instrucciones: (QLabel): Título de la tabla instrucciones.
        :var boton_agregar_instruccion: (BotonSecundarioWidget): Botón para agregar una fila en blanco a la tabla instrucciones.
        :var tabla_instrucciones: (TablaResponsivaRegular): Tabla donde se muestran las instrucciones.

    """

    llenar_forma_signal = Signal(Receta)
    volver_vista_anterior_signal = Signal()
    guardar_receta_signal = Signal()

    def __init__(self, receta_editar=None):
        super().__init__()

        self.layout = QVBoxLayout()

        self.titulo = QLabel()
        self.titulo.setObjectName("titulo")
        self.titulo.setProperty("cssClass", "titulo")

        self.botones_contenedor = QWidget()
        self.botones_contenedor.setLayout(QHBoxLayout())
        self.boton_guardar_receta = BotonPrincipalWidget("Guardar")
        self.boton_guardar_receta.setFixedWidth(self.boton_guardar_receta.sizeHint().width() * 2)
        self.boton_guardar_receta.clicked.connect(self.emitir_evento_guardar_receta)
        self.boton_volver = BotonPrincipalWidget("Volver")
        self.boton_volver.setFixedWidth(self.boton_volver.sizeHint().width() * 2)
        self.boton_volver.clicked.connect(self.emitir_evento_abrir_volver)
        self.botones_contenedor.layout().addWidget(self.boton_volver)
        self.botones_contenedor.layout().addSpacerItem(EspacioHorizontalWidget())
        self.botones_contenedor.layout().addWidget(self.boton_guardar_receta)

        self.nombre_receta_contenedor = QWidget()
        self.nombre_receta_contenedor.setLayout(QHBoxLayout())
        self.nombre_receta_contenedor.layout().setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.etiqueta_nombre_receta = QLabel("Nombre:")
        self.etiqueta_nombre_receta.setObjectName("etiqueta_nombre_receta")
        self.etiqueta_nombre_receta.setFixedWidth(self.etiqueta_nombre_receta.sizeHint().width())
        self.campo_nombre_receta = QLineEdit()
        self.campo_nombre_receta.setObjectName("campo_nombre_receta")
        self.nombre_receta_contenedor.layout().addWidget(self.etiqueta_nombre_receta)
        self.nombre_receta_contenedor.layout().addWidget(self.campo_nombre_receta)

        self.num_porciones_contenedor = QWidget()
        self.num_porciones_contenedor.setObjectName("num_porciones_contenedor")
        self.num_porciones_contenedor.setLayout(QHBoxLayout())
        self.num_porciones_contenedor.layout().setObjectName("num_porciones_contenedor_layout")
        self.num_porciones_contenedor.layout().setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.etiqueta_num_porciones = QLabel("Número de porciones: ")
        self.etiqueta_num_porciones.setObjectName("etiqueta_num_porciones")
        self.selector_num_porciones = QSpinBox()
        self.selector_num_porciones.setObjectName("selector_num_porciones")
        self.num_porciones_contenedor.layout().addWidget(self.etiqueta_num_porciones)
        self.num_porciones_contenedor.layout().addWidget(self.selector_num_porciones)

        self.tabla_ingredientes_titulo_contenedor = QWidget()
        self.tabla_ingredientes_titulo_contenedor.setObjectName("tabla_ingredientes_titulo_contenedor")
        self.tabla_ingredientes_titulo_contenedor.setLayout(QHBoxLayout())
        self.tabla_ingredientes_titulo_contenedor.layout().setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.tabla_ingredientes_titulo_contenedor.layout().setObjectName("tabla_ingredientes_titulo_contenedor_layout")
        self.etiqueta_tabla_ingredientes = QLabel("Ingredientes")
        self.etiqueta_tabla_ingredientes.setFixedWidth(self.etiqueta_tabla_ingredientes.sizeHint().width())
        self.etiqueta_tabla_ingredientes.setObjectName("etiqueta_tabla_ingredientes")
        self.boton_agregar_ingrediente = BotonSecundarioWidget("Agregar")
        self.boton_agregar_ingrediente.setObjectName("boton_agregar_ingrediente")
        self.boton_agregar_ingrediente.clicked.connect(self.agregar_fila_ingrediente)
        self.tabla_ingredientes_titulo_contenedor.layout().addWidget(self.etiqueta_tabla_ingredientes)
        self.tabla_ingredientes_titulo_contenedor.layout().addWidget(self.boton_agregar_ingrediente)

        self.tabla_ingredientes = TablaResponsivaRegular()
        self.tabla_ingredientes.setObjectName("tabla_ingredientes")

        self.tabla_instrucciones_titulo_contenedor = QWidget()
        self.tabla_instrucciones_titulo_contenedor.setObjectName("tabla_instrucciones_titulo_contenedor")
        self.tabla_instrucciones_titulo_contenedor.setLayout(QHBoxLayout())
        self.tabla_instrucciones_titulo_contenedor.layout().setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.tabla_instrucciones_titulo_contenedor.layout().setObjectName("tabla_instrucciones_titulo_contenedor_layout")
        self.etiqueta_tabla_instrucciones = QLabel("Instrucciones")
        self.etiqueta_tabla_instrucciones.setObjectName("instrucciones")
        self.etiqueta_tabla_instrucciones.setFixedWidth(self.etiqueta_tabla_instrucciones.sizeHint().width())
        self.boton_agregar_instruccion = BotonSecundarioWidget("Agregar")
        self.boton_agregar_instruccion.clicked.connect(self.agregar_fila_instruccion)
        self.boton_agregar_instruccion.setObjectName("boton_agregar_instruccion")
        self.tabla_instrucciones_titulo_contenedor.layout().addWidget(self.etiqueta_tabla_instrucciones)
        self.tabla_instrucciones_titulo_contenedor.layout().addWidget(self.boton_agregar_instruccion)

        self.tabla_instrucciones = TablaResponsivaRegular()
        self.tabla_instrucciones.setObjectName("tabla_instrucciones")

        self.layout.addWidget(self.botones_contenedor)
        self.layout.addWidget(self.titulo)
        self.layout.addWidget(self.nombre_receta_contenedor)
        self.layout.addWidget(self.num_porciones_contenedor)
        self.layout.addWidget(self.tabla_ingredientes_titulo_contenedor)
        self.layout.addWidget(self.tabla_ingredientes)
        self.layout.addWidget(self.tabla_instrucciones_titulo_contenedor)
        self.layout.addWidget(self.tabla_instrucciones)

        self.configurar_tabla_ingredientes()
        self.configurar_tabla_instrucciones()

        if receta_editar is None:
            self.titulo.setText("Crear receta")
        else:
            self.titulo.setText("Editar receta")

        self.setLayout(self.layout)

        self.setStyleSheet((Path('views/styles/estilos_recetas.qss').read_text()))

    def configurar_tabla_ingredientes(self) -> None:
        """
        Configura columnas y encabezados de la tabla ingredientes.
        :return:
        """
        encabezados_columnas = ["Nombre", "Cantidad", "Unidad de medida"]
        self.tabla_ingredientes.setColumnCount(3)
        self.tabla_ingredientes.setHorizontalHeaderLabels(encabezados_columnas)
        self.tabla_ingredientes.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        # self.tabla_ingredientes.setFixedWidth(self.width() // 2)

        ancho_col = self.tabla_ingredientes.width() // 3

        for i in range(len(encabezados_columnas)):
            self.tabla_ingredientes.setColumnWidth(i, ancho_col)

        self.agregar_fila_ingrediente()

    def configurar_tabla_instrucciones(self) -> None:
        """
        Configura columnas y encabezados de la tabla instrucciones.
        :return:
        """
        encabezados_columnas = ["Instrucción"]
        self.tabla_instrucciones.setColumnCount(1)
        self.tabla_instrucciones.setHorizontalHeaderLabels(encabezados_columnas)
        self.tabla_instrucciones.horizontalHeader().setStretchLastSection(True)
        self.agregar_fila_instruccion()

    def agregar_fila_ingrediente(self) -> None:
        """
        Agrega una fila en blanco a la tabla ingredientes.
        :return:
        """
        contador_tabla_ingredientes = self.tabla_ingredientes.rowCount()
        self.tabla_ingredientes.setRowCount(contador_tabla_ingredientes + 1)

        campo_nombre = QLineEdit()
        campo_nombre.setObjectName(f"campo_nombre_{contador_tabla_ingredientes}")

        selector_cantidad = QSpinBox()
        selector_cantidad.setObjectName(f"selector_cantidad_{contador_tabla_ingredientes}")

        selector_unidad_medida = QComboBox()
        selector_unidad_medida.setObjectName(f"selector_unidad_medida_{contador_tabla_ingredientes}")

        fila = {"Nombre": campo_nombre, "Cantidad": selector_cantidad, "Unidad de medida": selector_unidad_medida}

        self.tabla_ingredientes.setCellWidget(contador_tabla_ingredientes, 0, fila["Nombre"])
        self.tabla_ingredientes.setCellWidget(contador_tabla_ingredientes, 1, fila["Cantidad"])
        self.tabla_ingredientes.setCellWidget(contador_tabla_ingredientes, 2, fila["Unidad de medida"])

    def agregar_fila_instruccion(self) -> None:
        """
        Agrega una fila en blanco a la tabla instrucciones.
        :return:
        """
        contador_tabla_instrucciones = self.tabla_instrucciones.rowCount()
        self.tabla_instrucciones.setRowCount(contador_tabla_instrucciones + 1)

        campo_instruccion = QLineEdit()
        campo_instruccion.setObjectName(f"campo_instruccion_{contador_tabla_instrucciones}")

        self.tabla_instrucciones.setCellWidget(contador_tabla_instrucciones, 0, campo_instruccion)

    def emitir_evento_abrir_volver(self) -> None:
        """
        Emite la señal para volver a la vista anterior.
        """

        self.volver_vista_anterior_signal.emit()

    def emitir_evento_guardar_receta(self) -> None:
        """
        Emite la señal para guardar los datos en el formulario actual.
        """

        self.guardar_receta_signal.emit()