from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PySide6.QtCore import Signal

class InventarioView(QWidget):
    # POE: Creamos una señal personalizada que envía un 'string' (el nombre del insumo)
    pedir_verificacion_signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Control de Almacén - Restaurante")
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.input_insumo = QLineEdit(placeholderText="Ingresa el insumo...")
        self.layout.addWidget(self.input_insumo)

        self.btn_verificar = QPushButton("Verificar Stock")
        # Conectamos el clic físico del botón a un método interno de la vista
        self.btn_verificar.clicked.connect(self.emitir_evento_verificar)
        self.layout.addWidget(self.btn_verificar)

        self.lbl_resultado = QLabel("...")
        self.layout.addWidget(self.lbl_resultado)
        self.setLayout(self.layout)

    def emitir_evento_verificar(self):
        insumo_texto = self.input_insumo.text()
        self.pedir_verificacion_signal.emit(insumo_texto)

    def mostrar_resultado(self, mensaje):
        # Metodo publico para que el controller modifique la pantalla
        self.lbl_resultado.setText(mensaje)