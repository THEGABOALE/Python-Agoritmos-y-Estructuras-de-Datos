class Nodo:
    def __init__(self, dato):
        self.__dato = dato
        self.siguiente = None #None significa nulo

class ListaEnlazada:
    def __init__(self):
        self.inicio = None
    
    def agregar(self, dato):
    
    
    def imprimir(self):


def menu():
    lista = ListaEnlazada
    while True:
        print("Menú de opciones")
        print("1. Agregar")
        print("2. Eliminar")
        print("3. Buscar")
        print("4. Modificar")
        print("5. Imprimir")
        print("6. Salir")
        print("Elija su opción: ", end = '')
        opcion = int(input())
        
        if opcion == '1':
            try:
                print("Ingrese un número entero: ", end = '')
                dato = int(input())
                lista.agregar(dato)
                print("Elemento agregado.")
            except ValueError:
                print("Elemento no agregado.")
        elif opcion == '5':
            lista.imprimir
        elif opcion == '6':
            print("Salida del programa")
            break
        else:
            print("Intente de nuevo ingresar un número")
        
if __name__ == '__main__':
    menu()