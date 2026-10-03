class OrdenCompra:
    def __init__(self, num, fecha_creacion, fecha_cierre, total_bruto=0.0):
        self._num = num
        self._fecha_creacion = fecha_creacion
        self._fecha_cierre = fecha_cierre
        self._total_bruto = total_bruto

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value

    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    @fecha_creacion.setter
    def fecha_creacion(self, value):
        self._fecha_creacion = value

    @property
    def fecha_cierre(self):
        return self._fecha_cierre

    @fecha_cierre.setter
    def fecha_cierre(self, value):
        self._fecha_cierre = value

    @property
    def total_bruto(self):
        return self._total_bruto

    @total_bruto.setter
    def total_bruto(self, value):
        self._total_bruto = value