class Llamada:
    def __init__(self, nombre, motivo):
        self.nombre = nombre
        self.motivo = motivo

    def __str__(self):
        return f"{self.nombre} - Motivo: {self.motivo}"

class CallCenter:
    def __init__(self):
        self.llamadas = []

    def agregar_llamada(self, nombre, motivo):
        llamada = Llamada(nombre, motivo)
        self.llamadas.append(llamada)
        print(f"Llamada agregada: {llamada}")

    def atender_llamada(self):
        if self.llamadas:
            llamada = self.llamadas.pop(0)
            print(f"Atendiendo llamada de {llamada.nombre} - Motivo: {llamada.motivo}")
        else:
            print("No hay llamadas en espera.")

    def mostrar_cola(self):
        if self.llamadas:
            print("\nLlamadas en espera:")
            for i, llamada in enumerate(self.llamadas, start=1):
                print(f"{i}. {llamada}")
        else:
            print("\nNo hay llamadas en la cola.")