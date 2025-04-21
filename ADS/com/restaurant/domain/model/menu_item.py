from abc import ABC, abstractmethod

class MenuItem(ABC):
    @abstractmethod
    def get_nombre(self) -> str:
        pass

    @abstractmethod
    def get_precio(self) -> float:
        pass

    @abstractmethod
    def get_descripcion(self) -> str:
        pass
