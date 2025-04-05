'''Crear una  clase Factura que simule el proceso de facturación de una  venta. Los 
estudiantes deberán encapsular  los datos  internos de  la factura  (como  los 
detalles de los productos, cantidades, precios y descuentos) y proveer métodos 
para calcular el total de la venta, generar rep ortes simples y validar la integridad 
de la información. Este ejercicio enfatiza la importancia de ocultar la 
implementación interna y de diseñar interfaces claras y seguras  para la gestión 
de transacciones comerciales.'''

from clase_factura import Factura

def main():
    factura = Factura()
    print("\n--Bienvenido al sistema de facturación--\n")
    while True:
        nombre = input("\nIngrese el nombre del producto: ")
        
        try:
            cantidad = int(input("\nCantidad del producto: "))
            precio = float(input("\nPrecio del producto($): "))
            factura.agregar_producto(nombre, cantidad, precio)
            print("\n✔ Producto agregado.")
        except ValueError:
            print("\nError. Inténtelo de nuevo.")
            continue
        
        continuar = input("\n¿Desea agregar otro producto? (s/n): ")
        if continuar not in ["si", "sí", "s"]:
            break
        
    try:
        descuento = float(input("\nIngrese el porcentaje de descuento que desea agregar (0-100):"))
        factura.descuento(descuento)
    except ValueError:
        print("\nDescuento inválido. No se aplicará ninguno.")
        
    if factura.validador():
        factura.reporte()
    else:
        print("\nEror: Hay productos con datos inválidos.")
        
if __name__ == '__main__':
    main()