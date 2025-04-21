# com/restaurant/ui/restaurant_console_app.py

from com.restaurant.application.menu_service import MenuService
from com.restaurant.application.order_service import OrderService
from com.restaurant.domain.model.cliente_observador import ClienteObservador
from com.restaurant.domain.model.customer import Customer

class RestaurantConsoleApp: 
    
    def __init__(self):
        self.menu_service = MenuService()
        self.order_service = OrderService()
        self.pedidos = {}  # id: Order

    def opcion_crear_pedido(self):
        nombre_cliente = input("Nombre del cliente: ")
        direccion = input("Dirección (opcional): ")
        telefono = input("Teléfono (opcional): ")
        id_cliente = str(len(self.pedidos) + 1)

        # Aquí creas el objeto cliente
        cliente = Customer(id_cliente, nombre_cliente, direccion, telefono)

        # Y pasas el objeto, no el string
        pedido = self.order_service.crear_pedido(cliente)

        observador = ClienteObservador(cliente.get_nombre())
        pedido.agregar_observador(observador)

        self.pedidos[pedido.id] = pedido
        print(f"Pedido creado con ID: {pedido.id}")




    def mostrar_menu_principal(self):
        while True:
            print("\n=== SISTEMA DE PEDIDOS - RESTAURANTE ===")
            print("1. Ver menú")
            print("2. Agregar plato al menú")
            print("3. Crear nuevo pedido")
            print("4. Agregar plato a un pedido")
            print("5. Avanzar estado de un pedido")
            print("6. Ver detalle de un pedido")
            print("7. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.menu_service.mostrar_menu()
            elif opcion == "2":
                self.opcion_agregar_plato()
            elif opcion == "3":
                self.opcion_crear_pedido()
            elif opcion == "4":
                self.opcion_agregar_item_a_pedido()
            elif opcion == "5":
                self.opcion_avanzar_estado()
            elif opcion == "6":
                self.opcion_ver_detalle_pedido()
            elif opcion == "7":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida.")

    def opcion_agregar_plato(self):
        nombre = input("Nombre del plato: ")
        precio = float(input("Precio: "))
        descripcion = input("Descripción: ")
        self.menu_service.agregar_plato(nombre, precio, descripcion)

    def opcion_crear_pedido(self):
        nombre_cliente = input("Nombre del cliente: ")
        pedido = self.order_service.crear_pedido(nombre_cliente)
        observador = ClienteObservador(nombre_cliente)
        pedido.agregar_observador(observador)
        self.pedidos[pedido.id] = pedido
        print(f"Pedido creado con ID: {pedido.id}")

    def opcion_agregar_item_a_pedido(self):
        try:
            pedido_id = int(input("ID del pedido: "))
            pedido = self.pedidos.get(pedido_id)
            if not pedido:
                print("Pedido no encontrado.")
                return
            self.menu_service.mostrar_menu()
            index = int(input("Seleccione el número del plato: ")) - 1
            item = self.menu_service.obtener_menu()[index]
            pedido.agregar_item(item)
            print("Plato agregado al pedido.")
        except Exception as e:
            print(f"Error: {e}")

    def opcion_avanzar_estado(self):
        try:
            pedido_id = int(input("ID del pedido: "))
            pedido = self.pedidos.get(pedido_id)
            if not pedido:
                print("Pedido no encontrado.")
                return
            pedido.avanzar_estado()
        except Exception as e:
            print(f"Error: {e}")

    def opcion_ver_detalle_pedido(self):
        try:
            pedido_id = int(input("ID del pedido: "))
            pedido = self.pedidos.get(pedido_id)
            if not pedido:
                print("Pedido no encontrado.")
                return
            print(pedido.get_detalle())
        except Exception as e:
            print(f"Error: {e}")
