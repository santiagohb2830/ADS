from model.ResultadoLaboratorio import ResultadoLaboratorio

class ControladorResultados:
    def agregar_resultado(self, paciente, tipo_examen, valor, unidad, umbral_critico):
        # Determina si el resultado es crítico comparando con el umbral
        critico = valor >= umbral_critico
        # Crea un resultado de laboratorio con el estado crítico si aplica
        resultado = ResultadoLaboratorio(tipo_examen, valor, unidad, critico)
        # Agrega el resultado al historial del paciente
        paciente.agregar_historial(resultado)
        # Notifica si el resultado fue crítico
        if critico:
            print("ALERTA: Resultado crítico detectado.")
        else:
            print("Resultado registrado.")
        return resultado
