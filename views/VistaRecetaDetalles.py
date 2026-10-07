from PySide6 import QtWidgets, QtGui


class VistaRecetaDetalles(QtWidgets.QWidget):
    def __init__(self, receta):
        super().__init__()

        self.boton_editar_wrapper = QtWidgets.QWidget()
        self.boton_editar_wrapper_layout = QtWidgets.QHBoxLayout()
        self.boton_editar_wrapper_layout.setAlignment(QtGui.Qt.AlignmentFlag.AlignRight)
        self.boton_editar = QtWidgets.QPushButton("Editar")
        self.boton_editar.setObjectName("boton_editar")
        self.boton_editar.setProperty("cssClass", "boton_principal")
        self.estilizar_boton_principal(self.boton_editar)
        self.boton_editar_wrapper_layout.addWidget(self.boton_editar)
        self.boton_editar_wrapper.setLayout(self.boton_editar_wrapper_layout)

        self.boton_volver_wrapper = QtWidgets.QWidget()
        self.boton_volver_wrapper_layout = QtWidgets.QHBoxLayout()
        self.boton_volver_wrapper_layout.setAlignment(QtGui.Qt.AlignmentFlag.AlignLeft)
        self.boton_volver = QtWidgets.QPushButton("Volver")
        self.boton_volver.setObjectName("boton_volver")
        self.boton_volver.setProperty("cssClass", "boton_principal")
        self.estilizar_boton_principal(self.boton_volver)
        self.boton_volver_wrapper_layout.addWidget(self.boton_volver)
        self.boton_volver_wrapper.setLayout(self.boton_volver_wrapper_layout)

        self.layout = QtWidgets.QGridLayout(self)
        self.titulo = QtWidgets.QLabel(receta.nombre)
        self.titulo.setObjectName("titulo_principal")

        self.etiqueta_num_porciones = QtWidgets.QLabel(f"Porciones: {receta.num_porciones}")
        self.etiqueta_num_porciones.setObjectName("etiqueta_num_porciones")

        self.lista_ingredientes = QtWidgets.QListWidget()
        self.lista_ingredientes.setObjectName("lista_ingredientes")

        self.lista_instrucciones = QtWidgets.QListWidget()
        self.lista_instrucciones.setObjectName("lista_instrucciones")

        self.layout.addWidget(self.boton_volver_wrapper, 0, 0, )
        self.layout.addWidget(self.boton_editar_wrapper, 0, 1)
        self.layout.addWidget(self.titulo, 1, 0)
        self.layout.addWidget(self.etiqueta_num_porciones, 2, 0)
        self.layout.addWidget(self.lista_ingredientes, 3, 0, 3, 2)
        self.layout.addWidget(self.lista_instrucciones, 4, 0, 4, 2)

        self.setLayout(self.layout)

    def estilizar_boton_principal(self, boton):
        efecto_sombra = QtWidgets.QGraphicsDropShadowEffect(self)
        efecto_sombra.setOffset(1, 1)
        efecto_sombra.setBlurRadius(4)
        efecto_sombra.setColor(QtGui.QColor(122, 122, 133, 100))
        boton.setFixedWidth(int(boton.sizeHint().width()) * 2)
        boton.setGraphicsEffect(efecto_sombra)