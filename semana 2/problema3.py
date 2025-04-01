'''Simulación de un diccionario Inglés-Español limitado a 5 pares de palabras'''

def crearDiccionario():
    diccionario = {}
    print("\nIntroduce 5 parejas de palabras (inglés-español).\n")
    for i in range(5):
        palabra_ing = input(f"\nIngrese la palabra {i+1} en inglés: ").strip().lower()
        # .strip() -> Elimina espacios en blanco al inicio y final  
        # .lower() -> Convierte la palabra a minúsculas para evitar diferencias en la búsqueda  
        palabra_esp = input(f"\nIntroduzca la palabra {i+1} en español: ").strip().lower()
        diccionario[palabra_ing] = palabra_esp #Inglés -> Español
        diccionario[palabra_esp] = palabra_ing #Español -> Inglés
    return diccionario

def traducir(diccionario):  # Se recibe el diccionario como argumento
    print("\n== MODO DE TRADUCCIÓN ==\n")
    print("\nIngrese la palabra 'salir' si desea terminar.\n")
    
    while True:
        palabra = input("\nIngrese una palabra en inglés para traducir: ").strip().lower()
        if palabra == 'salir':
            print("\nGracias por usar el traductor.")
            break
        elif palabra in diccionario:
            print(f"\nLa traducción es: {diccionario[palabra]}")
        else:
            print("\nPalabra no encontrada en el diccionario.")

def main():
    diccionario = crearDiccionario()
    traducir(diccionario)
    
if __name__ == '__main__':
    main()
