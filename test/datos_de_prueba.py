import pytest

from models.Insumo import Insumo
from models.Receta import Receta
from models.Ingrediente import Ingrediente
from models.Merma import Merma
from models.Platillo import Platillo


@pytest.fixture
def insumo_datos_prueba():
    return [
        Insumo(1, "Azúcar", "27/12/2026", 15, "kilos", 5, fecha_compra="02/10/2026"),
        Insumo(2, "Harina", "19/06/2027", 10, "kilos", 2, fecha_compra="18/09/2026"),
        Insumo(3, "Pollo", "15/10/2027", 30, "kilos", 6, fecha_compra="30/09/2026"),
        Insumo(4, "Carne de res", "05/10/2027", 5, "kilos", 4, fecha_compra="30/09/2026"),
        Insumo(5, "Café", "30/03/2027", 20, "kilos", 5, fecha_compra="06/08/2026"),
        Insumo(6, "Tomate", "03/10/2026", 7, "kilos", 8, fecha_compra="01/10/2026"),
        Insumo(7, "Papas", "12/11/2026", 17, "kilos", 10, fecha_compra="28/09/2026"),
        Insumo(8, "Pasta", "18/06/2027", 21, "kilos", 10, fecha_compra="07/09/2026"),
        Insumo(9, "Carne de res", "15/10/2026", 20, "kilos", 5, fecha_compra="02/10/2026"),
        Insumo(10, "Leche", "10/10/2026", 13, "litros", 10, fecha_compra="25/09/2026"),
    ]

@pytest.fixture
def receta_datos_prueba():
    return [
        Receta(1, "Pasta en salsa de tomate", "", 10),
        Receta(2, "Puré de papas", "", 15),
        Receta(3, "Filete de res", "", 2),
        Receta(4, "Caldo de pollo", "", 20),
        Receta(5, "Café", "", 40),
    ]

@pytest.fixture
def ingrediente_datos_prueba():
    return [
        Ingrediente(1, "Azúcar"),
        Ingrediente(2, "Harina"),
        Ingrediente(3, "Pollo"),
        Ingrediente(4, "Carne de res"),
        Ingrediente(5, "Café"),
        Ingrediente(6, "Tomate"),
        Ingrediente(7, "Papas"),
        Ingrediente(8, "Pasta"),
        Ingrediente(9, "Leche")
    ]

@pytest.fixture
def merma_datos_prueba():
    return [
        Merma(1, "27/12/2026","Se cayó" , 15, "gramos"),
        Merma(2, "19/06/2026","" , 10, "gramos"),
        Merma(3, "15/10/2026", "Se derramó", 30, "gramos"),
        Merma(4, "05/10/2026", "", 5, "gramos"),
        Merma(5, "30/03/2026","",  20, "gramos"),
        Merma(6, "03/10/2026", "No sirve", 7, "gramos"),
        Merma(7, "12/11/2026", "", 17, "gramos"),
        Merma(8, "18/06/2026", "", 21, "gramos"),
        Merma(9, "10/10/2026", "", 13, "mililitros"),
    ]

@pytest.fixture
def platillo_datos_prueba():
    return [
        Platillo(1, "Pasta en salsa de tomate", 150),
        Platillo(2, "Puré de papas", 70),
        Platillo(3, "Filete de res", 250),
        Platillo(4, "Caldo de pollo", 180),
        Platillo(5, "Café", 50),
    ]