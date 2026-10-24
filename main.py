import sys
from pathlib import Path

from PySide6 import QtWidgets
from views.VistaVentanaPrincipal import VistaVentanaPrincipal
from controllers.ControladorPrincipal import ControladorPrincipal

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyleSheet((Path('views/styles/estilos_principal.qss').read_text()))

    # Capa de DAO
    # db_connection = "Conexión MySQL"
    # dao = InsumoDAO(db_connection)

    # Capa Servicios
    # service = InventarioServicio(dao)

    # Capa Vista
    # view = InventarioView()

    vista_principal = VistaVentanaPrincipal()

    # Capa Controladora
    controlador_principal = ControladorPrincipal(vista_principal)

    vista_principal.resize(800, 600)
    vista_principal.show()
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


