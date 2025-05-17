from cola import Impresora

def menu():
    impresora = Impresora()
    while True:
        print("-----------------------------")
        print("\nMENÚ DE IMPRESIÓN\n")
        print("1. Enviar documento a imprimir")
        print("2. Imprimir siguiente documento")
        print("3. Ver cola de impresión")
        print("4. Salir")
        print("-----------------------------")

        try: 
            opcion = int(input("\nSeleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
        
        if opcion == 1:
            nombre = input("Ingrese el nombre del documento: ")
            usuario = input("Usuario que lo envía: ")
            paginas = int(input("Ingrese el número de páginas: "))
            impresora.agregar(nombre, paginas, usuario)
        elif opcion == 2:
            impresora.imprimir_documento()
        elif opcion == 3:
            impresora.mostrar_cola()
        elif opcion == 4:
            print("Saliendo del menú de impresión...")
            break
        else:
            print("Opción no válida, favor intentarlo de nuevo.")