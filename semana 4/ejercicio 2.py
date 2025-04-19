'''Construir un método cantVocales que determine la cantidad de vocales 
almacenadas en una lista de caracteres.'''

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
    
    def cantVocales(self):
        vocales = 'aeiouAEIOU'
        actual = self.inicio
        contador = 0
        while actual:
            if isinstance(actual.dato, str) and actual.dato in vocales:
                contador += 1
            actual = actual.siguiente
        print(f"Cantidad de vocales en la lista: {contador}")
              
    def imprimir(self):
        actual = self.inicio
        if actual is None:
            print("La lista está vacía")
        else:
            print("Elementos de la Lista Enlazada")
            while actual:
                print(f" -> {actual.dato}")
                actual = actual.siguiente

def menu():
    lista = ListaEnlazada()
    while True:
        print("Menú de opciones")
        print("1. Agregar")
        print("2. Eliminar")
        print("3. Contar vocales")
        print("4. Imprimir")
        print("5. Salir")
        print("Elija su opción: ", end = '')
        
        try:
            opcion = int(input())
        except ValueError:
            print("Por favor, ingrese una opción válida.")
            continue
        
        if opcion == 1:
            dato = input("Ingrese un dato (letra o número): ")
            if len(dato) == 1:
                lista.agregar(dato)
                print("Elemento agregado.")
            else:
                try:
                    lista.agregar(int(dato))
                    print("Elemento agregado.")
                except ValueError:
                    print("Dato no válido. Ingrese solo un número o una letra.")
        elif opcion == 2:
            valor = input("Ingrese el elemento a eliminar: ")
            try: 
                valor = int(valor)
            except ValueError:
                pass #Sigue siendo un carácter
            lista.eliminar(valor)
            print("Elemento eliminado correctamente.")
        elif opcion == 3:
            lista.cantVocales()
        elif opcion == 4:
            lista.imprimir()
        elif opcion == 5:
            print("Salida del programa")
            break
        else:
            print("Intente de nuevo ingresar un número")
        
if __name__ == '__main__':
    menu()