# com/restaurant/domain/model/plato_base.py

from com.restaurant.domain.model.menu_item import MenuItem

class PlatoBase(MenuItem):
    def __init__(self, nombre: str, precio: float, descripcion: str):
        self._nombre = nombre
        self._precio = precio
        self._descripcion = descripcion

    def get_nombre(self) -> str:
        return self._nombre

    def get_precio(self) -> float:
        return self._precio

    def get_descripcion(self) -> str:
        return self._descripcion
