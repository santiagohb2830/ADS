# com/restaurant/application/order_service.py

from com.restaurant.domain.model.order import Order

class OrderService:
    def __init__(self):
        self.pedidos = []

    def crear_pedido(self, cliente_nombre: str) -> Order:
        pedido = Order(cliente_nombre)
        self.pedidos.append(pedido)
        return pedido

    def avanzar_estado_pedido(self, pedido: Order):
        pedido.avanzar_estado()

    def mostrar_detalle_pedido(self, pedido: Order):
        print(pedido.get_detalle())
