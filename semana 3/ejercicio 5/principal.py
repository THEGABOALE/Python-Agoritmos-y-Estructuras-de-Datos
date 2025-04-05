'''Crear una clase Cliente con atributos básicos (por  ejemplo, ID, nombre y 
contacto) y una  clase Pedido que  contenga información sobre el cliente,  la lista 
de productos solicitados y el total de la venta. Se podrá incluir el uso de herencia 
para diferenciar entre tipos de clientes (por ejemplo, cliente regular y cliente VIP) 
y aplicar descuentos especiales, demostrando el uso de la herencia y el 
polimorfismo para adaptar el  comportamiento de  los  objetos según  el  tipo  de 
cliente.'''

from clases import Cliente, ClienteVIP, Pedido

def main():
    print("\n--Registro de Clientes--")
    id = int(input("\nIngrese el ID del cliente: "))
    nombre = input("\nIngrese el nombre del cliente: ")
    contacto = input("\nIngrese el contacto del cliente: ")
    tipo_cliente = input("\nEl cliente es VIP o no?: ")
    
    if tipo_cliente in ["si", "sí", "s"]:
        cliente = ClienteVIP(id, nombre, contacto)
    else:
        cliente = Cliente(id, nombre, contacto)
        
    print("\n--Ingreso de Productos--")
    productos = []
    while True:
        nombre_producto = input("\nIngrese el nombre del producto: ")
        if not nombre_producto:
            print("\nEl nombre del producto no puede estar vacío.")
            continue
        
        try:
            precio_producto = float(input("\nIngrese el precio del producto($): "))
            if precio_producto < 0:
                print("\nEl precio del producto no puede ser negativo.")
                continue
            productos.append((nombre_producto, precio_producto))
        except ValueError:
            print("\nError: Ingresa un precio válido.")
            continue
        
        seguir = input("\n¿Desea ingresar otro producto? (sí/no): ")
        if seguir not in ["si", "sí", "s"]:
            break
        
    pedido = Pedido(cliente, productos)
    print("\n--Detalles del pedido--")
    pedido.detalles()
    
if __name__ == '__main__':
    main()
    