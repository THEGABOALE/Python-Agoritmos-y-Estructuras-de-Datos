def mostrar_total_general(gastos):
    total_mes = sum(g.get_monto() for g in gastos)
    print(f"\nTotal gastado en el mes: ${total_mes:.2f}")

def mostrar_totales_por_categoria(categorias, gastos):
    print("\nTotal por categoría:")
    for cat in categorias:
        total_categoria = sum(g.get_monto() for g in gastos if g.get_categoria() == cat)
        print(f"{cat}: ${total_categoria:.2f}")

def mostrar_promedios(categorias, gastos):
    print("\nPromedio por categoría:")
    for cat in categorias:
        # Usa los getters
        gastos_cat = [g.get_monto() for g in gastos if g.get_categoria() == cat]
        if gastos_cat:
            promedio = sum(gastos_cat) / len(gastos_cat)
            print(f"{cat}: ${promedio:.2f}")
        else:
            print(f"{cat}: No hay gastos registrados.")

def listar_gastos(gastos):
    print("\nLista de todos los gastos:")
    if not gastos:
        print("No hay gastos registrados.")
    for gasto in gastos:
        print(gasto)