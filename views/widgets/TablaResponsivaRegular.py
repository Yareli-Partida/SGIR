from PySide6.QtWidgets import QTableWidget, QGraphicsDropShadowEffect, QAbstractItemView
from PySide6.QtGui import QColor

class TablaResponsivaRegular(QTableWidget):
    """
    Tabla configurada para que sus columnas sean y crezcan al mismo tamaño.
    """

    def __init__(self):
        super().__init__()

        self.verticalHeader().hide()

        efecto_sombra = QGraphicsDropShadowEffect(self)
        efecto_sombra.setOffset(1, 1)
        efecto_sombra.setBlurRadius(4)
        efecto_sombra.setColor(QColor(122, 122, 133, 100))

        self.setGraphicsEffect(efecto_sombra)

    def resizeEvent(self, event):
        contador_cols = self.columnCount()

        ancho = ((self.width() - 18) // contador_cols) - 1

        for idx in range(contador_cols):
            self.setColumnWidth(idx, ancho)
