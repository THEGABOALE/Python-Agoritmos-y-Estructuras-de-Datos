'''Programa de atención al cliente'''

class Clinica:
    def __init__(self):
        self.pacientes = []
    
    def registrar(self, nombre):
        nombre = input("Ingrese su el nombre del paciente: ")
        self.pacientes.append(nombre)
        
    def atender(self):
        if self.pacientes:
            atendido = self.pacientes.pop(0)
            print(f'''El paciente {atendido} ha sido atentido. Vuelva pronto y más herido que gano más plata para apostarlo 
                  todo en el negro en el casino más cercano en las Vegas.''')
        else:
            print("No hay pacientes en la lista de espera.")
    
    def imprimir(self):
        if self.pacientes:
            print("Lista de pacientes en espera de atención")
            for i, paciente in enumerate(self.pacientes, start = 1):   
                print(f"{i}. {paciente}")
        else:
            print("No hay pacientes en la lista de espera.")