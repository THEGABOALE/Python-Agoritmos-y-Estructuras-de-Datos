print("Ingrese el número de trabajadores a recibir su salario: ", end="\n")
numtrabajadores = int(input())
print("Ingrese el pago a dar por cada hora laboral realizada: ", end="\n")
salarios = float(input())
pago = list()
for i in range(numtrabajadores):
    horas = int(input(f"Ingrese las horas realizadas del trabajador {i+1}:"))
    if int(horas) <= 48:
    pago=horas*salarios
    else int(horas) > 48:
    pago=48 * salarios + (horas - 48) * salarios * 2
    


