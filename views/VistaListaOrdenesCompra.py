from PySide6 import QtWidgets, QtGui

class VistaListaOrdenesCompra(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setSpacing(45)

        self.titulo = QtWidgets.QLabel("Ordenes de Compra")
        self.titulo.setProperty("cssClass", "titulo_principal")
        self.titulo.setObjectName("titulo_principal_lista_ordenes")

        self.boton_crear_orden_compra = QtWidgets.QPushButton("Crear orden")
        self.boton_crear_orden_compra.setProperty("cssClass", "boton_principal")
        self.boton_crear_orden_compra.setObjectName("boton_crear_orden_compra")
        self.estilizar_boton_principal(self.boton_crear_orden_compra)

        self.contenedor_titulo = QtWidgets.QWidget()
        self.contenedor_titulo.setObjectName("contenedor_titulo")
        self.contenedor_titulo_layout = QtWidgets.QHBoxLayout()
        self.contenedor_titulo_layout.addWidget(self.titulo)
        self.contenedor_titulo_layout.addWidget(self.boton_crear_orden_compra)
        self.contenedor_titulo.setLayout(self.contenedor_titulo_layout)

        self.tabla_ordenes_compra = self.crear_tabla_ordenes_compra()
        self.tabla_ordenes_compra.setObjectName("tabla_ordenes_compra")

        self.layout.addWidget(self.contenedor_titulo)
        self.layout.addWidget(self.tabla_ordenes_compra)

        self.setLayout(self.layout)

    def crear_tabla_ordenes_compra(self):
        tabla = QtWidgets.QTableWidget()
        encabezados = ["Número de orden", "Fecha de creación", "Estado", ""]

        tabla.setObjectName("tabla_ordenes_compra")
        tabla.setColumnCount(4)
        tabla.verticalHeader().hide()
        tabla.setHorizontalHeaderLabels(encabezados)
        tabla.setShowGrid(False)

        efecto_sombra = QtWidgets.QGraphicsDropShadowEffect(self)
        efecto_sombra.setOffset(1, 1)
        efecto_sombra.setBlurRadius(4)
        efecto_sombra.setColor(QtGui.QColor(122, 122, 133, 100))

        tabla.setGraphicsEffect(efecto_sombra)

        return tabla

    def crear_fila_tabla_ordenes_compra(self, orden_compra, boton):
        self.tabla_ordenes_compra.setRowCount(self.tabla_ordenes_compra.rowCount() + 1)
        current_row = self.tabla_ordenes_compra.rowCount() - 1

        orden_compra_num = QtWidgets.QTableWidgetItem(str(orden_compra.num))
        orden_compra_num.setTextAlignment(QtGui.Qt.AlignmentFlag.AlignCenter)

        orden_compra_fecha_creacion = QtWidgets.QTableWidgetItem(orden_compra.fecha_creacion)
        orden_compra_fecha_creacion.setTextAlignment(QtGui.Qt.AlignmentFlag.AlignCenter)
        # hardcoded para testeo
        orden_estado = QtWidgets.QTableWidgetItem("En Progreso")
        orden_estado.setTextAlignment(QtGui.Qt.AlignmentFlag.AlignCenter)

        if orden_estado.text() == "En Progreso":
            orden_estado.setBackground(QtGui.QColor.fromRgb(255, 178, 0))
        elif orden_estado.text() == "Terminada":
            orden_estado.setBackground(QtGui.QColor.fromRgb(57, 255, 0))
        elif orden_estado.text() == "Cancelada":
            orden_estado.setBackground(QtGui.QColor.fromRgb(255, 44, 0))

        self.tabla_ordenes_compra.setItem(current_row, 0, orden_compra_num)
        self.tabla_ordenes_compra.setItem(current_row, 1, orden_compra_fecha_creacion)
        self.tabla_ordenes_compra.setItem(current_row, 2, orden_estado)
        self.tabla_ordenes_compra.setCellWidget(current_row, 3, boton)

    def crear_boton_ver_orden(self):
        boton = QtWidgets.QPushButton("Ver orden")
        boton.setProperty("cssClass", "boton_secundario")
        largo = int(boton.sizeHint().width() * 1.25)
        boton.setMinimumWidth(largo)

        return boton

    def resizeEvent(self, event):
        boton_col_ancho = self.tabla_ordenes_compra.columnWidth(3)
        ancho_col = ((self.tabla_ordenes_compra.width() - boton_col_ancho) // 3) - 1

        for i in range(3):
            self.tabla_ordenes_compra.setColumnWidth(i, ancho_col)

    def estilizar_boton_principal(self, boton):
        efecto_sombra = QtWidgets.QGraphicsDropShadowEffect(self)
        efecto_sombra.setOffset(1, 1)
        efecto_sombra.setBlurRadius(4)
        efecto_sombra.setColor(QtGui.QColor(122, 122, 133, 100))

        boton.setFixedWidth(int(boton.sizeHint().width() * 1.25))
        boton.setGraphicsEffect(efecto_sombra)

