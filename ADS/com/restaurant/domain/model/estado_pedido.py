# com/restaurant/domain/model/estado_pedido.py

from abc import ABC, abstractmethod

class EstadoPedido(ABC):
    @abstractmethod
    def avanzar_estado(self, pedido) -> None:
        pass

    @abstractmethod
    def nombre(self) -> str:
        pass
