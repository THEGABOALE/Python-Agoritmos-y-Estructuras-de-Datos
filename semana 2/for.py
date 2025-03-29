'''
Calcular la nota de n estudiantes para los tres cortes de evaluación 
de la asignuta Algoritmos y Estructura de datos.
'''

print("\nNota final de la asignatura")
print("Ingrese la cantidad de estudiantes a evaluar: ",end='')
numestudiantes = int(input())
for contador in range(numestudiantes):
    print("Ingrese el nombre del estudiante: ",end='')
    print("Ingrese la nota del primer corte del estudiante: ",end='')
    nota1 = float(input())
    print("Ingrese la nota del segundo corte del estudiante: ",end='')
    nota2 = float(input())
    print("Ingrese la nota del tercer corte del estudiante: ",end='')
    nota3 = float(input())
    
