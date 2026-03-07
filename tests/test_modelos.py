import pytest
from src.modelos import Instrumento, Posicion

def test_instrumento_inmutable():
    inst = Instrumento("AAPL", "Acción", "Tecnología")
    with pytest.raises(AttributeError):
        inst.ticker = "MSFT"  # Debe lanzar FrozenInstanceError

def test_posicion_cantidad_negativa():
    with pytest.raises(ValueError):
        Posicion(Instrumento("AAPL", "Acción", "Tecnología"), _cantidad=-1, precio_entrada=100)

def test_valor_actual():
    inst = Instrumento("AAPL", "Acción", "Tecnología")
    pos = Posicion(inst, _cantidad=2, precio_entrada=150)
    assert pos.calcular_valor_actual(200) == 400
