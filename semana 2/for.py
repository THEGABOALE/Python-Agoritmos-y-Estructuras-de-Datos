'''
Calcular la nota de n estudiantes para los tres cortes de evaluación 
de la asignatura Algoritmos y Estructura de datos.
'''

print("\n==Nota final de la asignatura==",end="\n")
print("\nIngrese la cantidad de estudiantes a evaluar: ",end='')
numestudiantes = int(input())
for contador in range(numestudiantes):
    print(f"\nIngrese el nombre del estudiante{contador+1}: ",end='')
    nombre = input()
    print(f"\nIngrese la nota del primer corte del estudiante {contador+1}: ",end='')
    nota1 = float(input())
    print(f"\nIngrese la nota del segundo corte del estudiante {contador+1}: ",end='')
    nota2 = float(input())
    print(f"\nIngrese la nota del tercer corte del estudiante {contador+1}: ",end='')
    nota3 = float(input())

    promedio = (nota1 + nota2 + nota3)/3
    print(f"\nPromedio de notas de los tres cortes del estudiante {contador+1}: {promedio:.2f}")

    if promedio < 69:
        print(f"\n{nombre} ha reprobado.")
    elif promedio >= 70 and promedio <=79:
        print(f"\nEl rendimiento de {nombre} es regular.")
    elif promedio >= 80 and promedio <= 89:
        print(f"\nEl rendimiento de {nombre} es bueno.")
    elif promedio >= 90 and promedio <= 100:
        print(f"\nEl rendimiento de {nombre} es excelente.")
print("\n\n")
