import time

from rich.pretty import pprint

from models.ingrediente import Ingrediente
from models.insumo import Insumo
from models.receta import Receta
from views.VistaRecetas import VistaRecetas


class ControladorRecetas:
    def __init__(self, vista:VistaRecetas, servicio=None):
        self.vista = vista
        self.servicio = servicio
        self.receta_actual = None
        self.formulario = {"ingredientes":[], "instrucciones":[], "item_borrado":False}
        self.ing_idx = {}

        self.recetas_testeo = self.crear_recetas_testeo()

        self.configurar_listeners()
        self.mostrar_lista_recetas()

    def configurar_listeners(self):
        self.vista.input_menu_recetas.agregar_escuchante(self.evaluar_seleccion_menu_recetas)
        self.vista.input_abrir_detalles.agregar_escuchante(self.mostrar_detalles_receta)
        self.vista.input_menu_detalles.agregar_escuchante(self.evaluar_seleccion_menu_detalles)
        self.vista.input_menu_editar_receta.agregar_escuchante(self.evaluar_seleccion_menu_editar)
        self.vista.input_menu_editar_ing.agregar_escuchante(self.evaluar_seleccion_editar_ing)
        self.vista.input_menu_editar_inst.agregar_escuchante(self.evaluar_seleccion_editar_inst)

    def crear_recetas_testeo(self):
        receta1 = Receta(2, "Receta de Pizza", 4,
                         {1: "Mezclar los ingredientes", 2: "Amasar la masa", 3: "Hornear la pizza"})

        Ingrediente1 = Ingrediente(1, "Harina", Insumo(1, "Harina de Trigo", fecha_compra="2026-01-01",
                                                       fecha_caducidad="2026-01-01", precio_unitario=2.0, umbral=5,
                                                       stock=10, unidad_medida="kg", tipo_insumo=None, marca=None))
        receta1.agregarIngrediente(Ingrediente1, 2, "taza")
        receta1.agregarIngrediente(Ingrediente(2, "Levadura", Insumo(2, "Levadura", fecha_compra="2026-01-01",
                                                                     fecha_caducidad="2026-01-01",
                                                                     precio_unitario=1.0, umbral=5, stock=10,
                                                                     unidad_medida="kg", tipo_insumo=None,
                                                                     marca=None)), 1, "cucharada")

        return [Receta(1, "Pasta en salsa de tomate", 10, {}), receta1]

    def mostrar_lista_recetas(self):
        """
        Conecta con la capa de servicios para obtener la lista de recetas y crea un elemento de lista para cada una.
        """

        self.vista.mostrar_todas_recetas()

        for receta in self.recetas_testeo:
            self.vista.crear_elemento_tabla_recetas(receta)

        self.vista.refrescar_pantalla()
        self.vista.mostrar_menu_recetas_prompt()

    def mostrar_detalles_receta(self, receta_num=None):
        if self.receta_actual is None:
            # Si no tenemos un receta actual, busca la receta por el num pasado como arg
            # idealmente con un servicio pero por ahora uso un loop para testeo
            for receta in self.recetas_testeo:
                if str(receta.num) == receta_num:
                    # La receta encontrada se convierte en la nueva receta actual
                    self.receta_actual = receta
                    break

        self.mapear_ingredientes()
        # llama la función para crear la vista de tabla de detalles y le pasa los datos del formulario actual
        self.vista.mostrar_detalles_receta(self.receta_actual, datos_editados=self.formulario, mapa_idx_ing=self.ing_idx)

        if self.usuario_esta_editando():
            # si actualmente el formulario tiene info, muestra las opciones de edicion y su prompt
            self.vista.crear_banda_opciones_editar()
            self.vista.refrescar_pantalla()
            self.vista.mostrar_opciones_editar_prompt()
        else:
            # si no hay info en el formulario, entonces queremos que nos de las opciones normales
            self.vista.crear_banda_opciones_detalles()
            self.vista.refrescar_pantalla()
            self.vista.mostrar_opciones_detalles_prompt()

    def guardar_editar_receta(self):
        # Cambia los datos del formulario en el objeto actual
        if "nombre" in self.formulario:
            self.receta_actual.nombre = self.formulario["nombre"]

        elif "porciones" in self.formulario:
            self.receta_actual.num_porciones = self.formulario["porciones"]

        elif len(self.formulario["ingredientes"]):
            for ing in self.formulario["ingredientes"]:
                self.receta_actual.agregarIngrediente(Ingrediente("1",
                                                                  ing["nombre"]), ing["cantidad"], ing["unidad_m"])

        elif len(self.formulario["instrucciones"]):
            # Aquí crear instrucciones y agregarlos
            pass

        pprint("guardando obj receta con datos")
        pprint(f"{self.receta_actual.__dict__}")
        # resetea el formulario porque la info ya se guardó y vuelve a la vista de detalles
        # esta debería jalar de nuevo el dato, el cual debería estar actualizado ya
        self.cancelar_edicion_actual()
        self.mostrar_detalles_receta(self.vista.input_abrir_detalles.user_input)

    def cancelar_edicion_actual(self):
        # resetea formulario y receta actual
        self.receta_actual = None
        self.formulario = {"ingredientes":[], "instrucciones":[], "item_borrado":False}

    def usuario_esta_editando(self):
        # checa si el usuario ha hecho cambios desde que entró a la vista de detalles
        if (len(self.formulario["ingredientes"]) > 0
                or len(self.formulario["instrucciones"]) > 0
                or len(self.formulario.items()) > 3) or self.formulario["item_borrado"]:
            return True
        return False

    def agregar_edicion_ingrediente(self, dict_ing):
        lista_ing_editados_nombre = [ing["nombre"] for ing in self.formulario["ingredientes"]]

        if dict_ing["nombre"] in lista_ing_editados_nombre:
            # checa si un ingrediente ya fue editado antes y remueve esa edicion para agregar la nueva
            obj = [ing for ing in self.formulario["ingredientes"] if ing["nombre"] == dict_ing["nombre"]][0]
            self.formulario["ingredientes"].remove(obj)

        self.formulario["ingredientes"].append(dict_ing)

    def mapear_ingredientes(self):
        # toma los ingredientes de la receta y los potenciales ing de el formulario
        # itera sobre cada uno y les asigna un número para mostrar en la tabla de la vista
        self.ing_idx = {}
        lista_ing = self.receta_actual.lista_ingredientes

        for i in range(len(lista_ing)):
            # agregando al dict los ingredientes originales de la receta
            self.ing_idx[i + 1] = lista_ing[i].ingrediente.nombre

        if len(self.formulario["ingredientes"]) > 0:
            for ing_dict in self.formulario["ingredientes"]:
                nombre = ing_dict["nombre"]

                if nombre in self.ing_idx.values():
                    # ingrediente repetido, omitir el mapeo
                    continue
                else:
                    try:
                        # encuentra el idx que sigue de acuerdo a los valores actuales
                        idx = int(list(self.ing_idx.keys())[-1]) + 1
                    except IndexError:
                        idx = 1
                    self.ing_idx[idx] = ing_dict["nombre"]

    def evaluar_seleccion_menu_recetas(self, seleccion):
        match seleccion:
            case "1":
                # Aquí debería obtener la lista de todas las recetas y pasarlas
                self.vista.mostrar_abrir_detalles_prompt(self.recetas_testeo)
            case "2":
                # Aquí debería agregar filtros de búsqueda
                pass
            case "m":
                # cancela la edicion actual antes de volver al menu
                self.cancelar_edicion_actual()

    def evaluar_seleccion_menu_detalles(self, seleccion):
        match seleccion:
            case "1":
                # volver a la vista de todas las recetas
                self.cancelar_edicion_actual()
                self.mostrar_lista_recetas()
            case "2":
                # abrir opciones de editar receta
                self.vista.crear_banda_opciones_editar()
                self.vista.refrescar_pantalla()
                self.vista.mostrar_opciones_editar_prompt()
            case "m":
                # volver al menú principal
                self.cancelar_edicion_actual()

    def evaluar_seleccion_menu_editar(self, seleccion):
        match seleccion:
            case "1":
                # abre prompt para cambiar el nombre de la receta
                nombre = self.vista.mostrar_editar_nombre_prompt()
                # checa que haya una respuesta del usuario y si es así lo debe validar
                if nombre is not None:
                    self.formulario["nombre"] = nombre
                self.mostrar_detalles_receta()

            case "2":
                # abre prompt para cambiar el num de porciones
                porciones = self.vista.mostrar_editar_porciones_prompt()
                # checa que haya un valor y luego valida el num de porciones
                if porciones is not None:
                    self.formulario["porciones"] = porciones
                self.mostrar_detalles_receta()

            case "3":
                # abre opciones para editar ing
                self.vista.crear_banda_opciones_editar_ingrediente()
                self.vista.refrescar_pantalla()
                self.vista.mostrar_opciones_editar_ing_prompt()

            case "4":
                # abre opciones para editar instrucciones
                self.vista.crear_banda_opciones_editar_instrucciones()
                self.vista.refrescar_pantalla()
                self.vista.mostrar_opciones_editar_inst_prompt()
            case "5":
                # llama a la función para guardar receta
                self.guardar_editar_receta()
            case "6":
                # cancela la edición actual y vuelve a detalles
                self.cancelar_edicion_actual()
                self.mostrar_detalles_receta(self.vista.input_abrir_detalles.user_input)
            case "m":
                # vuelve al menú
                self.cancelar_edicion_actual()

    def evaluar_seleccion_editar_ing(self, seleccion):
        match seleccion:
            case "1":
                # crear nuevo ingrediente
                ingrediente_raw = self.vista.mostrar_crear_ingrediente_prompt()
                if ingrediente_raw is not None:
                    #  válida y convierte str a dict
                    ingrediente_raw = [ing.strip() for ing in ingrediente_raw.split(",")]
                    ingrediente_dict = {"nombre": ingrediente_raw[0],
                                        "cantidad": ingrediente_raw[1],
                                        "unidad_m": ingrediente_raw[2]}

                    self.agregar_edicion_ingrediente(ingrediente_dict)

                self.mostrar_detalles_receta()

            case "2":
                # modificar ingrediente
                opciones_idx = [str(ing) for ing in self.ing_idx]

                num_ing, detalles_ingrediente_raw = self.vista.mostrar_modificar_ingrediente_prompt(opciones_idx)

                if detalles_ingrediente_raw is not None:
                    # busca el ing con el num y valída los nuevos datos
                    detalles_ingrediente_raw = [ing.strip() for ing in detalles_ingrediente_raw.split(",")]
                    nombre = self.ing_idx[int(num_ing)]

                    ingrediente_dict = {"nombre": nombre,
                                        "cantidad": detalles_ingrediente_raw[0],
                                        "unidad_m": detalles_ingrediente_raw[1]}
                    self.agregar_edicion_ingrediente(ingrediente_dict)
                self.mostrar_detalles_receta()

            case "3":
                opciones_idx = [str(ing) for ing in self.ing_idx]
                num_ing = self.vista.mostrar_borrar_ingrediente_prompt(opciones_idx)

                # debería validar aquí
                if num_ing is not None:
                    # busca el nombre del ing basado en el num ingresado,
                    # luego busca el obj IngredientesReceta de la receta actual basado en el nombre
                    # y lo borra de la receta
                    nombre = self.ing_idx[int(num_ing)]
                    self.receta_actual.ing_idx = [ing for ing in self.receta_actual.lista_ingredientes if not ing.ingrediente.nombre == nombre]
                    self.formulario["item_borrado"] = True
                self.mostrar_detalles_receta()
            case "4":
                # volver a menu editar principal
                self.vista.crear_banda_opciones_editar()
                self.vista.refrescar_pantalla()
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
                # volver a menu editar principal
                self.vista.crear_banda_opciones_editar()
                self.vista.refrescar_pantalla()
                self.vista.mostrar_opciones_editar_prompt()
