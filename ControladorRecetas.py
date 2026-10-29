from models.Receta import Receta
from VistaRecetas import VistaRecetas


class ControladorRecetas:
    def __init__(self, vista:VistaRecetas, servicio=None):
        self.vista = vista
        self.servicio = servicio
        self.receta_edicion = None
        self.edicion_actual = {}

        self.configurar_listeners()
        self.mostrar_lista_recetas()

    def configurar_listeners(self):
        self.vista.input_menu_recetas.agregar_escuchante(self.evaluar_seleccion_menu_recetas)
        self.vista.input_abrir_detalles.agregar_escuchante(self.mostrar_detalles_receta)
        self.vista.input_menu_detalles.agregar_escuchante(self.evaluar_seleccion_menu_detalles)
        self.vista.input_menu_editar_receta.agregar_escuchante(self.evaluar_seleccion_menu_editar)
        self.vista.input_menu_editar_ing.agregar_escuchante(self.evaluar_seleccion_editar_ing)
        self.vista.input_menu_editar_inst.agregar_escuchante(self.evaluar_seleccion_editar_inst)

    def mostrar_lista_recetas(self):
        """
        Conecta con la capa de servicios para obtener la lista de recetas y crea un elemento de lista para cada una.
        """
        # esto es solo para testeo manual

        self.vista.mostrar_todas_recetas()

        lista_recetas = [Receta(1, "Pasta en salsa de tomate", 10, "")]

        for receta in lista_recetas:
            self.vista.crear_elemento_tabla_recetas(receta)

        self.vista.mostrar_layout()
        self.vista.mostrar_menu_recetas_prompt()

    def cancelar_edicion_actual(self):
        self.receta_edicion = None
        self.edicion_actual = {}

    def mostrar_detalles_receta(self, receta_num=None):
        if self.receta_edicion is None:
            # Aquí debería buscar la receta dependiendo el num ingresado
            receta = Receta(1, "Pasta en salsa de tomate", 10, "")
            self.receta_edicion = receta
        else:
            receta = self.receta_edicion

        self.vista.mostrar_detalles_receta(receta, datos_editados=self.edicion_actual)

        if len(self.edicion_actual.items()) == 0:
            self.vista.crear_banda_opciones_detalles()
            self.vista.mostrar_layout()
            self.vista.mostrar_opciones_detalles_prompt()
        else:
            self.vista.crear_banda_opciones_editar()
            self.vista.mostrar_layout()
            self.vista.mostrar_opciones_editar_prompt()

    def evaluar_seleccion_menu_recetas(self, seleccion):
        match seleccion:
            case "1":
                # Aquí debería obtener la lista de todas las recetas
                lista_recetas = [Receta(1, "Pasta en salsa de tomate", 10, "")]
                self.vista.mostrar_abrir_detalles_prompt(lista_recetas)
            case "2":
                # Aquí debería agregar filtros de búsqueda
                pass

    def evaluar_seleccion_menu_detalles(self, seleccion):
        match seleccion:
            case "1":
                self.cancelar_edicion_actual()
                self.mostrar_lista_recetas()
            case "2":
                self.vista.crear_banda_opciones_editar()
                self.vista.mostrar_layout()
                self.vista.mostrar_opciones_editar_prompt()

    def evaluar_seleccion_menu_editar(self, seleccion):
        match seleccion:
            case "1":
                nombre = self.vista.mostrar_editar_nombre_prompt()
                # valida el nombre
                self.edicion_actual["nombre"] = nombre
                self.mostrar_detalles_receta()
            case "2":
                porciones = self.vista.mostrar_editar_porciones_prompt()
                self.edicion_actual["porciones"] = porciones
                self.mostrar_detalles_receta()
            case "3":
                self.vista.crear_banda_opciones_editar_ingrediente()
                self.vista.mostrar_layout()
                self.vista.mostrar_opciones_editar_ing_prompt()
            case "4":
                self.vista.crear_banda_opciones_editar_instrucciones()
                self.vista.mostrar_layout()
                self.vista.mostrar_opciones_editar_inst_prompt()
            case "5":
                pass
            case "6":
                self.cancelar_edicion_actual()
                self.mostrar_detalles_receta(self.vista.input_menu_editar_receta.user_input)

    def evaluar_seleccion_editar_ing(self, seleccion):
        match seleccion:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                self.vista.crear_banda_opciones_editar()
                self.vista.mostrar_layout()
                self.vista.mostrar_opciones_editar_prompt()

    def evaluar_seleccion_editar_inst(self, seleccion):
        match seleccion:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                self.vista.crear_banda_opciones_editar()
                self.vista.mostrar_layout()
                self.vista.mostrar_opciones_editar_prompt()
