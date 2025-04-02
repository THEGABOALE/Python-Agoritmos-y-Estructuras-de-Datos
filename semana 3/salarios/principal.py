from clase_empleado import Empleado
def main():
    empleados = []
    print("\nIngrese la cantidad de empleados: ", end = '')
    n = int(input())
    print("Ingrese los datos de los empleados")
    for i in range(n):
        print(f"Nombre: ", end = '')
        nombre = input()
        print("Salario Bruto: ", end = '')
        salarioBruto = float(input())
        emp = Empleado(nombre, salarioBruto)
        empleados.append(emp)
        
    print("Datos de Empleado")
    for emp in empleados:
        print(f"{emp.getNombre()} {emp.get_salarioNeto():.2f}")
    
if __name__ == "__main__":
    main()