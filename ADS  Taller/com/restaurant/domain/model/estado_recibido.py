# com/restaurant/domain/model/estado_recibido.py

from com.restaurant.domain.model.estado_pedido import EstadoPedido
from com.restaurant.domain.model.estado_en_preparacion import EstadoEnPreparacion

class EstadoRecibido(EstadoPedido):
    def avanzar_estado(self, pedido):
        pedido.set_estado(EstadoEnPreparacion())

    def nombre(self) -> str:
        return "Recibido"
