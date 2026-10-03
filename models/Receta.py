class Receta:
    def __init__(self, num, nombre, instrucciones, num_porciones):
        self._num = num
        self._nombre = nombre
        self._instrucciones = instrucciones
        self._num_porciones = num_porciones

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
    def instrucciones(self):
        return self._instrucciones

    @instrucciones.setter
    def instrucciones(self, value):
        self._instrucciones = value

    @property
    def num_porciones(self):
        return self._num_porciones

    @num_porciones.setter
    def num_porciones(self, value):
        self._num_porciones = value