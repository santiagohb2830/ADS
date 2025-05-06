# com/restaurant/domain/model/extra_queso.py

from com.restaurant.domain.model.menu_item_decorator import MenuItemDecorator

class ExtraQueso(MenuItemDecorator):
    def get_precio(self) -> float:
        return self._menu_item.get_precio() + 3000

    def get_descripcion(self) -> str:
        return self._menu_item.get_descripcion() + " + extra queso"
