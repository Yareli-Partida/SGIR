from PySide6 import QtWidgets, QtGui

class VistaRecetas(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QGridLayout(self)

        self.titulo = QtWidgets.QLabel("Recetas")
        self.titulo.setObjectName("titulo_principal")

        self.efecto_sombra = QtWidgets.QGraphicsDropShadowEffect(self)
        self.efecto_sombra.setOffset(1, 1)
        self.efecto_sombra.setBlurRadius(4)
        self.efecto_sombra.setColor(QtGui.QColor(122, 122, 133, 100))

        self.boton_crear_receta = QtWidgets.QPushButton("Crear receta")
        self.boton_crear_receta.setObjectName("boton_crear_receta")
        self.boton_crear_receta.setProperty("cssClass", "boton_principal")
        largo_boton = int(self.boton_crear_receta.sizeHint().width() * 1.25)
        self.boton_crear_receta.setFixedWidth(largo_boton)
        self.boton_crear_receta.setGraphicsEffect(self.efecto_sombra)

        self.lista_recetas = QtWidgets.QListWidget()
        self.lista_recetas.setObjectName("lista_recetas")
        self.lista_recetas.setSpacing(10)

        self.layout.addWidget(self.titulo, 0, 0)
        self.layout.addWidget(self.boton_crear_receta, 0, 1)
        self.layout.addWidget(self.lista_recetas, 1, 0, 1, 2)


    def crear_elemento_lista(self, nombre, boton):
        elemento = QtWidgets.QListWidgetItem()
        widget = QtWidgets.QWidget()
        widget.setObjectName("elemento_lista")

        layout_elemento = QtWidgets.QHBoxLayout()
        etiqueta_nombre = QtWidgets.QLabel(nombre)
        etiqueta_nombre.setObjectName("etiqueta")

        layout_elemento.addWidget(etiqueta_nombre)
        layout_elemento.addWidget(boton)

        widget.setLayout(layout_elemento)
        sombra = QtWidgets.QGraphicsDropShadowEffect(self)
        sombra.setOffset(1, 1)
        sombra.setBlurRadius(4)
        sombra.setColor(QtGui.QColor(122, 122, 133, 100))
        widget.setGraphicsEffect(sombra)
        elemento.setSizeHint(widget.sizeHint())

        self.lista_recetas.addItem(elemento)
        self.lista_recetas.setItemWidget(elemento, widget)

    def crear_boton_detalles(self):
        boton = QtWidgets.QPushButton("Detalles")
        boton.setProperty("cssClass", "boton_secundario")
        largo = int(boton.sizeHint().width())
        boton.setMaximumWidth(largo)

        return boton
