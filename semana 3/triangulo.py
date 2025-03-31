'''
Desarrollar un programa que cargue los datos de un triángulo.
Implementar un método/función para determinar el tipo de triángulo
(equilátero, isósceles o escaleno).
'''

def triangulo():
    print("==MEDIDA DE CADA LADO DEL TRIÁNGULO==")
    lado1 = int(input("\nIngrese la medida del lado 1: "))
    lado2 = int(input("\nIngrese la medida del lado 2: "))
    lado3 = int(input("\nIngrese la medida del lado 3: "))
    if lado1 == lado2 == lado3:
        print("\nEl triángulo es equilatero")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("\nEl triángulo es isósceles.")
    else:
        print("\nEl triángulo es escaleno.")

def main():
    triangulo()
    
if __name__ == "__main__":
    main()