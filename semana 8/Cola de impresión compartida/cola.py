class Documento:
    def __init__(self, nombre, paginas, usuario):
        self.nombre = nombre
        self.paginas = paginas 
        self.usuario = usuario
        
    def __str__(self):
        return f"{self.nombre} (Usuario: {self.usuario}, Páginas: {self.paginas})"
    
class Impresora:
    def __init__(self):
        self.documentos = []
    
    def agregar(self, nombre, paginas, usuario):
        documento = Documento(nombre, paginas, usuario)
        self.documentos.append(documento)
        print(f"Documento agregado correctamente a la cola: {documento}")
    
    def imprimir_documento(self):
        if self.documentos:
            documento = self.documentos.pop(0)
            print(f"Imprimiendo documento: {documento}")
        else:
            print("No hay documentos en la cola de impresión.")
    
    def mostrar_cola(self):
        if self.documentos:
            print("Documentos en la cola de impresión: ")
            for i, doc in enumerate(self.documentos, start=1):
                print(f"{i}. {doc}")
        else:
            print("La cola de impresión está vacía.")