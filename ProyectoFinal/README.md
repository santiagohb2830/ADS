# Sistema de Gestión de Emergencias Hospitalarias

Este proyecto corresponde a un prototipo funcional desarrollado en Python que simula el flujo básico de un sistema de urgencias hospitalarias. Incluye funcionalidades para el registro de pacientes, asignación de prioridad médica mediante triaje, carga de resultados de laboratorio y visualización general del estado de cada paciente.

---

## Estructura del Proyecto

```
hospital-emergencias/
│
├── model/
│   ├── Paciente.py
│   ├── Triaje.py
│   ├── ResultadoLaboratorio.py
│   └── BaseDatos.py
│
├── controller/
│   ├── ControladorPacientes.py
│   ├── ControladorTriaje.py
│   └── ControladorResultados.py
│
├── view/
│   ├── MainMenu.py
│   ├── FormularioRegistro.py
│   └── DashboardPrioridad.py
│
├── main.py
└── README.md
```

---

## Descripción General del Sistema

El sistema permite:

- Registrar pacientes nuevos evitando duplicados.
- Realizar triaje con signos vitales y asignar prioridad médica de forma automática.
- Ingresar resultados de laboratorio y activar alertas si estos son críticos.
- Visualizar pacientes y su historial clínico reciente a través de una interfaz por consola.

---

## Instrucciones de Ejecución

1. Instalar Python 3.
2. Abrir una terminal y navegar hasta la carpeta del proyecto.
3. Ejecutar el archivo principal con el siguiente comando:

```bash
python main.py
```

---

## Funcionalidades Disponibles

| Opcion de Menú | Descripción |
|----------------|-------------|
| 1. Registrar nuevo paciente | Crea un nuevo registro en el sistema |
| 2. Realizar triaje | Captura signos vitales y calcula prioridad |
| 3. Ingresar resultado de laboratorio | Registra examen con valor y alerta crítica si aplica |
| 4. Listar pacientes | Muestra todos los pacientes con último registro |
| 5. Salir | Termina el programa |

---

## Ejemplo de Uso

### Entrada (vía consola):

```
Nombre completo: Ana Pérez
Fecha de nacimiento: 1992-06-01
Número de identificación: 10203040
```

```
Temperatura: 39.2
Presión arterial: 110/70
Saturación O2: 86
Conciencia: 12
Dolor: 6
```

```
Tipo de examen: Glucosa
Valor: 245
Unidad: mg/dL
Umbral crítico: 200
```

### Salida esperada:

```
Paciente registrado correctamente.
Triaje asignado. Prioridad: Amarillo
ALERTA: Resultado crítico detectado.
```

---

## Tecnologías Utilizadas

- Python 3
- Arquitectura MVC simplificada
- Interfaz por consola
- Simulación de base de datos en memoria (`BaseDatos.py`)

---

## Observaciones Adicionales

- El sistema es un prototipo y no implementa persistencia en disco ni acceso a bases de datos reales.
- La lógica del triaje está simplificada y puede ser adaptada a protocolos clínicos formales.
- La arquitectura permite futura extensión hacia interfaces gráficas u otros entornos.

Este proyecto se construyó siguiendo el diagrama de clases definido en la fase de diseño del sistema, aplicando una organización modular según el patrón MVC, y está alineado con los requerimientos funcionales y casos de uso previamente documentados.

---

## Autores

- Johan Sebastián Méndez Ibarra  
- Andrés David Ortiz Forero  

Proyecto desarrollado para el curso Análisis y Diseño de Sistemas (ADS).  
Pontificia Universidad Javeriana – 2025
