# com/restaurant/application/menu_service.py

from com.restaurant.domain.model.plato_base import PlatoBase

class MenuService:
    def __init__(self):
        self.menu = []

    def agregar_plato(self, nombre: str, precio: float, descripcion: str):
        plato = PlatoBase(nombre, precio, descripcion)
        self.menu.append(plato)
        print(f"Plato agregado: {plato.get_nombre()}")

    def obtener_menu(self):
        return self.menu

    def mostrar_menu(self):
        print("=== Menú del Restaurante ===")
        for i, plato in enumerate(self.menu, start=1):
            print(f"{i}. {plato.get_nombre()} - ${plato.get_precio():,.0f}")
            print(f"   {plato.get_descripcion()}")
