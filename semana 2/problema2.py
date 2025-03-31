'''Gestión de cuenta bancaria'''

lista = []



def main():
    while True:
        opcion = input("Seleccione una de las siguientes opciones: ")
        if opcion == '1':
            consultar_saldo(lista)
        elif opcion == '2':
            depositar_dinero(lista)
        elif opcion == '3':
            retirar_dinero(lista)
        elif opcion == '4':
            print("Salienda de su cuenta bancaria...")
            break
        else:
            print("Opción inválida, por favor inténtelo de nuevo.")