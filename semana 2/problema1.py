'''
Simulación de gestión de inventario en una tienda
'''

lista_menu = []

def menu():
    print("\n--Menú--")
    print("1. Agregar un producto")
    print("2. Eliminar un producto")
    print("3. Modificar un producto")
    print("4. Consultar un producto")
    print("5. Mostrar todos los productos")
    print("6. Salida")

def agregar_productos(lista_menu):
    cantidad = int(input("\nIngrese cuantos productos desea agregar: "))
    for _ in range(cantidad):
        nombre = input("\nIngrese el nombre del producto: ")
        while True:
            try:
                codigo = int(input("\nIngrese el código del producto: "))
                break
            except ValueError:
                print("\nEl código debe de ser un número entero.")
        precio = float(input("\nIngrese el precio del producto: "))
        cantidad_productos = int(input("\nIngrese la cantidad del producto: "))
        lista_menu.append((nombre, codigo, precio, cantidad_productos))
        print("Producto agregado correctamente.")

def eliminar_productos(lista_menu):
    nombre = input("\nIngrese el nombre del producto que desea eliminar: ")
    for producto in lista_menu:
        if producto[0] == nombre:  # Comparación directa por nombre
            lista_menu.remove(producto)
            print(f"\nEl producto '{nombre}' ha sido eliminado correctamente.")
            return
    print(f"\nEl producto '{nombre}' no ha sido encontrado.")

def modificar_productos(lista_menu):
    nombre = input("\nIngrese el nombre del producto que desea modificar: ")
    for i, producto in enumerate(lista_menu):
        if producto[0] == nombre:  # Compara directamente el nombre
            while True:
                print("\n1. Modificar nombre")
                print("2. Modificar código")
                print("3. Modificar precio")
                print("4. Modificar cantidad")
                print("5. Finalizar modificación")  # Opción para salir del bucle
                opcion = input("\nSeleccione qué desea modificar: ")

                nuevo_nombre = producto[0]
                codigo = producto[1]
                precio = producto[2]
                cantidad = producto[3]

                if opcion == '1':
                    nuevo_nombre = input("\nIngrese el nuevo nombre: ")
                elif opcion == '2':
                    codigo = int(input("\nIngrese el nuevo código: "))
                elif opcion == '3':
                    precio = float(input("\nIngrese el nuevo precio: "))
                elif opcion == '4':
                    cantidad = int(input("\nIngrese la nueva cantidad: "))
                elif opcion == '5':
                    print("\nTodos los cambios han sido guardados.")
                    return
                else:
                    print("\nOpción no válida. Intente de nuevo.")
                    continue

                lista_menu[i] = (nuevo_nombre, codigo, precio, cantidad)
                print("\nProducto modificado correctamente.")
            return
    print(f"\nProducto '{nombre}' no ha sido encontrado.")

def consultar_productos(lista_menu):
    nombre = input("\nIngrese el nombre del producto que desea consultar: ")
    for producto in lista_menu:
        if producto[0] == nombre:
            print(f"\nProducto encontrado:\nNombre: {producto[0]}, Código: {producto[1]}, Precio: {producto[2]}, Cantidad: {producto[3]}")
            return
    print(f"\nEl producto '{nombre}' no ha sido encontrado.")

def mostrar_productos(lista_menu):
    if not lista_menu:
        print("\nNo hay productos en el inventario.")
    else:
        print("\nInventario de productos:")
        for producto in lista_menu:
            print(f"Nombre: {producto[0]}, Código: {producto[1]}, Precio: {producto[2]}, Cantidad: {producto[3]}")
            print("-" * 40)

def main():
    while True:
        menu()
        opcion = input("Seleccione una de las siguientes opciones: ")
        if opcion == '1':
            agregar_productos(lista_menu)
        elif opcion == '2':
            eliminar_productos(lista_menu)
        elif opcion == '3':
            modificar_productos(lista_menu)
        elif opcion == '4':
            consultar_productos(lista_menu)
        elif opcion == '5':
            mostrar_productos(lista_menu)
        elif opcion == '6':
            print("Saliendo del menú. ¡Tenga un buen día usuario!")
            break
        else:
            print("Opción inválida, por favor inténtelo de nuevo.")

if __name__ == "__main__":
    main()
