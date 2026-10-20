import sys
from pathlib import Path

from PySide6 import QtWidgets
from controllers.ControladorPrincipal import ControladorPrincipal

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyleSheet((Path('views/styles/estilos_principal.qss').read_text()))

    widget = ControladorPrincipal()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())


# from models.Insumo import Insumo
#
# insumos = []
#
# persona = Insumo(1,'nombre',20,'kg',50,50)
# insumos.append(persona)
#
# for persona in insumos:
#     print(persona._num)


