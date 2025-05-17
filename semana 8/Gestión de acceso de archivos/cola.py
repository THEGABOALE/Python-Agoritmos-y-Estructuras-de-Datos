class Solicitud:
    def __init__(self, usuario, archivo):
        self.usuario = usuario
        self.archivo = archivo

    def __str__(self):
        return f"{self.usuario} → {self.archivo}"

class ServidorArchivos:
    def __init__(self):
        self.solicitudes = []

    def registrar_solicitud(self, usuario, archivo):
        solicitud = Solicitud(usuario, archivo)
        self.solicitudes.append(solicitud)
        print(f"Solicitud registrada: {solicitud}")

    def atender_solicitud(self):
        if self.solicitudes:
            solicitud = self.solicitudes.pop(0)
            print(f"Acceso concedido a '{solicitud.usuario}' para el archivo '{solicitud.archivo}'")
        else:
            print("No hay solicitudes pendientes.")

    def mostrar_solicitudes_pendientes(self):
        if self.solicitudes:
            print("\nSolicitudes pendientes:")
            for i, solicitud in enumerate(self.solicitudes, start=1):
                print(f"{i}. {solicitud}")
        else:
            print("\nNo hay solicitudes pendientes.")
