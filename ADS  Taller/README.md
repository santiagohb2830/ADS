# Sistema de Gestión de Pedidos - Taller de Diseño y Arquitectura de Software
## Santiago Hernandez, Jose Manuel Guerrero
## 1. Introducción

Taller de Diseño y Arquitectura de Software, cuyo objetivo es aplicar principios de diseño como SOLID, técnicas de descomposición en componentes y patrones arquitectónicos, para construir una solución organizada y extensible. 

Se desarrolló un sistema básico de gestión de pedidos para un restaurante, incluyendo funcionalidades como creación de ítems de menú, construcción de pedidos personalizados y cálculo del costo total.

El enfoque adoptado en este proyecto sigue una arquitectura orientada a objetos, respetando los principios de diseño aprendidos a lo largo del curso. Además, se estructura el código en paquetes (módulos) y se documenta tanto el código como las decisiones de diseño tomadas durante el desarrollo.

## 2. Estructura del Proyecto y Descomposición del Sistema

El sistema está organizado siguiendo una arquitectura en capas y un enfoque modular que permite la separación de responsabilidades. Se describen las capas y los paquetes principales:

### 2.1 Arquitectura en Capa

- **Capa de Presentación (`ui/`)**: Contiene la interfaz de usuario por consola. Se encarga de interactuar con el usuario y capturar sus entradas.
- **Capa de Aplicación (`application/`)**: Contiene los servicios que coordinan las operaciones del sistema, como `OrderService` y `MenuService`.
- **Capa de Dominio (`domain/`)**: Incluye los modelos principales del negocio (`Order`, `MenuItem`, `Customer`, etc.), los estados del pedido (`State`) y decoradores (`Decorator`) para los platos.
- **(Opcional) Infraestructura (`infrastructure/`)**: Preparada para futuras implementaciones como persistencia en archivos, bases de datos o servicios externos.

### 2.2 Paquetes del Proyecto

```
com.restaurant/
├── ui/
│   └── restaurant_console_app.py
├── application/
│   ├── menu_service.py
│   └── order_service.py
├── domain/
│   ├── model/
│   │   ├── menu_item.py
│   │   ├── plato_base.py
│   │   ├── extra_queso.py
│   │   ├── empaque_para_llevar.py
│   │   ├── order.py
│   │   ├── customer.py
│   │   ├── estado_pedido.py
│   │   ├── estado_recibido.py
│   │   ├── estado_en_preparacion.py
│   │   ├── estado_listo.py
│   │   ├── estado_entregado.py
│   │   ├── observador.py
│   │   └── cliente_observador.py
```

Esta organización permite mantener una alta cohesión dentro de los módulos y un bajo acoplamiento entre ellos, cumpliendo con los principios de diseño orientado a objetos y SOLID.


## 3. Modelo de Dominio y Diagrama UML

El sistema modela un flujo de pedidos para un restaurante, donde el cliente selecciona ítems del menú, personaliza su pedido mediante extras, y este avanza por distintos estados hasta ser entregado.

### 3.1 Entidades Principales

- **MenuItem (interface)**: Define la estructura básica de cualquier ítem de menú.
- **PlatoBase**: Implementación concreta de MenuItem.
- **Decoradores**: `ExtraQueso`, `EmpaqueParaLlevar`, extienden funcionalidad de un MenuItem.
- **Order**: Representa un pedido. Contiene una lista de MenuItems y un estado.
- **EstadoPedido (interface)**: Define los métodos para avanzar el estado del pedido.
- **Estados concretos**: `EstadoRecibido`, `EstadoEnPreparacion`, `EstadoListo`, `EstadoEntregado`.
- **Customer**: Contiene la información del cliente que realiza el pedido.
- **Observador (interface)**: Se notifica de cambios en el pedido.
- **ClienteObservador**: Implementación concreta de observador para clientes.

### 3.2 Diagrama de Clases (UML)


