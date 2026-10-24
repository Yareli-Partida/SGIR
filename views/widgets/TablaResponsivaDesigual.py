from PySide6 import QtWidgets, QtGui

class TablaResponsivaDesigual(QtWidgets.QTableWidget):
    """
    Una tabla configurada para que su última columna sea a la medida de sus contenidos mientras que el resto tiene
    un tamaño equitativo asignado.
    Hecha para cuando se necesita una tabla donde la última col es más pequeña que el resto.

    """

    def __init__(self):
        super().__init__()

        self.verticalHeader().hide()

        efecto_sombra = QtWidgets.QGraphicsDropShadowEffect(self)
        efecto_sombra.setOffset(1, 1)
        efecto_sombra.setBlurRadius(4)
        efecto_sombra.setColor(QtGui.QColor(122, 122, 133, 100))

        self.setGraphicsEffect(efecto_sombra)

    def resizeEvent(self, event):
        idx_ultima_col = self.columnCount() - 1
        self.resizeColumnToContents(idx_ultima_col)
        ultima_col_ancho = self.columnWidth(idx_ultima_col)
        ancho_col = ((self.width() - ultima_col_ancho) // idx_ultima_col) - 1

        for i in range(idx_ultima_col):
            self.setColumnWidth(i, ancho_col)
