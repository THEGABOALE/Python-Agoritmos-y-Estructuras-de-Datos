print("Ingrese el número de trabajadores a recibir su salario: ", end="\n")
numtrabajadores = int(input())
print("Ingrese el pago a dar por cada hora laboral realizada: ", end="\n")
salarios = float(input())
pago = list()
for i in range(numtrabajadores):
    while True:
        try:
            horas = int(input(f"Ingrese las horas realizadas del trabajador {i+1}:"))
            if horas < 0:
                print("Las horas no pueden ser negativas. Intentelo de nuevo.",endl="\n")
                continue
            break
        except ValueError:
            print("Error. Ingrese un número válido.")
    if horas <= 48:
        pago.append(horas*salarios)
    else:
        pago.append(48 * salarios + (horas - 48) * salarios * 2)
print("\nSalarios de los trabajadores:")
for i in range(numtrabajadores):
    print(f"Trabajador {i+1}: ${pago[i]}")

