class FormularioRegistro:
    def pedir_datos_paciente(self):
        # Solicita los datos básicos del paciente desde la consola
        print("\n--- Registro de Paciente ---")
        nombre = input("Nombre completo: ")
        fecha_nacimiento = input("Fecha de nacimiento (AAAA-MM-DD): ")
        identificacion = input("Número de identificación: ")
        return nombre, fecha_nacimiento, identificacion
