# com/restaurant/domain/model/customer.py

class Customer:
    def __init__(self, id: str, nombre: str, direccion: str = "", telefono: str = ""):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_direccion(self):
        return self.direccion

    def get_telefono(self):
        return self.telefono
