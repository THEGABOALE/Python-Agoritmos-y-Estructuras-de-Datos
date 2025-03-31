'''Ejercicios de funciones en Python: suma, menor y mayor de los números'''
#Definición de Funciones
def suma(lista):
    total = 0
    for x in lista:
        total = total + x
    return(total)

def menor(lista):
    men = lista[0]
    for x in lista:
        if x < men:
            men = x
    return(men)

def mayor(lista):
    may = lista[0]
    for x in lista:
        if x > may:
            may = x
    return(may)


#Programa principal
def main():
    #Captura de la cantidad de elementos
    lista = []
    print("Ingrese la cantidad de elementos a procesar: ", end='')
    n = int(input())
    
    #Captura de datos
    for i in range(n):
        print(f"Ingrese el elemento {i+1}: ", end='')
        num = int(input())
        lista.append(num)
        
    #Llamado a las funciones
    print("Los elementos de la lista son: ", lista)
    print("La suma de todos los elementos es: ", suma(lista))
    print("El número menor de la lista es: ", menor(lista))
    print("El número mayor de la lista: ", mayor(lista))
    
if __name__ == "__main__":
    main()