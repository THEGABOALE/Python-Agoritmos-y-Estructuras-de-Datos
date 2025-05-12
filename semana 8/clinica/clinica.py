'''Programa de atención al cliente'''

class Clinica:
    def __init__(self):
        self.pacientes = []
    
    def registrar(self, nombre):
        nombre = input("Ingrese su el nombre del paciente: ")
        self.pacientes.append(nombre)
        
        