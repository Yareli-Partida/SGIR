class Insumo:
    def __init__(self, num, nombre, fecha_caducidad, stock, unidad_medida, umbral=None, precio_unitario=None, fecha_compra=None):
        self._num = num
        self._nombre = nombre
        self._fecha_caducidad = fecha_caducidad
        self._stock = stock
        self._unidad_medida = unidad_medida
        self._umbral = umbral 
        self._precio_unitario = precio_unitario  
        self._fecha_compra = fecha_compra  

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def fecha_caducidad(self):
        return self._fecha_caducidad

    @fecha_caducidad.setter
    def fecha_caducidad(self, value):
        self._fecha_caducidad = value

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        self._stock = value

    @property
    def unidad_medida(self):
        return self._unidad_medida

    @unidad_medida.setter
    def unidad_medida(self, value):
        self._unidad_medida = value

    @property
    def umbral(self):
        return self._umbral

    @umbral.setter
    def umbral(self, value):
        self._umbral = value

    @property
    def precio_unitario(self):
        return self._precio_unitario

    @precio_unitario.setter
    def precio_unitario(self, value):
        self._precio_unitario = value

    @property
    def fecha_compra(self):
        return self._fecha_compra

    @fecha_compra.setter
    def fecha_compra(self, value):
        self._fecha_compra = value

