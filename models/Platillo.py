class Platillo:
    def __init__(self, num, nombre, precio):
        self._num = num
        self._nombre = nombre
        self._precio = precio #duda si poner o no

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
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        self._precio = value