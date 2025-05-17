class Proceso:
    def __init__(self, identificador, nombre, duracion):
        self.identificador = identificador
        self.nombre = nombre
        self.duracion = duracion 

    def __str__(self):
        return f"{self.identificador} - {self.nombre} ({self.duracion} ms)"

class Microprocesador:
    def __init__(self):
        self.procesos = []

    def agregar_proceso(self, identificador, nombre, duracion):
        proceso = Proceso(identificador, nombre, duracion)
        self.procesos.append(proceso)
        print(f"Proceso agregado: {proceso}")

    def ejecutar_proceso(self):
        if self.procesos:
            proceso = self.procesos.pop(0)
            print(f"Ejecutando: {proceso.nombre} | ID: {proceso.identificador} | Duración: {proceso.duracion} ms")
        else:
            print("No hay procesos en la cola.")

    def mostrar_procesos_pendientes(self):
        if self.procesos:
            print("\nProcesos pendientes:")
            for i, proceso in enumerate(self.procesos, start=1):
                print(f"{i}. {proceso}")
        else:
            print("\nNo hay procesos pendientes.")