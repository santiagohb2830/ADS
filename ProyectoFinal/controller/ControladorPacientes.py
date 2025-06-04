from model.Paciente import Paciente

class ControladorPacientes:
    def __init__(self, base_datos):
        # Recibe una instancia de BaseDatos para acceder a los pacientes
        self.base_datos = base_datos

    def registrar_paciente(self, nombre, fecha_nacimiento, identificacion):
        # Verifica si el paciente ya está registrado por su identificación
        if self.base_datos.buscar_por_identificacion(identificacion):
            print("Paciente ya registrado.")
            return None
        # Crea un nuevo paciente y lo agrega a la base de datos
        nuevo = Paciente(None, nombre, fecha_nacimiento, identificacion)
        self.base_datos.agregar_paciente(nuevo)
        print("Paciente registrado correctamente.")
        return nuevo

    def listar_pacientes(self):
        # Retorna la lista de pacientes registrados
        return self.base_datos.listar_pacientes()
