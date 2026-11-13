from pynput import keyboard

class MonitorTeclado:
    instancia = None

    def __new__(cls):
        if cls.instancia is None:
            cls.instancia = super().__new__(cls)
        return cls.instancia

    def __init__(self):
        self.hilo_monitor_teclado = None
        self.monitoreando = False
        self.escuchante = None

    def definir_escuchante(self, listener):
        self.escuchante = listener

    def evaluar_tecla(self, key):
        if key == keyboard.Key.shift_l:
            if self.escuchante:
                self.escuchante("left")
        elif key == keyboard.Key.shift_r:
            if self.escuchante:
                self.escuchante("right")

    def iniciar(self):
        self.monitoreando = True
        self.hilo_monitor_teclado = keyboard.Listener(on_press=self.evaluar_tecla)
        self.hilo_monitor_teclado.daemon = True
        self.hilo_monitor_teclado.start()

    def detener(self):
        if self.hilo_monitor_teclado:
            self.hilo_monitor_teclado.stop()
            self.monitoreando = False
