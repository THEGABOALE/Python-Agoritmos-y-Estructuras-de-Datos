class Pedido:
    def __init__(self, cliente, productos):
        self.__cliente = cliente
        self.__productos = productos
        self.total, self.descuento = self.calculartotal()

    def calculartotal(self):
        subtotal = sum(precio for _, precio in self.__productos)
        descuento = subtotal * self.__cliente.obtenerDescuento()
        total = subtotal - descuento
        return total, descuento

    def detalles(self):
        print(f"Cliente: {self.__cliente.nombre} (ID: {self.__cliente.id})")
        print(f"Tipo de cliente: {self.__cliente.tipo()}")
        print("\nProductos:")
        for nombre, precio in self.__productos:
            print(f" - {nombre}: ${precio:.2f}")
        print(f"\nDescuento aplicado: ${self.descuento:.2f}")
        print(f"Total con descuento aplicado: ${self.total:.2f}")