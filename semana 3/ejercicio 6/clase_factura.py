from datetime import datetime #Importo datetime para poner la fecha y hora en la factura

class Factura:
    def __init__(self):
        self.__productos = [] #Lista privada de productos
        self.__descuento = 0.0
    
    def agregar_producto(self, nombre, cantidad, precio):
        if cantidad <= 0 or precio <= 0:
            print("\nCantidad y precio deben de ser mayor a 0. Inténtelo de nuevo.")
            return
        producto = {
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio
        } 
        self.__productos.append(producto)
        
    def descuento(self, porcentaje):
        if 0 <= porcentaje <= 100:
            self.__descuento = porcentaje / 100
        else:
            print("\nError: El descuento debe de estar entre 0 y 100")
            
    def calcular_total(self):
        subtotal = sum(p["cantidad"] * p["precio"] for p in self.__productos)
        total = subtotal * (1 - self.__descuento)
        return round(total, 2)
    
    def reporte(self):
        #Obtener la fecha y hora actual con formato día/mes/año horas:minutos:segundos
        hora_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("=" * 40) #Separaciones
        print("FACTURA DE COMPRA".center(40)) #Ocupo center para centrar el texto
        print(f"Fecha y hora: {hora_actual}\n") #Muestra la hora y fecha en el recibo de factura
        print("-" * 40)
        print(f"{'Cant.':<6} {'Producto':<20} {'Precio':>10}") #Formateado con f-strings
        print("-" * 40)
        for p in self.__productos:
            #Formateo de cada producto
            cantidad = str(p['cantidad']).ljust(6) #Alinear el texto a la izquierda a 6 espacios
            nombre = p['nombre'].ljust(20) #Alinear el texto a la izquierda a 20 espacios
            precio = f"${p['precio']:.2f}".rjust(10) #Alinear el texto a la derecha a 10 espacios
            print(f"{cantidad}{nombre}{precio}")
        subtotal = sum(p["cantidad"] * p["precio"] for p in self.__productos)
        descuento_aplicado = int(self.__descuento * 100)
        total = self.calcular_total()
        print("-" * 40)
        #Imprimir resumen de totales
        print(f"{'Subtotal:':<30}${round(subtotal, 2):>8}") #Subtotal alineado
        print(f"{'Descuento:':<30}{descuento_aplicado:>7}%") #Descuento alineado
        print(f"{'TOTAL A PAGAR:':<30}${total:>8}") #Total alineado
        print("=" * 40)
        
    def validador(self):
        for p in self.__productos:
            if p['cantidad'] <= 0 or p['precio'] <= 0:
                return False
        return True