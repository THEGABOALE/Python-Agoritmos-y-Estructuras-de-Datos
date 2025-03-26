'''
Control de ventas de los empleados (3) de una empresa de electrodomésticos para un trimestre
'''

tablaEmpleados = []
tablaVentas = []

for i in range(3):
    print(f"\nIngrese el nombre del empleado {i+1}: ")
    nombre = input()
    tablaEmpleados.append(nombre)
    
for fil in range(3):
    fila = []
    for col in range(3):
        print(f"\nIngrese la venta del empleado {fil+1} del mes {col+1}: ")
        venta = float(input())
        fila.append(venta)
    tablaVentas.append(fila)

print("\nEmpleados: ", tablaEmpleados)
print("\n Ventas: ",tablaVentas)

print("\Información de Ventas")
print("Enero\t\tFebrero\tMarzo")
for i, nombre in enumerate(tablaEmpleados):
    print(f"{nombre}\t{tablaVentas[i][0]:,.1}\t{tablaVentas[i][1]:,.1}\t{tablaVentas[i][2]:,.1}")
