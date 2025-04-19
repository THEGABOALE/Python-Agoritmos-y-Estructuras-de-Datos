'''Implementar un método que recibe una lista de enteros L y un número entero n de 
forma que modifique la lista mediante el borrado de todos los elementos de la lista 
que tengan este valor.'''

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None #None significa nulo

class ListaEnlazada:
    def __init__(self):
        self.inicio = None
    
    def agregar(self, dato):
        nuevo = Nodo(dato)
        if self.inicio is None:
            self.inicio = nuevo
        else:
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
              
    def imprimir(self):
        actual = self.inicio
        if actual is None:
            print("La lista está vacía")
        else:
            print("Elementos de la Lista Enlazada")
            while actual:
                print(f" -> {actual.dato}")
                actual = actual.siguiente
                
    def eliminar(self, n):
        #Eliminar los nodos desde el inicio si contienen el valor n
        while self.inicio is not None and self.inicio.dato == n:
            self.inicio = self.inicio.siguiente
        actual = self.inicio
        anterior = None
        while actual is not None:
            if actual.dato == n:
                anterior.siguiente = actual.siguiente
            else:
                anterior = actual
            actual = actual.siguiente

def menu():
    lista = ListaEnlazada()
    while True:
        print("Menú de opciones")
        print("1. Agregar")
        print("2. Eliminar")
        print("3. Imprimir")
        print("4. Salir")
        print("Elija su opción: ", end = '')
        opcion = int(input())
        
        if opcion == 1:
            try:
                print("Ingrese un número entero: ", end = '')
                dato = int(input())
                lista.agregar(dato)
                print("Elemento agregado.")
            except ValueError:
                print("Elemento no agregado.")
        elif opcion == 2:
            try:
                print("Ingrese el número a eliminar: ", end = '')
                valor = int(input())
                lista.eliminar(valor)
                print("Eliminación completada correctamente.")
            except ValueError:
                print("Entrada inválida.")
        elif opcion == 3:
            lista.imprimir()
        elif opcion == 4:
            print("Salida del programa")
            break
        else:
            print("Intente de nuevo ingresar un número")
        
if __name__ == '__main__':
    menu()