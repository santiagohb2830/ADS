class BaseDatos:
    def __init__(self):
        self.pacientes = []
        self.id_contador = 1

    def agregar_paciente(self, paciente):
        paciente.id_paciente = self.id_contador
        self.pacientes.append(paciente)
        self.id_contador += 1

    def buscar_por_identificacion(self, identificacion):
        for paciente in self.pacientes:
            if paciente.identificacion == identificacion:
                return paciente
        return None

    def listar_pacientes(self):
        return self.pacientes
