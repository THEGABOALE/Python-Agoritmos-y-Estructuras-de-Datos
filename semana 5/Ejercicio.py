class Nodo: #Se define la clase Nodo. Representa cada elemento individual en la lista enlazada.
    def __init__(self, dato): #Método constructor (__init__) al iniciar una nueva instancia. Recibe un dato.
        self.dato = dato #Almacena el dato proporcionado en el atributo dato del nodo.
        self.siguiente = None #None significa Nulo
        '''Inicializa el atributo siguiente con None, lo que indica que este nodo no apunta a ningún 
        otro nodo aún (es el final de la lista por ahora).'''

class ListaEnlazada: #Se define la clase de Lista Enlazada, que representa toda la lista como tal.
    def __init__(self): #Constructor de la clase.
        self.inicio = None #Inicializa la lista con inicio = None, lo que significa que al principio la lista está vacía.
    
    def agregar(self, dato): #Se define el método para agregar elementos al final de la lista.
        nuevo = Nodo(dato) #Crea un nuevo nodo con el dato proporcionado.
        if self.inicio is None: #Verifica si la lista está vacía.
            self.inicio = nuevo #Si está vacía, el nuevo nodo se convierte en el primer nodo de la lista.
        else:
            actual = self.inicio 
        #Si ya hay datos se inicializa una variable actual apuntando al primer nodo.
            while actual.siguiente:
                actual = actual.siguiente
            #
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
                
    def imprimeInverso(self, p):
        elementos = []
        actual = self.inicio
        indice = 0
        while actual and indice < p:
            actual = actual.siguiente
            indice += 1
        if actual is None:
            print(f"La posición {p} no es válida.")
            return
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        print("Elementos en orden inverso desde la posición", p)
        for dato in reversed(elementos):
            print(f" -> {dato}")

def menu():
    lista = ListaEnlazada()
    while True:
        print("Menú de opciones")
        print("1. Agregar")
        print("2. Imprimir")
        print("3. Imprimir inverso")
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
            lista.imprimir()
        elif opcion == 3:
            try:
                p = int(input("Ingrese la posición inicial (p): "))
                lista.imprimeInverso
            except ValueError:
                print("Posición no válida.")
        elif opcion == 4:
            print("Salida del programa")
            break
        else:
            print("Intente de nuevo ingresar un número")
        
if __name__ == '__main__':
    menu()