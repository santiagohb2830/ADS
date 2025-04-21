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

