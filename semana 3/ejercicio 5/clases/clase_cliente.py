class Cliente:
    def __init__(self, id, nombre, contacto):
        self.id = id
        self.nombre = nombre
        self.contacto = contacto

    def obtenerDescuento(self):
        return 0.0  # Cliente normal no tiene descuento
    
    def tipo(self):
        return "Cliente Regular"
    