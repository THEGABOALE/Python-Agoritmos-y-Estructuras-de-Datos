from clase_gastos import Gasto

def agregar_gasto(categorias, gastos):
    if not categorias:
        print("No hay categorías registradas. Primero registre una.")
        return

    fecha = input("Ingrese la fecha del gasto (DD/MM/AAAA): ")
    print("Categorías disponibles:")
    for i, cat in enumerate(categorias, 1):
        print(f"{i}. {cat}")
    try:
        indice = int(input("Seleccione el número de categoría: ")) - 1
        categoria = categorias[indice]
        monto = float(input("Ingrese el monto del gasto ($): "))
        descripcion = input("Ingrese una descripción corta del gasto: ")
        gasto = Gasto(fecha, categoria, monto, descripcion)
        gastos.append(gasto)
        print("Gasto registrado exitosamente.")
    except (IndexError, ValueError):
        print("Entrada inválida.")