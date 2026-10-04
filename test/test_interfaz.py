from controllers.ControladorRecetas import ControladorRecetas
from datos_de_prueba import *

def test_tabla_inventario():
    pass


def test_lista_recetas(qtbot, receta_datos_prueba):
    lista_errores = []

    widget = ControladorRecetas()
    # el qtbot va a inicializar el widget y correr la función para agregar recetas
    qtbot.addWidget(widget)
    widget.mostrar_lista_recetas(receta_datos_prueba)
    ui = widget._vista_lista_recetas
    lista_recetas = ui.lista_recetas

    # toma el widget de lista para iterar sobre cada elem y checar que el texto en el label widget concuerde
    # con el platillo que corresponde, el resultado se guarda en una lista
    for x in range(lista_recetas.count()-1):
        etiqueta = lista_recetas.itemWidget(lista_recetas.item(x)).layout().itemAt(0).widget()
        if etiqueta.text() == receta_datos_prueba[x].nombre:
            lista_errores.append(False)
        else:
            lista_errores.append(True)

    # Checa si hubo algún resultado malo en la lista
    assert lista_errores.count(True) == 0

def test_abrir_detalles_recetas(qtbot, receta_datos_prueba, capsys):
    widget = ControladorRecetas()
    qtbot.addWidget(widget)
    widget.mostrar_lista_recetas(receta_datos_prueba)
    ui = widget._vista_lista_recetas
    lista_recetas = ui.lista_recetas
    receta_prueba = receta_datos_prueba[0]

    # Agarra el botón de la primer receta de la lista y lo presiona
    boton_detalles = lista_recetas.itemWidget(lista_recetas.item(0)).layout().itemAt(1).widget()
    boton_detalles.click()
    vista = widget.layout().itemAt(0).widget()

    # checa si sí se abrió la página de detalles
    if vista.objectName() == "vista_receta_detalles":
        #checa que se abrió la receta correcta
        assert vista.layout.itemAt(0).widget().text() == receta_prueba.nombre
    else:
        assert False



def test_tabla_merma():
    pass

def test_lista_platillos():
    pass

def test_lista_ingredientes():
    pass