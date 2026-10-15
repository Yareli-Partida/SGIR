from PySide6 import QtWidgets, QtGui

from models.Platillo import Platillo


class VistaMenuDetalles(QtWidgets.QWidget):
    def __init__(self, menu):
        super().__init__()
        self.layout = QtWidgets.QVBoxLayout()

        self.boton_volver = QtWidgets.QPushButton("Volver")
        self.boton_volver.setObjectName("boton_volver")
        self.boton_volver.setFixedWidth(int(self.boton_volver.sizeHint().width() * 1.25))
        self.boton_volver.setProperty("cssClass", "boton_principal")
        self.estilizar_boton_principal(self.boton_volver)

        self.boton_editar_menu = QtWidgets.QPushButton("Editar")
        self.boton_editar_menu.setObjectName("boton_editar_menu")
        self.boton_editar_menu.setFixedWidth(int(self.boton_editar_menu.sizeHint().width() * 1.25))
        self.boton_editar_menu.setProperty("cssClass", "boton_principal")
        self.estilizar_boton_principal(self.boton_editar_menu)

        self.contenedor_botones = QtWidgets.QWidget()
        self.contenedor_botones_layout = QtWidgets.QHBoxLayout()
        self.contenedor_botones_layout.addWidget(self.boton_volver)
        self.contenedor_botones_layout.addSpacerItem(QtWidgets.QSpacerItem(40, 20,
                                                                  QtWidgets.QSizePolicy.Policy.Expanding,
                                                                  QtWidgets.QSizePolicy.Policy.Minimum))
        self.contenedor_botones_layout.addWidget(self.boton_editar_menu)
        self.contenedor_botones.setLayout(self.contenedor_botones_layout)

        self.titulo_principal = QtWidgets.QLabel(menu.nombre)
        self.titulo_principal.setObjectName("titulo_principal_detalles")
        self.titulo_principal.setProperty("cssClass", "titulo_principal")

        self.tabla_detalles_platillos = self.crear_tabla_platillos()
        self.tabla_detalles_platillos.setObjectName("tabla_detalles_platillos")

        self.layout.addWidget(self.contenedor_botones)
        self.layout.addWidget(self.titulo_principal)
        self.layout.addWidget(self.tabla_detalles_platillos)

        lista_test = [
        Platillo(1, "Pasta en salsa de tomate", 150),
        Platillo(2, "Puré de papas", 70),
        Platillo(3, "Filete de res", 250),
        Platillo(4, "Caldo de pollo", 180),
        Platillo(5, "Café", 50),
        ]
        self.agregar_platillos_tabla(lista_test)

        self.setLayout(self.layout)

    def agregar_platillos_tabla(self, lista_platillos):
        self.tabla_detalles_platillos.setRowCount(len(lista_platillos))
        contador_fila = 0

        for platillo in lista_platillos:
            platillo_nombre = QtWidgets.QTableWidgetItem(platillo.nombre)
            platillo_precio = QtWidgets.QTableWidgetItem(f"${platillo.precio}")
            platillo_precio.setTextAlignment(QtGui.Qt.AlignmentFlag.AlignVCenter)
            # Categoria hard coded para testeo
            platillo_categoria = QtWidgets.QTableWidgetItem("Platillo Fuerte")

            self.tabla_detalles_platillos.setItem(contador_fila, 0, platillo_categoria)
            self.tabla_detalles_platillos.setItem(contador_fila, 1, platillo_nombre)
            self.tabla_detalles_platillos.setItem(contador_fila, 2, platillo_precio)

            contador_fila += 1

        self.tabla_detalles_platillos.resizeColumnToContents(2)

    def crear_tabla_platillos(self):
        tabla_platillos = QtWidgets.QTableWidget()
        encabezados = ["Categoría", "Platillo", "Precio"]
        tabla_platillos.verticalHeader().hide()
        tabla_platillos.setColumnCount(3)
        tabla_platillos.setHorizontalHeaderLabels(encabezados)
        tabla_platillos.setShowGrid(False)

        efecto_sombra = QtWidgets.QGraphicsDropShadowEffect(self)
        efecto_sombra.setOffset(1, 1)
        efecto_sombra.setBlurRadius(4)
        efecto_sombra.setColor(QtGui.QColor(122, 122, 133, 100))

        tabla_platillos.setGraphicsEffect(efecto_sombra)

        return tabla_platillos

    def resizeEvent(self, event):
        precio_col_ancho = self.tabla_detalles_platillos.columnWidth(2)
        ancho_col = ((self.tabla_detalles_platillos.width() - precio_col_ancho) // 3) - 1

        for i in range(2):
            self.tabla_detalles_platillos.setColumnWidth(i, ancho_col * (i + 1))

    def estilizar_boton_principal(self, boton):
        efecto_sombra = QtWidgets.QGraphicsDropShadowEffect(self)
        efecto_sombra.setOffset(1, 1)
        efecto_sombra.setBlurRadius(4)
        efecto_sombra.setColor(QtGui.QColor(122, 122, 133, 100))

        boton.setFixedWidth(int(boton.sizeHint().width() * 2))
        boton.setGraphicsEffect(efecto_sombra)