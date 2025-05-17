from cola import Microprocesador

def menu():
    cpu = Microprocesador()

    while True:
        print("\n "+"=" * 25)
        print("Simulación de Microprocesador")
        print("=" * 25)
        print("1. Agregar proceso")
        print("2. Ejecutar proceso")
        print("3. Mostrar procesos pendientes")
        print("4. Salir")
        print("=" * 25)
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == '1':
            identificador = input("ID del proceso: ")
            nombre = input("Nombre del proceso: ")
            duracion = input("Duración estimada (ms): ")
            if duracion.isdigit():
                cpu.agregar_proceso(identificador, nombre, int(duracion))
            else:
                print("Duración inválida.")
        elif opcion == '2':
            cpu.ejecutar_proceso()
        elif opcion == '3':
            cpu.mostrar_procesos_pendientes()
        elif opcion == '4':
            print("Saliendo del simulador...")
            break
        else:
            print("Opción no válida.")
