import subprocess
import os

from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns
from rich.prompt import Prompt

from models.Receta import Receta
from VistaBase import VistaBase
from views.clases_personalizadas.InputEmisor import InputEmisor

class VistaRecetas(VistaBase):
    def __init__(self, console):
        super().__init__()
        self.console = console

        self.tabla_recetas = Table(title="Recetas")
        self.configurar_tabla_recetas()

        self.tabla_ingredientes = Table()
        self.configurar_tabla_ingredientes()

        self.tabla_instrucciones = Table()
        self.configurar_tabla_instrucciones()

        self.input_menu_recetas = InputEmisor()
        self.input_abrir_detalles = InputEmisor()
        self.input_menu_detalles = InputEmisor()
        self.input_menu_editar_receta = InputEmisor()
        self.input_menu_editar_ing = InputEmisor()
        self.input_menu_editar_inst = InputEmisor()

        self.layout["contenido"].split_column(Layout(name="main"), Layout(name="opciones"))

        self.mostrar_todas_recetas()
        self.crear_banda_opciones_principal()

    def resetear_vista(self):
        self.layout["main"].unsplit()

        self.tabla_recetas = Table(title="Recetas")
        self.configurar_tabla_recetas()
        self.tabla_ingredientes = Table()
        self.configurar_tabla_ingredientes()
        self.tabla_instrucciones = Table()
        self.configurar_tabla_instrucciones()

        self.crear_banda_opciones_principal()

    def mostrar_todas_recetas(self):
        if self.tabla_recetas.row_count > 0:
            self.resetear_vista()

        self.layout["main"].update(self.tabla_recetas)

    def configurar_tabla_recetas(self):
        columnas = ["#", "Nombre"]

        for columna in columnas:
            self.tabla_recetas.add_column(columna)

    def crear_elemento_tabla_recetas(self, receta:Receta):
        self.tabla_recetas.add_row(str(receta.num), receta.nombre)

    def mostrar_detalles_receta(self, receta:Receta, lista_ingredientes=None, lista_instrucciones=None, datos_editados={}):
        if self.tabla_ingredientes.row_count > 0 or self.tabla_instrucciones.row_count > 0:
            self.resetear_vista()

        self.layout["main"].split_column(Layout(name="panel_receta"),
                                         Layout(name="tabla_ing"),
                                         Layout(name="tabla_ins"))

        self.layout["panel_receta"].size = 2

        nombre_receta = datos_editados["nombre"] if "nombre" in datos_editados else receta.nombre
        nombre_receta += "**" if "nombre" in datos_editados else ""

        porciones_receta = datos_editados["porciones"] if "porciones" in datos_editados else str(receta.num_porciones)
        porciones_receta += "**" if "porciones" in datos_editados else ""

        panel = Panel(renderable=f"{"[bold red]" if "nombre" in datos_editados else "[bold yellow]"}"
                                 f"{nombre_receta}"
                                 f"{"[/bold red]" if "nombre" in datos_editados else "[/bold yellow]"}: "
                                 f"{"[bold red]" if "porciones" in datos_editados else "[italic yellow]"}"
                                 f"{porciones_receta}"
                                 f"{"[/bold red]" if "porciones" in datos_editados else "[/italic yellow]"}"
                                 f"[italic yellow] porciones [/italic yellow]")

        panel.height = 7

        self.layout["panel_receta"].update(panel)
        self.layout["tabla_ing"].update(self.tabla_ingredientes)
        self.layout["tabla_ins"].update(self.tabla_instrucciones)

        # self.llenar_tabla_ingredientes(lista_ingredientes)
        # self.llenar_tabla_instrucciones(lista_instrucciones)

    def configurar_tabla_ingredientes(self):
        columnas = ["Nombre", "Cantidad", "Unidad de medida"]
        self.tabla_ingredientes.title = "Ingredientes"
        self.tabla_ingredientes.expand = True

        for col in columnas:
            self.tabla_ingredientes.add_column(col)

    def llenar_tabla_ingredientes(self, lista_ingredientes):
        for ingrediente in lista_ingredientes:
            self.tabla_ingredientes.add_row(ingrediente.nombre)

    def configurar_tabla_instrucciones(self):
        columnas = ["#", "Instrucción"]
        self.tabla_instrucciones.title = "Instrucciones de preparación"
        self.tabla_instrucciones.expand = True

        for col in columnas:
            self.tabla_instrucciones.add_column(col)

    def llenar_tabla_instrucciones(self, lista_instrucciones):
        for instruccion in lista_instrucciones:
            self.tabla_instrucciones.add_row(instruccion)

    def crear_banda_opciones_principal(self):
        opciones_columna = Columns()
        opciones = ["[bold yellow]Opciones:[/bold yellow]",
                    "[1] Ver detalles de receta",
                    "[2] Crear receta",
                    "[3] Filtrar búsqueda",
                    "[M] Volver al menú"]

        opciones_columna.expand = True

        self.layout["opciones"].size = 1

        for opcion in opciones:
            opciones_columna.add_renderable(opcion)

        self.layout["opciones"].update(opciones_columna)

    def crear_banda_opciones_detalles(self):
        opciones_columna = Columns()
        opciones = ["[bold yellow]Opciones:[/bold yellow]",
                    "[1] Volver a recetas",
                    "[2] Editar receta",
                    "[M] Volver al menú"]

        opciones_columna.expand = True

        self.layout["opciones"].size = 1

        for opcion in opciones:
            opciones_columna.add_renderable(opcion)

        self.layout["opciones"].update(opciones_columna)

    def crear_banda_opciones_editar(self):
        opciones_columna = Columns()
        opciones = ["[bold yellow]Opciones:[/bold yellow]",
                    "[1] Editar nombre",
                    "[2] Editar porciones",
                    "[3] Editar ingredientes",
                    "[4] Editar instrucciones",
                    "[5] Guardar",
                    "[6] Cancelar",
                    "[M] Volver al menú"]

        opciones_columna.expand = True
        self.layout["opciones"].size = 1

        for opcion in opciones:
            opciones_columna.add_renderable(opcion)

        self.layout["opciones"].update(opciones_columna)

    def crear_banda_opciones_editar_ingrediente(self):
        opciones_columna = Columns()
        opciones = ["[bold yellow]Opciones:[/bold yellow]",
                    "[1] Agregar ingrediente",
                    "[2] Modificar ingrediente",
                    "[3] Eliminar ingrediente",
                    "[4] Volver"]

        opciones_columna.expand = True
        self.layout["opciones"].size = 1

        for opcion in opciones:
            opciones_columna.add_renderable(opcion)

        self.layout["opciones"].update(opciones_columna)

    def crear_banda_opciones_editar_instrucciones(self):
        opciones_columna = Columns()
        opciones = ["[bold yellow]Opciones:[/bold yellow]",
                    "[1] Agregar instrucción",
                    "[2] Modificar instrucción",
                    "[3] Eliminar instrucción",
                    "[4] Volver"]

        opciones_columna.expand = True
        self.layout["opciones"].size = 1

        for opcion in opciones:
            opciones_columna.add_renderable(opcion)

        self.layout["opciones"].update(opciones_columna)

    def mostrar_menu_recetas_prompt(self):
        self.input_menu_recetas.imprimir("Selecciona una opción",
                                         choices=["1", "2", "m"],
                                         show_choices=False)

    def mostrar_abrir_detalles_prompt(self, lista_recetas:list[Receta]):
        self.input_abrir_detalles.imprimir("Ingresa el índice de la receta a mostrar",
                                           choices=[str(receta.num) for receta in lista_recetas],
                                           show_choices=False)

    def mostrar_opciones_detalles_prompt(self):
        self.input_menu_detalles.imprimir("Selecciona una opción",
                                          choices=["1", "2", "m"],
                                          show_choices=False)

    def mostrar_opciones_editar_prompt(self):
        self.input_menu_editar_receta.imprimir("Selecciona una opción",
                                               choices=["1", "2", "3", "4", "5", "6", "M"],
                                               show_choices=False)

    def mostrar_editar_nombre_prompt(self):
        return Prompt.ask("[bold red]Ingresa el nuevo nombre de la receta[/bold red]")

    def mostrar_editar_porciones_prompt(self):
        return Prompt.ask("[bold red]Ingresa la nueva cantidad de porciones[/bold red]")

    def mostrar_opciones_editar_ing_prompt(self):
        self.input_menu_editar_ing.imprimir("Selecciona una opción",
                                            choices=[str(i) for i in range(1, 5)],
                                            show_choices=False)

    def mostrar_opciones_editar_inst_prompt(self):
        self.input_menu_editar_inst.imprimir("Selecciona una opción",
                                             choices=[str(i) for i in range(1, 5)],
                                             show_choices=False)

    def mostrar_layout(self):
        subprocess.run('cls' if os.name == 'nt' else 'clear')
        self.console.print(self.layout, justify="center")

