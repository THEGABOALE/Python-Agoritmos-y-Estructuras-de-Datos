def registrar_categoria(categorias):
    nueva_categoria = input("Ingrese la nueva categoría: ")
    if nueva_categoria not in categorias:
        categorias.append(nueva_categoria)
        print(f"Categoría '{nueva_categoria}' registrada correctamente.")
    else:
        print("Esta categoría ya existe.")