from PySide6 import QtWidgets, QtGui, QtCore

from models.Platillo import Platillo

class VistaCrearEditarMenu(QtWidgets.QWidget):
    def __init__(self, menu=None):
        super().__init__()
        self.layout = QtWidgets.QVBoxLayout()

        self.boton_volver = QtWidgets.QPushButton("Volver")
        self.boton_volver.setObjectName("boton_volver")
        self.boton_volver.setProperty("cssClass", "boton_principal")
        self.estilizar_boton_principal(self.boton_volver)

        self.boton_guardar_menu = QtWidgets.QPushButton("Guardar")
        self.boton_guardar_menu.setObjectName("boton_guardar_menu")
        self.boton_guardar_menu.setProperty("cssClass", "boton_principal")
        self.estilizar_boton_principal(self.boton_guardar_menu)

        self.contenedor_botones = QtWidgets.QWidget()
        self.contenedor_botones_layout = QtWidgets.QHBoxLayout()
        self.contenedor_botones_layout.addWidget(self.boton_volver)
        self.contenedor_botones_layout.addSpacerItem(QtWidgets.QSpacerItem(40, 20,
                                                                           QtWidgets.QSizePolicy.Policy.Expanding,
                                                                           QtWidgets.QSizePolicy.Policy.Minimum))
        self.contenedor_botones_layout.addWidget(self.boton_guardar_menu)
        self.contenedor_botones.setLayout(self.contenedor_botones_layout)

        self.titulo = QtWidgets.QLabel()
        self.titulo.setObjectName("titulo_crear_editar")
        self.titulo.setProperty("cssClass", "titulo_principal")

        self.boton_agregar_platillo = QtWidgets.QPushButton("Agregar Platillo")
        self.boton_agregar_platillo.setFixedWidth(int(self.boton_agregar_platillo.sizeHint().width() * 1.25))
        self.boton_agregar_platillo.setProperty("cssClass", "boton_secundario")
        self.boton_agregar_platillo.setObjectName("boton_agregar_platillo")
        self.boton_agregar_platillo.clicked.connect(self.agregar_fila_tabla_platillo)

        self.tabla_platillos = self.crear_tabla_platillos()
        self.agregar_fila_tabla_platillo()

        if menu:
            self.titulo.setText("Editar Menú")
            lista_test = [
                Platillo(1, "Pasta en salsa de tomate", 150),
                Platillo(2, "Puré de papas", 70),
                Platillo(3, "Filete de res", 250),
                Platillo(4, "Caldo de pollo", 180),
                Platillo(5, "Café", 50),
            ]
            self.llenar_forma(menu, lista_test)
        else:
            self.titulo.setText("Crear Menú")

        self.layout.addWidget(self.contenedor_botones)
        self.layout.addWidget(self.titulo)
        self.layout.addWidget(self.boton_agregar_platillo)
        self.layout.addWidget(self.tabla_platillos)

        self.setLayout(self.layout)

    def llenar_forma(self, menu, lista_platillos):
        self.tabla_platillos.setRowCount(len(lista_platillos))
        contador_fila = 0

        for platillo in lista_platillos:
            platillo_nombre = QtWidgets.QComboBox()
            # Hardcoded para testeo manual
            platillo_nombre.insertItems(len(lista_platillos), [platillo.nombre for platillo in lista_platillos])
            platillo_nombre.setCurrentIndex(contador_fila)

            platillo_precio = QtWidgets.QDoubleSpinBox()
            platillo_precio.setMaximum(999999)
            platillo_precio.setValue(int(platillo.precio))
            platillo_precio.setPrefix("$")
            # Categoria hard coded para testeo
            platillo_categoria = QtWidgets.QTableWidgetItem("Platillo Fuerte")

            self.tabla_platillos.setItem(contador_fila, 0, platillo_categoria)
            self.tabla_platillos.setCellWidget(contador_fila, 1, platillo_nombre)
            self.tabla_platillos.setCellWidget(contador_fila, 2, platillo_precio)

            contador_fila += 1

        self.tabla_platillos.resizeColumnToContents(2)

    def crear_tabla_platillos(self):
        tabla_platillos = QtWidgets.QTableWidget()
        encabezados = ["Categoría", "Platillo", "Precio"]
        tabla_platillos.verticalHeader().hide()
        tabla_platillos.setColumnCount(3)
        tabla_platillos.setRowCount(0)
        tabla_platillos.setHorizontalHeaderLabels(encabezados)

        efecto_sombra = QtWidgets.QGraphicsDropShadowEffect(self)
        efecto_sombra.setOffset(1, 1)
        efecto_sombra.setBlurRadius(4)
        efecto_sombra.setColor(QtGui.QColor(122, 122, 133, 100))

        tabla_platillos.setGraphicsEffect(efecto_sombra)

        return tabla_platillos

    def agregar_fila_tabla_platillo(self):
        self.tabla_platillos.setRowCount(self.tabla_platillos.rowCount() + 1)
        num_fila = self.tabla_platillos.rowCount() - 1
        platillo_nombre = QtWidgets.QComboBox()

        # Harcoded de nuevo para testear
        lista_test = [
            Platillo(1, "Pasta en salsa de tomate", 150),
            Platillo(2, "Puré de papas", 70),
            Platillo(3, "Filete de res", 250),
            Platillo(4, "Caldo de pollo", 180),
            Platillo(5, "Café", 50),
        ]

        platillo_nombre.insertItems(len(lista_test), [platillo.nombre for platillo in lista_test])
        platillo_nombre.setCurrentIndex(-1)

        platillo_precio = QtWidgets.QDoubleSpinBox()
        platillo_precio.setMaximum(999999)
        platillo_precio.setPrefix("$")
        # Categoria hard coded para testeo
        platillo_categoria = QtWidgets.QTableWidgetItem("")

        platillo_nombre.currentIndexChanged.connect(lambda: self.cambiar_texto_etiqueta_categoria(platillo_categoria))

        self.tabla_platillos.setItem(num_fila, 0, platillo_categoria)
        self.tabla_platillos.setCellWidget(num_fila, 1, platillo_nombre)
        self.tabla_platillos.setCellWidget(num_fila, 2, platillo_precio)

        num_fila += 1

    def estilizar_boton_principal(self, boton):
        efecto_sombra = QtWidgets.QGraphicsDropShadowEffect(self)
        efecto_sombra.setOffset(1, 1)
        efecto_sombra.setBlurRadius(4)
        efecto_sombra.setColor(QtGui.QColor(122, 122, 133, 100))

        boton.setFixedWidth(int(boton.sizeHint().width() * 1.25))
        boton.setGraphicsEffect(efecto_sombra)

    def cambiar_texto_etiqueta_categoria(self, etiqueta):
        etiqueta.setText("Platillo Fuerte")

    def resizeEvent(self, event):
        precio_col_ancho = self.tabla_platillos.columnWidth(2)
        ancho_col = ((self.tabla_platillos.width() - precio_col_ancho) // 3) - 1

        for i in range(2):
            self.tabla_platillos.setColumnWidth(i, ancho_col * (i + 1))