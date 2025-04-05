from .clase_cliente import Cliente

class ClienteVIP(Cliente):
    def __init__(self, id, nombre, contacto):
        super().__init__(id, nombre, contacto)

    def obtenerDescuento(self):
        return 0.15  # Cliente VIP tiene 15% de descuento
    
    def tipo(self):
        return "Cliente VIP"
    