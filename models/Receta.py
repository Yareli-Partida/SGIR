class Receta:
    def __init__(self, num, nombre, num_porciones, instrucciones):
        self._num = num
        self._nombre = nombre
        self._num_porciones = num_porciones

        #diccionario para las instrucciones {"numeroIntruccion":"instruccion"}
        self._instrucciones = instrucciones

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
    def num_porciones(self):
        return self._num_porciones

    @num_porciones.setter
    def num_porciones(self, value):
        self._num_porciones = value

    @property
    def instrucciones(self):
        return self._instrucciones

    @instrucciones.setter
    def instrucciones(self, value):
        self._instrucciones = value


'''EJEMPLO DE USO
receta1 = Receta(1, "Receta de Pizza", 4, {1: "Mezclar los ingredientes", 2: "Amasar la masa", 3: "Hornear la pizza"}) 

for num, instruccion in receta1.instrucciones.items():
    print(f"Instrucción {num}: {instruccion}")

'''