Este diagrama refleja el uso de los patrones Decorator, State y Observer, y cómo se integran para representar el dominio del problema de forma modular, escalable y extensible.
Link: https://mermaid.live/edit#pako:eNq1VV1v2jAU_SvIT5sKiKU0ySLEw2gfJnUa2-MUKbrEF2otsTPbQV0p_30mAWInpGIPzRM-5377XLMjqaBIIpJmoNQ9g42EPOYD81XI4Bvy8qvGfLCr0cM3mzGuUa4hxfm8gW82qBMu8pXEDx9bcCExZaIDU1SpZIWh-Inbx9zOv8xAiy-g0C5gVGexgDq-BViR37nC04TuMRXSFCudSnPDJszQ0dnwnet5eNYSfpSohIPmBfwpcQkSHjPcgnSdvkuKbuGMWoc0Y2iu3KZNI8o6o9JA7QsQK4VyazCJlt2NERhuQFYjcZqDLfAXQ9SBXOro04R0aC40W7MUXJSihixD1TelKs0SKaPiGm23yisqRztfkigtk-TNdD_Nla4YFV3mgS8lFuZyGsHa9CNT-qKXPkzmENC5zPOcruos1SVkzDTndtXqYFFL4HLs_wzy9i5rzHAtuLhuT07WncGfX67Z63jcvCOXyM4Ku0bNZs9eR6POgvWZ9W1cvWuj0bz1IjS4Lc6ac-Ra1XxJUX1WF9TVZ2oprT9aS3VN4Y06jkyjlipAR0TtAIvTQ0OGZCMZJZGWJQ5JjjKHw5FU0omJfsIcYxKZnxTk75jEfG98CuC_hMhPblKUmycSrSFT5lQWFDQe_-TOqERusi9EyTWJfL-KQaIdeSbRNBh_vvPCIJhMp34QBLfTIflrjKZjPwzuPC8Mw0_hrb8fkpcq6WRs4In5vInv-b5nqH_BTkpY

## 4. Patrones de Diseño Aplicados

Este sistema implementa tres patrones de diseño fundamentales, uno de cada tipo (creacional, estructural y de comportamiento), tal como exige el taller.

### 4.1 Patrón Estructural: Decorator

**Propósito:** Permite agregar responsabilidades adicionales a un objeto de forma dinámica, sin modificar su estructura original.

**Implementación:**
- `MenuItem`: Interfaz base.
- `PlatoBase`: Implementación básica de un plato.
- `ExtraQueso`, `EmpaqueParaLlevar`: Decoradores que modifican la descripción y el precio del plato original.

**Ventajas:**
- Sigue el principio abierto/cerrado (OCP).
- Permite agregar múltiples combinaciones de extras sin herencia múltiple.

---

### 4.2 Patrón de Comportamiento: State

**Propósito:** Permite que un objeto altere su comportamiento cuando cambia su estado interno.

**Implementación:**
- `EstadoPedido`: Interfaz del estado.
- `EstadoRecibido`, `EstadoEnPreparacion`, `EstadoListo`, `EstadoEntregado`: Estados concretos que implementan la transición entre fases del pedido.
- La clase `Order` mantiene una referencia al estado actual y delega el cambio de comportamiento.

**Ventajas:**
- Separa la lógica específica de cada estado.
- El código es más fácil de extender y mantener.

---

### 4.3 Patrón de Comportamiento: Observer

**Propósito:** Permite que múltiples objetos escuchen y reaccionen a los cambios en otro objeto sin acoplarse fuertemente.

**Implementación:**
- `Observador`: Interfaz para observadores.
- `ClienteObservador`: Implementación que recibe notificaciones.
- `Order`: Actúa como sujeto. Al cambiar de estado, notifica a sus observadores registrados.

**Ventajas:**
- Desacopla el código del pedido y del observador.
- Permite múltiples suscriptores si se desea escalar la solución.

---

Estos patrones ayudan a mantener el sistema escalable, flexible y organizado, en línea con los principios SOLID y la arquitectura orientada a objetos.


## 5. Funcionalidades del Sistema

El sistema permite al usuario interactuar desde una consola mediante un menú textual, ofreciendo una experiencia completa de gestión de pedidos en un restaurante.

### 5.1 Menú Principal del Sistema

```
=== SISTEMA DE PEDIDOS - RESTAURANTE ===
1. Ver menú
2. Agregar plato al menú
3. Crear nuevo pedido
4. Agregar plato a un pedido
5. Avanzar estado de un pedido
6. Ver detalle de un pedido
7. Salir
```

---

### 5.2 Funciones disponibles

- **Ver Menú**: Muestra todos los platos actualmente registrados en el sistema.
- **Agregar Plato al Menú**: Permite registrar un nuevo `PlatoBase` indicando nombre, precio y descripción.
- **Crear Pedido**: Solicita los datos del cliente y genera un nuevo pedido con ID único.
- **Agregar Ítem a un Pedido**: Permite seleccionar un pedido existente y añadir un plato del menú.
- **Avanzar Estado del Pedido**: Cambia el estado del pedido entre: Recibido → En preparación → Listo → Entregado.
- **Ver Detalle del Pedido**: Muestra la información completa del pedido: cliente, ítems, precios, estado y total.
- **Notificaciones**: Al cambiar el estado, el sistema notifica automáticamente al cliente gracias al patrón Observer.

