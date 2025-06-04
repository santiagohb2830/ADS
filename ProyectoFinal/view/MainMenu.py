class MainMenu:
    def mostrar(self):
        # Menú principal del sistema
        print("\n--- Sistema de Gestión de Emergencias Hospitalarias ---")
        print("1. Registrar nuevo paciente")
        print("2. Realizar triaje")
        print("3. Ingresar resultado de laboratorio")
        print("4. Listar pacientes")
        print("5. Salir")
        return input("Seleccione una opción: ")
