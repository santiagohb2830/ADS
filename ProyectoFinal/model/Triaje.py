class Triaje:
    def __init__(self, temperatura, presion, saturacion, conciencia, dolor):
        self.temperatura = temperatura
        self.presion = presion
        self.saturacion = saturacion
        self.conciencia = conciencia
        self.dolor = dolor
        self.prioridad = self.calcular_prioridad()

    def calcular_prioridad(self):
        if self.saturacion < 85 or self.conciencia < 8:
            return "Rojo"
        elif self.dolor >= 7 or self.saturacion < 92:
            return "Amarillo"
        else:
            return "Verde"

    def __str__(self):
        return f"Triaje: {self.temperatura}°C, {self.presion}, O2: {self.saturacion}%, Prioridad: {self.prioridad}"
