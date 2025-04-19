'''Construir un método imprimeInverso que imprima los elementos de una lista 
enlazada de enteros en orden inverso a partir de una posición p.'''

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

    def eliminar(self, valor):
        while self.inicio and self.inicio.dato == valor:
            self.inicio = self.inicio.siguiente
        actual = self.inicio
        while actual and actual.siguiente:
            if actual.siguiente.dato == valor:
                actual.siguiente = actual.siguiente.siguiente
            else:
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

    def imprimir(self):
        actual = self.inicio
        if actual is None:
            print("La lista está vacía")
        else:
            print("Elementos de la Lista Enlazada:")
            while actual:
                print(f" -> {actual.dato}")
                actual = actual.siguiente

def menu():
    lista = ListaEnlazada()
    while True:
        print("\nMenú de opciones")
        print("1. Agregar elemento")
        print("2. Eliminar valor")
        print("3. Contar vocales")
        print("4. Imprimir lista")
        print("5. Imprimir desde posición en orden inverso")
        print("6. Salir")
        print("Elija su opción: ", end='')

        try:
            opcion = int(input())
        except ValueError:
            print("Por favor, ingrese un número válido.")
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
            valor = input("Ingrese el valor a eliminar: ")
            try:
                valor = int(valor)
            except ValueError:
                pass
            lista.eliminar(valor)
            print("Elementos eliminados si existían.")
        elif opcion == 3:
            lista.cantVocales()
        elif opcion == 4:
            lista.imprimir()
        elif opcion == 5:
            try:
                p = int(input("Ingrese la posición inicial (p): "))
                lista.imprimeInverso(p)
            except ValueError:
                print("Posición no válida.")
        elif opcion == 6:
            print("Salida del programa")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    menu()