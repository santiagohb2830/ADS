
# Sistema de Gestión de Emergencias Hospitalarias

Este proyecto es un prototipo funcional desarrollado en Python que simula el flujo básico de un sistema de urgencias hospitalarias. Incluye registro de pacientes, asignación de prioridad médica mediante triaje, carga de resultados de laboratorio y visualización general del estado de cada paciente.

---

## 📂 Estructura del Proyecto

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

## 🧠 ¿Qué hace el sistema?

- **Registrar pacientes** nuevos, evitando duplicados.
- **Realizar triaje** con signos vitales y asignar prioridad médica automáticamente.
- **Ingresar resultados de laboratorio** y activar alertas si son críticos.
- **Visualizar pacientes** y su historial clínico reciente desde consola.

---

## 🖥️ Cómo ejecutar

1. Asegúrate de tener Python 3 instalado.
2. Abre una terminal y navega a la carpeta del proyecto.
3. Ejecuta el archivo principal:

```bash
python main.py
```

---

## ✅ Funcionalidades disponibles

| Opción de Menú | Descripción |
|----------------|-------------|
| 1. Registrar nuevo paciente | Crea un nuevo registro en el sistema |
| 2. Realizar triaje | Captura signos vitales y calcula prioridad |
| 3. Ingresar resultado de laboratorio | Registra examen con valor y alerta crítica si aplica |
| 4. Listar pacientes | Muestra todos los pacientes con último registro |
| 5. Salir | Termina el programa |

---

## 💾 Ejemplo de uso

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

## 📚 Tecnologías usadas

- **Python 3**
- Estructura MVC simplificada
- Consola como interfaz de usuario
- Simulación de base de datos en memoria (`BaseDatos.py`)

---

## 📌 Notas adicionales

- Este proyecto es un prototipo. No incluye persistencia en archivos o base de datos real.
- La lógica del triaje es simplificada, y puede adaptarse a protocolos clínicos reales.
- La arquitectura está preparada para escalar con una interfaz gráfica en el futuro.

---

Proyecto desarrollado para el curso **Análisis y Diseño de Sistemas (ADS)**.  
Pontificia Universidad Javeriana – 2025
