# com/restaurant/domain/model/cliente_observador.py

from com.restaurant.domain.model.observador import Observador

class ClienteObservador(Observador):
    def __init__(self, nombre: str):
        self.nombre = nombre

    def actualizar(self, pedido, mensaje: str):
        print(f"[Notificación para {self.nombre}] {mensaje}")
