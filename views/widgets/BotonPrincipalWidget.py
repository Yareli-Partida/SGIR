from PySide6 import QtWidgets, QtGui

class BotonPrincipalWidget(QtWidgets.QPushButton):
    """
    Un botón estilizado grande.

    :param nombre: (str): El texto que mostrará el botón.
    """

    def __init__(self, nombre:str):
        super().__init__()

        self.setProperty("cssClass", "boton_principal")

        self.setText(nombre)

        nombre_formateado = nombre.replace(" ", "_").lower()
        self.setObjectName(f"boton_{nombre_formateado}")

        efecto_sombra = QtWidgets.QGraphicsDropShadowEffect(self)
        efecto_sombra.setOffset(1, 1)
        efecto_sombra.setBlurRadius(4)
        efecto_sombra.setColor(QtGui.QColor(122, 122, 133, 100))

        self.setFixedWidth(int(self.sizeHint().width() * 1.25))
        self.setGraphicsEffect(efecto_sombra)

