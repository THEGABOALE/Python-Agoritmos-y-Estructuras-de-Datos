from cola import CallCenter

def menu():
    cc = CallCenter()

    while True:
        print("\n--- Call Center ---")
        print("1. Agregar llamada")
        print("2. Atender llamada")
        print("3. Ver cola de llamadas")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre del cliente: ")
            motivo = input("Motivo de la llamada: ")
            cc.agregar_llamada(nombre, motivo)
        elif opcion == '2':
            cc.atender_llamada()
        elif opcion == '3':
            cc.mostrar_cola()
        elif opcion == '4':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida.")
