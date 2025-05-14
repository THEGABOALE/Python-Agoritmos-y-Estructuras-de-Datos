'''Simulación de Supermercado'''
class Supermercado:
    def __init__(self):
        self.cliente = []

    def registrar(self, nombre):
        self.cliente.append(nombre)

    def atender(self):
        if self.cliente:
            atendido = self.cliente.pop(0)
            print(f"El cliente {atendido} ha sido atendido")
        else:
            print("No hay clientes en espera")
    
    def imprimir(self):
        if self.cliente:
            print("Lista de clientes en espera de atención: ")
            for i, cliente in enumerate(self.cliente, start=1):
                print(f"{i}. {cliente}")
        else:
            print("No hay clientes en espera")

def menu():
    supermercado = Supermercado()
    while True:
        print("Programa de atencion al cliente")
        print("1. Registrar cliente")
        print("2. Atender cliente")
        print("3. Imprimir lista de clientes")
        print("4. Salir")
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            nombre = input("Ingrese el nombre del cliente: ")
            supermercado.registrar(nombre)
        elif opcion == 2:
            supermercado.atender()
        elif opcion == 3:
            supermercado.imprimir()
        elif opcion == 4:
            print("Saliendo del programa")
            break
        else:
            print("Opcion invalida, intentelo nuevamente")

if __name__ == "__main__":
    menu()
