class ResultadoLaboratorio:
    def __init__(self, tipo_examen, valor, unidad, es_critico=False):
        self.tipo_examen = tipo_examen
        self.valor = valor
        self.unidad = unidad
        self.es_critico = es_critico

    def marcar_critico(self):
        self.es_critico = True

    def __str__(self):
        estado = "CRÍTICO" if self.es_critico else "Normal"
        return f"{self.tipo_examen}: {self.valor} {self.unidad} [{estado}]"
