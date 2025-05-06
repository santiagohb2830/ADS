# com/restaurant/domain/model/empaque_para_llevar.py

from com.restaurant.domain.model.menu_item_decorator import MenuItemDecorator

class EmpaqueParaLlevar(MenuItemDecorator):
    def get_precio(self) -> float:
        return self._menu_item.get_precio() + 2000

    def get_descripcion(self) -> str:
        return self._menu_item.get_descripcion() + " (Empaque para llevar)"
