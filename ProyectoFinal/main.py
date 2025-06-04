from model.BaseDatos import BaseDatos
from controller.ControladorPacientes import ControladorPacientes
from controller.ControladorTriaje import ControladorTriaje
from controller.ControladorResultados import ControladorResultados
from view.MainMenu import MainMenu
from view.FormularioRegistro import FormularioRegistro
from view.DashboardPrioridad import DashboardPrioridad

# Inicialización de módulos principales
bd = BaseDatos()
cp = ControladorPacientes(bd)
ct = ControladorTriaje()
cr = ControladorResultados()

menu = MainMenu()
form = FormularioRegistro()
dashboard = DashboardPrioridad()

# Bucle principal del programa
while True:
    opcion = menu.mostrar()

    if opcion == "1":
        # Registro de paciente nuevo
        nombre, fecha_nacimiento, identificacion = form.pedir_datos_paciente()
        cp.registrar_paciente(nombre, fecha_nacimiento, identificacion)

    elif opcion == "2":
        # Realizar triaje a un paciente existente
        identificacion = input("Ingrese número de identificación del paciente: ")
        paciente = bd.buscar_por_identificacion(identificacion)
        if paciente:
            print("Ingrese signos vitales:")
            temperatura = float(input("Temperatura (°C): "))
            presion = input("Presión arterial (ej. 120/80): ")
            saturacion = int(input("Saturación O2 (%): "))
            conciencia = int(input("Nivel de conciencia (1–15): "))
            dolor = int(input("Nivel de dolor (1–10): "))
            ct.asignar_triaje(paciente, temperatura, presion, saturacion, conciencia, dolor)
        else:
            print("Paciente no encontrado.")

    elif opcion == "3":
        # Agregar resultado de laboratorio
        identificacion = input("Ingrese número de identificación del paciente: ")
        paciente = bd.buscar_por_identificacion(identificacion)
        if paciente:
            tipo = input("Tipo de examen: ")
            valor = float(input("Valor numérico del resultado: "))
            unidad = input("Unidad de medida: ")
            umbral = float(input("Umbral crítico para este examen: "))
            cr.agregar_resultado(paciente, tipo, valor, unidad, umbral)
        else:
            print("Paciente no encontrado.")

    elif opcion == "4":
        # Mostrar todos los pacientes
        pacientes = cp.listar_pacientes()
        dashboard.mostrar_lista(pacientes)

    elif opcion == "5":
        print("Saliendo del sistema. Hasta luego.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")
