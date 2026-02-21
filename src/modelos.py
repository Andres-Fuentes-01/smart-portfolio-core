from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class Instrumento:
    """Representa un activo financiero, inmutable.

    Args:
        ticker: Sigla del instrumento (ej. "AAPL", "US10Y").
        tipo: Tipo de instrumento ("Acción", "Bono", etc.).
        sector: Sector económico ("Tecnología", "Gobierno", etc.).
    """
    ticker: str
    tipo: str
    sector: str


@dataclass
class Posicion:
    """Representa una posición en un instrumento financiero.

    Args:
        instrumento: Instancia de `Instrumento` asociada a la posición.
        cantidad: Número de unidades compradas. Debe ser positivo.
        precio_entrada: Precio al que se adquirió la posición.
    """
    instrumento: Instrumento
    cantidad: float          # nombre público en el constructor
    precio_entrada: float
    _cantidad: float = field(init=False, repr=False)  # almacenamiento interno

    def __post_init__(self) -> None:
        """Valida los atributos después de inicializar la instancia."""
        if not isinstance(self.instrumento, Instrumento):
            raise TypeError("instrumento debe ser de tipo Instrumento")
        if not isinstance(self.precio_entrada, (int, float)):
            raise TypeError("precio_entrada debe ser numérico")
        # Dispara el setter para validar y mover el valor al campo interno
        self.cantidad = self.cantidad  # llama al setter definido abajo

    @property
    def cantidad(self) -> float:
        """Cantidad de unidades (no negativa)."""
        return self._cantidad

    @cantidad.setter
    def cantidad(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("cantidad debe ser numérica")
        if value < 0:
            raise ValueError("cantidad no puede ser negativa")
        self._cantidad = float(value)

    def calcular_valor_actual(self, precio_mercado: float) -> float:
        """Calcula el valor actual de la posición.

        Args:
            precio_mercado: Precio actual del instrumento.

        Returns:
            Valor de la posición = cantidad * precio_mercado.
        """
        if not isinstance(precio_mercado, (int, float)):
            raise TypeError("precio_mercado debe ser numérico")
        return self.cantidad * precio_mercado