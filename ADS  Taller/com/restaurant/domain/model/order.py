# com/restaurant/domain/model/order.py

from typing import List
from com.restaurant.domain.model.menu_item import MenuItem
from com.restaurant.domain.model.estado_recibido import EstadoRecibido
from com.restaurant.domain.model.estado_pedido import EstadoPedido


class Order:
    _contador_id = 1

    def __init__(self, cliente_nombre: str):
        self.id = Order._contador_id
        Order._contador_id += 1
        self.cliente_nombre = cliente_nombre
        self.items: List[MenuItem] = []
        self.estado: EstadoPedido = EstadoRecibido()
        self.observadores = []


    def set_estado(self, nuevo_estado: EstadoPedido):
        self.estado = nuevo_estado
        self.notificar_observadores(f"El pedido #{self.id} cambió a estado: {self.get_estado()}")

    def avanzar_estado(self):
        self.estado.avanzar_estado(self)



    def get_estado(self):
        return self.estado.nombre()

    def agregar_item(self, item: MenuItem):
        self.items.append(item)

    def calcular_total(self) -> float:
        return sum(item.get_precio() for item in self.items)

    def get_detalle(self) -> str:
        detalles = f"Pedido #{self.id} para {self.cliente_nombre} - Estado: {self.get_estado()}\n"
        for item in self.items:
            detalles += f"  - {item.get_nombre()} | ${item.get_precio():,.0f} | {item.get_descripcion()}\n"
        detalles += f"Total: ${self.calcular_total():,.0f}\n"
        return detalles
    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def notificar_observadores(self, mensaje: str):
        for observador in self.observadores:
            observador.actualizar(self, mensaje)
