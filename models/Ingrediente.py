class Ingrediente:
    KG = 'kg'


    def __init__(self, id, nombre, cantidad, unidad_medida):
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._unidad_medida = unidad_medida

    @property
    def nombre(self):
        return self._id

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def unidad_medida(self):
        return self._unidad_medida
