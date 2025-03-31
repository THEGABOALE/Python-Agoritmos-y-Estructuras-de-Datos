'''Gestión de cuenta bancaria'''

saldo = 0

while True:
    print("\nMenú de opciones:")
    print("1. Consultar saldo")
    print("2. Depositar saldo")
    print("3. Retirar dinero")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        print(f"Su saldo actual es: {saldo:.2f}")
    elif opcion == '2':
        try:
            deposito = float(input("Ingrese la cantidad a depositar: "))
            if deposito > 0:
                saldo += deposito
                print(f"Depósito exitoso. Su nuevo saldo ahora es: {saldo:.2f}")
            else:
                print("La cantidad a depositar debe ser mayor a 0.")
        except:
            print("La entrada no es válida.")
    elif opcion == '3':
        try:
            retiro = float(input("Ingrese la cantidad retirar: "))
            if retiro > 0:
                if retiro <= saldo:
                    saldo -= retiro
                    print(f"Retiro exitoso. Su nuevo saldo ahora es: {saldo:.2f}")
                else:
                    print("Saldo insuficiente.")
            else:
                print("La cantidad debe ser mayor a cero.")
        except ValueError:
            print("La entrada no es válida.")
    elif opcion == '4':
        print("Saliendo de cuenta bancaria...")
        print("¡Que tenga un buen día usuario!")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")
        
        