---

### 5.3 Ejemplo de ejecución

```
Nombre del cliente: Valentina
Dirección (opcional): Cra 12 #34-56
Teléfono (opcional): 3001234567
Pedido creado con ID: 1

[Notificación para Valentina] El pedido #1 cambió a estado: En preparación

Pedido #1 para Valentina - Estado: En preparación
  - Pizza Margarita | $27,000 | Pizza con tomate, mozzarella y albahaca + extra queso (Empaque para llevar)
  - Limonada | $8,000 | Bebida natural con hielo
Total: $35,000
```

---

Estas funcionalidades permiten simular la operación básica de un restaurante y probar la interacción entre todos los componentes del sistema.


## 6. Justificación de Decisiones Técnicas

Durante el diseño e implementación del sistema, se tomaron decisiones estratégicas basadas en principios sólidos de ingeniería de software y buenas prácticas.

### 6.1 Elección de Arquitectura en Capas

Se optó por una arquitectura en capas para separar claramente la lógica de presentación, la lógica de aplicación y la lógica de dominio. Esto permite:

- Mantenimiento más sencillo.
- Posibilidad de reusar servicios desde otros entornos (por ejemplo, una futura interfaz web).
- Pruebas unitarias más efectivas al aislar componentes.

---

### 6.2 Uso de Decoradores para Composición de Platos

En lugar de crear una clase por cada combinación posible de plato con extras, se usó el patrón **Decorator**, lo que permitió:

- Agregar dinámicamente funcionalidades como "extra queso" o "empaque para llevar".
- Evitar la explosión de subclases.
- Mantener abierto el sistema para extensión, pero cerrado para modificación (OCP).

---

### 6.3 Control de Estado con Patrón State

El patrón **State** permite encapsular el comportamiento asociado a cada estado de un pedido. Esto:

- Elimina múltiples condicionales del tipo `if estado == "X"`.
- Centraliza la lógica de transición entre estados en sus respectivas clases.
- Facilita la incorporación de nuevos estados en el futuro sin modificar la clase `Order`.

---

### 6.4 Desacoplamiento con el Patrón Observer

La lógica de notificación al cliente se desacopló usando **Observer**, permitiendo:

- Agregar múltiples observadores si se desea notificar a más de un actor.
- Mantener la clase `Order` libre de responsabilidades específicas de notificación.
- Preparar el sistema para extensiones como envío de correos, logs, o mensajes externos.

---

### 6.5 Aplicación de Principios SOLID

- **SRP**: Cada clase tiene una única responsabilidad bien definida.
- **OCP**: Nuevas funcionalidades se agregan mediante extensiones (por ejemplo, nuevos decoradores).
- **LSP**: Los estados concretos pueden reemplazar a la interfaz `EstadoPedido` sin romper el sistema.
- **ISP**: Interfaces como `MenuItem` y `Observador` son pequeñas y específicas.
- **DIP**: `OrderService` y `MenuService` dependen de abstracciones del dominio, no de implementaciones directas.

Estas decisiones técnicas aseguran un sistema flexible, mantenible, escalable y fácil de entender por otros desarrolladores.


## 7. Instrucciones para Ejecutar el Sistema
### 7.1 Estructura del Proyecto

Asegurese de que su proyecto esté ubicado en una ruta similar a:

```
~/Documentos/ADS/
```

Y que contenga la siguiente estructura:

```
ADS/
├── main.py
├── com/
    └── restaurant/
        ├── ui/
        ├── application/
        └── domain/
            └── model/
```

---

### 7.3 Ejecutar el Sistema

1. Abra una terminal y navegue al directorio raíz del proyecto:

```bash
cd ~/Documentos/ADS
```

2. Ejecute el sistema con:

```bash
python3 main.py
```

---

### 7.4 Uso del Programa

Una vez ejecutado, vera el menú principal del sistema:

```
=== SISTEMA DE PEDIDOS - RESTAURANTE ===
1. Ver menú
2. Agregar plato al menú
3. Crear nuevo pedido
4. Agregar plato a un pedido
5. Avanzar estado de un pedido
6. Ver detalle de un pedido
7. Salir
```

Seleccione una opción numérica para interactuar con el sistema. Cada operación será guiada paso a paso desde la consola.

---
