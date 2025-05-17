from cola import ServidorArchivos

def menu():
    servidor = ServidorArchivos()

    while True:
        print("\n" + "=" * 30)
        print("SERVIDOR DE ARCHIVOS")
        print("=" * 30)
        print("1. Registrar nueva solicitud de acceso")
        print("2️. Atender solicitud")
        print("3️. Ver solicitudes pendientes")
        print("4️. Salir del sistema")
        print("-" * 30)
        
        opcion = input("\nSeleccione una opción (1-4): ")

        if opcion == '1':
            print("\nNueva solicitud")
            usuario = input("Nombre del usuario: ")
            archivo = input("Nombre del archivo: ")
            servidor.registrar_solicitud(usuario, archivo)

        elif opcion == '2':
            print("\nAtendiendo solicitud...")
            servidor.atender_solicitud()

        elif opcion == '3':
            print("\nLista de solicitudes pendientes")
            servidor.mostrar_solicitudes_pendientes()

        elif opcion == '4':
            print("\nCerrando sistema... ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")