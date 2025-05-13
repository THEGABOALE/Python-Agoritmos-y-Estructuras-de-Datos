from Pila import Pila
pila = Pila()

while True:
    print("1. Agregar pan")
    print("2. Vender pan")
    print("3. Mostrar pan")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        pan = input("Ingrese el nombre del pan: ")
        pila.agregarPanes(pan)
    elif opcion == 2:
        panVendido = pila.venderPan()
        if panVendido:
            print(f"Pan vendido: {panVendido}")
        else:
            print("No hay panes para vender.")
    elif opcion == 3:
        pila.mostrarPanes()
    elif opcion == 4:
        break
    else:
        print("Opción no válida. Intente de nuevo.")