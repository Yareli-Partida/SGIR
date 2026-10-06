from PySide6 import QtWidgets, QtGui, QtCore

from PySide6.QtCore import Qt

from models.Receta import Receta


class VistaCrearEditarReceta(QtWidgets.QWidget):
    def __init__(self, receta_editar=None):
        super().__init__()
        self.layout = QtWidgets.QVBoxLayout()

        self.titulo = QtWidgets.QLabel()
        self.titulo.setObjectName("titulo_principal")

        self.botones_wrapper = QtWidgets.QWidget()
        self.botones_wrapper_layout = QtWidgets.QHBoxLayout()
        self.boton_guardar_receta = QtWidgets.QPushButton("Guardar")
        self.boton_guardar_receta.setObjectName("boton_guardar_receta")
        self.estilizar_boton_principal(self.boton_guardar_receta)
        self.boton_volver = QtWidgets.QPushButton("Volver")
        self.boton_volver.setObjectName("boton_volver")
        self.estilizar_boton_principal(self.boton_volver)
        self.botones_wrapper_layout.addWidget(self.boton_volver)
        self.botones_wrapper_layout.addSpacerItem(QtWidgets.QSpacerItem(40, 20,
                                                                        QtWidgets.QSizePolicy.Policy.Expanding,
                                                                        QtWidgets.QSizePolicy.Policy.Minimum))
        self.botones_wrapper_layout.addWidget(self.boton_guardar_receta)
        self.botones_wrapper.setLayout(self.botones_wrapper_layout)

        self.nombre_receta_wrapper = QtWidgets.QWidget()
        self.nombre_receta_wrapper_layout = QtWidgets.QHBoxLayout()
        self.nombre_receta_wrapper_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.etiqueta_nombre_receta = QtWidgets.QLabel("Nombre:")
        self.etiqueta_nombre_receta.setObjectName("etiqueta_nombre_receta")
        self.etiqueta_nombre_receta.setFixedWidth(self.etiqueta_nombre_receta.sizeHint().width())
        self.campo_nombre_receta = QtWidgets.QLineEdit()
        self.campo_nombre_receta.setObjectName("campo_nombre_receta")
        self.campo_nombre_receta.setFixedWidth(self.calcular_ancho_por_caracteres(30))
        self.nombre_receta_wrapper_layout.addWidget(self.etiqueta_nombre_receta)
        self.nombre_receta_wrapper_layout.addWidget(self.campo_nombre_receta)
        self.nombre_receta_wrapper.setLayout(self.nombre_receta_wrapper_layout)

        self.num_porciones_wrapper = QtWidgets.QWidget()
        self.num_porciones_wrapper.setObjectName("num_porciones_wrapper")
        self.num_porciones_wrapper_layout = QtWidgets.QHBoxLayout()
        self.num_porciones_wrapper_layout.setObjectName("num_porciones_wrapper_layout")
        self.num_porciones_wrapper_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.etiqueta_num_porciones = QtWidgets.QLabel("Número de porciones: ")
        self.etiqueta_num_porciones.setObjectName("etiqueta_num_porciones")
        self.selector_num_porciones = QtWidgets.QSpinBox()
        self.selector_num_porciones.setObjectName("selector_num_porciones")
        self.selector_num_porciones.setFixedWidth(self.calcular_ancho_por_caracteres(7))
        self.num_porciones_wrapper_layout.addWidget(self.etiqueta_num_porciones)
        self.num_porciones_wrapper_layout.addWidget(self.selector_num_porciones)
        self.num_porciones_wrapper.setLayout(self.num_porciones_wrapper_layout)

        self.tabla_ingredientes_titulo_wrapper = QtWidgets.QWidget()
        self.tabla_ingredientes_titulo_wrapper.setObjectName("tabla_ingredientes_titulo_wrapper")
        self.tabla_ingredientes_titulo_layout = QtWidgets.QHBoxLayout()
        self.tabla_ingredientes_titulo_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.tabla_ingredientes_titulo_layout.setObjectName("tabla_ingredientes_titulo_layout")
        self.etiqueta_tabla_ingredientes = QtWidgets.QLabel("Ingredientes")
        self.etiqueta_tabla_ingredientes.setFixedWidth(self.etiqueta_tabla_ingredientes.sizeHint().width())
        self.etiqueta_tabla_ingredientes.setObjectName("etiqueta_tabla_ingredientes")
        self.boton_agregar_ingrediente = QtWidgets.QPushButton("Agregar")
        self.boton_agregar_ingrediente.setObjectName("boton_agregar_ingrediente")
        self.boton_agregar_ingrediente.clicked.connect(self.agregar_fila_ingrediente)
        self.boton_agregar_ingrediente.setFixedWidth(self.boton_agregar_ingrediente.sizeHint().width())
        self.tabla_ingredientes_titulo_layout.addWidget(self.etiqueta_tabla_ingredientes)
        self.tabla_ingredientes_titulo_layout.addWidget(self.boton_agregar_ingrediente)
        self.tabla_ingredientes_titulo_wrapper.setLayout(self.tabla_ingredientes_titulo_layout)

        self.tabla_ingredientes = QtWidgets.QTableWidget()
        self.tabla_ingredientes.setObjectName("tabla_ingredientes")
        self.lista_tabla_ingredientes = []
        self.contador_tabla_ingredientes_filas = 0

        self.tabla_instrucciones_titulo_wrapper = QtWidgets.QWidget()
        self.tabla_instrucciones_titulo_wrapper.setObjectName("tabla_instrucciones_titulo_wrapper")
        self.tabla_instrucciones_titulo_layout = QtWidgets.QHBoxLayout()
        self.tabla_instrucciones_titulo_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.tabla_instrucciones_titulo_layout.setObjectName("tabla_instrucciones_titulo_layout")
        self.etiqueta_tabla_instrucciones = QtWidgets.QLabel("Instrucciones")
        self.etiqueta_tabla_instrucciones.setObjectName("instrucciones")
        self.etiqueta_tabla_instrucciones.setFixedWidth(self.etiqueta_tabla_instrucciones.sizeHint().width())
        self.boton_agregar_instruccion = QtWidgets.QPushButton("Agregar")
        self.boton_agregar_instruccion.setFixedWidth(self.boton_agregar_instruccion.sizeHint().width())
        self.boton_agregar_instruccion.clicked.connect(self.agregar_fila_instruccion)
        self.boton_agregar_instruccion.setObjectName("boton_agregar_instruccion")
        self.tabla_instrucciones_titulo_layout.addWidget(self.etiqueta_tabla_instrucciones)
        self.tabla_instrucciones_titulo_layout.addWidget(self.boton_agregar_instruccion)
        self.tabla_instrucciones_titulo_wrapper.setLayout(self.tabla_instrucciones_titulo_layout)

        self.tabla_instrucciones = QtWidgets.QTableWidget()
        self.tabla_instrucciones.setObjectName("tabla_instrucciones")
        self.lista_tabla_instrucciones = []
        self.contador_tabla_instrucciones_filas = 0

        self.layout.addWidget(self.botones_wrapper)
        self.layout.addWidget(self.titulo)
        self.layout.addWidget(self.nombre_receta_wrapper)
        self.layout.addWidget(self.num_porciones_wrapper)
        self.layout.addWidget(self.tabla_ingredientes_titulo_wrapper)
        self.layout.addWidget(self.tabla_ingredientes)
        self.layout.addWidget(self.tabla_instrucciones_titulo_wrapper)
        self.layout.addWidget(self.tabla_instrucciones)

        self.configurar_tabla_ingredientes()
        self.configurar_tabla_instrucciones()

        if receta_editar is None:
            self.titulo.setText("Crear receta")
        else:
            self.titulo.setText("Editar receta")
            self.rellena_forma(receta_editar)

        self.setLayout(self.layout)

    def estilizar_boton_principal(self, boton):
        efecto_sombra = QtWidgets.QGraphicsDropShadowEffect(self)
        efecto_sombra.setOffset(1, 1)
        efecto_sombra.setBlurRadius(4)
        efecto_sombra.setColor(QtGui.QColor(122, 122, 133, 100))

        boton.setFixedWidth(int(boton.sizeHint().width() * 1.25))
        boton.setGraphicsEffect(efecto_sombra)

    def configurar_tabla_ingredientes(self):
        encabezados_columnas = ["Nombre", "Cantidad", "Unidad de medida"]
        self.tabla_ingredientes.setColumnCount(3)
        self.tabla_ingredientes.setHorizontalHeaderLabels(encabezados_columnas)
        self.tabla_ingredientes.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tabla_ingredientes.setFixedWidth(self.width() // 2)

        ancho_col = self.tabla_ingredientes.width() // 3

        for i in range(len(encabezados_columnas)):
            self.tabla_ingredientes.setColumnWidth(i, ancho_col)

        self.agregar_fila_ingrediente()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.tabla_ingredientes.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tabla_ingredientes.setFixedWidth(self.width() // 2)
        self.tabla_instrucciones.horizontalHeader().setStretchLastSection(True)

    def configurar_tabla_instrucciones(self):
        encabezados_columnas = ["Instrucción"]
        self.tabla_instrucciones.setColumnCount(1)
        self.tabla_instrucciones.setHorizontalHeaderLabels(encabezados_columnas)
        self.tabla_instrucciones.horizontalHeader().setStretchLastSection(True)
        self.agregar_fila_instruccion()

    def agregar_fila_ingrediente(self):
        self.tabla_ingredientes.setRowCount(self.contador_tabla_ingredientes_filas + 1)

        campo_nombre = QtWidgets.QLineEdit()
        campo_nombre.setObjectName(f"campo_nombre_{self.contador_tabla_ingredientes_filas}")

        selector_cantidad = QtWidgets.QSpinBox()
        selector_cantidad.setObjectName(f"selector_cantidad_{self.contador_tabla_ingredientes_filas}")

        selector_unidad_medida = QtWidgets.QComboBox()
        selector_unidad_medida.setObjectName(f"selector_unidad_medida_{self.contador_tabla_ingredientes_filas}")

        fila = {"Nombre": campo_nombre, "Cantidad": selector_cantidad, "Unidad de medida": selector_unidad_medida}

        self.tabla_ingredientes.setCellWidget(self.contador_tabla_ingredientes_filas, 0, fila["Nombre"])
        self.tabla_ingredientes.setCellWidget(self.contador_tabla_ingredientes_filas, 1, fila["Cantidad"])
        self.tabla_ingredientes.setCellWidget(self.contador_tabla_ingredientes_filas, 2, fila["Unidad de medida"])

        self.contador_tabla_ingredientes_filas += 1
        self.lista_tabla_ingredientes.append(fila)

    def agregar_fila_instruccion(self):
        self.tabla_instrucciones.setRowCount(self.contador_tabla_instrucciones_filas + 1)

        campo_instruccion = QtWidgets.QLineEdit()
        campo_instruccion.setObjectName(f"campo_instruccion_{self.contador_tabla_ingredientes_filas}")

        self.tabla_instrucciones.setCellWidget(self.contador_tabla_ingredientes_filas, 0, campo_instruccion)

        self.contador_tabla_instrucciones_filas += 1
        self.lista_tabla_instrucciones.append(campo_instruccion)

    def rellena_forma(self, receta):
        self.selector_num_porciones.setValue(receta.num_porciones)
        self.campo_nombre_receta.setText(receta.nombre)

    def calcular_ancho_por_caracteres(self, num_caracteres: int):
        palabra = "a" * (num_caracteres + 1)
        x = QtWidgets.QLabel(palabra)
        return x.sizeHint().width()