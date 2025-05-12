'''Programa de atención al cliente'''

class Clinica:
    def __init__(self):
        self.pacientes = []
    
    def registrar(self, nombre):
        self.pacientes.append(nombre)
        
    def atender(self):
        if self.pacientes:
            atendido = self.pacientes.pop(0)
            print(f'\nEl paciente {atendido} ha sido atentido.')
        else:
            print("\nNo hay pacientes en la lista de espera.")
    
    def imprimir(self):
        if self.pacientes:
            print("\nLista de pacientes en espera de atención")
            for i, paciente in enumerate(self.pacientes, start = 1):   
                print(f"{i}. {paciente}")
        else:
            print("\nNo hay pacientes en la lista de espera.")

def menu():
    clinica = Clinica()
    while True:
        print("\n--Menú principal--\n")
        print("1. Registrar")
        print("2. Atender")
        print("3. Imprimir")
        print("4. Salir")
        
        opcion = int(input("\nSeleccione una de las siguientes opciones: "))
        
        if opcion == 1:
            nombre = input("\nIngrese el nombre del paciente: ")
            clinica.registrar(nombre)
        elif opcion == 2:
            clinica.atender()
        elif opcion == 3:
            clinica.imprimir()
        elif opcion == 4:
            print("\nSaliendo de la clínica... ¡Vuelva pronto!")
            break
        else:
            print("\nVuelva a intentarlo nuevamente, favor seleccionar una opción válida.")

if __name__ == '__main__':
    menu()