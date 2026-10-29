class TipoMerma:
    def __init__(self, clave, nombre):
        self._clave = clave
        self._nombre = nombre

    @property
    def clave(self):
        return self._clave

    @clave.setter
    def clave(self, value):
        self._clave = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value