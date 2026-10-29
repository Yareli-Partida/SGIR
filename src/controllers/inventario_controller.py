from PySide6.QtCore import QObject, Slot

class InventarioController(QObject):
    def __init__(self, view, inventario_servicio):
        super().__init__()
        self.view = view
        self.service = inventario_servicio

        # El Controller se "suscribe" a los eventos de la Vista
        self.view.pedir_verificacion_signal.connect(self.procesar_verificacion)

    @Slot(str)
    def procesar_verificacion(self, insumo):
        # 1. Validar (Aquí interactúa con la capa de Utils)
        if not insumo.strip():
            self.view.mostrar_resultado("Error: Ingresa un texto válido.")
            return

        #2. Delegar a la Lógica de Negocio (Service)
        resultado_logico = self.service.evaluar_stock(insumo)

        #3. Actualizar la Vista
        self.view.mostrar_resultado(resultado_logico)
