from model.Triaje import Triaje

class ControladorTriaje:
    def asignar_triaje(self, paciente, temperatura, presion, saturacion, conciencia, dolor):
        # Crea una instancia de Triaje con los datos ingresados
        triaje = Triaje(temperatura, presion, saturacion, conciencia, dolor)
        # Asocia el triaje al historial del paciente
        paciente.agregar_historial(triaje)
        print(f"Triaje asignado. Prioridad: {triaje.prioridad}")
        return triaje
