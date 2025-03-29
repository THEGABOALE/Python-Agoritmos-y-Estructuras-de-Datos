'''
Programa para calcular la quinta potencia, la raíz cuadrada, el exponencial, 
el logaritmo natural y el valor absoluto de un número introducido por el teclado.
'''
import math

print("Ingrese un número: ",end='')
num=float(input())
print("\n==RESULTADOS==",end="\n")
print(f"\nEl resultado de la quinta potencia es: {num**5:.2f}")
print(f"\nEl resultado de la raíz cuadrada es: {math.sqrt(num):.2f}")
print(f"\nEL resultado de la exponencial es: {math.exp(num):.2f}")
print (f"\nEl resultado del logaritmo natural es: {math.log(num):.2f}")
print(f"\nEl resultado del valor absoluto es: {abs(num)}")
