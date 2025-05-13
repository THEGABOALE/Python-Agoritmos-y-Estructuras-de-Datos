class Pila:
    def __init__(self):
        self.panes = []

    def agregarPanes(self, pan):
        self.panes.append(pan)
    
    def venderPan(self):
        if self.panes:
            return self.panes.pop()
        else:
            return None
        
    def mostrarPanes(self):
        if self.panes:
            print("Panes en la pila:")
            print(self.panes)
        else:
            print("No hay panes en la pila.")