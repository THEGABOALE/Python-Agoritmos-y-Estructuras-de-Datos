class Cola:
    def __init__(self):
        self.lista = []
    
    def estaVacia(self):
        return len(self.lista) == 0

    def encolar(self, nombre):
        self.lista.append(nombre)
    
    def desencolar(self):
        return self.lista.pop(0)

    def verfrente(self):
        return self.lista[0]
    
    def imprimir(self):
        return self.lista

def menu():
    cola = Cola()
    
    while True:
        print("\n---Menú de opciones---\n")
        print("1. Agregar clientes")
        print("2. Atender clientes")
        print("3. Verificar si la cola está vacía")
        print("4. Ver siguiente cliente")
        print("5. Imprimir lista de clientes")
        print("6. Salir del programa")
        print("\n----------------------\n")
        
        opcion = int(input("\nSeleccione una de las siguienes opciones: \n"))
        if opcion == 1:
            if len(cola.lista) < 5:
                nombre = input("Ingrese el nombre del cliente: ")
                cola.encolar(nombre)
            else: 
                print("Cola LLena. Empiece a atender clientes si quiere agregar más.")
        elif opcion == 2:
            atendido = cola.desencolar()
            if atendido:
                print(f"El cliente {atendido} ha sido atendido.")
            else:
                print("La cola está vacía.")
        elif opcion == 3:  
            if cola.estaVacia():
                print("La cola está vacía.")
            else:
                print("La cola NO está vacía.")
        elif opcion == 4: 
            siguiente = cola.verfrente()
            if siguiente:
                print(f"El siguiente cliente en ser atendido es {siguiente}.")
            else:
                print("La cola está vacía")
        elif opcion == 5:
            cantidad = len(cola.lista)
            print("Lista de clientes en espera: ", cola.imprimir(), cantidad, " clientes esperando.")
        elif opcion == 6:
            print("Saliendo del programa.")
            break
        else:
            print("Por favor, seleccione una opción válida.")
            
if __name__ == '__main__':
    menu()