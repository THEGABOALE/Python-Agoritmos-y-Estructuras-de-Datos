'''
Control de ventas de los empleados (3) de una empresa de electrodomésticos para un trimestre
'''

tablaEmpleados = []
tablaVentas = []

for i in range(3):
    print(f"\nIngrese el nombre del empleado {i+1}: ",end='')
    nombre = input()
    tablaEmpleados.append(nombre)
   
for fil in range(3):
    fila = []
    for col in range(3):
        print(f"\nIngrese la venta del empleado {fil+1} del mes {col+1}: ",end='')
        venta = float(input())
        fila.append(venta)
    tablaVentas.append(fila)

print("\nEmpleados: ", tablaEmpleados)
print("\n Ventas: ",tablaVentas)

print("\nInformación de Ventas")
print("Nombre\tEnero\tFebrero\tMarzo")
for i, nombre in enumerate(tablaEmpleados):
    print(f"{nombre}\t{tablaVentas[i][0]:,.1f}\t{tablaVentas[i][1]:,.1f}\t{tablaVentas[i][2]:,.1f}")
