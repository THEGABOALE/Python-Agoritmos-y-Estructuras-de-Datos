class Paciente:
    def __init__(self, nombre, servicio):
        self.nombre = nombre
        self.servicio = servicio

    def __str__(self):
        return f"{self.nombre} - Servicio: {self.servicio}"

class Farmacia:
    def __init__(self):
        self.pacientes = []

    def registrar_paciente(self, nombre, servicio):
        paciente = Paciente(nombre, servicio)
        self.pacientes.append(paciente)
        print(f"Paciente registrado: {paciente}")

    def atender_paciente(self):
        if self.pacientes:
            paciente = self.pacientes.pop(0)
            print(f"Atendiendo a {paciente.nombre} - Servicio: {paciente.servicio}")
        else:
            print("No hay pacientes en espera.")

    def mostrar_turnos_pendientes(self):
        if self.pacientes:
            print("\nTurnos pendientes:")
            for i, paciente in enumerate(self.pacientes, start=1):
                print(f"{i}. {paciente}")
        else:
            print("\nNo hay turnos pendientes.")