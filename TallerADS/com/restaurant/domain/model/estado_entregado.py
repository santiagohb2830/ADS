from com.restaurant.domain.model.estado_pedido import EstadoPedido

class EstadoEntregado(EstadoPedido):
    def avanzar_estado(self, pedido):
        print("El pedido ya fue entregado. No puede avanzar más.")

    def nombre(self) -> str:
        return "Entregado"
