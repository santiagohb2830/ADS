# com/restaurant/domain/model/observador.py

from abc import ABC, abstractmethod
from com.restaurant.domain.model.order import Order

class Observador(ABC):
    @abstractmethod
    def actualizar(self, pedido: Order, mensaje: str):
        pass
