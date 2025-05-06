# com/restaurant/domain/model/estado_listo.py

from com.restaurant.domain.model.estado_pedido import EstadoPedido
from com.restaurant.domain.model.estado_entregado import EstadoEntregado


class EstadoListo(EstadoPedido):
    def avanzar_estado(self, pedido):
        pedido.set_estado(EstadoEntregado())

    def nombre(self) -> str:
        return "Listo para entregar"
