# com/restaurant/domain/model/menu_item_decorator.py

from com.restaurant.domain.model.menu_item import MenuItem

class MenuItemDecorator(MenuItem):
    def __init__(self, menu_item: MenuItem):
        self._menu_item = menu_item

    def get_nombre(self) -> str:
        return self._menu_item.get_nombre()

    def get_precio(self) -> float:
        return self._menu_item.get_precio()

    def get_descripcion(self) -> str:
        return self._menu_item.get_descripcion()
