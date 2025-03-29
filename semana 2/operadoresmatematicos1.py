'''
Programa que solicita dos números enteros y da como resultado 
cada uno de los operadores matemáticos básicos.
'''

print("Escribe un número: ",end='')
num1=int(input())
print("Escribe otro número ",end='')
num2=int(input())

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1*num2
division = num1/num2

print("\n==RESULTADO DE TODOS LOS OPERADORES MATEMÁTICOS==",end="\n")
print("\nSUMA DE LOS DOS NÚMEROS: ",suma)
print("\nRESTA DE LOS DOS NÚMEROS: ",resta)
print("\nMULTIPLICACIÓN DE LOS DOS NÚMEROS: ",multiplicacion)
print("\nDIVISIÓN DE LOS DOS NÚMEROS: ",division)
