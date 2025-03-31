'''Gestión de cuenta bancaria'''

saldo = 0

while True:
    print("\nMenú de opciones:")
    print("1. Consultar saldo")
    print("2. Depositar saldo")
    print("3. Retirar dinero")
    print("4. Salir")
    
    opcion = input("\nSeleccione una opción: ")
    
    if opcion == '1':
        print(f"\nSu saldo actual es: ${saldo:.2f}")
    elif opcion == '2':
        try:
            deposito = float(input("\nIngrese la cantidad a depositar ($): "))
            if deposito > 0:
                saldo += deposito
                print(f"\nDepósito exitoso. Su nuevo saldo ahora es de: ${saldo:.2f}")
            else:
                print("\nLa cantidad a depositar debe ser mayor a 0.")
        except:
            print("\nLa entrada no es válida.")
    elif opcion == '3':
        try:
            retiro = float(input("\nIngrese la cantidad retirar ($): "))
            if retiro > 0:
                if retiro <= saldo:
                    saldo -= retiro
                    print(f"\nRetiro exitoso. Su nuevo saldo ahora es de: ${saldo:.2f}")
                else:
                    print("\nSaldo insuficiente.")
            else:
                print("\nLa cantidad debe ser mayor a cero.")
        except ValueError:
            print("\nLa entrada no es válida.")
    elif opcion == '4':
        print("\nSaliendo de la cuenta bancaria...")
        print("\n¡Que tenga un buen día usuario!")
        break
    else:
        print("\nOpción no válida. Inténtelo de nuevo.")