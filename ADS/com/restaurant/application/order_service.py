# com/restaurant/application/order_service.py

from com.restaurant.domain.model.order import Order
from com.restaurant.domain.model.customer import Customer


class OrderService:
    def __init__(self):
        self.pedidos = []

    def crear_pedido(self, cliente: Customer) -> Order:
        pedido = Order(cliente)
        self.pedidos.append(pedido)
        return pedido

    def avanzar_estado_pedido(self, pedido: Order):
        pedido.avanzar_estado()

    def mostrar_detalle_pedido(self, pedido: Order):
        print(pedido.get_detalle())
