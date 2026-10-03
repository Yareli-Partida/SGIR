class Venta:
    def __init__(self, num, fecha, numero_comensales, monto_total=0.0):
        self._num = num
        self._fecha = fecha
        self._numero_comensales = numero_comensales
        self._monto_total = monto_total

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, valor):
        self._num = valor

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha

    @property
    def numero_comensales(self):
        return self._numero_comensales

    @numero_comensales.setter
    def numero_comensales(self, num):
        self._numero_comensales = num

    @property
    def monto_total(self):
        return self._monto_total

    @monto_total.setter
    def monto_total(self, monto):
        self._monto_total = monto