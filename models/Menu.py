class Menu:
    def __init__(self, num, nombre, cantidad_recetas=0):
        self._num = num
        self._nombre = nombre
        self._cantidad_recetas = cantidad_recetas 

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
    def cantidad_recetas(self):
        return self._cantidad_recetas

    @cantidad_recetas.setter
    def cantidad_recetas(self, value):
        self._cantidad_recetas = value