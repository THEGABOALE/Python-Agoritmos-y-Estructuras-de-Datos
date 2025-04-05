'''Se requiere que los estudiantes diseñen un módulo independiente que contenga 
implementaciones  de algoritmos  de ordenamiento  simples  (bubble  sort). El 
objetivo es  que,  a  partir de  una  función  principal, se  invoquen los  métodos del 
módulo para ordenar una lista de números y demostrar la correcta separación de 
responsabilidades, fomentando la modularidad y la reutilización del código.'''

from ordenamiento import bubble_sort

def main():
    entrada = input("\nIngrese números separados por comas: ")
    num = list(map(int, entrada.split(',')))
    print("\nLista de números ingresados: ", num)
    orden = bubble_sort(num)
    print("\nLista ordenada: ", orden)

if __name__ == "__main__":
    main()
    