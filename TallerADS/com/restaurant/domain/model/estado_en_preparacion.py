# com/restaurant/domain/model/estado_en_preparacion.py

from com.restaurant.domain.model.estado_pedido import EstadoPedido
from com.restaurant.domain.model.estado_listo import EstadoListo

class EstadoEnPreparacion(EstadoPedido):
    def avanzar_estado(self, pedido):
        pedido.set_estado(EstadoListo())

    def nombre(self) -> str:
        return "En preparación"
