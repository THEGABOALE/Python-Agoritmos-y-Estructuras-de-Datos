'''
Programa para calcular la quinta potencia, la raíz cuadrada, el exponencial, 
el logaritmo natural y el valor absoluto de un número introducido por el teclado.
'''
import math

print("Ingrese un número: ",end="\n")
num=float(input())
print("El resultado de la quinta potencia es: ",num**5)
print("El resultado de la raíz cuadrada es: ",math.sqrt(num))
print("EL resultado de la exponencial es: ",math.exp(num))
print ("El resultado del logaritmo natural es: ",math.log(num))
print("El resultado del valor absoluto es: ",abs(num))
