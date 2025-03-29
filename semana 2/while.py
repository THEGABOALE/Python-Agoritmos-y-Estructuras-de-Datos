'''
Calcular la nota de n estudiantes para los tres cortes de evaluación 
de la asignuta Algoritmos y Estructura de datos.
'''

print("\n==Nota final de la asignatura==",end="\n")
numestudiantes = int(input("\nIngrese la cantidad de estudiantes a evaluar: "))
i = 0
while i < numestudiantes:
    print(f"\nIngrese el nombre del estudiante {i+1}: ",end='')
    nombre = input()
    print(f"\nIngrese la nota del primer corte del estudiante {i+1}: ",end='')
    nota1 = float(input())
    print(f"\nIngrese la nota del segundo corte del estudiante {i+1}: ",end='')
    nota2 = float(input())
    print(f"\nIngrese la nota del tercer corte del estudiante {i+1}: ",end='')
    nota3 = float(input())

    promedio = (nota1 + nota2 + nota3)/3
    print(f"\nPromedio de notas de los tres cortes del estudiante {i+1}: {promedio:.2f}")

    if promedio < 70:
        print(f"\n{nombre} ha reprobado.")
    elif promedio >= 70 and promedio <=79:
        print(f"\nEl rendimiento de {nombre} es regular.")
    elif promedio >= 80 and promedio <= 89:
        print(f"\nEl rendimiento de {nombre} es bueno.")
    elif promedio >= 90 and promedio <= 100:
        print(f"\nEl rendimiento de {nombre} es excelente.")

    i += 1
print("\n\n")
