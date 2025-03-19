print("Ingrese el número de estudiantes: ", end="\n")
numestudiantes = int(input())
notasfinales = list()
for i in range(numestudiantes):
    nota = float(input(f"Ingrese la nota del estudiante {i+1}: "))
    if float(nota) < 60:
        print("Reprobado")
    elif float(nota) <= 60 and float(nota) >= 69:
        print("Regular")
    elif float(nota) >= 70 and float(nota) <= 79:
        print("Bueno")
    elif float(nota) >= 80 and float(nota) <= 89:
        print("Muy bueno")
    elif float(nota) >= 90 and float(nota) <= 100:
        print("Exelente")
        
notasfinales.append(int(nota))
print(f"Notas Finales: {notasfinales}")