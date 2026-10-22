from PySide6.QtWidgets import QTableWidget, QGraphicsDropShadowEffect
from PySide6.QtGui import QColor

class TablaResponsivaRegular(QTableWidget):
    def __init__(self):
        super().__init__()

        efecto_sombra = QGraphicsDropShadowEffect(self)
        efecto_sombra.setOffset(1, 1)
        efecto_sombra.setBlurRadius(4)
        efecto_sombra.setColor(QColor(122, 122, 133, 100))

        self.setGraphicsEffect(efecto_sombra)

    def resizeEvent(self, event):
        contador_cols = self.columnCount()

        ancho = (self.width() // contador_cols) - 1

        for idx in range(contador_cols):
            self.setColumnWidth(idx, ancho)
