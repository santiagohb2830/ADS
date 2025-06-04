class Paciente:
    def __init__(self, id_paciente, nombre, fecha_nacimiento, identificacion):
        self.id_paciente = id_paciente
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.identificacion = identificacion
        self.historial = []

    def agregar_historial(self, entrada):
        self.historial.append(entrada)

    def __str__(self):
        return f"Paciente({self.id_paciente}): {self.nombre} - ID: {self.identificacion}"
