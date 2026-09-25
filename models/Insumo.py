class Insumo:
    def __init__(self, id, nombre, cantidad, unidad_medida, fecha_caducidad, umbral):
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._unidad_medida = unidad_medida
        self._fecha_caducidad = fecha_caducidad
        self._umbral = umbral

    @property
    def nombre(self):
        return self._id

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def unidad_medida(self):
        return self._unidad_medida

    @property
    def fecha_caducidad(self):
            return self._fecha_caducidad

    @property
    def umbral(self):
            return self._umbral

    

