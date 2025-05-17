from cola import Farmacia

def menu():
    farmacia = Farmacia()

    while True:
        print("\n---Farmacia ---")
        print("1. Registrar paciente")
        print("2. Atender siguiente paciente")
        print("3. Mostrar turnos pendientes")
        print("4. Salir")
        print("---------------")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre del paciente: ")
            servicio = input("Tipo de servicio (compra, consulta, receta): ")
            farmacia.registrar_paciente(nombre, servicio)
        elif opcion == '2':
            farmacia.atender_paciente()
        elif opcion == '3':
            farmacia.mostrar_turnos_pendientes()
        elif opcion == '4':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida.")