from clase_gastos import Gastos

def resgistrar_categoria(categorias):
    nuevacategoria = input("Ingrese la nueva categoría: ")
    if nuevacategoria not in categorias:
        categorias.append(nuevacategoria)
        print(f"Categoría: {nuevacategoria} registrada correctamente.")
    else:
        print("Esta categoría ya existe.")

def agregar_gastos(categorias, gastos):
    if not categorias:
        print("No hay ninguna categoría. Primero registre una y vuelva a intentarlo más tarde.")
        
    