'''Un estudiante universitario desea llevar el control de sus gastos mensuales 
relacionados con sus estudios, como transporte, alimentación, materiales educativos, 
conexión a internet, alquiler, entre otros.'''

from categorias import registrar_categoria
from registro import agregar_gasto
from reportes import mostrar_totales_por_categoria, mostrar_total_general, mostrar_promedios, listar_gastos

def main():
    categoria = []
    gastos = []
    
    while True:
        print("\n-- Menú --")
        print("1. Registrar categoría")
        print("2. Agregar gasto")
        print("3. Mostrar total gastado")
        print("4. Mostrar total por categoría")
        print("5. Listar todos los gastos")
        print("6. Mostrar promedio por categoría")
        print("7. Salir")

        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            registrar_categoria(categoria)
        elif opcion == "2":
            agregar_gasto(categoria, gastos)
        elif opcion == "3":
            mostrar_total_general(gastos)
        elif opcion == "4":
            mostrar_totales_por_categoria(categoria, gastos)
        elif opcion == "5":
            listar_gastos(gastos)
        elif opcion == "6":
            mostrar_promedios(categoria, gastos)
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")
    
if __name__ == '__main__':
    main()