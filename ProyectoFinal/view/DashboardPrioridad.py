class DashboardPrioridad:
    def mostrar_lista(self, pacientes):
        # Muestra todos los pacientes y sus últimas prioridades asignadas (si existen)
        print("\n--- Lista de Pacientes Registrados ---")
        if not pacientes:
            print("No hay pacientes registrados.")
            return

        for paciente in pacientes:
            print(f"\nNombre: {paciente.nombre}")
            print(f"ID: {paciente.identificacion}")
            if paciente.historial:
                ultimo = paciente.historial[-1]
                print(f"Último Registro: {ultimo}")
            else:
                print("Sin historial clínico registrado.")
