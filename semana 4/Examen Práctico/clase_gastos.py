class Gasto:
    def __init__(self, fecha, categoria, monto, descripcion):
        self.__fecha = fecha
        self.__categoria = categoria
        self.__monto = monto
        self.__descripcion = descripcion
    
    def __str__(self):
        return f"Fecha: {self.__fecha} | Categoría: {self.__categoria} | Monto: ${self.__monto} | Descripción: {self.__descripcion}"
    
    def get_monto(self):
        return self.__monto

    def get_categoria(self):
        return self.__categoria