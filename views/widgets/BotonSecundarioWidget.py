from PySide6 import QtWidgets

class BotonSecundarioWidget(QtWidgets.QPushButton):
    """
    Un botón estilizado pequeño.

    :param nombre: (str): El texto que mostrará el botón.
    :param ancho_fijo: (bool): Determina si el botón se expandirá en su Parent Widget o no.

    """

    def __init__(self, nombre:str, ancho_fijo=True):
        super().__init__()

        self.setProperty("cssClass", "boton_secundario")

        self.setText(nombre)

        nombre_formateado = nombre.replace(" ", "_").lower()
        self.setObjectName(f"boton_{nombre_formateado}")

        if ancho_fijo:
            self.setFixedWidth(int(self.sizeHint().width() * 1.25))
        else:
            self.setMinimumWidth(int(self.sizeHint().width() * 1.25))
