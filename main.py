'''from models.Insumo import Insumo

insumos = []

insumo1 = Insumo(1,'Aceite','30-12-2026',5,'litros',1,30.0,'2-10-2026')
insumos.append(insumo1)

for insumo in insumos:
    print(insumo.unidad_medida)
    print(insumo.fecha_caducidad)

'''

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


print('iniciando app...')

#dao's imports

# main.py
import sys
from PySide6.QtWidgets import QApplication

from daos.insumo_dao import InsumoDAO
from services.inventario_servicio import InventarioServicio
from views.vista_inventario import InventarioView
from controllers.inventario_controller import InventarioController

def main():
    app = QApplication(sys.argv)
    
    #Capa de DAO
    db_connection = "Conexión MySQL"
    dao = InsumoDAO(db_connection)
    
    #Capa Servicios
    service = InventarioServicio(dao)
    
    #Capa Vista
    view = InventarioView()
    
    #Capa Controladora
    controller = InventarioController(view, service)
    
    # Mostrar la aplicación
    view.resize(400, 200)
    view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
