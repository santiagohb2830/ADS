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

                      +----------------+
                      |   MenuItem     |<-----------------------------+
                      +----------------+                              |
                      | +get_nombre()  |                              |
                      | +get_precio()  |                              |
                      | +get_desc()    |                              |
                      +----------------+                              |
                              ^                                        |
                              |                                        |
                   +---------------------+                             |
                   |     PlatoBase       |                             |
                   +---------------------+                             |
                   | -nombre             |                             |
                   | -precio             |                             |
                   | -descripcion        |                             |
                   +---------------------+                             |
                              ^                                        |
                              |                                        |
                   +---------------------------+     +-----------------------------+
                   |     MenuItemDecorator     |<----|     ExtraQueso              |
                   +---------------------------+     +-----------------------------+
                   | -menu_item: MenuItem      |     | +get_precio(), +get_desc()  |
                   +---------------------------+     +-----------------------------+
                              ^                              +-----------------------------+
                              |                              | EmpaqueParaLlevar           |
                              |                              +-----------------------------+
                                                             
                      +------------------+       uses        +------------------+
                      |     Order        |------------------>|    Customer      |
                      +------------------+                   +------------------+
                      | -items: MenuItem[]                   | -id, nombre...   |
                      | -estado: EstadoPedido                +------------------+
                      +------------------+
                              |
                              | has a
                              v
                  +--------------------------+
                  |     EstadoPedido         |<-----------------------------+
                  +--------------------------+                              |
                  | +avanzar_estado()        |                              |
                  +--------------------------+                              |
                    ^         ^         ^         ^                         |
                    |         |         |         |                         |
     +----------------+ +----------------------+ +----------------+ +--------------------+
     | EstadoRecibido | | EstadoEnPreparacion  | | EstadoListo    | | EstadoEntregado   |
     +----------------+ +----------------------+ +----------------+ +--------------------+

                   +-------------------------+
                   |      Observador         |<------------------+
                   +-------------------------+                   |
                   | +actualizar(pedido,msg) |                   |
                   +-------------------------+                   |
                             ^                                   |
                             |                                   |
                    +------------------------+                   |
                    |   ClienteObservador    |--------------------+
                    +------------------------+
```

Este diagrama refleja el uso de los patrones Decorator, State y Observer, y cómo se integran para representar el dominio del problema de forma modular, escalable y extensible.


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

