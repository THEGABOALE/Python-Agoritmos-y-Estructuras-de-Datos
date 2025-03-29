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
        cantidad = int(input())
        for i in range(cantidad):
            try:
                nombre = input("\nIngrese el nombre del producto: ")
                codigo = int(input("\nIngrese el código del producto: "))
                precio = float(input("\nIngrese el precio del producto: "))
            except ValueError: print("\nError. Ingrese los datos de nuevo.")

def eliminar_productos(lista_menu):
        producto = input("\nIngrese el producto que desea eliminar: ")
        if producto in lista_menu:
            lista_menu.remove(producto)
            print(f"{producto} eliminado correctamente")
        else:
            print(f"{producto} no encontrado.")

def modificar_productos(lista_menu):
    producto = input("\nIngrese el nombre del producto que desea modificar: ")
    for producto in lista_menu:
        print("1. Modificar nombre del producto")
        print("2. Modificar código del producto")
        print("3. Modificar precio del producto")
        opciones = input("\nSeleccione que desea modificar: ")
        if opciones == '1':
            producto['nombre'] = input("\nIngrese el nuevo nombre del producto: ")
        elif opciones == '2':
            producto['codigo'] = int(input("\nIngrese el nuevo código del producto: "))
        elif opciones == '3':
            producto['precio'] = float(input("\nIngrese el nuevo precio del producto: "))
        print("Producto modificado correctamente.")
        return
    print("\nEl producto que quiere modificar no existe.")    

def consultar_productos(lista_menu):
    producto = input("\nIngrese el nombre del producto que desea consultar: ")
    for producto in lista_menu:
        if producto['nombre'] == producto:
            print("\nSu producto ha sido encontrado: {producto}")
            return
    print("\nProducto no encontrado.")
            
def mostrar_productos(lista_menu):



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
        print("Saliendo del menú. ¡Tenga un buen día!")
        break
    else:
        print("Opción inválida, por favor inténtelo de nuevo.")