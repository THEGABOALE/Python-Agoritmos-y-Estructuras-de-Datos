class Pila:
    def __init__(self):
        self.lista = []
    def estaVacia(self):
        return self.lista == []
    def agregar(self, elemento):
        self.lista.append(elemento)
    def extraer(self):
        return self.lista.pop()
    def imprimir(self):
        return self.lista
    def tamaño(self):
        return len(self.lista)